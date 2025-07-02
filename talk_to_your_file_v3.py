import os
from pathlib import Path
import torch
# Now import everything else
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_chroma import Chroma
from langchain.vectorstores import FAISS
from langchain_aws import ChatBedrock
import webbrowser
from helpers.helpers_fn import extract_text_from_local_file, get_all_files, google_cse_search, load_file_map
# Configuration
PERSIST_DIR = "db"  # ChromaDB persistence directory
CHUNK_SIZE = 1300   # Size of text chunks
CHUNK_OVERLAP = 150  # Overlap between chunks
EMBEDDING_MODEL = "intfloat/multilingual-e5-base"  # Model for embeddings
NUM_CHUNKS = 6  # Number of relevant chunks to retrieve
BEDROCK_MODEL = "anthropic.claude-3-sonnet-20240229-v1:0"  # Claude model version
AWS_REGION = "us-east-1"  # AWS region for Bedrock
TEMPERATURE = 0.3  # Temperature for response generation
MAX_HISTORY = 3  # Maximum number of conversation turns to remember

# Initialize ChromaDB with persistence
os.makedirs(PERSIST_DIR, exist_ok=True)
os.chmod(PERSIST_DIR, 0o770)
# Initialize LangChain chat model
@st.cache_resource(show_spinner=False)
def init_chat_model():
    return ChatBedrock(
        model_id=BEDROCK_MODEL,
        model_kwargs={"temperature": TEMPERATURE},
        region_name=AWS_REGION
    )

# Initialize embeddings
@st.cache_resource(show_spinner=False)
def init_embeddings():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={'device': device},
        encode_kwargs={'normalize_embeddings': True}
    )
@st.cache_resource(show_spinner=False)
def init_faiss():
    embeddings = init_embeddings()
    # Створюємо порожню FAISS базу
    vectorstore = FAISS.from_texts(["stub"], embedding=embeddings)
    return vectorstore
# Initialize ChromaDB and create retriever
@st.cache_resource(show_spinner=False)
def init_chromadb():
    """Initialize ChromaDB with persistence and transformer embeddings"""
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    
    # Initialize embeddings
    embeddings = init_embeddings()
    
    # Create or load Chroma vector store
    vectorstore = Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=embeddings,
        collection_name="documents"
    )
    
    return vectorstore

# Initialize conversation memory
@st.cache_resource(show_spinner=False)
def init_memory():
    return ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )

def handle_segment_change():
    selected = st.session_state["sources"] 
    webbrowser.open_new_tab(file_map[selected])
# Create the conversation chain
def create_conversation_chain(llm, retriever, memory):
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

    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        combine_docs_chain_kwargs={"prompt": PROMPT},
        return_source_documents=True,
        verbose=True
    )

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'vectorstore' not in st.session_state:
    vectorstore =  init_faiss()#init_chromadb()
    st.session_state.vectorstore = vectorstore
    st.session_state.llm = init_chat_model()
    st.session_state.memory = init_memory()
    st.session_state.chain = create_conversation_chain(
        st.session_state.llm,
        vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={'k': 6, 'lambda_mult': 0.25}
        ),
        st.session_state.memory
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

# --- File map caching ---
@st.cache_resource(show_spinner=False)
def get_file_map():
    return load_file_map()

file_map = get_file_map()  # Use cached file_map

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
    # Додаємо чекбокс для очищення ChromaDB
    clear_db = st.checkbox("Очистити ChromaDB перед індексацією", value=False)
    if st.button(t("index_btn")):
        if clear_db:
            # Видаляємо всі файли з папки db/
            import shutil
            if os.path.exists(PERSIST_DIR):
                shutil.rmtree(PERSIST_DIR)
                os.makedirs(PERSIST_DIR, exist_ok=True)
            # Оновлюємо vectorstore після очищення
            st.session_state.vectorstore = init_faiss()#init_chromadb()
            st.session_state.processed_files = set()
            st.session_state.memory.clear()
        with st.spinner(t("indexing")):
            root_folder = "/home/mikola/projects/ai/data/structured"
            files = get_all_files(root_folder)
            processed_count = 0
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
                        # Використовуємо пошук по підрядку (case-insensitive)
                        source_path = None
                        for key in file_map:
                            if filenamesplit.lower() in key.lower():
                                source_path = file_map[key]
                                break
                    chunks = [chunk for chunk in text_splitter.split_text(content) if chunk.strip()]
                    if not chunks:
                        st.warning(f"{t('error', error='Не вдалося створити непорожні чанки з файлу ' + filename)}")
                        continue
                    try:
                        st.session_state.vectorstore.add_texts(
                            texts=chunks,
                            metadatas=[{
                                "filename": filename,
                                "type": Path(file_path).suffix,
                                "source": source_path if source_path else "Unknown"
                            }] * len(chunks)
                        )
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
        count = st.session_state.vectorstore._collection.count()
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
                            "filename": doc.metadata.get("filename", "Unknown"),
                            "text": doc.page_content
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