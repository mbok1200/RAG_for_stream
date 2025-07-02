import os
from pathlib import Path
import torch
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from pinecone import (
    Pinecone,
    ServerlessSpec,
    CloudProvider,
    AwsRegion,
    VectorType
)
from langchain_aws import ChatBedrock
import webbrowser
from helpers.helpers_fn import extract_text_from_local_file, get_all_files, google_cse_search, load_file_map
import re
from math import ceil
def batch_upsert(index, vectors, batch_size=50, namespace="default"):
    for i in range(0, len(vectors), batch_size):
        batch = vectors[i:i+batch_size]
        index.upsert(
            vectors=batch,
            namespace=namespace
        )
# --- Config ---
PERSIST_DIR = "db"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 120
EMBEDDING_MODEL = "intfloat/multilingual-e5-base"
NUM_CHUNKS = 6
BEDROCK_MODEL = "anthropic.claude-3-sonnet-20240229-v1:0"
AWS_REGION = "us-east-1"
TEMPERATURE = 0.3
MAX_HISTORY = 3

os.makedirs(PERSIST_DIR, exist_ok=True)
os.chmod(PERSIST_DIR, 0o770)

@st.cache_resource(show_spinner=False)
def init_chat_model():
    return ChatBedrock(
        model_id=BEDROCK_MODEL,
        model_kwargs={"temperature": TEMPERATURE},
        region_name=AWS_REGION
    )

@st.cache_resource(show_spinner=False)
def init_embeddings():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={'device': device},
        encode_kwargs={'normalize_embeddings': True}
    )

@st.cache_resource(show_spinner=False)
def init_pinecone():
    pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
    index_name = "streamlit"
    if index_name not in pc.list_indexes().names():
        # pc.delete_index(index_name)
        pc.create_index(
            name=index_name,
            dimension=768,
            spec=ServerlessSpec(
                cloud=CloudProvider.AWS,
                region=AwsRegion.US_EAST_1
            ),
            vector_type=VectorType.DENSE
        )
    idx = pc.Index(index_name)
    return idx, pc

@st.cache_resource(show_spinner=False)
def init_memory():
    return ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )
def to_ascii_id(s):
    # Залишаємо тільки латиницю, цифри, дефіс, підкреслення і крапку
    s = s.encode("ascii", "ignore").decode()
    s = re.sub(r"[^A-Za-z0-9_\-\.]", "_", s)
    return s
def handle_segment_change():
    selected = st.session_state["sources"] 
    webbrowser.open_new_tab(file_map[selected])

# --- Custom Pinecone retriever ---
def pinecone_retrieve(query, embeddings, index, k=NUM_CHUNKS, namespace="default"):
    query_emb = embeddings.embed_query(query)
    print("Query embedding shape:", len(query_emb))
    print("Query embedding (first 5):", query_emb[:5])
    print("Namespace:", namespace)
    res = index.query(
        vector=query_emb,
        top_k=k,
        include_metadata=True,
        namespace=namespace
    )
    print("Raw Pinecone query result:", res)
    # Діагностика: скільки векторів у namespace
    stats = index.describe_index_stats()
    print("Pinecone index stats:", stats)
    docs = []
    for match in res.matches:
        docs.append({
            "page_content": match.metadata.get("text", ""),
            "metadata": match.metadata
        })
    print("Docs found:", len(docs))
    return docs

# --- LangChain chain with custom retriever ---
def create_conversation_chain(llm, memory, embeddings, index):
    template = """You are a helpful and friendly AI assistant.
    Your tasks:
    1. Answer questions using the information provided in the documents below.
    2. If the information in the documents is insufficient, honestly state that you cannot find the answer.
    3. If the question is unrelated to the documents, feel free to engage in general friendly conversation.
    4. Remember the context of the conversation to provide better answers.
    5. Use the context from the documents to answer the question.
    6. Provide sources for your answers when possible.
    7. if the question is not related to the documents, you can use Google Search to find the answer.
    8. If you use Google Search, provide the answer in a friendly manner.
    9. If user ask give them answer in not Ukrainian, you can use the answer in Ukrainian.
    10. Always answer in Ukrainian, regardless of the language of the question.
    Current conversation:
    {chat_history}

    Context from documents:
    {context}

    Human: {question}
    Assistant:"""
    PROMPT = ChatPromptTemplate.from_template(template)

    def custom_chain(inputs):
        question = inputs["question"]
        docs = pinecone_retrieve(
            question,
            embeddings,
            index,
            k=NUM_CHUNKS
        )
        context = "\n\n".join([doc["page_content"] for doc in docs])
        print(f"Context:", docs)  # Debugging output
        prompt = PROMPT.format_prompt(
            chat_history="\n".join([
                m['content'] for m in st.session_state.chat_history
                if isinstance(m, dict) and not m.get("pending")
            ]),
            context=context,
            question=question
        ).to_string()
        answer_obj = llm.invoke(prompt)
        answer = answer_obj.content if hasattr(answer_obj, "content") else str(answer_obj)
        if not answer.strip():
            answer = t("no_info")
        return {
            "answer": answer,
            "source_documents": docs
        }
    return custom_chain

# --- Session state ---
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'pinecone_index' not in st.session_state:
    pinecone_index, pinecone_client = init_pinecone()
    st.session_state.pinecone_index = pinecone_index
    st.session_state.pinecone_client = pinecone_client
    st.session_state.embeddings = init_embeddings()
    st.session_state.llm = init_chat_model()
    st.session_state.memory = init_memory()
    st.session_state.chain = create_conversation_chain(
        st.session_state.llm,
        st.session_state.memory,
        st.session_state.embeddings,
        pinecone_index
    )

if 'processed_files' not in st.session_state:
    st.session_state.processed_files = set()

# --- Multilanguage support ---
LANGUAGES = {
    "uk": {
        "title": "🤖 AI Асистент & Чат з Документами",
        "description": """
Цей AI асистент може:
- Відповідати на питання щодо ваших завантажених документів
- Запам'ятовувати деталі розмови
- Допомагати з загальними питаннями
- Утримувати контекст у чаті
""",
        "sidebar_header": "📄 Завантаження документів",
        "index_btn": "Індексувати локальну папку data/drive",
        "indexing": "Індексація файлів у /data/gdrive...",
        "index_done": "Індексація завершена. Оброблено файлів: {count}",
        "clear_chat": "Очистити історію чату",
        "check_docs": "Перевірити кількість документів у ChromaDB",
        "docs_count": "Кількість документів у ChromaDB: {count}",
        "sources": "Джерела",
        "ask": "Поставте питання про документи або поспілкуйтесь зі мною",
        "no_info": "🤔 Не знайдено релевантної інформації у документах. Спробуйте переформулювати питання.",
        "from": "**✅З файлу**: {filename}",
        "thinking": "⏳ Думаю...",
        "google": "\n\n🌐 **Google Search:**\n{answer}",
        "error": "Помилка: {error}"
    },
    "en": {
        "title": "🤖 AI Assistant & Document Chat",
        "description": """
This AI assistant can:
- Answer questions about your uploaded documents
- Remember details from your conversation
- Help with general questions
- Maintain context across the chat
""",
        "sidebar_header": "📄 Document Upload",
        "index_btn": "Index local folder data/drive",
        "indexing": "Indexing files in /data/gdrive...",
        "index_done": "Indexing complete. Files processed: {count}",
        "clear_chat": "Clear Chat History",
        "check_docs": "Check number of documents in ChromaDB",
        "docs_count": "Number of documents in ChromaDB: {count}",
        "sources": "Sources",
        "ask": "Ask a question about your documents or chat with me",
        "no_info": "🤔 No relevant information found in documents. Try rephrasing your question.",
        "from": "**✅From**: {filename}",
        "thinking": "⏳ Thinking...",
        "google": "\n\n🌐 **Google Search:**\n{answer}",
        "error": "Error: {error}"
    }
}

if 'lang' not in st.session_state:
    st.session_state.lang = "uk"

def t(key, **kwargs):
    return LANGUAGES[st.session_state.lang][key].format(**kwargs)

@st.cache_resource(show_spinner=False)
def get_file_map():
    return load_file_map()

file_map = get_file_map()

# --- Language selector ---
with st.sidebar:
    st.selectbox(
        "🌐 Мова / Language",
        options=[("uk", "Українська"), ("en", "English")],
        format_func=lambda x: x[1],
        key="lang",
        index=0 if st.session_state.lang == "uk" else 1,
        on_change=lambda: st.rerun()
    )

# --- UI with multilanguage ---
st.title(t("title"))
st.markdown(t("description"))

with st.sidebar:
    st.header(t("sidebar_header"))
    clear_db = st.checkbox("Очистити ChromaDB перед індексацією", value=False)
    if st.button(t("index_btn")):
        if clear_db:
            import shutil
            if os.path.exists(PERSIST_DIR):
                shutil.rmtree(PERSIST_DIR)
                os.makedirs(PERSIST_DIR, exist_ok=True)
            pinecone_index, pinecone_client = init_pinecone()
            st.session_state.pinecone_index = pinecone_index
            st.session_state.pinecone_client = pinecone_client
            st.session_state.processed_files = set()
            st.session_state.memory.clear()
        with st.spinner(t("indexing")):
            root_folder = "data/structured"
            files = get_all_files(root_folder)
            processed_count = 0
            embeddings = st.session_state.embeddings
            index = st.session_state.pinecone_index
            for file_path in files:
                filename = os.path.relpath(file_path, root_folder)
                source_path = None
                filenamesplit = os.path.splitext(os.path.basename(filename))[0]
                if filename not in st.session_state.processed_files:
                    content = extract_text_from_local_file(file_path)
                    if not content.strip():
                        st.warning(f"{t('error', error='Не вдалося витягти текст з файлу ' + filename + ' або файл порожній.')}")
                        continue
                    text_splitter = RecursiveCharacterTextSplitter(
                        chunk_size=CHUNK_SIZE,
                        chunk_overlap=CHUNK_OVERLAP,
                        separators=["\n\n", "\n", ".", " "]
                    )
                    if filenamesplit in file_map:
                        source_path = None
                        for key in file_map:
                            if filenamesplit.lower() in key.lower():
                                source_path = file_map[key]
                                break
                    chunks = [chunk for chunk in text_splitter.split_text(content) if chunk.strip()]
                    if not chunks:
                        st.warning(f"{t('error', error='Не вдалося створити непорожні чанки з файлу ' + filename)}")
                        continue
                    metadatas = [{
                        "filename": filename,
                        "type": Path(file_path).suffix,
                        "source": source_path if source_path else "Unknown",
                        "text": chunk
                    } for chunk in chunks]
                    try:
                        vectors = []
                        for i, chunk in enumerate(chunks):
                            vector = embeddings.embed_documents([chunk])[0]
                            vector_id = to_ascii_id(f"{filename}_{i}")
                            vectors.append((
                                vector_id,
                                vector,
                                metadatas[i]
                            ))
                        batch_upsert(index, vectors, batch_size=50, namespace="default")
                    except Exception as e:
                        st.warning(t("error", error=f"Error adding chunks from {filename}: {e}"))
                    st.session_state.processed_files.add(filename)
                    processed_count += 1
            st.success(t("index_done", count=processed_count))

    if st.button(t("clear_chat")):
        st.session_state.chat_history = []
        st.session_state.memory.clear()
        st.rerun()
    if st.button(t("check_docs")):
        try:
            index = st.session_state.pinecone_client.Index("streamlit")
            stats = index.describe_index_stats()
            count = stats.get("total_vector_count", 0)
        except Exception as e:
            count = f"Error: {e}"
        st.info(t("docs_count", count=count))
    st.segmented_control(
        t("sources"),
        options=file_map.keys(),
        on_change=handle_segment_change,
        key="sources",
        selection_mode="single"
    )

# --- Chat interface ---
chat_container = st.container()
with chat_container:
    for message in st.session_state.chat_history:
        with st.chat_message("assistant" if message["is_assistant"] else "user"):
            st.write(message["content"])
            if message.get("sources"):
                with st.expander("View sources"):
                    if not message["sources"]:
                        st.info(t("no_info"))
                    for source in message["sources"]:
                        filenamesplit = os.path.splitext(os.path.basename(source['filename']))[0]
                        st.markdown(t("from", filename=source['filename']))
                        file_url = file_map.get(filenamesplit.strip())
                        if file_url:
                            st.link_button(filenamesplit, file_url)
                        else:
                            st.info(t("error", error=f"No file path found for {filenamesplit}"))

if question := st.chat_input(t("ask")):
    st.session_state.chat_history.append({"is_assistant": False, "content": question})
    st.session_state.chat_history.append({"is_assistant": True, "content": t("thinking"), "pending": True})
    st.session_state.pending_question = question
    st.rerun()

if getattr(st.session_state, "pending_question", None):
    for idx, msg in enumerate(st.session_state.chat_history):
        if msg.get("pending"):
            try:
                result = st.session_state.chain({"question": st.session_state.pending_question})
                answer = result["answer"]
                sources = []
                if result.get("source_documents"):
                    for doc in result["source_documents"]:
                        sources.append({
                            "filename": doc["metadata"].get("filename", "Unknown"),
                            "text": doc["page_content"]
                        })
                if not sources:
                    google_answer = google_cse_search(st.session_state.pending_question)
                    answer += t("google", answer=google_answer)
                st.session_state.chat_history[idx] = {
                    "is_assistant": True,
                    "content": answer,
                    "sources": sources if sources else None
                }
            except Exception as e:
                st.session_state.chat_history[idx] = {
                    "is_assistant": True,
                    "content": t("error", error=str(e))
                }
            st.session_state.pending_question = None
            st.rerun()
            break