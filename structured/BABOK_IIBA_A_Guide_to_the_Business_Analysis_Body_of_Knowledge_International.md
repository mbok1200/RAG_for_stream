


A  G U I D E  T O  T H E  B U S I N E S S  A N A LY S I S
B O DY  O F  K N O W L E D G E
®
v3






BABOK
®
v3
A GUIDE TO THE BUSINESS ANALYSIS
BODY OF KNOWLEDGE®



International Institute of Business Analysis, Toronto, Ontario, Canada.
©2005, 2006, 2008, 2009, 2015 International Institute of Business Analysis. All rights reserved.
Version 1.0 and 1.4 published 2005. Version 1.6 Draft published 2006. Version 1.6 Final published 2008. Version 2.0
published 2009. Version 3.0 published 2015.
ISBN-13: 97978-1-927584-03-3
This document is provided to the business analysis community for educational purposes. IIBA® does not warrant that it is
suitable for any other purpose and makes no expressed or implied warranty of any kind and assumes no responsibility for
errors or omissions. No liability is assumed for incidental or consequential damages in connection with or arising out of the
use of the information contained herein.
IIBA®, the IIBA® logo, BABOK® and Business Analysis Body of Knowledge® are registered trademarks owned by
International Institute of Business Analysis. CBAP® is a registered certification mark owned by International Institute of
Business Analysis. Certified Business Analysis Professional, EEP and the EEP logo are trademarks owned by International
Institute of Business Analysis.
Archimate® is a registered trademark of The Open Group in the US and other countries.
Business Model Canvas is copyrighted by BusinessModelGeneration.com and released under Creative Commons license.
CMMI® is a registered trademark of Carnegie Mellon University.
COBIT® is a trademark of the Information Systems Audit and Control Association and the IT Governance Institute.
Mind Map® is a registered trademark of the Buzan Organization.
Scaled Agile Framework® and SAFe™ are trademarks of Scaled Agile, Inc.
TOGAF® is a registered trademark of The Open Group in the US and other countries.
Unified Modelling Language™ and UML® are trademarks of the Object Management Group.
Zachman Framework for Enterprise Architecture is a trademark of the Zachman Institute for Framework Advancement.
No challenge to the status or ownership of these or any other trademarked terms contained herein is intended by the
International Institute of Business Analysis.
Any inquiries regarding this publication, requests for usage rights for the material included herein, or corrections should be
sent by email to bok@iiba.org.



i
Table of Contents
Chapter 1: Introduction
1.1
Purpose of the BABOK® Guide   1
1.2
What is Business Analysis?   2
1.3
Who is a Business Analyst?   2
1.4
Structure of the BABOK® Guide   3
Chapter 2: Business Analysis Key Concepts
2.1
The Business Analysis Core Concept Model™   12
2.2
Key Terms   14
2.3
Requirements Classification Schema   16
2.4
Stakeholders   16
2.5
Requirements and Designs   19
Chapter 3: Business Analysis Planning and Monitoring
3.1
Plan Business Analysis Approach   24
3.2
Plan Stakeholder Engagement   31
3.3
Plan Business Analysis Governance   37
3.4
Plan Business Analysis Information Management   42
3.5
Identify Business Analysis Performance Improvements   47



Table of Contents
ii
Chapter 4: Elicitation and Collaboration
4.1
Prepare for Elicitation   56
4.2
Conduct Elicitation   61
4.3
Confirm Elicitation Results   65
4.4
Communicate Business Analysis Information   67
4.5
Manage Stakeholder Collaboration   71
Chapter 5: Requirements Life Cycle Management
5.1
Trace Requirements   79
5.2
Maintain Requirements   83
5.3
Prioritize Requirements   86
5.4
Assess Requirements Changes   91
5.5
Approve Requirements   95
Chapter 6: Strategy Analysis
6.1
Analyze Current State   103
6.2
Define Future State   110
6.3
Assess Risks   120
6.4
Define Change Strategy   124
Chapter 7: Requirements Analysis and Design Definition
7.1
Specify and Model Requirements   136
7.2
Verify Requirements   141
7.3
Validate Requirements   144
7.4
Define Requirements Architecture   148
7.5
Define Design Options   152
7.6
Analyze Potential Value and Recommend Solution   157
Chapter 8: Solution Evaluation
8.1
Measure Solution Performance   166
8.2
Analyze Performance Measures   170
8.3
Assess Solution Limitations   173
8.4
Assess Enterprise Limitations   177
8.5
Recommend Actions to Increase Solution Value   182
Chapter 9: Underlying Competencies
9.1
Analytical Thinking and Problem Solving   188



Table of Contents
iii
9.2
Behavioural Characteristics   194
9.3
Business Knowledge   199
9.4
Communication Skills   203
9.5
Interaction Skills   207
9.6
Tools and Technology   211
Chapter 10: Techniques
10.1
Acceptance and Evaluation Criteria   217
10.2
Backlog Management   220
10.3
Balanced Scorecard   223
10.4
Benchmarking and Market Analysis   226
10.5
Brainstorming   227
10.6
Business Capability Analysis   230
10.7
Business Cases   234
10.8
Business Model Canvas   236
10.9
Business Rules Analysis   240
10.10
Collaborative Games   243
10.11
Concept Modelling   245
10.12
Data Dictionary   247
10.13
Data Flow Diagrams   250
10.14
Data Mining   253
10.15
Data Modelling   256
10.16
Decision Analysis   261
10.17
Decision Modelling   265
10.18
Document Analysis   269
10.19
Estimation   271
10.20
Financial Analysis   274
10.21
Focus Groups   279
10.22
Functional Decomposition   283
10.23
Glossary   286
10.24
Interface Analysis   287
10.25
Interviews   290
10.26
Item Tracking   294
10.27
Lessons Learned   296
10.28
Metrics and Key Performance Indicators (KPIs)   297
10.29
Mind Mapping   299
10.30
Non-Functional Requirements Analysis   302
10.31
Observation   305
10.32
Organizational Modelling   308



Table of Contents
iv
10.33
Prioritization   311
10.34
Process Analysis   314
10.35
Process Modelling   318
10.36
Prototyping   323
10.37
Reviews   326
10.38
Risk Analysis and Management   329
10.39
Roles and Permissions Matrix   333
10.40
Root Cause Analysis   335
10.41
Scope Modelling   338
10.42
Sequence Diagrams   341
10.43
Stakeholder List, Map, or Personas   344
10.44
State Modelling   348
10.45
Survey or Questionnaire   350
10.46
SWOT Analysis   353
10.47
Use Cases and Scenarios   356
10.48
User Stories   359
10.49
Vendor Assessment   361
10.50
Workshops   363
Chapter 11: Perspectives
11.1
The Agile Perspective   368
11.2
The Business Intelligence Perspective   381
11.3
The Information Technology Perspective   394
11.4
The Business Architecture Perspective   408
11.5
The Business Process Management Perspective   424
Appendix A: Glossary 441
Appendix B: Techniques to Task Mapping 457
Appendix C: Contributors 473
Appendix D: Summary of Changes from BABOK® Guide v 2.0 483



v
Preface
IIBA® was founded in Toronto, Canada in October of 2003 to support the business analysis community
by:
• creating and developing awareness and recognition of the value and contribution of the business
analyst,
• defining the Business Analysis Body of Knowledge® (BABOK®),
• providing a forum for knowledge sharing and contribution to the business analysis profession, and
• publicly recognizing and certifying qualified practitioners through an internationally
acknowledged certification program.
The Body of Knowledge Committee was formed in October of 2004 to define and draft a global
standard for the practice of business analysis. In January of 2005, IIBA released version 1.0 of A Guide
to the Business Analysis Body of Knowledge® (BABOK® Guide) for feedback and comment. That version
included an outline of the proposed content and some key definitions. Version 1.4 was released in
October of 2005, with draft content in some knowledge areas. Version 1.6, which included detailed
information regarding most of the knowledge areas, was published in draft form in June of 2006 and
updated to incorporate errata in October of 2008.
The Body of Knowledge Committee developed version 2.0 of A Guide to the Business Analysis Body of
Knowledge® (BABOK® Guide) with the guidance of expert writing teams, and feedback garnered from
expert, practitioner, and public reviews. Version 2.0 introduced such concepts as the Requirements
Classification Schema and the Input/Output models. Version 2.0 was published in 2009 and became the
globally recognized standard for the practice of business analysis.
Following the publication of version 2.0, IIBA sought out a number of recognized experts in business
analysis and related fields and solicited their feedback on the content of that edition. The Body of
Knowledge Committee used these comments to plan the vision and scope of this revision. The Body of
Knowledge Committee worked with teams of expert writers to revise and update the content. The
revised draft of A Guide to the Business Analysis Body of Knowledge® (BABOK® Guide) was reviewed
by teams of both expert and practitioner reviewers. The Body of Knowledge Committee used the
feedback provided to further enhance and refine the text and then made the content available to the
business analysis community for review in 2014. The thousands of items of feedback from this public
review were used to further revise the text to form A Guide to the Business Analysis Body of
Knowledge® (BABOK® Guide) version 3.0.
The goal of this revision was to:
• incorporate new concepts and practices in use since the last revision,
• address the broadening and evolving scope of the profession,
• incorporate lessons learned from practitioners who have worked with the current version,
• improve the readability and usability of the guide,
• improve the consistency and quality of text and illustrations, and
• improve consistency with other generally accepted standards relating to the practice of business
analysis.



vi
The major changes in this release include:
• the inclusion of the Business Analysis Core Concept Model™ (BACCM™),
• the expanded scope of the role of business analysis in creating better business outcomes,
• the inclusion of Perspectives which describe specialized ways in which business analysis
professionals provide unique value to the enterprise,
• new and expanded Underlying Competencies to better reflect the diverse skill sets of the business
analyst, and
• new techniques that have emerged in the practice of business analysis.
This publication supersedes A Guide to the Business Analysis Body of Knowledge® (BABOK® Guide)
version 2.0.
The BABOK® Guide contains a description of generally accepted practices in the field of business
analysis. The content included in this release has been verified through reviews by practitioners, surveys
of the business analysis community, and consultations with recognized experts in the field. The data
available to IIBA demonstrates that the tasks and techniques described in this publication are in use by a
majority of business analysis practitioners. As a result, we can have confidence that the tasks and
techniques described in the BABOK® Guide should be applicable in most contexts where business
analysis is performed, most of the time.
The BABOK® Guide should not be construed to mandate that the practices described in this publication
should be followed under all circumstances. Any set of practices must be tailored to the specific
conditions under which business analysis is being performed. In addition, practices which are not
generally accepted by the business analysis community at the time of publication may be equally
effective, or more effective, than the practices described in the BABOK® Guide. As such practices
become generally accepted, and as data is collected to verify their effectiveness, they will be
incorporated into future editions of this publication. IIBA encourages all practitioners of business
analysis to be open to new approaches and new ideas, and wishes to encourage innovation in the
practice of business analysis.
IIBA would like to extend its thanks and the thanks of the business analysis community to all those who
volunteered their time and effort to the development of this revision, as well as those who provided
informal feedback to us in other ways.



1
1
Introduction
A Guide to the Business Analysis Body of Knowledge® (BABOK® Guide) is the
globally recognized standard for the practice of business analysis. The BABOK®
Guide describes business analysis knowledge areas, tasks, underlying
competencies, techniques and perspectives on how to approach business
analysis.
1.1
Purpose of the BABOK® Guide
The primary purpose of the BABOK® Guide is to define the profession of business
analysis and provide a set of commonly accepted practices. It helps practitioners
discuss and define the skills necessary to effectively perform business analysis
work. The BABOK® Guide also helps people who work with and employ business
analysts to understand the skills and knowledge they should expect from a skilled
practitioner.
Business analysis is a broad profession in which business analysts might perform
work for many different types of initiatives across an enterprise. Practitioners may
employ different competencies, knowledge, skills, terminology, and attitudes that
they use when performing business analysis tasks. The BABOK® Guide is a
common framework for all perspectives, describing business analysis tasks that
are performed to properly analyze a change or evaluate the necessity for a
change. Tasks may vary in form, order, or importance for individual business
analysts or for various initiatives.
The six knowledge areas of the BABOK® Guide (Business Analysis Planning and
Monitoring, Elicitation and Collaboration, Requirements Life Cycle Management,
Strategy Analysis, Requirements Analysis and Design Definition (RADD), and



What is Business Analysis?
Introduction
2
Solution Evaluation) describe the practice of business analysis as it is applied
within the boundaries of a project or throughout enterprise evolution and
continuous improvement. The following image shows how three of the
knowledge areas support the delivery of business value before, during, and after
the life cycle of a project.
Figure 1.1.1: Business Analysis Beyond Projects
1.2
What is Business Analysis?
Business analysis is the practice of enabling change in an enterprise by defining
needs and recommending solutions that deliver value to stakeholders. Business
analysis enables an enterprise to articulate needs and the rationale for change,
and to design and describe solutions that can deliver value.
Business analysis is performed on a variety of initiatives within an enterprise.
Initiatives may be strategic, tactical, or operational. Business analysis may be
performed within the boundaries of a project or throughout enterprise evolution
and continuous improvement. It can be used to understand the current state, to
define the future state, and to determine the activities required to move from the
current to the future state.
Business analysis can be performed from a diverse array of perspectives. The
BABOK® Guide describes several of these perspectives: agile, business
intelligence, information technology, business architecture, and business process
management. A perspective can be thought of as a lens through which the
business analysis practitioner views their work activities based on the current
context. One or many perspectives may apply to an initiative, and the perspectives
outlined in the BABOK® Guide do not represent all the contexts for business
analysis or the complete set of business analysis disciplines.
1.3
Who is a Business Analyst?
A business analyst is any person who performs business analysis tasks described in
the BABOK® Guide, no matter their job title or organizational role. Business
analysts are responsible for discovering, synthesizing, and analyzing information
Pre-Project
Post-Project
Benefits
Project
Delivery
Strategy Analysis
RADD
Rationale
Project
Solution Evaluation



Introduction
Structure of the BABOK® Guide
3
from a variety of sources within an enterprise, including tools, processes,
documentation, and stakeholders. The business analyst is responsible for eliciting
the actual needs of stakeholders—which frequently involves investigating and
clarifying their expressed desires—in order to determine underlying issues and
causes.
Business analysts play a role in aligning the designed and delivered solutions with
the needs of stakeholders. The activities that business analysts perform include:
• understanding enterprise problems and goals,
• analyzing needs and solutions,
• devising strategies,
• driving change, and
• facilitating stakeholder collaboration.
Other common job titles for people who perform business analysis include:
• business architect,
• business systems analyst,
• data analyst,
• enterprise analyst,
• management consultant,
• process analyst,
• product manager,
• product owner,
• requirements engineer, and
• systems analyst.
1.4
Structure of the BABOK® Guide
The core content of the BABOK® Guide is composed of business analysis tasks
organized into knowledge areas. Knowledge areas are a collection of logically
(but not sequentially) related tasks. These tasks describe specific activities that
accomplish the purpose of their associated knowledge area.
The Business Analysis Key Concepts, Underlying Competencies, Techniques, and
Perspectives sections form the extended content in the BABOK® Guide that helps
guide business analysts to better perform business analysis tasks.
• Business Analysis Key Concepts: define the key terms needed to
understand all other content, concepts, and ideas within the BABOK®
Guide.
• Underlying Competencies: provide a description of the behaviours,
characteristics, knowledge, and personal qualities that support the effective
practice of business analysis.



Structure of the BABOK® Guide
Introduction
4
• Techniques: provide a means to perform business analysis tasks. The
techniques described in the BABOK® Guide are intended to cover the most
common and widespread techniques practiced within the business analysis
community.
• Perspectives: describe various views of business analysis. Perspectives help
business analysts working from various points of view to better perform
business analysis tasks, given the context of the initiative.
1.4.1
Key Concepts
The Business Analysis Key Concepts chapter provides a basic understanding of
the central ideas necessary for understanding the BABOK® Guide.
This chapter consists of:
• Business Analysis Core Concept Model™ (BACCM™)
• Key Terms
• Requirements Classification Schema
• Stakeholders
• Requirements and Design
1.4.2
Knowledge Areas
Knowledge areas represent areas of specific business analysis expertise that
encompass several tasks.
The six knowledge areas are:
Each knowledge
area includes a
visual
representation of
its inputs and
outputs.
• Business Analysis Planning and Monitoring: describes the tasks that
business analysts perform to organize and coordinate the efforts of
business analysts and stakeholders. These tasks produce outputs that are
used as key inputs and guidelines for the other tasks throughout the
BABOK® Guide.
• Elicitation and Collaboration: describes the tasks that business analysts
perform to prepare for and conduct elicitation activities and confirm the
results obtained. It also describes the communication with stakeholders
once the business analysis information is assembled and the ongoing
collaboration with them throughout the business analysis activities.
• Requirements Life Cycle Management: describes the tasks that business
analysts perform in order to manage and maintain requirements and design
information from inception to retirement. These tasks describe establishing
meaningful relationships between related requirements and designs, and
assessing, analyzing and gaining consensus on proposed changes to
requirements and designs.
• Strategy Analysis: describes the business analysis work that must be
performed to collaborate with stakeholders in order to identify a need of
strategic or tactical importance (the business need), enable the enterprise to



Introduction
Structure of the BABOK® Guide
5
address that need, and align the resulting strategy for the change with
higher- and lower-level strategies.
• Requirements Analysis and Design Definition: describes the tasks that
business analysts perform to structure and organize requirements
discovered during elicitation activities, specify and model requirements and
designs, validate and verify information, identify solution options that meet
business needs, and estimate the potential value that could be realized for
each solution option. This knowledge area covers the incremental and
iterative activities ranging from the initial concept and exploration of the
need through the transformation of those needs into a particular
recommended solution.
• Solution Evaluation: describes the tasks that business analysts perform to
assess the performance of and value delivered by a solution in use by the
enterprise, and to recommend removal of barriers or constraints that
prevent the full realization of the value.
The following diagram shows a general relationship between the knowledge
areas.
Figure 1.4.1: Relationships Between Knowledge Areas
1.4.3
Tasks
A task is a discrete piece of work that may be performed formally or informally as
part of business analysis. The BABOK® Guide defines a list of business analysis
tasks. The definition of a given task is universally applicable to business analysis
efforts, independent of the initiative type. A business analyst may perform other
Business Analysis
Planning and
Monitoring
Requirements Life
Cycle Management
Solution Evaluation
Elicitation and
Collaboration
Requirements
Analysis and Design
Definition
Strategy Analysis



Structure of the BABOK® Guide
Introduction
6
activities as assigned by their organization, but these additional activities are not
considered to be part of the business analysis profession.
Tasks are grouped into knowledge areas. Business analysts perform tasks from all
knowledge areas sequentially, iteratively, or simultaneously. The BABOK® Guide
does not prescribe a process or an order in which tasks are performed. Tasks may
be performed in any order, as long as the necessary inputs to a task are present.
A business analysis initiative may start with any task, although likely candidates
are Analyze Current State (p. 103) or Measure Solution Performance (p. 166).
Each task in the BABOK® Guide is presented in the following format:
• Purpose
• Description
• Inputs
• Elements
• Guidelines/Tools
• Techniques
• Stakeholders
• Outputs
.1 Purpose
The Purpose section provides a short description of the reason for a business
analyst to perform the task, and the value created through performing the task.
.2 Description
The Description section explains in greater detail what the task is, why it is
performed, and what it should accomplish.
.3 Inputs
The Inputs section lists the inputs for the task. Inputs are information consumed
or transformed to produce an output, and represent the information necessary
for a task to begin. They may be explicitly generated outside the scope of
business analysis or generated by a business analysis task. Inputs that are
generated outside of the business analysis efforts are identified with the qualifier
'(external)' in the input list.
There is no assumption that the presence of an input means that the associated
deliverable is complete or in its final state. The input only needs to be sufficiently
complete to allow successive work to begin. Any number of instances of an input
may exist during the life cycle of an initiative.
The Inputs section includes a visual representation of the inputs and outputs, the
other tasks that use the outputs, as well as the guidelines and tools listed in the
task.



Introduction
Structure of the BABOK® Guide
7
.4 Elements
The Elements section describes the key concepts that are needed to understand
how to perform the task. Elements are not mandatory as part of performing a
task, and their usage might depend upon the business analysis approach.
.5 Guidelines and Tools
The Guidelines and Tools section lists resources that are required to transform the
input into an output. A guideline provides instructions or descriptions on why or
how to undertake a task. A tool is something used to undertake a task.
Guidelines and tools can include outputs of other tasks.
.6 Techniques
The Techniques section lists the techniques that can be used to perform the
business analysis task.
.7 Stakeholders
The Stakeholders section is composed of a generic list of stakeholders who are
likely to participate in performing that task or who will be affected by it. The
BABOK® Guide does not mandate that these roles be filled for any given
initiative.
.8 Outputs
The Outputs section describes the results produced by performing the task.
Outputs are created, transformed, or changed in state as a result of the successful
completion of a task. An output may be a deliverable or be a part of a larger
deliverable. The form of an output is dependent on the type of initiative
underway, standards adopted by the organization, and best judgment of the
business analyst as to an appropriate way to address the information needs of key
stakeholders.
As with inputs, an instance of a task may be completed without an output being
in its final state. Tasks that use a specific output do not necessarily have to wait
for its completion for work within the task to begin.
1.4.4
Underlying Competencies
Underlying competencies reflect knowledge, skills, behaviours, characteristics,
and personal qualities that help one successfully perform the role of the business
analyst. These underlying competencies are not unique to the business analysis
profession. However, successful execution of tasks and techniques is often
dependent on proficiency in one or more underlying competencies.
Underlying competencies have the following structure:
• Purpose
• Definition
• Effectiveness Measures



Structure of the BABOK® Guide
Introduction
8
.1 Purpose
The Purpose section describes why it is beneficial for business analysts to have this
underlying competency.
.2 Definition
The Definition section describes the skills and expertise involved in the application
of this competency.
.3 Effectiveness Measures
The Effectiveness Measures section describes how to determine whether a person
is demonstrating skills in this underlying competency.
1.4.5
Techniques
Techniques provide additional information on ways that a task may be performed.
The list of techniques included in the BABOK® Guide is not exhaustive. There are
multiple techniques that may be applied alternatively or in conjunction with other
techniques to accomplish a task. Business analysts are encouraged to modify
existing techniques or engineer new ones to best suit their situation and the goals
of the tasks they perform.
Techniques have the following structure:
• Purpose
• Description
• Elements
• Usage Considerations
.1 Purpose
The Purpose section describes what the technique is used for and the
circumstances under which it is most likely to be applicable.
.2 Description
The Description section describes what the technique is and how it is used.
.3 Elements
The Elements section describes key concepts that are needed to understand how
to use the technique.
.4 Usage Considerations
The Usage Considerations section describes the conditions under which the
technique may be more or less effective.



Introduction
Structure of the BABOK® Guide
9
1.4.6
Perspectives
Perspectives are used within business analysis work to provide focus to tasks and
techniques specific to the context of the initiative. Most initiatives are likely to
engage one or more perspectives. The perspectives included in the BABOK®
Guide are:
• Agile
• Business Intelligence
• Information Technology
• Business Architecture
• Business Process Management
These perspectives do not presume to represent all the possible perspectives from
which business analysis is practiced. The perspectives discussed in the BABOK®
Guide represent some of the more common views of business analysis at the time
of writing.
Perspectives are not mutually exclusive, in that a given initiative might employ
more than one perspective.
Perspectives have the following structure:
• Change Scope
• Business Analysis Scope
• Methodologies, Approaches, and Techniques
• Underlying Competencies
• Impact on Knowledge Areas
.1 Change Scope
The Change Scope section describes what parts of the enterprise the change
encompasses when viewed from this perspective and to what extent it impacts
both the objectives and operations of the enterprise. The change scope also
identifies the type of problems solved, the nature of the solutions being sought,
and the approach to delivering these solutions and measuring their value.
.2 Business Analysis Scope
The Business Analysis Scope section describes the key stakeholders, including a
profile of the likely types of sponsors, the target stakeholders, and the business
analyst's role within an initiative. It also defines likely outcomes that would be
expected from business analysis work in this perspective.
.3 Methodologies, Approaches, and Techniques
The composition of this section is unique to each perspective. In each case it
describes the methodologies, approaches, or techniques that are common and
specific to the application of business analysis in the perspective. Methodologies



Structure of the BABOK® Guide
Introduction
10
and approaches are specialized ways of undertaking the business analysis work.
The techniques included in this section are techniques that are not included in the
Techniques chapter of the BABOK® Guide but are especially relevant to the
perspective.
In the Business Architecture perspective, reference models are listed instead of
methodologies or approaches. In the Business Process Management perspective,
frameworks are listed instead of approaches.
.4 Underlying Competencies
The Underlying Competencies section describes the competencies that are most
prevalent in the perspective.
.5 Impact on Knowledge Areas
The Impact on Knowledge Areas section describes how knowledge areas are
applied or modified. It also explains how specific activities within a perspective are
mapped to tasks in the BABOK® Guide.



11
2
Business Analysis Key Concepts
The Business Analysis Key Concepts chapter includes information that provides a
foundation for all other content, concepts, and ideas within the BABOK® Guide.
It provides business analysts with a basic understanding of the central ideas
necessary for understanding and employing the BABOK® Guide in their daily
practice of business analysis.
This chapter consists of:
• Business Analysis Core Concept Model™ (BACCM™): defines a
conceptual framework for the business analysis profession.
• Key Terms: provides definitions of essential concepts, which are
highlighted because of their importance to the BABOK® Guide.
• Requirements Classification Schema: identifies levels or types of
requirements that assist the business analyst and other stakeholders in
categorizing requirements.
• Stakeholders: defines roles, and characteristics of groups or individuals
participating in or affected by the business analysis activities within a
change.
• Requirements and Designs: describes the distinction between—and the
importance of—requirements and designs as they relate to business
analysis.



The Business Analysis Core Concept Model™
Business Analysis Key Concepts
12
2.1
The Business Analysis Core Concept Model™
The Business Analysis Core Concept Model™ (BACCM™) is a conceptual
framework for business analysis. It encompasses what business analysis is and
what it means to those performing business analysis tasks regardless of
perspective, industry, methodology, or level in the organization. It is composed of
six terms that have a common meaning to all business analysts and helps them
discuss both business analysis and its relationships with common terminology.
Each of these terms is considered to be a core concept.
The six core concepts in the BACCM are: Change, Need, Solution, Stakeholder,
Value, and Context. Each core concept is an idea fundamental to the practice of
business analysis, and all the concepts are equal and necessary. Each core concept
is defined by the other five core concepts and cannot be fully understood until all
the concepts are understood. No single concept holds greater importance or
significance over any other concept. These concepts are instrumental to
understanding the type of information elicited, analyzed, or managed in business
analysis tasks.
The BACCM can be used to:
• describe the profession and domain of business analysis,
• communicate about business analysis with a common terminology,
• evaluate the relationships of key concepts in business analysis,
• perform better business analysis by holistically evaluating the relationships
among these six concepts, and
• evaluate the impact of these concepts and relationships at any point during
a work effort in order to establish both a foundation and a path forward.
Table 2.1.1: The BACCM
Core Concept
Description
Change
The act of transformation in response to a need.
Change works to improve the performance of an enterprise.
These improvements are deliberate and controlled through
business analysis activities.
Need
A problem or opportunity to be addressed.
Needs can cause changes by motivating stakeholders to act.
Changes can also cause needs by eroding or enhancing the
value delivered by existing solutions.
Solution
A specific way of satisfying one or more needs in a context.
A solution satisfies a need by resolving a problem faced by
stakeholders or enabling stakeholders to take advantage of
an opportunity.



Business Analysis Key Concepts
The Business Analysis Core Concept Model™
13
The core concepts can be used by business analysts to consider the quality and
completeness of the work being done. Within each knowledge area description
there are examples of how the core concepts may be used and/or applied during
the tasks within the knowledge area. While planning or performing a task or
technique, business analysts can consider how each core concept is addressed by
asking questions such as:
• What are the kinds of changes we are doing?
• What are the needs we are trying to satisfy?
• What are the solutions we are creating or changing?
Stakeholder
A group or individual with a relationship to the change, the
need, or the solution.
Stakeholders are often defined in terms of interest in, impact
on, and influence over the change. Stakeholders are
grouped based on their relationship to the needs, changes,
and solutions.
Value
The worth, importance, or usefulness of something to a
stakeholder within a context.
Value can be seen as potential or realized returns, gains, and
improvements. It is also possible to have a decrease in value
in the form of losses, risks, and costs.
Value can be tangible or intangible. Tangible value is directly
measurable. Tangible value often has a significant monetary
component. Intangible value is measured indirectly.
Intangible value often has a significant motivational
component, such as a company's reputation or employee
morale.
In some cases, value can be assessed in absolute terms, but
in many cases is assessed in relative terms: one solution
option is more valuable than another from the perspective of
a given set of stakeholders.
Context
The circumstances that influence, are influenced by, and
provide understanding of the change.
Changes occur within a context. The context is everything
relevant to the change that is within the environment.
Context may include attitudes, behaviours, beliefs,
competitors, culture, demographics, goals, governments,
infrastructure, languages, losses, processes, products,
projects, sales, seasons, terminology, technology, weather,
and any other element meeting the definition.
Table 2.1.1: The BACCM (Continued)
Core Concept
Description



Key Terms
Business Analysis Key Concepts
14
• Who are the stakeholders involved?
• What do stakeholders consider to be of value?
• What are the contexts that we and the solution are in?
If any of the core concepts experience a change, it should cause us to re-evaluate
these core concepts and their relationships to value delivery.
Figure 2.1.1: The BACCM
2.2
Key Terms
Business Analysis
For more
information, see
What is Business
Analysis? (p. 2).
The BABOK® Guide describes and defines business analysis as the practice of
enabling change in an enterprise by defining needs and recommending solutions
that deliver value to stakeholders.
Business Analysis Information
Business analysis information refers to the broad and diverse sets of information
that business analysts analyze, transform, and report. It is information of any
Stakeholders
Contexts
Solutions
Needs
Value
Changes



Business Analysis Key Concepts
Key Terms
15
kind—at any level of detail—that is used as an input to, or is an output of,
business analysis work. Examples of business analysis information include
elicitation results, requirements, designs, solution options, solution scope, and
change strategy.
It is essential to expand the object of many business analysis activities from
'requirements' to 'information' to ensure that all inputs and outputs of business
analysis are subject to the tasks and activities described in the BABOK® Guide. For
example, when performing 'Plan Business Analysis Information Management' it
includes all the examples listed above. If the BABOK® Guide described 'Plan
Requirements Management', it would exclude important outputs like elicitation
results, solution options, and change strategy.
Design
For more
information, see
Requirements and
Designs (p. 19).
A design is a usable representation of a solution. Design focuses on
understanding how value might be realized by a solution if it is built. The nature
of the representation may be a document (or set of documents) and can vary
widely depending on the circumstances.
Enterprise
An enterprise is a system of one or more organizations and the solutions they use
to pursue a shared set of common goals. These solutions (also referred to as
organizational capabilities) can be processes, tools or information. For the
purpose of business analysis, enterprise boundaries can be defined relative to the
change and need not be constrained by the boundaries of a legal entity,
organization, or organizational unit. An enterprise may include any number of
business, government, or any other type of organization.
Organization
An autonomous group of people under the management of a single individual or
board, that works towards common goals and objectives. Organizations often
have a clearly defined boundary and operate on a continuous basis, as opposed
to an initiative or project team, which may be disbanded once its objectives are
achieved.
Plan
A plan is a proposal for doing or achieving something. Plans describe a set of
events, the dependencies among the events, the expected sequence, the
schedule, the results or outcomes, the materials and resources needed, and the
stakeholders involved.
Requirement
For more
information, see
Requirements and
Designs (p. 19).
A requirement is a usable representation of a need. Requirements focus on
understanding what kind of value could be delivered if a requirement is fulfilled.
The nature of the representation may be a document (or set of documents), but
can vary widely depending on the circumstances.



Requirements Classification Schema
Business Analysis Key Concepts
16
Risk
Risk is the effect of uncertainty on the value of a change, a solution, or the
enterprise. Business analysts collaborate with other stakeholders to identify,
assess, and prioritize risks, and to deal with those risks by altering the likelihood of
the conditions or events that lead to the uncertainty: mitigating the
consequences, removing the source of the risk, avoiding the risk altogether by
deciding not to start or continue with an activity that leads to the risk, sharing the
risk with other parties, or accepting or even increasing the risk to deal with an
opportunity.
2.3
Requirements Classification Schema
For the purposes of the BABOK® Guide, the following classification schema
describes requirements:
• Business requirements: statements of goals, objectives, and outcomes
that describe why a change has been initiated. They can apply to the whole
of an enterprise, a business area, or a specific initiative.
• Stakeholder requirements: describe the needs of stakeholders that must
be met in order to achieve the business requirements. They may serve as a
bridge between business and solution requirements.
• Solution requirements: describe the capabilities and qualities of a
solution that meets the stakeholder requirements. They provide the
appropriate level of detail to allow for the development and
implementation of the solution. Solution requirements can be divided into
two sub-categories:
• functional requirements: describe the capabilities that a solution
must have in terms of the behaviour and information that the solution
will manage, and
For more
information, see
Non-Functional
Requirements
Analysis (p. 302).
• non-functional requirements or quality of service requirements:
do not relate directly to the behaviour of functionality of the solution,
but rather describe conditions under which a solution must remain
effective or qualities that a solution must have.
• Transition requirements: describe the capabilities that the solution must
have and the conditions the solution must meet to facilitate transition from
the current state to the future state, but which are not needed once the
change is complete. They are differentiated from other requirements types
because they are of a temporary nature. Transition requirements address
topics such as data conversion, training, and business continuity.
2.4
Stakeholders
Each task includes a list of stakeholders who are likely to participate in the
execution of that task or who will be affected by it. A stakeholder is an individual
or group that a business analyst is likely to interact with directly or indirectly. The



Business Analysis Key Concepts
Stakeholders
17
BABOK® Guide does not mandate that these roles be filled for any given
initiative. Any stakeholder can be a source of requirements, assumptions, or
constraints.
This list is not intended to be an exhaustive list of all possible stakeholder
classifications. Some additional examples of people who fit into each of these
generic roles are listed in the definitions below. In most cases there will be
multiple stakeholder roles found within each category. Similarly, a single
individual may fill more than one role.
For the purpose of the BABOK® Guide, the generic list of stakeholders includes
the following roles:
• business analyst,
• customer,
• domain subject matter expert,
• end user,
• implementation subject matter
expert,
• operational support,
• project manager,
• regulator,
• sponsor,
• supplier, and
• tester.
2.4.1
Business Analyst
The business analyst is inherently a stakeholder in all business analysis activities.
The BABOK® Guide presumes that the business analyst is responsible and
accountable for the execution of these activities. In some cases the business
analyst may also be responsible for performing activities that fall under another
stakeholder role.
2.4.2
Customer
A customer uses or may use products or services produced by the enterprise and
may have contractual or moral rights that the enterprise is obliged to meet.
2.4.3
Domain Subject Matter Expert
A domain subject matter expert is any individual with in-depth knowledge of a
topic relevant to the business need or solution scope. This role is often filled by
people who may be end users or people who have in-depth knowledge of the
solution such as managers, process owners, legal staff, consultants, and others.
2.4.4
End User
End users are stakeholders who directly interact with the solution. End users can
include all participants in a business process, or who use the product or solution.
2.4.5
Implementation Subject Matter Expert
An implementation subject matter expert is any stakeholder who has specialized
knowledge regarding the implementation of one or more solution components.



Stakeholders
Business Analysis Key Concepts
18
While it is not possible to define a listing of implementation subject matter expert
roles that are appropriate for all initiatives, some of the most common roles are:
project librarian, change manager, configuration manager, solution architect,
developer, database administrator, information architect, usability analyst, trainer,
and organizational change consultant.
2.4.6
Operational Support
Operational support is responsible for the day-to-day management and
maintenance of a system or product.
While it is not possible to define a listing of operational support roles that are
appropriate for all initiatives, some of the most common roles are: operations
analyst, product analyst, help desk, and release manager.
2.4.7
Project Manager
Project managers are responsible for managing the work required to deliver a
solution that meets a business need, and for ensuring that the project's objectives
are met while balancing the project factors including scope, budget, schedule,
resources, quality, and risk.
While it is not possible to completely define a listing of project management roles
that are appropriate for all initiatives, some of the most common roles are: project
lead, technical lead, product manager, and team leader.
2.4.8
Regulator
Regulators are responsible for the definition and enforcement of standards.
Standards can be imposed on the solution by regulators through legislation,
corporate governance standards, audit standards, or standards defined by
organizational centers of competency. Alternate roles are government, regulatory
bodies, and auditor.
2.4.9
Sponsor
Sponsors are responsible for initiating the effort to define a business need and
develop a solution that meets that need. They authorize the work to be
performed, and control the budget and scope for the initiative. Alternate roles are
executive and project sponsor.
2.4.10
Supplier
A supplier is a stakeholder outside the boundary of a given organization or
organizational unit. Suppliers provide products or services to the organization and
may have contractual or moral rights and obligations that must be considered.
Alternate roles are providers, vendors, and consultants.



Business Analysis Key Concepts
Requirements and Designs
19
2.4.11
Tester
Testers are responsible for determining how to verify that the solution meets the
requirements defined by the business analyst, as well as conducting the
verification process. Testers also seek to ensure that the solution meets applicable
quality standards, and that the risk of defects or failures is understood and
minimized. An alternate role is quality assurance analyst.
2.5
Requirements and Designs
Eliciting, analyzing, validating, and managing requirements have consistently
been recognized as key activities of business analysis. However, it is important to
recognize that business analysts are also responsible for the definition of design,
at some level, in an initiative. The level of responsibility for design varies based on
the perspective within which a business analyst is working.
Requirements are focused on the need; designs are focused on the solution. The
distinction between requirements and designs is not always clear. The same
techniques are used to elicit, model, and analyze both. A requirement leads to a
design which in turn may drive the discovery and analysis of more requirements.
The shift in focus is often subtle.
The classification as a requirement or a design may become less significant as the
business analyst's work progresses to a greater understanding of and eventual
fulfillment of the need. The tasks in the BABOK® Guide such as Trace
Requirements (p. 79) or Specify and Model Requirements (p. 136) may refer to
requirements, but the intent is to include designs as well.
Business analysis can be complex and recursive. A requirement (or set of
requirements) may be used to define a design. That design may then be used to
elicit additional requirements that are used to define more detailed designs. The
business analyst may hand off requirements and designs to other stakeholders
who may further elaborate on the designs. Whether it is the business analyst or
some other role that completes the designs, the business analyst often reviews
the final designs to ensure that they align with the requirements.
The following table provides some basic examples of how information may be
viewed as either a requirement or a design.
Table 2.5.1: Requirements and Design
Requirement
Design
View six months sales data across multiple
organizational units in a single view.
A sketch of a dashboard.
Reduce amount of time required to pick
and pack a customer order.
Process model.
Record and access a medical patient’s
history.
Screen mock-up showing specific
data fields.



Requirements and Designs
Business Analysis Key Concepts
20
Stakeholders may present a need or a solution to an assumed need. A business
analyst uses activities found in Elicitation and Collaboration (p. 53), Strategy
Analysis (p. 99), Requirements Analysis and Design Definition (p. 133), and
Solution Evaluation (p. 163) to transform that request into a requirement or
design. Regardless of the focus of the stakeholder, the importance of the role of
the business analyst lies in continuously asking the question ‘why?’. For example,
“Why is either the requirement or design necessary to provide value to an
enterprise and to facilitate the realization of an enterprise’s goals and objectives?”
Figure 2.5.1: Requirements and Design Cycle
Develop business strategy, goals, and
objectives for a new business.
Business Capability Model.
Provide information in English and French.
Prototype with text displayed in
English and French.
Table 2.5.1: Requirements and Design (Continued)
Requirement
Design
Transition
Requirements
What are the
conditions?
Business
Requirements
Why do I want it?
Solution
Requirements
What do I want?
Stakeholder
Requirements
What are the needs?
Cycle continues until
requirements are met.
A
ss
es
s
O
ut
co
m
es
De
si
gn
D
es
ig
n
D
es
ig
n



21
3
Business Analysis Planning
and Monitoring
The Business Analysis Planning and Monitoring knowledge area tasks organize
and coordinate the efforts of business analysts and stakeholders. These tasks
produce outputs that are used as key guidelines for the other tasks throughout
the BABOK® Guide.
The Business Analysis Planning and Monitoring knowledge area includes the
following tasks:
• Plan Business Analysis Approach: describes the planning of business
analysis work from creation or selection of a methodology to planning the
individual activities, tasks, and deliverables.
• Plan Stakeholder Engagement: describes understanding which
stakeholders are relevant to the change, what business analysts need from
them, what they need from business analysts, and the best way to
collaborate.
• Plan Business Analysis Governance: defines the components of business
analysis that are used to support the governance function of the
organization. It helps ensure that decisions are made properly and
consistently, and follows a process that ensures decision makers have the
information they need. Examples of this include requirements
management, business analysis risk management, and allocation of
business analysis resources.
• Plan Business Analysis Information Management: defines how
information developed by business analysts (including requirements and
designs) is captured, stored, and integrated with other information for
long-term use.



Business Analysis Planning and Monitoring
22
• Identify Business Analysis Performance Improvements: describes
managing and monitoring how business analysis work is performed to
ensure that commitments are met and continuous learning and
improvement opportunities are realized.
The Core Concept Model in Business Analysis
Planning and Monitoring
The Business Analysis Core Concept Model™ (BACCM™) describes the
relationships among the six core concepts. The following table describes the
usage and application of each of the core concepts within the context of Business
Analysis Planning and Monitoring.
Table 3.0.1: The Core Concept Model in Business Analysis Planning and Monitoring
Core Concept
During Business Analysis Planning and
Monitoring, business analysts...
Change: the act of
transformation in response to a
need.
are responsible for determining how
changes to business analysis results will
be requested and authorized.
Need: a problem or opportunity
to be addressed.
choose a business analysis approach that
provides adequate analysis for the
change.
Solution: a specific way of
satisfying one or more needs in a
context.
evaluate if business analysis performance
was a key contributor to the successful
implementation of a solution.
Stakeholder: a group or
individual with a relationship to
the change, the need, or the
solution.
perform a stakeholder analysis to ensure
planning and monitoring activities reflect
stakeholder needs and account for
stakeholder characteristics.
Value: the worth, importance, or
usefulness of something to a
stakeholder within a context.
conduct performance analysis to ensure
business analysis activities continue to
produce sufficient value for the
stakeholders.
Context: the circumstances that
influence, are influenced by, and
provide understanding of the
change.
ensure a complete understanding of the
context under analysis in order to develop
an efficient business analysis approach.



Business Analysis Planning and Monitoring
23
Figure 3.0.1: Business Analysis Planning and Monitoring Input/Output Diagram
Input
Tasks
3.3
Plan Business
Analysis
Governance
3.2
Plan Stakeholder
Engagement
3.1
Plan Business
Analysis Approach
3.4
Plan Business
Analysis
Information
Management
3.5
Identify Business
Analysis
Performance
Improvements
Needs
Performance
Objectives (external)
3.1
Business Analysis
Approach
3.2
Stakeholder
Engagement
Approach
3.3
Governance Approach
3.5
Business Analysis
Performance
Assessment
3.4
Information
Management
Approach
Output



Plan Business Analysis Approach
Business Analysis Planning and Monitoring
24
3.1
Plan Business Analysis Approach
3.1.1
Purpose
The purpose of Plan Business Analysis Approach is to define an appropriate
method to conduct business analysis activities.
3.1.2
Description
Business analysis approaches describe the overall method that will be followed
when performing business analysis work on a given initiative, how and when
tasks will be performed, and the deliverables that will be produced.
The business analyst may also identify an initial set of techniques to use. This list
may change as the initiative proceeds and the business analyst gains a deeper
understanding of the change and its stakeholders.
The business analysis approach may be defined by a methodology or by
organizational standards. In some organizations, elements of the business
analysis approach may be standardized and formalized into a repeatable business
analysis process which can be leveraged for each effort. Even where a standard
approach exists, it may be tailored to the needs of a specific initiative. Tailoring
may be governed by standards that define which approaches are permitted,
which elements of those processes may be tailored, and general guidelines for
selecting a process.
If organizational standards do not exist, the business analyst works with the
appropriate stakeholders to determine how the work will be completed. For
example, if the change is delivered via a project, the standards and approach may
be developed during the project planning phase.
The business analysis approach should:
• align to the overall goals of the change,
• coordinate the business analysis tasks with the activities and deliverables of
the overall change,
• include tasks to manage any risks that could reduce the quality of business
analysis deliverables or impede task efficiency, and
• leverage approaches and select techniques and tools that have historically
worked well.
3.1.3
Inputs
• Needs: the business analysis approach is shaped by the problem or opportunity
faced by the organization. It is necessary to consider what is known about the
need at the time of planning, while acknowledging that understanding evolves
throughout business analysis activities.



Business Analysis Planning and Monitoring
Plan Business Analysis Approach
25
Figure 3.1.1: Plan Business Analysis Approach Input/Output Diagram
Input
Guidelines and Tools
Tasks Using This Output
Output
3.1 Plan Business Analysis
Approach
Business Analysis
Performance Assessment
3.1
Business Analysis
Approach
3.2
Plan Stakeholder
Engagement
Needs
Business Policies
Expert Judgment
Methodologies and
Frameworks
Stakeholder Engagement
Approach
3.3
Plan Business
Analysis
Governance
3.4
Plan Business
Analysis
Information
Management
3.5
Identify Business
Analysis
Performance
Improvements
4.1
Prepare for
Elicitation
4.2
Conduct Elicitation
4.4
Communicate
Business Analysis
Information
4.5
Manage
Stakeholder
Collaboration
6.1
Analyze Current
State
6.3
Assess Risks
6.4
Define Change
Strategy



Plan Business Analysis Approach
Business Analysis Planning and Monitoring
26
3.1.4
Elements
.1 Planning Approach
There are various planning methods used across perspectives, industries, and
enterprises. Many planning methods fit somewhere along a continuum between
predictive and adaptive approaches.
Predictive approaches focus on minimizing upfront uncertainty and ensuring that
the solution is defined before implementation begins in order to maximize control
and minimize risk. These approaches are often preferred in situations where
requirements can effectively be defined ahead of implementation, the risk of an
incorrect implementation is unacceptably high, or when engaging stakeholders
presents significant challenges.
Adaptive approaches focus on rapid delivery of business value in short iterations
in return for acceptance of a higher degree of uncertainty regarding the overall
delivery of the solution. These approaches tend to be preferred when taking an
exploratory approach to finding the best solution or for incremental improvement
of an existing solution.
Different approaches may be used within the same initiative. Among other
factors, the business analyst may consider the organization’s standards, tolerance
for uncertainty, and previous experience with different approaches when
planning for business analysis activities.
Regardless of the approach, planning is an essential task to ensure value is
delivered to an enterprise. Planning typically occurs more than once on a given
initiative as plans are updated to address changing business conditions and newly
raised issues. The business analysis approach should describe how plans will be
altered if changes are required.
.2 Formality and Level of Detail of Business Analysis Deliverables
When defining the business analysis approach, consider the level of formality that
is appropriate for approaching and planning the initiative.
Predictive approaches typically call for formal documentation and
representations. Business analysis information may be captured in a formal
document or set of representations following standardized templates.
Information is captured at various levels of detail. The specific content and format
of business analysis information can vary depending on the organizational
methodologies, processes, and templates in use.
Adaptive approaches favour defining requirements and designs through team
interaction and gathering feedback on a working solution. Mandatory
requirements representations are often limited to a prioritized requirements list.
Additional business analysis documentation may be created at the discretion of
the team, and generally consists of models developed to enhance the team’s
understanding of a specific problem. Formal documentation is often produced
after the solution is implemented to facilitate knowledge transfer.



Business Analysis Planning and Monitoring
Plan Business Analysis Approach
27
Other considerations that may affect the approach include:
• the change is complex and high risk,
• the organization is in, or interacts with, heavily regulated industries,
• contracts or agreements necessitate formality,
• stakeholders are geographically distributed,
• resources are outsourced,
• staff turnover is high and/or team members may be inexperienced,
• requirements must be formally signed off, and
• business analysis information must be maintained long-term or handed
over for use on future initiatives.
Figure 3.1.2: Formality and Level of Detail of Business Analysis Deliverables
.3 Business Analysis Activities
A business analysis approach provides a description of the types of activities that
the business analyst will perform. Frequently the organization’s adopted
methodologies influence the activities that are selected.
Integrating business analysis activities in the business analysis approach includes:
• identifying the activities required to complete each deliverable and then
breaking each activity into tasks,
• dividing the work into iterations, identifying the deliverables for each
iteration, and then identifying the associated activities and tasks, or
Predictive
Tasks are performed in
specific phases.
Tasks are performed
iteratively.
Solution
Definition
Level of
Formality
Activities
Timing
Activities required to
complete deliverables are
identified first and then
divided into tasks.
Activities are divided into
iterations with deliverables
first and then the associated
tasks are identified.
Formal—information is
captured in standardized
templates.
Informal—information is
gathered through team
interaction and feedback.
Defined before
implementation to maximize
control and minimize risk.
Defined in iterations to
arrive at best solution or
improve an existing solution.
Adaptive
Approach



Plan Business Analysis Approach
Business Analysis Planning and Monitoring
28
• using a previous similar initiative as an outline and applying the detailed
tasks and activities unique to the current initiative.
.4 Timing of Business Analysis Work
Business analysts determine when the business analysis tasks need to be
performed and if the level of business analysis effort will need to vary over time.
This type of planning includes determining whether the business analysis tasks
performed within the other knowledge areas will be performed primarily in
specific phases or iteratively over the course of the initiative.
The timing of business analysis activities can also be affected by:
• the availability of resources,
• priority and/or urgency of the initiative,
• other concurrent initiatives, or
• constraints such as contract terms or regulatory deadlines.
.5 Complexity and Risk
The complexity and size of the change and the overall risk of the effort to the
organization are considered when determining the business analysis approach. As
complexity and risk increase or decrease, the nature and scope of business
analysis work can be altered and reflected in the approach.
The approach may also be altered based on the number of stakeholders or
business analysis resources involved in the initiative. As the number of
stakeholders increases, the approach may be adjusted to include additional
process steps to better manage the business analysis work.
Other factors that can impact complexity include:
• size of the change,
• number of business areas or systems affected,
• geographic and cultural considerations,
• technological complexities, and
• any risks that could impede the business analysis effort.
Factors that can impact the risk level of a business analysis effort include:
• experience level of the business analyst,
• extent of domain knowledge held by the business analyst,
• level of experience stakeholders have in communicating their needs,
• stakeholder attitudes about the change and business analysis in general,
• amount of time allocated by stakeholders to the business analysis activities,
• any pre-selected framework, methodology, tools, and/or techniques



Business Analysis Planning and Monitoring
Plan Business Analysis Approach
29
imposed by organizational policies and practices, and
• cultural norms of the organization.
.6 Acceptance
The business analysis approach is reviewed and agreed upon by key stakeholders.
In some organizations, the business analysis process may be more structured and
require key stakeholders to sign off on the approach to ensure all business
analysis activities have been identified, estimates are realistic, and the proposed
roles and responsibilities are correct. Any issues raised by stakeholders when
reviewing the approach are documented by the business analyst and resolutions
are sought. Stakeholders also play a role in reviewing and accepting changes to
the approach as alterations are made to accommodate changing conditions
across the initiative.
3.1.5
Guidelines and Tools
• Business Analysis Performance Assessment: provides results of previous
assessments that should be reviewed and incorporated into all planning
approaches.
• Business Policies: define the limits within which decisions must be made. They
may be described by regulations, contracts, agreements, deals, warranties,
certifications, or other legal obligations. These policies can influence the
business analysis approach.
• Expert Judgment: used to determine the optimal business analysis approach.
Expertise may be provided from a wide range of sources including stakeholders
on the initiative, organizational Centres of Excellence, consultants, or
associations and industry groups. Prior experiences of the business analyst and
other stakeholders should be considered when selecting or modifying an
approach.
• Methodologies and Frameworks: shape the approach that will be used by
providing methods, techniques, procedures, working concepts, and rules. They
may need to be tailored to better meet the needs of the specific business
challenge.
• Stakeholder Engagement Approach: understanding the stakeholders and
their concerns and interests may influence decisions made when determining
the business analysis approach.
3.1.6
Techniques
• Brainstorming: used to identify possible business analysis activities,
techniques, risks and other relevant items to help build the business analysis
approach.
• Business Cases: used to understand whether elements of the problem or
opportunity are especially time-sensitive, high-value, or whether there is any
particular uncertainty around elements of the possible need or solution.



Plan Business Analysis Approach
Business Analysis Planning and Monitoring
30
• Document Analysis: used to review existing organizational assets that might
assist in planning the approach.
• Estimation: used to determine how long it may take to perform business
analysis activities.
• Financial Analysis: used to assess how different approaches (and the
supported delivery options) affect the value delivered.
• Functional Decomposition: used to break down complex business analysis
processes or approaches into more feasible components.
• Interviews: used to help build the plan with an individual or small group.
• Item Tracking: used to track any issues raised during planning activities with
stakeholders. Can also track risk related items raised during discussions when
building the approach.
• Lessons Learned: used to identify an enterprise’s previous experience (both
successes and challenges) with planning business analysis approach.
• Process Modelling: used to define and document the business analysis
approach.
• Reviews: used to validate the selected business analysis approach with
stakeholders.
• Risk Analysis and Management: used to assess risks in order to select the
proper business analysis approach.
• Scope Modelling: used to determine the boundaries of the solution as an
input to planning and to estimating.
• Survey or Questionnaire: used to identify possible business analysis activities,
techniques, risks and other relevant items to help build the business analysis
approach.
• Workshops: used to help build the plan in a team setting.
3.1.7
Stakeholders
• Domain Subject Matter Expert: can be a source of risk when their
involvement is required and availability is lacking. The approach taken may
depend on availability and level of their involvement with the initiative.
• Project Manager: determines that the approach is realistic for the overall
schedule and timelines. The business analysis approach must be compatible
with other activities.
• Regulator: may be needed to provide approval for aspects of the business
analysis approach or decisions made in tailoring the process, especially in
organizations where the business analysis process is audited.
• Sponsor: can provide needs and objectives for the approach and ensures that
organizational policies are followed. The selected approach may depend on
availability and involvement with the initiative.



Business Analysis Planning and Monitoring
Plan Stakeholder Engagement
31
3.1.8
Outputs
• Business Analysis Approach: identifies the business analysis approach and
activities that will be performed across an initiative including who will perform
the activities, the timing and sequencing of the work, the deliverables that will
be produced and the business analysis techniques that may be utilized. The
remaining outputs of the Business Analysis Planning and Monitoring knowledge
area may be integrated into an overall approach or be independent based upon
methodology, organization, and perspective.
3.2
Plan Stakeholder Engagement
3.2.1
Purpose
The purpose of Plan Stakeholder Engagement is to plan an approach for
establishing and maintaining effective working relationships with the
stakeholders.
3.2.2
Description
Plan Stakeholder Engagement involves conducting a thorough stakeholder
analysis to identify all of the involved stakeholders and analyze their
characteristics. The results of the analysis are then utilized to define the best
collaboration and communication approaches for the initiative and to
appropriately plan for stakeholder risks.
When planning for stakeholder engagement, the degree of complexity can
increase disproportionately as the number of stakeholders involved in the
business analysis activities increases. This is important because new or different
techniques for the management of stakeholders may be required when the
engagement moves from collaborating with a few stakeholders into dozens,
hundreds, or even thousands of people.
3.2.3
Inputs
• Needs: understanding the business need and the parts of the enterprise that it
affects helps in the identification of stakeholders. The need may evolve as
stakeholder analysis is performed.
• Business Analysis Approach: incorporating the overall business analysis
approach into the stakeholder analysis, collaboration, and communication
approaches is necessary to ensure consistency across the approaches.



Plan Stakeholder Engagement
Business Analysis Planning and Monitoring
32
Figure 3.2.1: Plan Stakeholder Engagement Input/Output Diagram
3.2.4
Elements
.1 Perform Stakeholder Analysis
Stakeholder analysis involves identifying the stakeholders (who will be directly or
indirectly impacted by the change) and their characteristics, as well as analyzing
the information once collected. Stakeholder analysis is performed repeatedly as
business analysis activities continue.
A thorough and detailed stakeholder list ensures that stakeholders are not
overlooked. Understanding who the stakeholders are, the impact of proposed
changes on them, and the influence they may have on the change is vital to
understanding what needs, wants, and expectations must be satisfied by a
Tasks Using This Output
Output
3.2 Plan Stakeholder
Engagement
Business Analysis
Performance Assessment
3.2
Stakeholder
Engagement
Approach
3.3
Plan Business
Analysis
Governance
3.1
Business Analysis
Approach
Needs
Change Strategy
Current State Description
3.4
Plan Business
Analysis
Information
Management
4.1
Prepare for
Elicitation
4.5
Manage
Stakeholder
Collaboration
4.2
Conduct Elicitation
4.4
Communicate
Business Analysis
Information
6.3
Assess Risks
6.4
Define Change
Strategy
3.1
Plan Business
Analysis Approach
Input
Guidelines and Tools



Business Analysis Planning and Monitoring
Plan Stakeholder Engagement
33
solution. If stakeholders are not identified, the business analyst may miss
uncovering critical needs. Stakeholder needs uncovered late will often require a
revision to business analysis tasks that are either in progress or are completed.
This can result in increased costs and decreased stakeholder satisfaction.
How business analysts perform stakeholder analysis can vary between projects,
methodologies, and organizations. A company’s organizational chart and
business processes can serve as an initial source for identifying internal
stakeholders. The sponsor may also identify stakeholders. Stakeholders outside
the organization may be identified and can be uncovered by understanding any
existing contracts that may be in place, anticipated vendors that may have a role
based on existing relationships with the organization, as well as regulatory and
governing bodies that may influence the work. Shareholders, customers, and
suppliers are also considered when searching for external stakeholders.
Roles
Business analysts identify stakeholder roles in order to understand where and
how the stakeholders will contribute to the initiative. It is important that the
business analyst is aware of the various roles a stakeholder is responsible for
within the organization.
Attitudes
Stakeholder attitudes can positively or negatively impact a change. Business
analysts identify stakeholder attitudes in order to fully understand what may
impact a stakeholder’s actions and behaviours. Knowing how a stakeholder
perceives the initiative allows an opportunity for the business analyst to
specifically plan their collaboration and engagement with that stakeholder.
Business analysts analyze stakeholder attitudes about:
• business goals, objectives of the initiative, and any proposed solutions,
• business analysis in general,
• the level of interest in the change,
• the sponsor,
• team members and other stakeholders, and
• collaboration and a team-based approach.
Stakeholders with positive attitudes may be strong champions and great
contributors. Other stakeholders may not see value in the work, may
misunderstand the value being provided, or may be concerned about the effect
the change will have on them. Stakeholders who are expected to serve in key
roles and participate heavily in business analysis activities, but who view a change
negatively, may require collaboration approaches that increase their cooperation.
Decision Making Authority
Business analysts identify the authority level a stakeholder possesses over business
analysis activities, deliverables, and changes to business analysis work.



Plan Stakeholder Engagement
Business Analysis Planning and Monitoring
34
Understanding authority levels upfront eliminates confusion during the business
analysis effort and ensures the business analyst collaborates with the proper
stakeholders when looking for a decision to be made or seeking approvals.
Level of Power or Influence
Understanding the nature of influence and the influence structures and channels
within an organization can prove invaluable when seeking to build relationships
and trust. Understanding the influence and attitude each stakeholder may have
can help develop strategies for obtaining buy-in and collaboration. Business
analysts evaluate how much influence is needed to implement a change
compared to the amount of influence the key stakeholders can bring. If there is a
mismatch between the influence required and the amount of influence the
stakeholder has or is perceived to have, business analysts develop risk plans,
responses and other strategies that might be needed to obtain the required level
of support.
.2 Define Stakeholder Collaboration
Ensuring effective collaboration with stakeholders is essential for maintaining
their engagement in business analysis activities. Collaboration can be a
spontaneous event. However, much collaboration is deliberate and planned, with
specific activities and outcomes determined ahead of time during planning
activities.
The business analyst may plan different collaboration approaches for internal and
external stakeholders, and approaches may differ by business analysis activity. The
objective is to select the approaches that work best to meet the needs of each
stakeholder group and ensure their interest and involvement is maintained across
the initiative. Some considerations when planning collaboration include:
• timing and frequency of collaboration,
• location,
• available tools such as wikis and online communities,
• delivery method such as in-person or virtual, and
• preferences of the stakeholders.
Planning considerations can be documented in the form of a stakeholder
collaboration plan. As factors change, plans can be revisited, and adjustments
and adaptations can be made to ensure ongoing engagement of stakeholders.
.3 Stakeholder Communication Needs
The business analyst evaluates:
• what needs to be communicated,
• what is the appropriate delivery method (written or verbal),
• who the appropriate audience is,
• when communication should occur,
• frequency of communication,



Business Analysis Planning and Monitoring
Plan Stakeholder Engagement
35
• geographic location of stakeholders who will receive communications,
• level of detail appropriate for the communication and stakeholder, and
• level of formality of communications.
Communication considerations can be documented in the form of a stakeholder
communication plan. Business analysts build and review communication plans
with stakeholders to ensure their communication requirements and expectations
are met.
3.2.5
Guidelines and Tools
• Business Analysis Performance Assessment: provides results of previous
assessments that should be reviewed and incorporated.
• Change Strategy: used for improved assessment of stakeholder impact and
the development of more effective stakeholder engagement strategies.
• Current State Description: provides the context within which the work needs
to be completed. This information will lead to more effective stakeholder
analysis and better understanding of the impact of the desired change.
3.2.6
Techniques
• Brainstorming: used to produce the stakeholder list and identify stakeholder
roles and responsibilities.
• Business Rules Analysis: used to identify stakeholders who were the source
of the business rules.
• Document Analysis: used to review existing organizational assets that might
assist in planning stakeholder engagement.
• Interviews: used to interact with specific stakeholders to gain more
information or knowledge about stakeholder groups.
• Lessons Learned: used to identify an enterprise’s previous experience (both
successes and challenges) with planning stakeholder engagement.
• Mind Mapping: used to identify potential stakeholders and help understand
the relationships between them.
• Organizational Modelling: used to determine if the organizational units or
people listed have any unique needs and interests that should be considered.
Organizational models describe the roles and functions in the organization and
the ways in which stakeholders interact which can help to identify stakeholders
who will be affected by a change.
• Process Modelling: used to categorize stakeholders by the systems that
support their business processes.
• Risk Analysis and Management: used to identify risks to the initiative
resulting from stakeholder attitudes or the inability of key stakeholders to
participate in the initiative.



Plan Stakeholder Engagement
Business Analysis Planning and Monitoring
36
• Scope Modelling: used to develop scope models to show stakeholders that
fall outside the scope of the solution but still interact with it in some way.
• Stakeholder List, Map, or Personas: used to depict the relationship of
stakeholders to the solution and to one another.
• Survey or Questionnaire: used to identify shared characteristics of a
stakeholder group.
• Workshops: used to interact with groups of stakeholders to gain more
information about stakeholder groups.
3.2.7
Stakeholders
• Customers: a source of external stakeholders.
• Domain Subject Matter Expert: may help to identify stakeholders and may
themselves be identified to fulfill one or more roles on the initiative.
• End User: a source of internal stakeholders.
• Project Manager: may be able to identify and recommend stakeholders.
Responsibility for stakeholder identification and management may be shared
with the business analyst.
• Regulator: may require that specific stakeholder representatives or groups be
involved in the business analysis activities.
• Sponsor: may request that specific stakeholders be involved in the business
analysis activities.
• Supplier: a source of external stakeholders.
3.2.8
Outputs
• Stakeholder Engagement Approach: contains a list of the stakeholders,
their characteristics which were analyzed, and a listing of roles and
responsibilities for the change. It also identifies the collaboration and
communication approaches the business analyst will utilize during the initiative.



Business Analysis Planning and Monitoring
Plan Business Analysis Governance
37
3.3
Plan Business Analysis Governance
3.3.1
Purpose
The purpose of Plan Business Analysis Governance is to define how decisions are
made about requirements and designs, including reviews, change control,
approvals, and prioritization.
3.3.2
Description
Business analysts ensure that a governance process is in place and clarify any
ambiguities within it. A governance process identifies the decision makers,
process, and information required for decisions to be made. A governance
process describes how approvals and prioritization decisions are made for
requirements and designs.
When planning the governance approach, business analysts identify:
• how business analysis work will be approached and prioritized,
• what the process for proposing a change to business analysis information is,
• who has the authority and responsibility to propose changes and who
should be involved in the change discussions,
• who has responsibility for analyzing change requests,
• who has the authority to approve changes, and
• how changes will be documented and communicated.
3.3.3
Inputs
• Business Analysis Approach: incorporating the overall business analysis
approach into the governance approach is necessary to ensure consistency
across the approaches.
• Stakeholder Engagement Approach: identifying stakeholders and
understanding their communication and collaboration needs is useful in
determining their participation in the governance approach. The engagement
approach may be updated based on the completion of the governance
approach.



Plan Business Analysis Governance
Business Analysis Planning and Monitoring
38
Figure 3.3.1: Plan Business Analysis Governance Input/Output Diagram
3.3.4
Elements
.1 Decision Making
Decisions are made throughout the initiative. A stakeholder may serve in various
roles in the decision-making process such as:
• participant in decision-making discussions,
• subject matter expert (SME) lending experience and knowledge to the
decision-making process,
• reviewer of information, and
• approver of decisions.
The decision-making process defines what happens when teams cannot reach
consensus, by identifying escalation paths and key stakeholders who hold final
decision-making authority.
Output
Input
Guidelines and Tools
Tasks Using This Output
3.3 Plan Business Analysis
Governance
Business Analysis
Performance Assessment
3.3
Governance
Approach
3.4
Plan Business
Analysis
Information
Management
3.2 Stakeholder
Engagement
Approach
3.1
Business Analysis
Approach
Business Policies
Current State Description
5.3
Prioritize
Requirements
5.4
Assess
Requirements
Changes
5.5
Approve
Requirements
Legal/Regulatory
Information



Business Analysis Planning and Monitoring
Plan Business Analysis Governance
39
.2 Change Control Process
When business analysts develop a change control process, they:
• Determine the process for requesting changes: specify which
requirements and designs the change control process covers and determine
whether it applies to all changes or only to changes of a specific size, cost,
or level of effort. This process details the steps for proposing a change,
when changes can be proposed, who can propose changes and how
change requests are communicated.
• Determine the elements of the change request: identify the
information to be included in a proposal to support decision making and
implementation if it is approved.
Possible components to consider on a change request are:
• Cost and time estimates: for each area affected by the proposed
change, the expected cost of change is estimated.
• Benefits: an explanation of how the change aligns with the initiative
and business objectives to show how the change adds value. Benefits
considered include both financial benefits and tactical benefits such as
implications to scope, time, cost, quality, and resources.
• Risks: an analysis of risks to the initiative, the solution, or business
objectives.
• Priority: the level of importance of the change relative to other factors
such as organizational objectives, regulatory compliance requirements,
and stakeholder needs.
• Course(s) of action: the course of action for the change includes an
assessment of the components of the change request (cost, time,
benefits, risks and priority). It is common to identify several alternative
courses, including those recommended by the requester and by other
stakeholders so decision makers can make a choice that will best serve
the needs of the initiative.
• Determine how changes will be prioritized: the priority of the proposed
change is established relative to other competing interests within the
current initiative.
• Determine how changes will be documented: configuration
management and traceability standards establish product baselines and
version control practices that identify which baseline is affected by the
change.
• Determine how changes will be communicated: how proposed
changes, changes under review, and approved, declined, or deferred
changes will be communicated to stakeholders.
• Determine who will perform the impact analysis: specify who is
responsible for performing an analysis of the impacts the proposed change
will have across the initiative.



Plan Business Analysis Governance
Business Analysis Planning and Monitoring
40
• Determine who will authorize changes: include a designation of who
can approve changes and what business analysis information their authority
covers.
.3 Plan Prioritization Approach
For more
information, see
Prioritize
Requirements
(p. 86).
Timelines, expected value, dependencies, resource constraints, adopted
methodologies, and other factors influence how requirements and designs are
prioritized.
When planning the prioritization process, business analysts determine the:
• formality and rigour of the prioritization process,
• participants who will be involved in prioritization,
• process for deciding how prioritization will occur, including which
prioritization techniques will be utilized, and
• criteria to be used for prioritization. For example, requirements may be
prioritized based on cost, risk, and value.
The approach should also determine which stakeholders will have a role in
prioritization.
.4 Plan for Approvals
An approval formalizes the agreement between all stakeholders that the content
and presentation of the requirements and designs are accurate, adequate, and
contain sufficient detail to allow for continued progress to be made.
The timing and frequency of approvals are dependent on the size and complexity
of the change and associated risks of foregoing or delaying an approval.
The business analyst must determine the type of requirements and designs to be
approved, the timing for the approvals, the process to follow to gain approval,
and who will approve the requirements and designs.
When planning the appropriate approval process, business analysts consider the
organizational culture and the type of information being approved. For example,
new systems or processes for highly regulated industries such as financial,
pharmaceutical, or healthcare are likely to require frequent and rigorous review
and approval of very detailed specifications. For other types of initiatives, a less
intensive approval process may be more appropriate and result in a faster
implementation.
Planning for approvals also includes the schedule of events where approvals will
occur and how they will be tracked. Stakeholder availability, attitude, and
willingness to engage determine the efficiency of the approval process and may
significantly affect delivery timelines.
3.3.5
Guidelines and Tools
• Business Analysis Performance Assessment: provides results of previous
assessments that should be reviewed and incorporated into all planning
approaches.



Business Analysis Planning and Monitoring
Plan Business Analysis Governance
41
• Business Policies: define the limits within which decisions must be made. They
may be described by regulations, contracts, agreements, warranties,
certifications or other legal obligations.
• Current State Description: provides the context within which the work needs
to be completed. This information can help drive how to make better decisions.
• Legal/Regulatory Information: describes legislative rules or regulations that
must be followed, and can be used to help develop a framework that ensures
sound business decision making.
3.3.6
Techniques
• Brainstorming: used to generate an initial list of potential stakeholder names
who may need approval roles in the defined governance process.
• Document Analysis: used to evaluate existing governance processes or
templates.
• Interviews: used to identify possible decision-making, change control,
approval, or prioritization approaches and participants with an individual or
small group.
• Item Tracking: used to track any issues that arise when planning a governance
approach.
• Lessons Learned: used to find if past initiatives have identified valuable
experiences with governance that can be leveraged on current or future
initiatives.
• Organizational Modelling: used to understand roles/responsibilities within
the organization in an effort to define a governance approach that involves the
right stakeholders.
• Process Modelling: used to document the process or method for governing
business analysis.
• Reviews: used to review the proposed governance plan with key stakeholders.
• Survey or Questionnaire: used to identify possible decision-making, change
control, approval, or prioritization approaches and participants.
• Workshops: used to identify possible decision-making, change control,
approval, or prioritization approaches and participants within a team setting.
3.3.7
Stakeholders
• Domain Subject Matter Expert: may be a possible source of a requested
change or may be identified as needing to be involved in change discussions.
• Project Manager: works with the business analyst to ensure that overall
project governance aligns with the business analysis governance approach.
• Regulator: may impose rules or regulations that need to be considered when
determining the business analysis governance plan. May also be a possible
source of a requested change.



Plan Business Analysis Information Management
Business Analysis Planning and Monitoring
42
• Sponsor: can impose their own requirements for how business analysis
information should be managed. Participates in change discussions and
approves proposed changes.
3.3.8
Outputs
• Governance Approach: identifies the stakeholders who will have the
responsibility and authority to make decisions about business analysis work
including who will be responsible for setting priorities and who will approve
changes to business analysis information. It also defines the process that will be
utilized to manage requirement and design changes across the initiative.
3.4
Plan Business Analysis Information Management
3.4.1
Purpose
The purpose of Plan Business Analysis Information Management is to develop an
approach for how business analysis information will be stored and accessed.
3.4.2
Description
Business analysis information is comprised of all the information business analysts
elicit, create, compile, and disseminate in the course of performing business
analysis. Models, scope statements, stakeholder concerns, elicitation results,
requirements, designs, and solution options are just a few examples. This includes
requirements and designs, from lightweight user stories to formal requirement
documents to functioning prototypes.
Information management entails identifying:
• how information should be organized,
• the level of detail at which information should be captured,
• any relationships between the information,
• how information may be used across multiple initiatives and throughout the
enterprise,
• how information should be accessed and stored, and
• characteristics about the information that must be maintained.
Information management helps ensure that business analysis information is
organized in a functional and useful manner, is easily accessible to appropriate
personnel, and is stored for the necessary length of time.
3.4.3
Inputs
• Business Analysis Approach: incorporating the overall business analysis
approach into the information management approach is necessary to ensure
consistency across the approaches.



Business Analysis Planning and Monitoring
Plan Business Analysis Information Management
43
• Governance Approach: defines how business analysts manage changes to
requirements and designs, how decisions and approvals for business analysis
deliverables will be made, and how priorities will be set.
• Stakeholder Engagement Approach: identifying stakeholders and
understanding their communication and collaboration needs is useful in
determining their specific information management needs.
Figure 3.4.1: Plan Business Analysis Information Management Input/Output
Diagram
3.4.4
Elements
.1 Organization of Business Analysis Information
Business analysts are responsible for organizing business analysis information in a
manner that allows for efficient access and use. Information must be well
structured to ensure it is not difficult to locate, conflicts with other information, or
is needlessly duplicated.
Output
Input
3.4 Plan Business Analysis
Information Management
Business Analysis
Performance Assessment
3.4
Information
Management
Approach
4.4
Communicate
Business Analysis
Information
3.2
Stakeholder
Engagement
Approach
3.1
Business Analysis
Approach
Business Policies
Information Management
Tools
5.1
Trace
Requirements
5.2
Maintain
Requirements
7.4
Define
Requirements
Architecture
3.3
Governance
Approach
Guidelines and Tools
Tasks Using This Output
Legal/Regulatory
Information



Plan Business Analysis Information Management
Business Analysis Planning and Monitoring
44
The business analyst determines how best to structure and organize the business
analysis information at the start of an initiative. This involves taking into
consideration the type and amount of information to be collected, the
stakeholder's access and usage needs, and the size and complexity of the change.
Relationships among the types of information must be defined to assist in
managing the effect of new or changed information in the future.
.2 Level of Abstraction
Level of abstraction describes the breadth and depth of the information being
provided. Representations of information may range from highly conceptual or
summarized to very detailed. In determining how much detail each stakeholder
may require as the initiative evolves, consideration is given to the needs of the
stakeholders, the complexity of what is being explained, and the importance of
the change. Rather than present the same information to all stakeholders,
business analysts should present information with appropriate breadth and level
of detail based on each stakeholder's role. Business analysis information
regarding a topic of significant importance or high level of risk is frequently
represented in greater detail.
.3 Plan Traceability Approach
The traceability approach is based on:
For more
information, see
Trace
Requirements
(p. 79).
• the complexity of the domain,
• the number of views of requirements that will be produced,
• any requirement-related risks, organizational standards, applicable
regulatory requirements, and
• an understanding of the costs and benefits involved with tracing.
Business analysts plan to ensure the approach is at a level of detail to add value
without excessive overhead.
.4 Plan for Requirements Reuse
Reusing requirements can save an organization time, effort, and cost—provided
the requirements are accessible and structured in a manner that supports their
reuse.
Requirements that are potential candidates for long-term use are those an
organization must meet on an ongoing basis such as:
• regulatory requirements,
• contractual obligations,
• quality standards,
• service level agreements,
• business rules,
• business processes, or
• requirements describing products the enterprise produces.



Business Analysis Planning and Monitoring
Plan Business Analysis Information Management
45
Requirements may also be reused when describing common features or services
that are used across multiple systems, processes, or programs.
To make requirements useful beyond the current change, business analysts plan
ahead for requirements reuse by identifying how best to structure, store, and
access requirements so they are usable and accessible for future business analysis
efforts.
In order for requirements to be reused they must be clearly named, defined, and
stored in a repository that is available to other business analysts.
.5 Storage and Access
Business analysis information can be stored in many ways. Storage decisions
depend on many factors such as who must access the information, how often
they need to access it, and what conditions must be present for access.
Organizational standards and tool availability also influence storage and access
decisions. The business analysis approach defines how various tools will be used
on the initiative and how the information will be captured and stored within
those tools. Tools may shape the selection of business analysis techniques,
notations to be used, and the way that information is organized.
The repository may need to store information other than requirements and
designs. It should be able to indicate the status of any stored information, and
allow for modification of that information over time.
.6 Requirements Attributes
Requirements attributes provide information about requirements, and aid in the
ongoing management of the requirements throughout the change. They are
planned for and determined with the requirements themselves.
Requirements attributes allow business analysts to associate information with
individual or related groups of requirements. The information documented by the
attributes helps the team efficiently and effectively make trade-offs between
requirements, identify stakeholders affected by potential changes, and
understand the effect of a proposed change.
Some commonly used requirements attributes include:
• Absolute reference: provides a unique identifier. The reference is not
altered or reused if the requirement is moved, changed, or deleted.
• Author: provides the name of the person who needs to be consulted
should the requirement later be found to be ambiguous, unclear, or in
conflict.
• Complexity: indicates how difficult the requirement will be to implement.
• Ownership: indicates the individual or group that needs the requirement
or will be the business owner after the solution is implemented.
• Priority: indicates relative importance of requirements. Priority can refer to
the relative value of a requirement or to the sequence in which it will be
implemented.



Plan Business Analysis Information Management
Business Analysis Planning and Monitoring
46
• Risks: identifies uncertain events that may impact requirements.
• Source: identifies the origin of the requirement. The source is often
consulted if the requirement changes or if more information regarding the
requirement or the need that drove the requirement has to be obtained.
• Stability: indicates the maturity of the requirement.
• Status: indicates the state of the requirement, whether it is proposed,
accepted, verified, postponed, cancelled, or implemented.
• Urgency: indicates how soon the requirement is needed. It is usually only
necessary to specify this separately from the priority when a deadline exists
for implementation.
3.4.5
Guidelines and Tools
• Business Analysis Performance Assessment: provides results of previous
assessments that should be reviewed and incorporated into all planning
approaches.
• Business Policies: define the limits within which decisions must be made. They
may be described by regulations, contracts, agreements, warranties,
certifications, or other legal obligations.
• Information Management Tools: each organization uses some tools to store,
retrieve, and share business analysis information. These may be as simple as a
whiteboard, or as complex as a global wiki or robust requirements management
tool.
• Legal/Regulatory Information: describes legislative rules or regulations that
must be followed, and helps determine how business analysis information will
be managed.
3.4.6
Techniques
• Brainstorming: used to help stakeholders uncover their business analysis
information management needs.
• Interviews: used to help specific stakeholders uncover their business analysis
information management needs.
• Item Tracking: used to track issues with current information management
processes.
• Lessons Learned: used to create a source of information for analyzing
approaches for efficiently managing business analysis information.
• Mind Mapping: used to identify and categorize the kinds of information that
need to be managed.
• Process Modelling: used to document the process or method for managing
business analysis information.



Business Analysis Planning and Monitoring
Identify Business Analysis Performance Improvements
47
• Survey or Questionnaire: used to ask stakeholders to provide input into
defining business analysis information management.
• Workshops: used to uncover business analysis information management needs
in a group setting.
3.4.7
Stakeholders
• Domain Subject Matter Expert: may need to access and work with business
analysis information, and will be interested in a more specific view of business
analysis information which relates to their area of expertise.
• Regulator: may define rules and processes related to information
management.
• Sponsor: reviews, comments on, and approves business analysis information.
3.4.8
Outputs
• Information Management Approach: includes the defined approach for
how business analysis information will be stored, accessed, and utilized during
the change and after the change is complete.
3.5
Identify Business Analysis Performance
Improvements
3.5.1
Purpose
The purpose of Identify Business Analysis Performance Improvements is to assess
business analysis work and to plan to improve processes where required.
3.5.2
Description
To monitor and improve performance, it is necessary to establish the performance
measures, conduct the performance analysis, report on the results of the analysis,
and identify any necessary preventive, corrective, or developmental actions.
Performance analysis should occur throughout an initiative. Once potential
performance improvements are identified, they become guidelines for the next
time a task is executed.
3.5.3
Inputs
• Business Analysis Approach: identifies business analysis deliverables that will
be produced, activities that will need to be performed (including when they will
be performed and who will be performing them), and techniques that will be
used.
• Performance Objectives (external): describe the desired performance
outcomes that an enterprise or organization is hoping to achieve.



Identify Business Analysis Performance Improvements
Business Analysis Planning and Monitoring
48
Figure 3.5.1: Identify Business Analysis Performance Improvements Input/Output
Diagram
3.5.4
Elements
.1 Performance Analysis
What constitutes effective business analysis work depends on the context of a
particular organization or initiative. Reports on business analysis performance can
be informal and verbal, or they may include formal documentation. Reports on
business analysis performance are designed and tailored to meet the needs of the
various types of reviewers.
.2 Assessment Measures
If current measures exist, the business analyst may leverage them or determine
new measures. The business analyst may also elicit assessment measures from
stakeholders.
Performance measures may be based on deliverable due dates as specified in the
Output
Input
Guidelines and Tools
3.5 Identify Business Analysis
Performance Improvements
Organizational  Performance
Standards
3.5
Business Analysis
Performance
Assessment
3.1
Plan Business
Analysis Approach
3.1
Business Analysis
Approach
Performance
Objectives
(external)
3.2
Plan Stakeholder
Engagement
3.3
Plan Business
Analysis
Governance
3.4
Plan Business
Analysis
Information
Management
4.5
Manage
Stakeholder
Collaboration
Tasks Using This Output



Business Analysis Planning and Monitoring
Identify Business Analysis Performance Improvements
49
business analysis plan, metrics such as the frequency of the changes to business
analysis work products, the number of review cycles required, task efficiency, or
qualitative feedback from stakeholders and peers regarding the business analyst’s
deliverables. Appropriate performance measures enable the business analyst to
determine when problems are occurring that may affect the performance of
business analysis or identify opportunities for improvement. Measures may be
both quantitative and qualitative. Qualitative measures are subjective and can be
heavily influenced by the stakeholder’s attitudes, perceptions, and other
subjective criteria.
All performance
metrics will
encourage certain
behaviours and
discourage others.
Poorly chosen
metrics may drive
behaviour that is
detrimental to the
enterprise as a
whole.
Some possible measures are:
• Accuracy and Completeness: determine whether the business analyst
work products were correct and relevant when delivered, or whether
ongoing revisions were needed to gain acceptance by stakeholders.
• Knowledge: assess whether the business analyst had the skills and/or
experience to perform the assigned task.
• Effectiveness: assess whether the business analyst work products were
easy to use as standalone deliverables or whether they required extensive
explanation in order to be understood.
• Organizational Support: assess whether there were adequate resources
available to complete business analysis activities as needed.
• Significance: consider the benefit obtained from the work products and
assess whether the cost, time, and resource investments expended to
produce the work products were justified for the value they delivered.
• Strategic: look at whether business objectives were met, problems were
solved, and improvements were achieved.
• Timeliness: evaluate whether the business analyst delivered the work on
time per stakeholder expectations and schedule.
.3 Analyze Results
The business analysis process and deliverables are compared against the set of
defined measures. The analysis may be performed on the business analysis
process, the resources involved, and the deliverables.
Performance may be determined from the point of view of the stakeholders who
are the recipients of the business analysis work. Other times a personnel manager
or a Centre of Excellence may make this determination and provide assessments.
All stakeholders may have input in assessing the value of the business analysis
work but organizations may differ in terms of who has the authority to set the
targets against which performance is measured.
.4 Recommend Actions for Improvement
Once the analysis of performance results is complete, the business analyst
engages the appropriate stakeholders to identify the following actions:
• Preventive: reduces the probability of an event with a negative impact.



Identify Business Analysis Performance Improvements
Business Analysis Planning and Monitoring
50
• Corrective: establishes ways to reduce the negative impact of an event.
• Improvement: establishes ways to increase the probability or impact of
events with a positive impact.
These actions are likely to result in changes to the business analysis approach,
repeatable processes, and tools.
3.5.5
Guidelines and Tools
• Organizational Performance Standards: may include performance metrics
or expectations for business analysis work mandated by the organization.
3.5.6
Techniques
• Brainstorming: used to generate ideas for improvement opportunities.
• Interviews: used to gather assessments of business analysis performance.
• Item Tracking: used to track issues that occur during the performance of
business analysis for later resolution.
• Lessons Learned: used to identify recommended changes to business analysis
processes, deliverables, templates, and other organizational process assets that
can be incorporated into the current initiative and future work.
• Metrics and Key Performance Indicators (KPIs): used to determine what
metrics are appropriate for assessing business analysis performance and how
they may be tracked.
• Observation: used to witness business analysis performance.
• Process Analysis: used to analyze existing business analysis processes and
identify opportunities for improvement.
• Process Modelling: used to define business analysis processes and understand
how to improve those processes to reduce problems from hand-offs, improve
cycle times, or alter how business analysis work is performed to support
improvements in downstream processes.
• Reviews: used to identify changes to business analysis processes and
deliverables that can be incorporated into future work.
• Risk Analysis and Management: used to identify and manage potential
conditions or events that may impact business analysis performance.
• Root Cause Analysis: used to help identify the underlying cause of failures or
difficulties in accomplishing business analysis work.
• Survey or Questionnaire: used to gather feedback from stakeholders about
their satisfaction with business analysis activities and deliverables.
• Workshops: used to gather assessments of business analysis performance and
generate ideas for improvement opportunities.



Business Analysis Planning and Monitoring
Identify Business Analysis Performance Improvements
51
3.5.7
Stakeholders
• Domain Subject Matter Experts: should be informed about the business
analysis activities in order to set expectations regarding their involvement in the
work and to elicit their feedback regarding possible improvements to the
approach.
• Project Manager: is accountable for the success of a project and must be kept
informed of the current status of business analysis work. If potential problems
or opportunities for improvement are identified, the project manager must be
consulted before changes are implemented to assess whether those changes
will have an impact on the project. They may also deliver reports on business
analysis performance to the sponsor and other stakeholders.
• Sponsor: may require reports on business analysis performance to address
problems as they are identified. A manager of business analysts may also
sponsor initiatives to improve the performance of business analysis activities.
3.5.8
Outputs
• Business Analysis Performance Assessment: includes a comparison of
planned versus actual performance, identifying the root cause of variances from
the expected performance, proposed approaches to address issues, and other
findings to help understand the performance of business analysis processes.



Identify Business Analysis Performance Improvements
Business Analysis Planning and Monitoring
52



53
4
Elicitation and Collaboration
The Elicitation and Collaboration knowledge area describes the tasks that
business analysts perform to obtain information from stakeholders and confirm
the results. It also describes the communication with stakeholders once the
business analysis information is assembled.
Elicitation is the drawing forth or receiving of information from stakeholders or
other sources. It is the main path to discovering requirements and design
information, and might involve talking with stakeholders directly, researching
topics, experimenting, or simply being handed information. Collaboration is the
act of two or more people working together towards a common goal. The
Elicitation and Collaboration knowledge area describes how business analysts
identify and reach agreement on the mutual understanding of all types of
business analysis information. Elicitation and collaboration work is never a 'phase'
in business analysis; rather, it is ongoing as long as business analysis work is
occurring.
Elicitation and collaboration can be planned, unplanned, or both. Planned
activities such as workshops, experiments, and/or surveys can be structured and
organized in advance. Unplanned activities happen in the moment without
notice, such as last-minute or 'just in time' collaboration or conversations.
Business analysis information derived from an unplanned activity may require
deeper exploration through a planned activity.
Eliciting business analysis information is not an isolated activity. Information is
elicited while performing any task that includes interaction with stakeholders and
while the business analyst is performing independent analytical work. Elicitation
may trigger additional elicitation for details to fill in gaps or increase
understanding.



Elicitation and Collaboration
54
The Elicitation and Collaboration knowledge area is composed of the following
tasks:
• Prepare for Elicitation: involves ensuring that the stakeholders have the
information they need to provide and that they understand the nature of
the activities they are going to perform. It also sets a shared set of
expectations regarding the outcomes of the activity. Preparation may also
involve identifying research sources or preparing to conduct an experiment
to see if a process change actually results in an improvement.
• Conduct Elicitation: describes the work performed to understand
stakeholder needs and identify potential solutions that may meet those
needs. This may involve direct interaction with stakeholders, doing research,
or running experiments.
• Confirm Elicitation Results: involves ensuring that stakeholders have a
shared understanding of the outcomes of elicitation, that elicited
information is recorded appropriately, and that the business analyst has the
information sought from an elicitation activity. This task also involves
comparing the information received with other information to look for
inconsistencies or gaps.
• Communicate Business Analysis Information: provides stakeholders
with the information they need, at the time they need it. The information is
presented in a useful form, using the right terminology and concepts.
• Manage Stakeholder Collaboration: describes working with
stakeholders to engage them in the overall business analysis process and to
ensure that the business analyst can deliver the outcomes needed.
The Core Concept Model in Elicitation and
Collaboration
The Business Analysis Core Concept Model™ (BACCM™) describes the
relationships among the six core concepts.
The following table describes the usage and application of each of the core
concepts within the context of Elicitation and Collaboration.



Elicitation and Collaboration
55
Table 4.0.1: The Core Concept Model in Elicitation and Collaboration
Core Concept
During Elicitation and Collaboration,
business analysts...
Change: the act of transformation
in response to a need.
use a variety of elicitation techniques to
fully identify the characteristics of the
change including concerns that
stakeholders have about the change. The
change itself may determine the
appropriate types and extent of elicitation
and collaboration.
Need: a problem or opportunity to
be addressed.
elicit, confirm, and communicate needs
and supporting business analysis
information. As elicitation is iterative and
incremental, the understanding of needs
may evolve over time.
Solution: a specific way of
satisfying one or more needs in a
context.
elicit, confirm, and communicate
necessary or desired characteristics of
proposed solutions.
Stakeholder: a group or
individual with a relationship to
the change, the need, or the
solution.
manage the collaboration with the
stakeholders who participate in the
business analysis work. All stakeholders
may participate in different roles and at
different times during a change.
Value: the worth, importance, or
usefulness of something to a
stakeholder within a context.
collaborate with stakeholders to assess
the relative value of information provided
through elicitation, and apply a variety of
techniques to confirm and communicate
that value.
Context: the circumstances that
influence, are influenced by, and
provide understanding of the
change.
apply a variety of elicitation techniques to
identify business analysis information
about the context that may affect the
change.



Prepare for Elicitation
Elicitation and Collaboration
56
Figure 4.0.1: Elicitation and Collaboration Input/Output Diagram
4.1
Prepare for Elicitation
4.1.1
Purpose
The purpose of Prepare for Elicitation is to understand the scope of the elicitation
activity, select appropriate techniques, and plan for (or procure) appropriate
supporting materials and resources.
Input
Tasks
4.3
Confirm Elicitation
Results
4.2
Conduct Elicitation
4.1
Prepare for
Elicitation
4.4
Communicate
Business Analysis
Information
4.5
Manage
Stakeholder
Collaboration
Needs
Business Analysis
Information
3.5
Business Analysis
Performance
Assessment
3.2
Stakeholder
Engagement
Approach
4.1
Elicitation Activity
Plan
4.2
Elicitation Results
(unconfirmed)
4.3
Elicitation Results
(confirmed)
4.5
Stakeholder
Engagement
4.4
Business Analysis
Information
(communicated)
Output



Elicitation and Collaboration
Prepare for Elicitation
57
4.1.2
Description
Business analysts prepare for elicitation by defining the desired outcomes of the
activity, considering the stakeholders involved and the goals of the initiative. This
includes determining which work products will be produced using the elicitation
results, deciding which techniques are best suited to produce those results,
establishing the elicitation logistics, identifying any supporting materials needed,
and understanding circumstances to foster collaboration during an elicitation
activity.
4.1.3
Inputs
• Needs: guides the preparation in terms of the scope and purpose of elicitation
activities. Elicitation can be used to discover the needs, but in order to get
started there must be some need that exists—even if it has not yet been fully
elicited or understood.
• Stakeholder Engagement Approach: understanding stakeholders'
communication and collaboration needs helps plan and prepare appropriate
and effective elicitation events.
Figure 4.1.1: Prepare for Elicitation Input/Output Diagram
Tasks Using This Output
Output
4.1 Prepare for Elicitation
Business Analysis Approach
4.1
Elicitation
Activity Plan
4.2
Conduct Elicitation
3.2
Stakeholder
Engagement
Approach
Needs
Business Objectives
Existing Business Analysis
Information
Potential Value
4.3
Confirm Elicitation
Results
Guidelines and Tools
Input



Prepare for Elicitation
Elicitation and Collaboration
58
4.1.4
Elements
.1 Understand the Scope of Elicitation
To determine the type of business analysis information to be discovered during
the elicitation activity and the techniques that may be used, business analysts
consider:
• business domain,
• overall corporate culture and environment,
• stakeholder locations,
• stakeholders who are involved and their group dynamics,
• expected outputs the elicitation activities will feed,
• skills of the business analysis practitioner,
• other elicitation activities planned to complement this one,
• strategy or solution approach,
• scope of future solution, and
• possible sources of the business analysis information that might feed into
the specific elicitation activity.
Understanding the scope of the elicitation activity allows business analysts to
respond if the activity strays from the intended scope. It also allows them to
recognize if people and materials are not available in time, and when the activity
is complete.
.2 Select Elicitation Techniques
In most cases, multiple techniques are used during an elicitation activity. The
techniques used depend on cost and time constraints, the types of business
analysis information sources and their access, the culture of the organization, and
the desired outcomes. The business analyst may also factor in the needs of the
stakeholders, their availability, and their location (co-located or dispersed).
Choosing the right techniques and ensuring each technique is performed
correctly is extremely important to the success of the elicitation activity. When
selecting elicitation techniques, business analysts consider:
• techniques commonly used in similar initiatives,
• techniques specifically suited to the situation, and
• the tasks needed to prepare, execute, and complete each technique.
Due to changing dynamics and situations, the business analyst may be required to
adjust the initial selections by incorporating more appropriate techniques. A
thorough understanding of the variety of techniques available assists the business
analyst in adapting to changing circumstances.



Elicitation and Collaboration
Prepare for Elicitation
59
.3 Set Up Logistics
Logistics are planned prior to an elicitation activity. The logistics for each
elicitation activity include identifying:
• the activity's goals,
• participants and their roles,
• scheduled resources, including people, rooms, and tools,
• locations,
• communication channels,
• techniques, and
• languages used by stakeholders (oral and written).
The logistics may also involve creating an agenda if other stakeholders are
involved.
.4 Secure Supporting Material
Business analysts identify sources of information that are needed to conduct the
elicitation activity. There might be a great deal of information needed to conduct
elicitation including people, systems, historical data, materials and documents.
Documents could include existing system documents, relevant business rules,
organizational polices, regulations, and contracts. Supporting materials might
also take the form of outputs of analysis work, such as draft versions of analysis
models (see Specify and Model Requirements (p. 136)). Business analysts procure
or develop the materials and tools needed. Additional planning for experimental
elicitation might be required if novel tools, equipment, or techniques are going to
be used.
.5 Prepare Stakeholders
Business analysts may need to educate stakeholders on how an elicitation
technique works or what information is needed. It may be helpful to explain an
elicitation technique to stakeholders not involved in the activity to help them
understand the validity and relevance of the information elicited. Stakeholders
may be unresponsive or challenging during an elicitation activity if they feel that it
is not aligned to their individual objectives, don't understand the purpose, or are
confused about the process. In preparing for elicitation, the business analyst
should ensure that there is buy-in from all necessary stakeholders.
Business analysts may also prepare stakeholders by requesting that they review
supporting materials prior to the elicitation activity in order to make it as effective
as possible. An agenda might be provided in advance to support stakeholders in
coming prepared to the activity with the necessary frame of mind and
information.
Eliciting through research or exploration may be a solo activity for the business
analyst and not require preparing other stakeholders.



Prepare for Elicitation
Elicitation and Collaboration
60
4.1.5
Guidelines and Tools
• Business Analysis Approach: sets the general strategy to be used to guide
the business analysis work. This includes the general methodology, types of
stakeholders and how they should be involved, list of stakeholders, timing of
the work, expected format and level of detail of elicitation results, and
identified challenges and uncertainties.
• Business Objectives: describe the desired direction needed to achieve the
future state. They can be used to plan and prepare elicitation events, and to
develop supporting materials.
• Existing Business Analysis Information: may provide a better understanding
of the goals of the elicitation activity, and aid in preparing for elicitation.
• Potential Value: describes the value to be realized by implementing the
proposed future state, and can be used to shape elicitation events.
4.1.6
Techniques
• Brainstorming: used to collaboratively identify and reach consensus about
which sources of business analysis information should be consulted and which
elicitation techniques might be most effective.
• Data Mining: used to identify information or patterns that require further
investigation.
• Document Analysis: used to identify and assess candidate sources of
supporting materials.
• Estimation: used to estimate the time and effort required for the elicitation
and the associated cost.
• Interviews: used to identify concerns about the planned elicitation, and can be
used to seek authority to proceed with specific options.
• Mind Mapping: used to collaboratively identify and reach consensus about
which sources of business analysis information should be consulted and which
elicitation techniques might be most effective.
• Risk Analysis and Management: used to identify, assess, and manage
conditions or situations that could disrupt the elicitation, or affect the quality
and validity of the elicitation results. The plans for the elicitation should be
adjusted to avoid, transfer, or mitigate the most serious risks.
• Stakeholder List, Map, or Personas: used to determine who should be
consulted while preparing for the elicitation, who should participate in the
event, and the appropriate roles for each stakeholder.
4.1.7
Stakeholders
• Domain Subject Matter Expert: provides supporting materials as well as
guidance about which other sources of business analysis information to consult.
May also help to arrange research, experiments, and facilitated elicitation.



Elicitation and Collaboration
Conduct Elicitation
61
• Project Manager: ensures that the appropriate people and resources are
available to conduct the elicitation.
• Sponsor: has the authority to approve or deny a planned elicitation event, and
to authorize and require the participation of specific stakeholders.
4.1.8
Outputs
• Elicitation Activity Plan: used for each elicitation activity. It includes logistics,
scope of the elicitation activity, selected techniques, and supporting materials.
4.2
Conduct Elicitation
4.2.1
Purpose
The purpose of Conduct Elicitation is to draw out, explore, and identify
information relevant to the change.
4.2.2
Description
There are three common types of elicitation:
• Collaborative: involves direct interaction with stakeholders, and relies on
their experiences, expertise, and judgment.
• Research: involves systematically discovering and studying information
from materials or sources that are not directly known by stakeholders
involved in the change. Stakeholders might still participate in the research.
Research can include data analysis of historical data to identify trends or
past results.
• Experiments: involves identifying information that could not be known
without some sort of controlled test. Some information cannot be drawn
from people or documents—because it is unknown. Experiments can help
discover this kind of information. Experiments include observational studies,
proofs of concept, and prototypes.
One or more elicitation techniques may be used to produce the desired outcome
within the scope of elicitation.
Stakeholders may collaborate in elicitation by:
• participating and interacting during the elicitation activity, and
• researching, studying, and providing feedback on documents, systems,
models, and interfaces.
4.2.3
Inputs
• Elicitation Activity Plan: includes the planned elicitation activities and
techniques, activity logistics (for example, date, time, location, resources,



Conduct Elicitation
Elicitation and Collaboration
62
agenda), scope of the elicitation activity, and available sources of background
information.
Figure 4.2.1: Conduct Elicitation Input/Output Diagram
4.2.4
Elements
.1 Guide Elicitation Activity
Understanding the proposed representations of business analysis information,
which were defined in planning, helps ensure that the elicitation activities are
focused on producing the intended information at the desired level of detail. This
applies to each instance of an elicitation activity throughout a change and may
vary based on the activity. In order to help guide and facilitate towards the
expected outcomes, business analysts consider:
• the elicitation activity goals and agenda,
• scope of the change,
• what forms of output the activity will generate,
• what other representations the activity results will support,
• how the output integrates into what is already known,
• who provides the information,
Tasks Using This Output
Output
4.2
Conduct Elicitation
Business Analysis Approach
4.2
Elicitation
Results
(unconfirmed)
4.3
Confirm Elicitation
Results
4.1
Elicitation Activity
Plan
Existing Business Analysis
Information
Stakeholder Engagement
Approach
Supporting Materials
Input
Guidelines and Tools



Elicitation and Collaboration
Conduct Elicitation
63
• who will use the information, and
• how the information will be used.
While most of these are considered when planning for the elicitation activity (see
Prepare for Elicitation (p. 56)), they are also all important while performing the
elicitation activity in order to keep it on track and achieve its goal. For example,
stakeholders might have discussions that are out of scope for the activity or
change, and the business analyst needs to recognize that in the moment to
determine the next step; either acknowledge it and continue, or guide the
conversation differently.
The business analyst also uses this information to determine when there has been
sufficient elicitation, in order to stop the activity.
.2 Capture Elicitation Outcomes
Conducting elicitation is frequently iterative and takes place in a series of
sessions—in parallel or in sequence—according to the scope of the elicitation
activity (see Prepare for Elicitation (p. 56)). If the elicitation activity is unplanned,
outcomes are captured and integrated into the appropriate planned outcomes.
Capturing the elicitation outcomes helps to ensure that the information produced
during elicitation activities is recorded for later reference and use.
4.2.5
Guidelines and Tools
• Business Analysis Approach: influences how each elicitation activity is
performed, as it identifies the types of outputs that will be needed based on the
approach.
• Existing Business Analysis Information: may guide the questions posed
during elicitation and the approach used to draw out information from various
stakeholders.
• Stakeholder Engagement Approach: provides collaboration and
communication approaches that might be effective during elicitation.
• Supporting Materials: includes any materials to prepare both the business
analyst and participants before elicitation, as well as any information, tools, or
equipment to be used during the elicitation.
4.2.6
Techniques
• Benchmarking and Market Analysis: used as a source of business analysis
information by comparing a specific process, system, product, service, or
structure with some external baseline, such as a similar organization or baseline
provided by an industry association. Market analysis is used to determine what
customers want and what competitors provide.
• Brainstorming: used to generate many ideas from a group of stakeholders in a
short period, and to organize and prioritize those ideas.



Conduct Elicitation
Elicitation and Collaboration
64
• Business Rules Analysis: used to identify the rules that govern decisions in an
organization and that define, constrain, or enable organizational operations.
• Collaborative Games: used to develop a better understanding of a problem or
to stimulate creative solutions.
• Concept Modelling: used to identify key terms and ideas of importance and
define the relationships between them.
• Data Mining: used to identify relevant information and patterns.
• Data Modelling: used to understand entity relationships during elicitation.
• Document Analysis: used to review existing systems, contracts, business
procedures and policies, standards, and regulations.
• Focus Groups: used to identify and understand ideas and attitudes from a
group.
• Interface Analysis: used to understand the interaction, and characteristics of
that interaction, between two entities, such as two systems, two organizations,
or two people or roles.
• Interviews: used to ask questions of stakeholders to uncover needs, identify
problems, or discover opportunities.
• Mind Mapping: used to generate many ideas from a group of stakeholders in
a short period, and to organize and prioritize those ideas.
• Observation: used to gain insight about how work is currently done, possibly
in different locations and in different circumstances.
• Process Analysis: used to understand current processes and to identify
opportunities for improvement in those processes.
• Process Modelling: used to elicit processes with stakeholders during elicitation
activities.
• Prototyping: used to elicit and validate stakeholders' needs through an
iterative process that creates a model of requirements or designs.
• Survey or Questionnaire: used to elicit business analysis information,
including information about customers, products, work practices, and attitudes,
from a group of people in a structured way and in a relatively short period of
time.
• Workshops: used to elicit business analysis information, including information
about customers, products, work practices, and attitudes, from a group of
people in a collaborative, facilitated way.
4.2.7
Stakeholders
• Customer: will provide valuable business analysis information during
elicitation.
• Domain Subject Matter Expert: has expertise in some aspect of the situation
and can provide the required business analysis information. Often guides and



Elicitation and Collaboration
Confirm Elicitation Results
65
assists the business analyst in identifying appropriate research sources, and may
help to arrange research, experiments, and facilitated elicitation.
• End User: the user of existing and future solutions, who should participate in
elicitation.
• Implementation Subject Matter Expert: designs and implements a solution
and provides specialist expertise, and can participate in elicitation by asking
clarifying questions and offering alternatives.
• Sponsor: authorizes and ensures that the stakeholders necessary to participate
in elicitation are involved.
• Any stakeholders: could have relevant knowledge or experience to participate
in elicitation activities.
4.2.8
Outputs
• Elicitation Results (unconfirmed): captured information in a format that is
specific to the elicitation activity.
4.3
Confirm Elicitation Results
4.3.1
Purpose
The purpose of Confirm Elicitation Results is to check the information gathered
during an elicitation session for accuracy and consistency with other information.
4.3.2
Description
Elicited information is confirmed to identify any problems and resolve them
before resources are committed to using the information. This review may
discover errors, omissions, conflicts, and ambiguity.
The elicitation results can be compared against their source and other elicitation
results to ensure consistency. Collaboration with stakeholders might be necessary
to ensure their inputs are correctly captured and that they agree with the results
of non-facilitated elicitation. If information is not correct, the business analyst
determines what is correct, which can require more elicitation. Committing
resources to business analysis activities based on unconfirmed elicitation results
may mean stakeholder expectations are not met. If the results are inconsistent,
additional elicitation might need to be conducted to resolve the discrepancies.
Confirming the elicitation results is a much less rigorous and formal review than
occurs during analysis.
4.3.3
Inputs
• Elicitation Results (unconfirmed): capture information in a format specific to
the elicitation activity.



Confirm Elicitation Results
Elicitation and Collaboration
66
Figure 4.3.1: Confirm Elicitation Results
4.3.4
Elements
.1 Compare Elicitation Results Against Source Information
Task Conduct Elicitation (p. 61) describes sources from which elicitation results
may be derived, including documents and stakeholder knowledge. The business
analyst may lead follow-up meetings where stakeholders correct the elicitation
results. Stakeholders may also confirm the elicitation results independently.
.2 Compare Elicitation Results Against Other Elicitation Results
Business analysts compare results collected through multiple elicitation activities
to confirm that the information is consistent and accurately represented. As
comparisons are drawn, business analysts identify variations in results and resolve
them in collaboration with stakeholders. Comparisons may also be made with
historical data to confirm more recent elicitation results.
Inconsistencies in elicitation results are often uncovered when business analysts
develop specifications and models. These models may be developed during an
elicitation activity to improve collaboration.
Tasks Using This Output
Output
4.3
Confirm Elicitation Results
Elicitation Activity Plan
4.3
Elicitation Results
(confirmed)
6.1
Analyze Current
State
4.2
Elicitation Results
(unconfirmed)
Existing Business Analysis
Information
6.3
Assess Risks
Guidelines and Tools
Input



Elicitation and Collaboration
Communicate Business Analysis Information
67
4.3.5
Guidelines and Tools
• Elicitation Activity Plan: used to guide which alternative sources and which
elicitation results are to be compared.
• Existing Business Analysis Information: can be used to confirm the results
of elicitation activities or to develop additional questions to draw out more
detailed information.
4.3.6
Techniques
• Document Analysis: used to confirm elicitation results against source
information or other existing documents.
• Interviews: used to confirm the business analysis information and to confirm
that the integration of that information is correct.
• Reviews: used to confirm a set of elicitation results. Such reviews could be
informal or formal depending on the risks of not having correct, useful, and
relevant information.
• Workshops: used to conduct reviews of the drafted elicitation results using any
level of formality. A predetermined agenda, scripts, or scenario tests may be
used to walk through the elicitation results, and feedback is requested from the
participants and recorded.
4.3.7
Stakeholders
• Domain Subject Matter Experts: people with substantial knowledge,
experience, or expertise about the business analysis information being elicited,
or about the change or the solution, help to confirm that elicitation results are
correct, and can help to identify omissions, inconsistencies and conflicts in
elicitation results. They can also confirm that the right business analysis
information has been elicited.
• Any stakeholder: all types of stakeholders may need to participate in
confirming elicitation results.
4.3.8
Outputs
• Elicitation Results (confirmed): integrated output that the business analyst
and other stakeholders agree correctly reflects captured information and
confirms that it is relevant and useful as an input to further work.
4.4
Communicate Business Analysis Information
4.4.1
Purpose
The purpose of Communicate Business Analysis Information is to ensure
stakeholders have a shared understanding of business analysis information.



Communicate Business Analysis Information
Elicitation and Collaboration
68
4.4.2
Description
Business analysts must communicate appropriate information to stakeholders at
the right time and in formats that meet their needs. Consideration is given to
expressing the information in language, tone, and style that is appropriate to the
audience.
Communication of business analysis information is bi-directional and iterative. It
involves determining the recipients, content, purpose, context, and expected
outcomes. Task Plan Stakeholder Engagement (p. 31) evaluates communication
needs and plans anticipated messages.
Communicating information does not simply involve pushing information out and
assuming it was received and understood. Business analysts engage stakeholders
to ensure they understand the information and gain agreement. The business
analyst acts on any disagreements. The method of delivering the information may
need to change if the stakeholders are not receiving or understanding it. Multiple
forms of communication might be required for the same information.
4.4.3
Inputs
• Business Analysis Information: any kind of information at any level of detail
that is used as an input or output of business analysis work. Business analysis
information becomes an input for this task when the need is discovered to
communicate the information to additional stakeholders.
• Stakeholder Engagement Approach: describes stakeholder groups, roles,
and general needs regarding communication of business analysis information.
Figure 4.4.1: Communicate Business Analysis Information Input/Output Diagram
Output
4.4
Communicate Business Analysis
Information
Business Analysis Approach
4.4
Business Analysis
Information
(communicated)
3.2
Stakeholder
Engagement
Approach
Business Analysis
Information
Information Management
Approach
Guidelines and Tools
Input



Elicitation and Collaboration
Communicate Business Analysis Information
69
4.4.4
Elements
.1 Determine Objectives and Format of Communication
Business analysis information packages may be prepared for a number of reasons
including—but not limited to—the following:
• communication of requirements and designs to stakeholders,
• early assessment of quality and planning,
• evaluation of possible alternatives,
• formal reviews and approvals,
• inputs to solution design,
• conformance to contractual and regulatory obligations, and
• maintenance for reuse.
The primary goal of developing a package is to convey information clearly and in
usable format for continuing change activities. To help decide how to present
requirements, business analysts ask the following types of questions:
• Who is the audience of the package?
• What will each type of stakeholder understand and need from the
communication?
• What is each stakeholder’s preferred style of communication or learning?
• What information is important to communicate?
• Are the presentation and format of the package, and the information
contained in the package, appropriate for the type of audience?
• How does the package support other activities?
• Are there any regulatory or contractual constraints to conform to?
Possible forms for packages may include:
• Formal Documentation: is usually based on a template used by the
organization and may include text, matrices, or diagrams. It provides a
stable, easy to use, long-term record of the information.
• Informal Documentation: may include text, diagrams, or matrices that
are used during a change but are not part of a formal organizational
process.
• Presentations: deliver a high-level overview appropriate for understanding
goals of a change, functions of a solution, or information to support
decision making.
Consideration is given to the best way to combine and present the materials to
convey a cohesive and effective message to one or more stakeholder groups.
Packages can be stored in different online or offline repositories, including
documents or tools.



Communicate Business Analysis Information
Elicitation and Collaboration
70
.2 Communicate Business Analysis Package
The purpose of communicating the business analysis package is to provide
stakeholders with the appropriate level of detail about the change so they can
understand the information it contains. Stakeholders are given the opportunity to
review the package, ask questions about the information, and raise any concerns
they may have.
Selecting the appropriate communication platform is also important. Common
communication platforms include:
• Group collaboration: used to communicate the package to a group of
relevant stakeholders at the same time. It allows immediate discussion
about the information and related issues.
• Individual collaboration: used to communicate the package to a single
stakeholder at a time. It can be used to gain individual understanding of the
information when a group setting is not feasible, most productive, or going
to yield the best results.
• E-mail or other non-verbal methods: used to communicate the package
when there is a high maturity level of information that will need little or no
verbal explanation to support it.
4.4.5
Guidelines and Tools
• Business Analysis Approach: describes how the various types of information
will be disseminated rather than what will be disseminated. It describes the level
of detail and formality required, frequency of the communications, and how
communications could be affected by the number and geographic dispersion of
stakeholders.
• Information Management Approach: helps determine how business analysis
information will be packaged and communicated to stakeholders.
4.4.6
Techniques
• Interviews: used to individually communicate information to stakeholders.
• Reviews: used to provide stakeholders with an opportunity to express
feedback, request required adjustments, understand required responses and
actions, and agree or provide approvals. Reviews can be used during group or
individual collaboration.
• Workshops: used to provide stakeholders with an opportunity to express
feedback and to understand required adjustments, responses, and actions. They
are also useful for gaining consensus and providing approvals. Typically used
during group collaboration.
4.4.7
Stakeholders
• End User: needs to be communicated with frequently so they are aware of
relevant business analysis information.
• Customer: needs to be communicated with frequently so they are aware of
relevant business analysis information.



Elicitation and Collaboration
Manage Stakeholder Collaboration
71
• Domain Subject Matter Expert: needs to understand the business analysis
information as part of confirming and validating it throughout the change
initiative.
• Implementation Subject Matter Expert: needs to be aware of and
understand the business analysis information, particularly requirements and
designs, for implementation purposes.
• Tester: needs to be aware of and understand the business analysis information,
particularly requirements and designs for testing purposes.
• Any stakeholder: all types of stakeholders will likely need to be
communicated with at some point during the change initiative.
4.4.8
Outputs
• Business Analysis Information (communicated): business analysis
information is considered communicated when the target stakeholders have
reached an understanding of its content and implications.
4.5
Manage Stakeholder Collaboration
4.5.1
Purpose
The purpose of Manage Stakeholder Collaboration is to encourage stakeholders
to work towards a common goal.
4.5.2
Description
Business analysis work lends itself to many collaboration opportunities between
groups of stakeholders on the business analysis work products. Stakeholders hold
various degrees of influence and authority over the approval of work products,
and are also an important source of needs, constraints, and assumptions. As the
business analysis work progresses, the business analyst identifies stakeholders,
confirms their roles, and communicates with them to ensure that the right
stakeholders participate at the right times and in the appropriate roles.
Managing stakeholder collaboration is an ongoing activity. Although managing
stakeholder collaboration begins once stakeholders have been identified and
analyzed, new stakeholders may be identified at any point during an initiative. As
new stakeholders are identified, their role, influence, and relationship to the
initiative are analyzed. Each stakeholder's role, responsibility, influence, attitude,
and authority may change over time.
The more significant the impact of the change or its visibility within the
organization, the more attention is directed to managing stakeholder
collaboration. Business analysts manage stakeholder collaboration to capitalize
on positive reactions, and mitigate or avoid negative reactions. The business
analyst should constantly monitor and assess each stakeholder’s attitude to
determine if it might affect their involvement in the business analysis activities.



Manage Stakeholder Collaboration
Elicitation and Collaboration
72
Poor relationships with stakeholders can have many detrimental effects on
business analysis, including:
• failure to provide quality information,
• strong negative reactions to setbacks and obstacles,
• resistance to change,
• lack of support for, and participation in, business analysis work, and
• business analysis information being ignored.
These effects can be modified in part through strong, positive, and trust-based
relationships with stakeholders. Business analysts actively manage relationships
with stakeholders who:
• provide services to the business analyst, including inputs to business analysis
tasks and other support activities,
• depend on services provided by the business analyst, including outputs of
business analysis tasks, and
• participate in the execution of business analysis tasks.
4.5.3
Inputs
• Stakeholder Engagement Approach: describes the types of expected
engagement with stakeholders and how they might need to be managed.
• Business Analysis Performance Assessment: provides key information
about the effectiveness of business analysis tasks being executed, including
those focused on stakeholder engagement.
Figure 4.5.1: Manage Stakeholder Collaboration Input/Output Diagram
Output
4.5
Manage Stakeholder
Collaboration
Business Analysis Approach
4.5
Stakeholder
Engagement
3.5 Business
Analysis
Performance
Assessment
3.2
Stakeholder
Engagement
Approach
Business Objectives
Future State Description
Recommended Actions
Risk Analysis Results
Guidelines and Tools
Input



Elicitation and Collaboration
Manage Stakeholder Collaboration
73
4.5.4
Elements
.1 Gain Agreement on Commitments
Stakeholders participate in business analysis activities that may require time and
resource commitments. The business analyst and stakeholders identify and agree
upon these commitments as early in the initiative as possible. The specific details
of the commitments can be communicated formally or informally, as long as there
is explicit understanding of the expectations and desired outcomes of the
commitment.
There may be dialogue and negotiation regarding the terms and conditions of the
commitments. Effective negotiation, communication, and conflict resolution skills
are important to effective stakeholder management (see Negotiation and Conflict
Resolution (p. 210)).
.2 Monitor Stakeholder Engagement
Business analysts monitor the participation and performance of stakeholders to
ensure that:
• the right subject matter experts (SMEs) and other stakeholders are
participating effectively,
• stakeholder attitudes and interest are staying constant or improving,
• elicitation results are confirmed in a timely manner, and
• agreements and commitments are maintained.
Business analysts continually monitor for such risks as:
• stakeholders being diverted to other work,
• elicitation activities not providing the quality of business analysis
information required, and
• delayed approvals.
.3 Collaboration
Stakeholders are more likely to support change if business analysts collaborate
with them and encourage the free flow of information, ideas, and innovations.
Genuine stakeholder engagement requires that all stakeholders involved feel that
they are heard, their opinions matter, and their contributions are recognized.
Collaboration involves regular, frequent, and bi-directional communication.
Collaborative relationships help maintain the free flow of information when
obstacles and setbacks occur, and promote a shared effort to resolve problems
and achieve desired outcomes.



Manage Stakeholder Collaboration
Elicitation and Collaboration
74
4.5.5
Guidelines and Tools
• Business Analysis Approach: describes the nature and level of collaboration
required from each stakeholder group to perform planned business analysis
activities.
• Business Objectives: describe the desired direction needed to achieve the
future state. They can be used to focus diverse stakeholders on a common
vision of the desired business outcomes.
• Future State Description: defines the desired future state and the expected
value it delivers which can be used to focus diverse stakeholders on the
common goal.
• Recommended Actions: communicating what should be done to improve the
value of a solution can help to galvanize support and focus stakeholders on a
common goal.
• Risk Analysis Results: stakeholder-related risks will need to be addressed to
ensure stakeholder collaboration activities are successful.
4.5.6
Techniques
• Collaborative Games: used to stimulate teamwork and collaboration by
temporarily immersing participants in a safe and fun situation in which they can
share their knowledge and experience on a given topic, identify hidden
assumptions, and explore that knowledge in ways that may not occur during
the course of normal interactions.
• Lessons Learned: used to understand stakeholders' satisfaction or
dissatisfaction, and offer them an opportunity to help improve the working
relationships.
• Risk Analysis and Management: used to identify and manage risks as they
relate to stakeholder involvement, participation, and engagement.
• Stakeholder List, Map, or Personas: used to determine who is available to
participate in the business analysis work, show the informal relationships
between stakeholders, and understand which stakeholders should be consulted
about different kinds of business analysis information.
4.5.7
Stakeholders
• All stakeholders: all types of stakeholders who might be involved in
collaboration during change.
4.5.8
Outputs
• Stakeholder Engagement: willingness from stakeholders to engage in
business analysis activities and interact with the business analyst when
necessary.



75
5
Requirements Life Cycle Management
The Requirements Life Cycle Management knowledge area describes the tasks
that business analysts perform in order to manage and maintain requirements
and design information from inception to retirement. These tasks describe
establishing meaningful relationships between related requirements and designs,
assessing changes to requirements and designs when changes are proposed, and
analyzing and gaining consensus on changes.
The purpose of requirements life cycle management is to ensure that business,
stakeholder, and solution requirements and designs are aligned to one another
and that the solution implements them. It involves a level of control over
requirements and over how requirements will be implemented in the actual
solution to be constructed and delivered. It also helps to ensure that business
analysis information is available for future use.
The requirements life cycle:
• begins with the representation of a business need as a requirement,
• continues through the development of a solution, and
• ends when a solution and the requirements that represent it are retired.
The management of requirements does not end once a solution is implemented.
Throughout the life of a solution, requirements continue to provide value when
they are managed appropriately.
Within the Requirements Life Cycle Management knowledge area, the concept of
a life cycle is separate from a methodology or process used to govern business
analysis work. Life cycle refers to the existence of various phases or states that
requirements pass through as part of any change. Requirements may be in
multiple states at one time.



Requirements Life Cycle Management
76
The states listed
here are not
intended to be a
comprehensive
listing.
Figure 5.0.1: Requirements Life Cycle Management
The Requirements Life Cycle Management knowledge area includes the following
tasks:
• Trace Requirements: analyzes and maintains the relationships between
requirements, designs, solution components, and other work products for
impact analysis, coverage, and allocation.
• Maintain Requirements: ensures that requirements and designs are
accurate and current throughout the life cycle and facilitates reuse where
appropriate.
• Prioritize Requirements: assesses the value, urgency, and risks associated
with particular requirements and designs to ensure that analysis and/or
delivery work is done on the most important ones at any given time.
• Assess Requirements Changes: evaluates new and changing stakeholder
requirements to determine if they need to be acted on within the scope of a
change.
• Approve Requirements: works with stakeholders involved in the
governance process to reach approval and agreement on requirements and
designs.
The Core Concept Model in Requirements Life Cycle
Management
The Business Analysis Core Concept Model™ (BACCM™) describes the
relationships among the six core concepts.
The following table describes the usage and application of each of the core
concepts within the context of Requirements Life Cycle Management.
Assess
Approval/
Consensus
Potential
Requirement
Yes
No
Yes
No
Trace
Maintain
Prioritize
Manage
Bring Forward



Requirements Life Cycle Management
77
Table 5.0.1: The Core Concept Model in Requirements Life Cycle Management
Core Concept
During Requirements Life Cycle
Management, business analysts...
Change: the act of transformation
in response to a need.
manage how proposed changes to
requirements and designs are evaluated
during an initiative.
Need: a problem or opportunity to
be addressed.
trace, prioritize and maintain
requirements to ensure that the need is
met.
Solution: a specific way of
satisfying one or more needs in a
context.
trace requirements and designs to
solution components to ensure that the
solution satisfies the need.
Stakeholder: a group or
individual with a relationship to
the change, the need, or the
solution.
work closely with key stakeholders to
maintain understanding, agreement, and
approval of requirements and designs.
Value: the worth, importance, or
usefulness of something to a
stakeholder within a context.
maintain requirements for reuse to extend
value beyond the current initiative.
Context: the circumstances that
influence, are influenced by, and
provide understanding of the
change.
analyze the context to support tracing
and prioritization activities.



Requirements Life Cycle Management
78
Figure 5.0.2: Requirements Life Cycle Management Input/Output Diagram
Tasks
Output
5.3
Prioritize
Requirements
5.2
Maintain
Requirements
5.1
Trace
Requirements
5.4
Assess
Requirements
Changes
5.5
Approve
Requirements
Requirements
Designs
Proposed Change
7.2
Requirements
(verified)
5.1
Requirements (traced)
5.1
Designs (traced)
5.2
Requirements
(maintained)
5.3
Requirements
(prioritized)
5.2
Designs (maintained)
5.3
Designs (prioritized)
5.4
Designs Change
Assessment
5.4
Requirements Change
Assessment
5.5
Requirements
(approved)
5.5
Designs (approved)
Input



Requirements Life Cycle Management
Trace Requirements
79
5.1
Trace Requirements
5.1.1
Purpose
The purpose of Trace Requirements is to ensure that requirements and designs at
different levels are aligned to one another, and to manage the effects of change
to one level on related requirements.
5.1.2
Description
Requirements traceability identifies and documents the lineage of each
requirement, including its backward traceability, its forward traceability, and its
relationship to other requirements. Traceability is used to help ensure that the
solution conforms to requirements and to assist in scope, change, risk, time, cost,
and communication management. It is also used to detect missing functionality
or to identify if there is implemented functionality that is not supported by any
requirement.
Traceability enables:
• faster and simpler impact analysis,
• more reliable discovery of inconsistencies and gaps in requirements,
• deeper insights into the scope and complexity of a change, and
• reliable assessment of which requirements have been addressed and which
have not.
For more
information on
allocation, see
Define
Requirements
Architecture
(p. 148).
It is often difficult to accurately represent needs and solutions without taking into
account the relationships that exist between them. While traceability is valuable,
the business analyst balances the number of relationship types with the benefit
gained by representing them. Traceability also supports both requirements
allocation and release planning by providing a direct line of sight from
requirement to expressed need.
The following images show examples of visual representations of traceability for a
process and for software requirements.



Trace Requirements
Requirements Life Cycle Management
80
Figure 5.1.1: Process Traceability
Figure 5.1.2: Software Requirements Traceability
5.1.3
Inputs
• Requirements: may be traced to other requirements (including goals,
objectives, business requirements, stakeholder requirements, solution
requirements, and transition requirements), solution components, visuals,
business rules, and other work products.
• Designs: may be traced to other requirements, solution components, and other
work products.
Value Chain
Business
Process
Sub-process
Activity
Task
Business Needs
Business
Requirements
Stakeholder
Requirements
Design
Code
Test
Solution
Requirements



Requirements Life Cycle Management
Trace Requirements
81
Figure 5.1.3: Trace Requirements Input/Output Diagram
5.1.4
Elements
.1 Level of Formality
When tracing requirements, business analysts consider the value that each link is
supposed to deliver, as well as the nature and use of the specific relationships that
are being created.
The effort to trace requirements grows significantly when the number of
requirements or level of formality increases.
.2 Relationships
There are several types of relationships that the business analyst considers when
defining the traceability approach:
• Derive: relationship between two requirements, used when a requirement
is derived from another requirement. This type of relationship is appropriate
to link the requirements on different levels of abstraction. For example, a
solution requirement derived from a business or a stakeholder requirement.
Output
5.1
Trace Requirements
Domain Knowledge
Designs
Requirements
Information Management
Approach
Legal/Regulatory
Information
Requirements Management
Tools/Repository
Tasks Using This Output
5.1
Requirements
(traced)
5.1
Designs
(traced)
7.5
Define Design
Options
Input
Guidelines and Tools



Trace Requirements
Requirements Life Cycle Management
82
• Depends: relationship between two requirements, used when a
requirement depends on another requirement. Types of dependency
relationships include:
• Necessity: when it only makes sense to implement a particular
requirement if a related requirement is also implemented.
• Effort: when a requirement is easier to implement if a related
requirement is also implemented.
• Satisfy: relationship between an implementation element and the
requirements it is satisfying. For example, the relationship between a
functional requirement and a solution component that is implementing it.
• Validate: relationship between a requirement and a test case or other
element that can determine whether a solution fulfills the requirement.
.3 Traceability Repository
Requirements traceability is documented and maintained in accordance with the
methods identified by the business analysis approach. Requirements
management tools can provide significant benefits when there is a need to trace
a large number of requirements that may be deemed unmanageable with manual
approaches.
5.1.5
Guidelines and Tools
• Domain Knowledge: knowledge of and expertise in the business domain
needed to support traceability.
• Information Management Approach: provides decisions from planning
activities concerning the traceability approach.
• Legal/Regulatory Information: describes legislative rules or regulations that
must be followed. These may need to be considered when defining traceability
rules.
• Requirements Management Tools/Repository: used to store and manage
business analysis information. The tool may be as simple as a text document or
as complex as a dedicated requirements management tool.
5.1.6
Techniques
• Business Rules Analysis: used to trace business rules to requirements that
they support, or rules that support requirements.
• Functional Decomposition: used to break down solution scope into smaller
components for allocation, as well as to trace high-level concepts to low-level
concepts.
• Process Modelling: used to visually show the future state process, as well as
tracing requirements to the future state process.
• Scope Modelling: used to visually depict scope, as well as trace requirements
to the area of scope the requirement supports.



Requirements Life Cycle Management
Maintain Requirements
83
5.1.7
Stakeholders
• Customers: are affected by how and when requirements are implemented, and
may have to be consulted about, or agree to, the traceability relationships.
• Domain Subject Matter Expert: may have recommendations regarding the
set of requirements to be linked to a solution component or to a release.
• End User: may require specific dependency relationships that allow certain
requirements to be implemented at the same time or in a specific sequence.
• Implementation Subject Matter Expert: traceability ensures that the
solution being developed meets the business need and brings awareness of
dependencies between solution components during implementation.
• Operational Support: traceability documentation provides another reference
source for help desk support.
• Project Manager: traceability supports project change and scope
management.
• Sponsor: is required to approve the various relationships.
• Suppliers: are affected by how and when requirements are implemented.
• Tester: needs to understand how and where requirements are implemented
when creating test plans and test cases, and may trace test cases to
requirements.
5.1.8
Outputs
• Requirements (traced): have clearly defined relationships to other
requirements, solution components, or releases, phases, or iterations, within a
solution scope, such that coverage and the effects of change are clearly
identifiable.
• Designs (traced): clearly defined relationships to other requirements, solution
components, or releases, phases, or iterations, within a solution scope, such
that coverage and the effects of change are clearly identifiable.
5.2
Maintain Requirements
5.2.1
Purpose
The purpose of Maintain Requirements is to retain requirement accuracy and
consistency throughout and beyond the change during the entire requirements
life cycle, and to support reuse of requirements in other solutions.
5.2.2
Description
A requirement that represents an ongoing need must be maintained to ensure
that it remains valid over time.



Maintain Requirements
Requirements Life Cycle Management
84
In order to maximize the benefits of maintaining and reusing requirements, the
requirements should be:
• consistently represented,
• reviewed and approved for maintenance using a standardized process that
defines proper access rights and ensures quality, and
• easily accessible and understandable.
5.2.3
Inputs
• Requirements: include goals, objectives, business requirements, stakeholder
requirements, solution requirements, and transition requirements. These should
be maintained throughout their life cycle.
• Designs: can be maintained throughout their life cycle, as needed.
Figure 5.2.1: Maintain Requirements Input/Output Diagram
5.2.4
Elements
.1 Maintain Requirements
Requirements are maintained so that they remain correct and current after an
approved change. Business analysts are responsible for conducting maintenance
to ensure this level of accuracy is retained. For requirements to be properly
maintained they must be clearly named and defined, and easily available to
stakeholders.
Business analysts also maintain the relationships among requirements, sets of
requirements, and associated business analysis information to ensure the context
and original intent of the requirement is preserved. Repositories with accepted
Output
Input
5.2
Maintain Requirements
Information Management
Approach
5.2
Requirements
(maintained)
Designs
Requirements
5.2
Designs
(maintained)
Guidelines and Tools



Requirements Life Cycle Management
Maintain Requirements
85
taxonomies assist in establishing and maintaining links between maintained
requirements, and facilitate requirements and designs traceability.
.2 Maintain Attributes
While eliciting requirements, business analysts elicit requirement attributes.
Information such as the requirement’s source, priority, and complexity aid in
managing each requirement throughout the life cycle. Some attributes change as
the business analyst uncovers more information and conducts further analysis. An
attribute may change even though the requirement does not.
.3 Reusing Requirements
There are situations in which requirements can be reused.
Requirements that are candidates for long-term use by the organization are
identified, clearly named, defined, and stored in a manner that makes them easily
retrievable by other stakeholders. Depending on the level of abstraction and
intended need being addressed, requirements can be reused:
• within the current initiative,
• within similar initiatives,
• within similar departments, and
• throughout the entire organization.
Requirements at high levels of abstraction may be written with limited reference
to specific solutions. Requirements that are represented in a general manner,
without direct ties to a particular tool or organizational structure, tend to be more
reusable. These requirements are also less subject to revision during a change. As
requirements are expressed in more detail, they become more tightly associated
with a specific solution or solution option. Specific references to applications or
departments limit the reuse of requirements and designs across an organization.
Requirements that are intended for reuse reflect the current state of the
organization. Stakeholders validate the proposed requirements for reuse before
they can be accepted into a change.
5.2.5
Guidelines and Tools
• Information Management Approach: indicates how requirements will be
managed for reuse.
5.2.6
Techniques
• Business Rules Analysis: used to identify business rules that may be similar
across the enterprise in order to facilitate reuse.
• Data Flow Diagrams: used to identify information flow that may be similar
across the enterprise in order to facilitate reuse.
• Data Modelling: used to identify data structure that may be similar across the
enterprise in order to facilitate reuse.



Prioritize Requirements
Requirements Life Cycle Management
86
• Document Analysis: used to analyze existing documentation about an
enterprise that can serve as the basis for maintaining and reusing requirements.
• Functional Decomposition: used to identify requirements associated with the
components and available for reuse.
• Process Modelling: used to identify requirements associated with the
processes that may be available for reuse.
• Use Cases and Scenarios: used to identify a solution component that may be
utilized by more than one solution.
• User Stories: used to identify requirements associated with the story that may
be available for reuse.
5.2.7
Stakeholders
• Domain Subject Matter Expert: references maintained requirements on a
regular basis to ensure they are accurately reflecting stated needs.
• Implementation Subject Matter Expert: utilizes maintained requirements
when developing regression tests and conducting impact analysis for an
enhancement.
• Operational Support: maintained requirements are likely to be referenced to
confirm the current state.
• Regulator: maintained requirements are likely to be referenced to confirm
compliance to standards.
• Tester: maintained requirements are used by testers to aid in test plan and test
case creation.
5.2.8
Outputs
• Requirements (maintained): defined once and available for long-term usage
by the organization. They may become organizational process assets or be used
in future initiatives. In some cases, a requirement that was not approved or
implemented may be maintained for a possible future initiative.
• Designs (maintained): may be reusable once defined. For example, as a self-
contained component that can be made available for possible future use.
5.3
Prioritize Requirements
5.3.1
Purpose
The purpose of Prioritize Requirements is to rank requirements in the order of
relative importance.



Requirements Life Cycle Management
Prioritize Requirements
87
5.3.2
Description
Prioritization is the act of ranking requirements to determine their relative
importance to stakeholders. When a requirement is prioritized, it is given greater
or lesser priority. Priority can refer to the relative value of a requirement, or to the
sequence in which it will be implemented. Prioritization is an ongoing process,
with priorities changing as the context changes.
Inter-dependencies between requirements are identified and may be used as the
basis for prioritization. Prioritization is a critical exercise that seeks to ensure the
maximum value is achieved.
5.3.3
Inputs
• Requirements: any requirements in the form of text, matrices, or diagrams
that are ready to prioritize.
• Designs: any designs in the form of text, prototypes, or diagrams that are ready
to prioritize.
Figure 5.3.1: Prioritize Requirements Input/Output Diagram
Output
Input
Tasks Using This Output
5.3
Prioritize Requirements
Business Constraints
5.3
Requirements
(prioritized)
Designs
Requirements
Change Strategy
Domain Knowledge
Governance Approach
5.3
Designs
(prioritized)
Requirements Architecture
6.3
Assess Risks
Requirements Management
Tools/Repository
Solution Scope
Guidelines and Tools



Prioritize Requirements
Requirements Life Cycle Management
88
5.3.4
Elements
.1 Basis for Prioritization
The basis on which requirements are prioritized is agreed upon by relevant
stakeholders as defined in the Business Analysis Planning and Monitoring
knowledge area.
Typical factors that influence prioritization include:
• Benefit: the advantage that accrues to stakeholders as a result of
requirement implementation, as measured against the goals and objectives
for the change. The benefit provided can refer to a specific functionality,
desired quality, or strategic goal or business objective. If there are multiple
stakeholders, each group may perceive benefits differently. Conflict
resolution and negotiation may be employed to come to consensus on
overall benefit.
• Penalty: the consequences that result from not implementing a given
requirement. This includes prioritizing requirements in order to meet
regulatory or policy demands imposed on the organization, which may take
precedence over other stakeholder interests. Penalty may also refer to the
negative consequence of not implementing a requirement that improves
the experience of a customer.
• Cost: the effort and resources needed to implement the requirement.
Information about cost typically comes from the implementation team or
the vendor. Customers may change the priority of a requirement after
learning the cost. Cost is often used in conjunction with other criteria, such
as cost-benefit analysis.
• Risk: the chance that the requirement cannot deliver the potential value, or
cannot be met at all. This may include many factors such as the difficulty of
implementing a requirement, or the chance that stakeholders will not
accept a solution component. If there is a risk that the solution is not
technically feasible, the requirement that is most difficult to implement may
be prioritized to the top of the list in order to minimize the resources that
are spent before learning that a proposed solution cannot be delivered. A
proof of concept may be developed to establish that high risk options are
possible.
• Dependencies: relationships between requirements where one
requirement cannot be fulfilled unless the other requirement is fulfilled. In
some situations, it may be possible to achieve efficiencies by implementing
related requirements at the same time. Dependencies may also be external
to the initiative, including but not limited to other teams’ decisions, funding
commitments, and resource availability. Dependencies are identified as part
of the task Trace Requirements (p. 79).
• Time Sensitivity: the 'best before' date of the requirement, after which
the implementation of the requirement loses significant value. This includes
time-to-market scenarios, in which the benefit derived will be exponentially



Requirements Life Cycle Management
Prioritize Requirements
89
greater if the functionality is delivered ahead of the competition. It can also
refer to seasonal functionality that only has value at a specific time of year.
• Stability: the likelihood that the requirement will change, either because it
requires further analysis or because stakeholders have not reached a
consensus about it. If a requirement is not stable, it may have a lower
priority in order to minimize unanticipated rework and wasted effort.
• Regulatory or Policy Compliance: requirements that must be
implemented in order to meet regulatory or policy demands imposed on the
organization, which may take precedence over other stakeholder interests.
.2 Challenges of Prioritization
Prioritization is an assessment of relative value. Each stakeholder may value
something different. When this occurs, there may be conflict amongst
stakeholders. Stakeholders may also have difficulty characterizing any
requirement as a lower priority, and this may impact the ability to make necessary
trade-offs. In addition, stakeholders may (intentionally or unintentionally) indicate
priority to influence the result to their desired outcome.
Different types of requirements may not all respond to the criteria in the same
way and may appear to conflict. There may be a need for stakeholders to make
trade-offs in prioritization.
.3 Continual Prioritization
Priorities may shift as the context evolves and as more information becomes
available. Initially, prioritization is done at a higher level of abstraction. As the
requirements are further refined, prioritization is done at a more granular level
and will incorporate additional bases for prioritization as they become
appropriate. The basis for prioritization may be different at various stages of the
change. For example, stakeholders may initially prioritize based on benefits. The
implementation team may then re-prioritize the requirements based on the
sequence in which they must be implemented due to technical constraints. Once
the implementation team has provided the cost of each requirement, the
stakeholders may re-prioritize yet again.
5.3.5
Guidelines and Tools
• Business Constraints: regulatory statutes, contractual obligations and
business policies that may define priorities.
• Change Strategy: provides information on costs, timelines, and value
realization which are used to determine priority of requirements.
• Domain Knowledge: knowledge and expertise of the business domain
needed to support prioritization.
• Governance Approach: outlines the approach for prioritizing requirements.
• Requirements Architecture: utilized to understand the relationship with
other requirements and work products.



Prioritize Requirements
Requirements Life Cycle Management
90
• Requirements Management Tools/Repository: including a requirements
attribute for prioritization can help the business analyst to sort and access
requirements by priority.
• Solution Scope: considered when prioritizing requirements to ensure scope is
managed.
5.3.6
Techniques
• Backlog Management: used to compare requirements to be prioritized. The
backlog can be the location where the prioritization is maintained.
• Business Cases: used to assess requirements against identified business goals
and objectives to determine importance.
• Decision Analysis: used to identify high-value requirements.
• Estimation: used to produce estimates for the basis of prioritization.
• Financial Analysis: used to assess the financial value of a set of requirements
and how the timing of delivery will affect that value.
• Interviews: used to gain an understanding of a single or small group of
stakeholders' basis of prioritization or priorities.
• Item Tracking: used to track issues raised by stakeholders during prioritization.
• Prioritization: used to facilitate the process of prioritization.
• Risk Analysis and Management: used to understand the risks for the basis of
prioritization.
• Workshops: used to gain an understanding of stakeholders' basis of
prioritization or priorities in a facilitated group setting.
5.3.7
Stakeholders
• Customer: verifies that the prioritized requirements will deliver value from a
customer or end-user perspective. The customer can also negotiate to have the
prioritization changed based on relative value.
• End User: verifies that the prioritized requirements will deliver value from a
customer or end-user perspective.
• Implementation Subject Matter Expert: provides input relating to technical
dependencies and can negotiate to have the prioritization changed based on
technical constraints.
• Project Manager: uses the prioritization as input into the project plan and into
the allocation of requirements to releases.
• Regulator: can verify that the prioritization is consistent with legal and
regulatory constraints.
• Sponsor: verifies that the prioritized requirements will deliver value from an
organizational perspective.



Requirements Life Cycle Management
Assess Requirements Changes
91
5.3.8
Outputs
• Requirements (prioritized): prioritized or ranked requirements are available
for additional work, ensuring that the highest valued requirements are
addressed first.
• Designs (prioritized): prioritized or ranked designs are available for additional
work, ensuring that the highest valued designs are addressed first.
5.4
Assess Requirements Changes
5.4.1
Purpose
The purpose of Assess Requirements Changes is to evaluate the implications of
proposed changes to requirements and designs.
5.4.2
Description
The Assess Requirements Changes task is performed as new needs or possible
solutions are identified. These may or may not align to the change strategy and/
or solution scope. Assessment must be performed to determine whether a
proposed change will increase the value of the solution, and if so, what action
should be taken.
Business analysts assess the potential effect of the change to solution value, and
whether proposed changes introduce conflicts with other requirements or
increase the level of risk. Business analysts also ensure each proposed change can
be traced back to a need.
When assessing changes, business analysts consider if each proposed change:
• aligns with the overall strategy,
• affects value delivered to the business or stakeholder groups,
• impacts the time to deliver or the resources required to deliver the value,
and
• alters any risks, opportunities, or constraints associated with the overall
initiative.
The results of the assessment must support the decision making and change
control approaches defined by the task Plan Business Analysis Governance (p. 37).
5.4.3
Inputs
• Proposed Change: can be identified at any time and impact any aspect of
business analysis work or deliverables completed to date. There are many
triggers for a proposed change including business strategy changes,
stakeholders, legal requirements, or regulatory changes.



Assess Requirements Changes
Requirements Life Cycle Management
92
• Requirements: may need to be assessed to identify the impact of a proposed
modification.
• Designs: may need to be assessed to identify the impact of a proposed
modification.
Figure 5.4.1: Assess Requirements Changes Input/Output Diagram
5.4.4
Elements
.1 Assessment Formality
Business analysts will determine the formality of the assessment process based on
the information available, the apparent importance of the change, and the
governance process. Many proposed changes may be withdrawn from
consideration or declined before any formal approval is required. A predictive
approach may indicate a more formal assessment of proposed changes. In
predictive approaches, the impact of each change can be disruptive; the change
can potentially generate a substantial reworking of tasks and activities completed
in previous activities. An adaptive approach may require less formality in the
assessment of proposed changes. While there may be reworking needed as a
result of each change, adaptive approaches try to minimize the impact of changes
by utilizing iterative and incremental implementation techniques. This idea of
continuous evolution may reduce the need for formal impact assessment.
.2 Impact Analysis
Impact analysis is performed to assess or evaluate the effect of a change.
Traceability is a useful tool for performing impact analysis. When a requirement
Output
5.4
Assess Requirements Changes
Change Strategy
Designs
Requirements
Domain Knowledge
Governance Approach
Legal/Regulatory
Information
5.1
Requirements
Change
Assessment
5.1
Designs Change
Assessment
Proposed Change
Requirements Architecture
Solution Scope
Guidelines and Tools
Input



Requirements Life Cycle Management
Assess Requirements Changes
93
changes, its relationships to other requirements or solution components can be
reviewed. Each related requirement or component may also require a change to
support the new requirement.
When considering changes or additions to existing requirements, business
analysts assess the impact of the proposed change by considering:
• Benefit: the benefit that will be gained by accepting the change.
• Cost: the total cost to implement the change including the cost to make
the change, the cost of associated rework, and the opportunity costs such
as the number of other features that may need to be sacrificed or deferred
if the change is approved.
• Impact: the number of customers or business processes affected if the
change is accepted.
• Schedule: the impact to the existing delivery commitments if the change is
approved.
• Urgency: the level of importance including the factors which drive
necessity such as regulator or safety issues.
.3 Impact Resolution
Depending on the planned approach, various stakeholders (including the business
analyst) may be authorized to approve, deny, or defer the proposed change. All
impacts and resolutions resulting from the change analysis are to be documented
and communicated to all stakeholders. How decisions and changes will be made
and communicated across an initiative is determined by the task Plan Business
Analysis Governance (p. 37).
5.4.5
Guidelines and Tools
• Change Strategy: describes the purpose and direction for changes, establishes
the context for the change, and identifies the critical components for change.
• Domain Knowledge: knowledge of and expertise in the business domain is
needed to assess proposed requirements changes.
• Governance Approach: provides guidance regarding the change control and
decision-making processes, as well as the roles of stakeholders within this
process.
• Legal/Regulatory Information: describes legislative rules or regulations that
must be followed. These may impact requirements and must be considered
when making changes.
• Requirements Architecture: requirements may be related to each other,
therefore the business analyst examines and analyzes the requirement
relationships to determine which requirements will be impacted by a requested
requirements change.
• Solution Scope: must be considered when assessing changes to fully
understand the impact of a proposed change.



Assess Requirements Changes
Requirements Life Cycle Management
94
5.4.6
Techniques
• Business Cases: used to justify a proposed change.
• Business Rules Analysis: used to assess changes to business policies and
business rules, and develop revised guidance.
• Decision Analysis: used to facilitate the change assessment process.
• Document Analysis: used to analyze any existing documents that facilitate an
understanding of the impact of the change.
• Estimation: used to determine the size of the change.
• Financial Analysis: used to estimate the financial consequences of a proposed
change.
• Interface Analysis: used to help business analysts identify interfaces that can
be affected by the change.
• Interviews: used to gain an understanding of the impact on the organization
or its assets from a single or small group of stakeholders.
• Item Tracking: used to track any issues or conflicts discovered during impact
analysis.
• Risk Analysis and Management: used to determine the level of risk
associated with the change.
• Workshops: used to gain an understanding of the impact or to resolve
changes in a group setting.
5.4.7
Stakeholders
• Customer: provides feedback concerning the impact the change will have on
value.
• Domain Subject Matter Expert: has expertise in some aspect of the situation
and can provide insight into how the change will impact the organization and
value.
• End User: uses the solution or is a component of the solution, and can offer
information about the impact of the change on their activities.
• Operational Support: provides information on both their ability to support
the operation of the solution and their need to understand the nature of the
change in the solution in order to be able to support it.
• Project Manager: reviews the requirements change assessment to determine if
additional project work is required for a successful implementation of the
solution.



Requirements Life Cycle Management
Approve Requirements
95
• Regulator: changes are likely to be referenced by auditors to confirm
compliance to standards.
• Sponsor: accountable for the solution scope and can provide insight to be
utilized when assessing change.
• Tester: consulted for establishing impact of the proposed changes.
5.4.8
Outputs
• Requirements Change Assessment: the recommendation to approve,
modify, or deny a proposed change to requirements.
• Designs Change Assessment: the recommendation to approve, modify, or
deny a proposed change to one or more design components.
5.5
Approve Requirements
5.5.1
Purpose
The purpose of Approve Requirements is to obtain agreement on and approval of
requirements and designs for business analysis work to continue and/or solution
construction to proceed.
5.5.2
Description
Business analysts are responsible for ensuring clear communication of
requirements, designs, and other business analysis information to the key
stakeholders responsible for approving that information.
Approval of requirements and designs may be formal or informal. Predictive
approaches typically perform approvals at the end of the phase or during planned
change control meetings. Adaptive approaches typically approve requirements
only when construction and implementation of a solution meeting the
requirement can begin. Business analysts work with key stakeholders to gain
consensus on new and changed requirements, communicate the outcome of
discussions, and track and manage the approval.
5.5.3
Inputs
• Requirements (verified): a set of requirements that have been verified to be
of sufficient quality to be used as a reliable body of work for further
specification and development.
• Designs: a set of designs that have been determined as ready to be used for
further specification and development.



Approve Requirements
Requirements Life Cycle Management
96
Figure 5.5.1: Approve Requirements Input/Output Diagram
Once a
requirement has
been approved, it
is a finalized
business analysis
work product,
and is
implemented.
5.5.4
Elements
.1 Understand Stakeholder Roles
The approval process is defined by the task Plan Business Analysis Governance
(p. 37). Part of defining the approval process is understanding stakeholder roles
and authority levels. Business analysts are responsible for obtaining stakeholder
approvals and are required to understand who holds decision-making
responsibility and who possesses authority for sign-off across the initiative.
Business analysts also consider any influential stakeholders who should be
consulted or informed about the requirements. Few stakeholders may have the
authority to approve or deny changes, but many stakeholders may be able to
influence these decisions.
.2 Conflict and Issue Management
To maintain stakeholder support for the solution, consensus among stakeholders
is usually sought prior to requesting approval of requirements. The approach for
determining how to secure decisions and resolve conflicts across an initiative is
planned for in the task Plan Business Analysis Governance (p. 37).
Stakeholder groups frequently have varying points of view and conflicting
priorities. A conflict may arise among stakeholders as a result of different
interpretations of requirements or designs and conflicting values placed on them.
The business analyst facilitates communication between stakeholders in areas of
conflict so that each group has an improved appreciation for the needs of the
others. Conflict resolution and issue management may occur quite often, as the
business analyst is reviewing requirements and designs, and aiming to secure
sign-off.
Output
5.5
Approve Requirements
Change Strategy
Designs
Requirements
(verified)
Governance Approach
Legal/Regulatory
Information
Requirements Management
Tools/Repository
5.5
Requirements
(approved)
5.5
Designs
(approved)
Solution Scope
Guidelines and Tools
Input



Requirements Life Cycle Management
Approve Requirements
97
.3 Gain Consensus
Business analysts are responsible for ensuring that the stakeholders with approval
authority understand and accept the requirements. Approval may confirm that
stakeholders believe that sufficient value will be created for the organization to
justify investment in a solution. Business analysts obtain approval by reviewing the
requirements or changes to requirements with the accountable individuals or
groups and requesting that they approve, indicating their agreement with the
solution or designs described.
Using the methods and means established in the tasks Plan Business Analysis
Governance (p. 37) and Communicate Business Analysis Information (p. 67)
business analysts present the requirements to stakeholders for approval. Business
analysts facilitate this approval process by addressing any questions or providing
additional information when requested.
Complete agreement may not be necessary for a successful change, but if there is
a lack of agreement, the associated risks are to be identified and managed
accordingly.
.4 Track and Communicate Approval
The business analyst records approval decisions, possibly in requirements
maintenance and tracking tools. In order to communicate the status of
requirements, it is necessary to keep accurate records of current approval status.
Stakeholders must be able to determine what requirements and designs are
currently approved and in line for implementation. There may be value in
maintaining an audit history of changes to requirements: what was changed,
who made the change, the reason for the change, and when it was made.
5.5.5
Guidelines and Tools
• Change Strategy: provides information which assists in managing stakeholder
consensus regarding the needs of all stakeholders.
• Governance Approach: identifies the stakeholders who have the authority
and responsibility to approve business analysis information, and explains when
such approvals will take place and how they will align to organizational policies.
• Legal/Regulatory Information: describes legislative rules or regulations that
must be followed. They may impact the requirements and designs approval
process.
• Requirement Management Tools/Repository: tool to record requirements
approvals.
• Solution Scope: must be considered when approving requirements to
accurately assess alignment and completeness.
5.5.6
Techniques
• Acceptance and Evaluation Criteria: used to define approval criteria.



Approve Requirements
Requirements Life Cycle Management
98
• Decision Analysis: used to resolve issues and gain agreement.
• Item Tracking: used to track issues identified during the agreement process.
• Reviews: used to evaluate requirements.
• Workshops: used to facilitate obtaining approval.
5.5.7
Stakeholders
• Customer: may play an active role in reviewing and approving requirements
and designs to ensure needs are met.
• Domain Subject Matter Expert: may be involved in the review and approval
of requirements and designs as defined by stakeholder roles and responsibilities
designation.
• End User: people who use the solution, or who are a solution component, and
may be involved in the review, validation, and prioritization of requirements and
designs as defined by the stakeholder roles and responsibilities designation.
• Operational Support: responsible for ensuring that requirements and designs
are supportable within the constraints imposed by technology standards and
organizational capability plans. Operational support personnel may have a role
in reviewing and approving requirements.
• Project Manager: responsible for identifying and managing risks associated
with solution design, development, delivery, implementation, operation and
sustainment. The project manager may manage the project plan activities
pertaining to review and/or approval.
• Regulator: external or internal party who is responsible for providing opinions
on the relationship between stated requirements and specific regulations, either
formally in an audit, or informally as inputs to requirements life cycle
management tasks.
• Sponsor: responsible to review and approve the business case, solution or
product scope, and all requirements and designs.
• Tester: responsible for ensuring quality assurance standards are feasible within
the business analysis information. For example, requirements have the testable
characteristic.
5.5.8
Outputs
• Requirements (approved): requirements which are agreed to by stakeholders
and are ready for use in subsequent business analysis efforts.
• Designs (approved): designs which are agreed to by stakeholders and are
ready for use in subsequent business analysis or solution development efforts.



99
6
Strategy Analysis
Strategy defines the most effective way to apply the capabilities of an enterprise
in order to reach a desired set of goals and objectives. Strategies may exist for the
entire enterprise, for a division, department or region, and for a product, project,
or iteration.
The Strategy Analysis knowledge area describes the business analysis work that
must be performed to collaborate with stakeholders in order to identify a need of
strategic or tactical importance (the business need), enable the enterprise to
address that need, and align the resulting strategy for the change with higher-
and lower-level strategies.
Strategy analysis focuses on defining the future and transition states needed to
address the business need, and the work required is defined both by that need
and the scope of the solution space. It covers strategic thinking in business
analysis, as well as the discovery or imagining of possible solutions that will
enable the enterprise to create greater value for stakeholders, and/or capture
more value for itself.
Strategy analysis provides context to requirements analysis and design definition
for a given change. Strategy analysis should be performed as a business need is
identified. This allows stakeholders to make the determination of whether to
address that need or not. Strategy analysis is an ongoing activity that assesses any
changes in that need, in its context, or any new information that may indicate
that an adjustment to the change strategy may be required.
The following image illustrates the spectrum of value as business analysis
activities progress from delivering potential value to actual value.



Strategy Analysis
100
Figure 6.0.1: Business Analysis Value Spectrum
When performing strategy analysis, business analysts must consider the context
in which they are working, and how predictable the range of possible outcomes
is. When a change will have a predictable outcome, the future state and possible
transition states can typically be clearly defined, and a clear strategy can be
planned out. If the outcome of a change is difficult to predict, the strategy may
need to focus more on mitigating risk, testing assumptions, and changing course
until a strategy that will succeed in reaching the business goals can be identified
or until the initiative has ended. These tasks may be performed in any order,
though they are often performed concurrently, as strategy must be shaped by
what is actually achievable.
A strategy may be captured in a strategic plan, product vision, business case,
product roadmap, or other artifacts.
The Strategy Analysis knowledge area includes the following tasks:
• Analyze Current State: understands the business need and how it relates
to the way the enterprise functions today. Sets a baseline and context for
change.
• Define Future State: defines goals and objectives that will demonstrate
that the business need has been satisfied and defines what parts of the
enterprise need to change in order to meet those goals and objectives.
• Assess Risks: understands the uncertainties around the change, considers
the effect those uncertainties may have on the ability to deliver value
through a change, and recommends actions to address risks where
appropriate.
• Define Change Strategy: performs a gap analysis between current and
future state, assesses options for achieving the future state, and
recommends the highest value approach for reaching the future state
including any transition states that may be required along the way.
Solution Evaluation
Potential
Requirements Analysis
& Design Definition
Strategy Analysis
Need
Solution
Scope
Requirements
Design
Proof of Concept/
Prototype
Pilot/Beta
Operating
Actual



Strategy Analysis
101
The Core Concept Model in Strategy Analysis
The Business Analysis Core Concept Model™ (BACCM™) describes the
relationships among the six core concepts. The following table describes the
usage and application of each of the core concepts within the context of Strategy
Analysis.
Table 6.0.1: The Core Concept Model in Strategy Analysis
Core Concept
During Strategy Analysis, business
analysts...
Change: the act of transformation
in response to a need.
define the future state and develop a
change strategy to achieve the future
state.
Need: a problem or opportunity to
be addressed.
identify needs within the current state and
prioritize needs to determine the desired
future state.
Solution: a specific way of
satisfying one or more needs in a
context.
define the scope of a solution as part of
developing a change strategy.
Stakeholder: a group or
individual with a relationship to
the change, the need, or the
solution.
collaborate with stakeholders to
understand the business need and to
develop a change strategy and future
state that will meet those needs.
Value: the worth, importance, or
usefulness of something to a
stakeholder in a context.
examine the potential value of the
solution to determine if a change is
justified.
Context: the circumstances that
influence, are influenced by, and
provide understanding of the
change.
consider the context of the enterprise in
developing a change strategy.



Strategy Analysis
102
Figure 6.0.2: Strategy Analysis Input/Output Diagram
Tasks
Output
6.3
Assess Risks
6.2
Define Future State
6.1
Analyze Current
State
6.4
Define Change
Strategy
Needs
Influences
(internal, external)
3.2
Stakeholder
Engagement
Approach
5.3
Designs
(prioritized)
4.3
Elicitation Results
(confirmed)
6.1
Current State
Description
6.1
Business
Requirements
6.2
Business Objectives
6.2
Potential Value
6.2
Future State
Description
6.3
Risk Analysis Results
6.4
Change Strategy
6.4
Solution Scope
4.2
Elicitation Results
(unconfirmed)
5.3
Requirements
(prioritized)
Input



Strategy Analysis
Analyze Current State
103
6.1
Analyze Current State
6.1.1
Purpose
The purpose of Analyze Current State is to understand the reasons why an
enterprise needs to change some aspect of how it operates and what would be
directly or indirectly affected by the change.
6.1.2
Description
The starting point for any change is an understanding of why the change is
needed. Potential change is triggered by problems or opportunities that cannot
be addressed without altering the current state. Business analysts work to help
stakeholders enable change by exploring and articulating the business needs that
drive the desire to change. Without clearly understood business needs, it is
impossible to develop a coherent strategy, and the resulting change initiative is
almost certain to be driven by a mix of conflicting stakeholder demands.
Change always occurs in a context of existing stakeholders, processes,
technology, and policies which constitute the current state of the enterprise.
Business analysts examine the current state in the context of the business need to
understand what may influence proposed changes, and what will be affected by
them. The current state is explored in just enough detail to validate the need for
a change and/or the change strategy. Understanding the current state of the
enterprise prior to the change is necessary to identify what will need to change to
achieve a desired future state and how the effect of the change will be assessed.
The scope of the current state describes the important existing characteristics of
the environment. The boundaries of the current state scope are determined by
the components of the enterprise and its environment as they relate to the needs.
The current state can be described on different levels, ranging from the entire
enterprise to small components of a solution. Creating a model of the current
state might require collaboration throughout or outside the enterprise. For small
efforts, the scope might be only a small component of an enterprise.
The current state of an enterprise is rarely static while a change is being
developed and implemented. Internal and external influencers, as well as other
organizational changes, can affect the current state in ways that force alterations
in the desired future state, change strategy, or requirements and designs.
6.1.3
Inputs
• Elicitation Results: used to define and understand the current state.
• Needs: the problem or opportunity faced by an enterprise or organization often
launches business analysis work to better understand these needs.



Analyze Current State
Strategy Analysis
104
Figure 6.1.1: Analyze Current State Input/Output Diagram
6.1.4
Elements
.1 Business Needs
Business needs are the problems and opportunities of strategic importance faced
by the enterprise. An issue encountered in the organization, such as a customer
complaint, a loss of revenue, or a new market opportunity, usually triggers the
evaluation of a business need.
Output
Tasks Using This Output
Business Analysis Approach
6.1
Current State
Description
4.3
Elicitation Results
(confirmed)
Needs
Enterprise Limitation
Organizational Strategy
Solution Limitation
6.1 Business
Requirements
Solution Performance Goals
6.2
Define Future State
Solution Performance
Measures
Stakeholder Analysis
Results
6.3
Assess Risks
6.4
Define Change
Strategy
7.6
Analyze Potential
Value and
Recommend
Solution
8.4
Assess Enterprise
Limitations
8.5
Recommend
Actions to Increase
Solution Value
Tasks Using This Output
6.2
Define Future State
3.2
Plan Stakeholder
Engagement
3.3
Plan Business
Analysis
Governance
Guidelines and Tools
Input
Task
6.1 Analyze Current State



Strategy Analysis
Analyze Current State
105
A business need may be identified at many different levels of the enterprise:
• From the top-down: a strategic goal that needs to be achieved.
• From the bottom-up: a problem with the current state of a process,
function or system.
• From middle management: a manager needs additional information to
make sound decisions or must perform additional functions to meet
business objectives.
• From external drivers: customer demand or business competition in the
marketplace.
The definition of business needs is frequently the most critical step in any business
analysis effort. A solution must satisfy the business needs to be considered
successful. The way the need is defined determines which alternative solutions
will be considered, which stakeholders will be consulted, and which solution
approaches will be evaluated. Business needs are always expressed from the
perspective of the enterprise, and not that of any particular stakeholder.
Business needs are often identified or expressed along with a presumed solution.
The business analyst should question the assumptions and constraints that are
generally buried in the statement of the issue to ensure that the correct problem
is being solved and the widest possible range of alternative solutions are
considered.
A solution to a set of business needs must have the potential to generate benefits
for the enterprise or its stakeholders, or avoid losses that would otherwise occur.
Factors the business analyst may consider include:
• adverse impacts the problem is causing within the organization and
quantify those impacts (for example, potential lost revenue, inefficiencies,
dissatisfied customers, low employee morale),
• expected benefits from any potential solution (for example, increased
revenue, reduced costs, increased market share),
• how quickly the problem could potentially be resolved or the opportunity
could be taken, and the cost of doing nothing, and
• the underlying source of the problem.
Business needs will drive the overall analysis of the current state. Although it isn’t
necessary to fully detail all aspects of the current state before further developing
the change strategy, this exploration will often uncover deeper underlying causes
of the problem or the opportunity that triggered the investigation (which then
become additional business needs).
.2 Organizational Structure and Culture
Organizational structure defines the formal relationships between people
working in the enterprise. While communication channels and relationships are
not limited to that structure, they are heavily influenced by it, and the reporting
structure may aid or limit a potential change.



Analyze Current State
Strategy Analysis
106
Organizational culture is the beliefs, values, and norms shared by the members of
an organization. These beliefs drive the actions taken by an organization.
Business analysts perform a cultural assessment to:
• identify if cultural changes are required to better achieve the goals,
• identify whether stakeholders understand the rationale for the current state
of the enterprise and the value delivered by it, and
• ascertain whether the stakeholders view the current state as satisfactory or
if change is needed.
.3 Capabilities and Processes
Capabilities and processes describe the activities an enterprise performs. They also
include the knowledge the enterprise has, the products and services it provides,
the functions it supports, and the methods it uses to make decisions. Core
capabilities or processes describe the essential functions of the enterprise that
differentiate it from others. They are measured by performance indicators that
can be used to assess the benefits of a change.
Business analysts may use:
• A capability-centric view of the enterprise when looking for innovative
solutions that combine existing capabilities to produce a new outcome. A
capability-based view is useful in this situation because capabilities are
generally organized in a functional hierarchy with relationships to other
capabilities, making it easier to identify any gaps.
• A process-centric view of the enterprise when looking for ways to improve
the performance of current activities. A process-based view is useful in this
situation because processes are organized in an end-to-end fashion across
the enterprise to deliver value to its customers, making it easier to ensure
that a change does in fact increase performance.
.4 Technology and Infrastructure
Information systems used by the enterprise support people in executing
processes, making decisions, and in interactions with suppliers and customers.
The infrastructure describes the enterprise’s environment with respect to physical
components and capabilities. The infrastructure can include components such as
computer hardware, physical plants, and logistics, as well as their operation and
upkeep.
.5 Policies
Policies define the scope of decision making at different levels of an enterprise.
They generally address routine operations rather than strategic change. They
ensure that decisions are made correctly, provide guidance to staff on permitted
and appropriate behaviour and actions, support governance, and determine
when and how new resources can be acquired. Identification of relevant policies
may shape the scope of the solution space and may be a constraint on the types



Strategy Analysis
Analyze Current State
107
of action that can be pursued.
.6 Business Architecture
No part of the current state should be assessed in complete isolation from the
rest. Business analysts must understand how all of these elements of the current
state fit together and support one another in order to recommend changes that
will be effective. The existing business architecture typically meets an assortment
of business and stakeholder needs. If those needs are not recognized or do not
continue to be met by a proposed transition or future state, changes are likely to
result in a loss of value.
.7 Internal Assets
Business analysts identify enterprise assets used in the current state. Resources
can be tangible or intangible, such as financial resources, patents, reputation, and
brand names.
.8 External Influencers
There are external influences on the enterprise that do not participate in a change
but might present constraints, dependencies, or drivers on the current state.
Sources of external influence include:
• Industry Structure: individual industries have distinct ways in which value
is created within that industry. This is a particularly important influencer if a
proposed change involves entering a new industry.
• Competitors: the nature and intensity of competitors between enterprises
within an industry can be significant. The entry of a new competitor may
also change the nature of the industry or increase competition.
• Customers: the size and nature of existing and potential customer
segments can provide influences such as negotiating power and a degree of
price sensitivity. Alternatively, the emergence of new alternative ways that
customers can meet their needs may drive the enterprise to deliver greater
value.
• Suppliers: the variety and diversity of suppliers might be an influencer, as
can the power that suppliers have over their customers.
• Political and Regulatory Environment: there is often influence from the
current and potential impact of laws and regulations upon the industry.
• Technology: the productivity enhancing potential of recent and expected
technological innovations might influence the need.
• Macroeconomic Factors: the constraints and opportunities that exist
within the existing and expected macroeconomic environment (for
example, trade, unemployment, or inflation) might influence the need.
Some of these sources might use different terminology, based on whether the
enterprise is a for-profit corporation, a non-profit enterprise, or a government
agency. For example, a country does not have customers; it has citizens.



Analyze Current State
Strategy Analysis
108
6.1.5
Guidelines and Tools
• Business Analysis Approach: guides how the business analyst undertakes an
analysis of the current state.
• Enterprise Limitation: used to understand the challenges that exist within the
enterprise.
• Organizational Strategy: an organization will have a set of goals and
objectives which guides operations, establishes direction, and provides a vision
for the future state. This can be implicitly or explicitly stated.
• Solution Limitation: used to understand the current state and the challenges
of existing solutions.
• Solution Performance Goals: measure the current performance of an
enterprise or solution, and serve as a baseline for setting future state goals and
measuring improvement.
• Solution Performance Measures: describe the actual performance of existing
solutions.
• Stakeholder Analysis Results: stakeholders from across the organization will
contribute to an understanding and analysis of the current state.
6.1.6
Techniques
• Benchmarking and Market Analysis: provides an understanding of where
there are opportunities for improvement in the current state. Specific
frameworks that may be useful include 5 Forces analysis, PEST, STEEP, CATWOE,
and others.
• Business Capability Analysis: identifies gaps and prioritizes them in relation
to value and risk.
• Business Model Canvas: provides an understanding of the value proposition
that the enterprise satisfies for its customers, the critical factors in delivering
that value, and the resulting cost and revenue streams. Helpful for
understanding the context for any change and identifying the problems and
opportunities that may have the most significant impact.
• Business Cases: used to capture information regarding the business need and
opportunity.
• Concept Modelling: used to capture key terms and concepts in the business
domain and define the relationships between them.
• Data Mining: used to obtain information on the performance of the
enterprise.
• Document Analysis: analyzes any existing documentation about the current
state, including (but not limited to) documents created during the
implementation of a solution, training manuals, issue reports, competitor
information, supplier agreements, published industry benchmarks, published
technology trends, and performance metrics.



Strategy Analysis
Analyze Current State
109
• Financial Analysis: used to understand the profitability of the current state
and the financial capability to deliver change.
• Focus Groups: solicits feedback from customers or end users about the current
state.
• Functional Decomposition: breaks down complex systems or relationships in
the current state.
• Interviews: facilitate dialogue with stakeholders to understand the current
state and any needs evolving from the current state.
• Item Tracking: tracks and manages issues discovered about the current state.
• Lessons Learned: enables the assessment of failures and opportunities for
improvement in past initiatives, which may drive a business need for process
improvement.
• Metrics and Key Performance Indicators (KPIs): assesses performance of
the current state of an enterprise.
• Mind Mapping: used to explore relevant aspects of the current state and
better understand relevant factors affecting the business need.
• Observation: may provide opportunities for insights into needs within the
current state that have not been identified previously by a stakeholder.
• Organizational Modelling: describes the roles, responsibilities, and reporting
structures that exist within the current state organization.
• Process Analysis: identifies opportunities to improve the current state.
• Process Modelling: describes how work occurs within the current solution.
• Risk Analysis and Management: identifies risks to the current state.
• Root Cause Analysis: provides an understanding of the underlying causes of
any problems in the current state in order to further clarify a need.
• Scope Modelling: helps define the boundaries on the current state
description.
• Survey or Questionnaire: helps to gain an understanding of the current state
from a large, varied, or disparate group of stakeholders.
• SWOT Analysis: evaluates the strengths, weaknesses, opportunities, and
threats to the current state enterprise.
• Vendor Assessment: determines whether any vendors that are part of the
current state are adequately meeting commitments, or if any changes are
needed.
• Workshops: engage stakeholders to collaboratively describe the current state
and their needs.



Define Future State
Strategy Analysis
110
6.1.7
Stakeholders
• Customer: makes use of the existing solution and might have input about
issues with a current solution.
• Domain Subject Matter Expert: has expertise in some aspect of the current
state.
• End User: directly uses a solution and might have input about issues with a
current solution.
• Implementation Subject Matter Expert: has expertise in some aspect of the
current state.
• Operational Support: directly involved in supporting the operations of the
organization and provides information on their ability to support the operation
of an existing solution, as well as any known issues.
• Project Manager: may use information on current state as input to planning.
• Regulator: can inform interpretations of relevant regulations that apply to the
current state in the form of business policies, business rules, procedures, or role
responsibilities. The regulator might have unique input to the operational
assessment, as there might be new laws and regulations with which to comply.
• Sponsor: might have context for performance of existing solutions.
• Supplier: might be an external influencer of the current state.
• Tester: able to provide information about issues with any existing solutions.
6.1.8
Outputs
• Current State Description: the context of the enterprise’s scope, capabilities,
resources, performance, culture, dependencies, infrastructure, external
influences, and significant relationships between these elements.
• Business Requirements: the problem, opportunity, or constraint which is
defined based on an understanding of the current state.
6.2
Define Future State
6.2.1
Purpose
The purpose of Define Future State is to determine the set of necessary conditions
to meet the business need.
6.2.2
Description
All purposeful change must include a definition of success. Business analysts work
to ensure that the future state of the enterprise is well defined, that it is
achievable with the resources available, and that key stakeholders have a shared



Strategy Analysis
Define Future State
111
consensus vision of the outcome. As with current state analysis, the purpose of
future state analysis is not to create a comprehensive description of the outcome
at a level of detail that will directly support implementation. The future state will
be defined at a level of detail that:
• allows for competing strategies to achieve the future state to be identified
and assessed,
• provides a clear definition of the outcomes that will satisfy the business
needs,
• details the scope of the solution space,
• allows for value associated with the future state to be assessed, and
• enables consensus to be achieved among key stakeholders.
The future state description can include any context about the proposed future
state. It describes the new, removed, and modified components of the enterprise.
It can include changes to the boundaries of the organization itself, such as
entering a new market or performing a merger or acquisition. The future state
can also be simple changes to existing components of an organization, such as
changing a step in a process or removing a feature from an existing application.
Change may be needed to any component of the enterprise, including (but not
limited to):
• business processes,
• functions,
• lines of business,
• organization structures,
• staff competencies,
• knowledge and skills,
• training,
• facilities,
• desktop tools,
• organization locations,
• data and information,
• application systems, and/or
• technology infrastructure.
Descriptions may include visual models and text to clearly show the scope
boundaries and details. Relevant relationships between entities are identified and
described. The effort required to describe the future state varies depending on the
nature of the change. The expected outcomes from a change might include
specific metrics or loosely defined results. Describing the future state allows
stakeholders to understand the potential value that can be realized from a
solution, which can be used as part of the decision-making process regarding the
change strategy. In environments where changes result in predictable outcomes
and predictable delivery of value, and where there are a large number of possible
changes that can increase value, the purpose of future state analysis is to gather
sufficient information to make the best possible choices among potential options.
In cases where it is difficult to predict the value realized by a change, the future
state may be defined by identification of appropriate performance measures (to
produce an agreed-upon set of measures for business value), and the change
strategy will support exploration of multiple options.



Define Future State
Strategy Analysis
112
6.2.3
Inputs
• Business Requirements: the problems, opportunities, or constraints that the
future state will address.
Figure 6.2.1: Define Future State Input/Output Diagram
Guidelines and Tools
Tasks Using This Output
Constraints
Business
Objectives
Business
Requirements
Current State Description
Metrics and Key Performance
Indicators (KPIs)
Organizational Strategy
Potential Value
4.5
Manage
Stakeholder
Collaboration
6.4
Define Change
Strategy
7.3
Validate
Requirements
7.5
Define Design
Options
7.6
Analyze Potential
Value and
Recommend
Solution
8.1
Measure Solution
Performance
Tasks Using This Output
6.3
Assess Risks
6.2
Future State
Description
7.3
Validate
Requirements
7.6
Analyze Potential
Value and
Recommend
Solution
8.2
Analyze
Performance
Measures
8.4
Assess Enterprise
Limitations
Tasks Using This Output
6.3
Assess Risks
7.3
Validate
Requirements
7.6
Analyze Potential
Value and
Recommend
Solution
8.1
Measure Solution
Performance
8.4
Assess Enterprise
Limitations
8.5
Recommend
Actions to Increase
Solution Value
8.2
Analyze
Performance
Measures
4.1
Prepare for
Elicitation
4.5
Manage
Stakeholder
Collaboration
6.3
Assess Risks
4.1
Prepare for
Elicitation
Input
Output
6.2
Define Future State



Strategy Analysis
Define Future State
113
6.2.4
Elements
.1 Business Goals and Objectives
A future state can be described in terms of business objectives or goals in order to
guide the development of the change strategy and identify potential value.
Business goals and objectives describe the ends that the organization is seeking to
achieve. Goals and objectives can relate to changes that the organization wants
to accomplish, or current conditions that it wants to maintain.
Goals are longer term, ongoing, and qualitative statements of a state or condition
that the organization is seeking to establish and maintain. Examples of business
goals include:
• Create a new capability such as a new product or service, address a
competitive disadvantage, or create a new competitive advantage.
• Improve revenue by increasing sales or reducing cost.
• Increase customer satisfaction.
• Increase employee satisfaction.
• Comply with new regulations.
• Improve safety.
• Reduce time to deliver a product or service.
High-level goals can be decomposed to break down the general strategy into
areas that may lead to desired results, such as increased customer satisfaction,
operational excellence, and/or business growth. For example, a goal may be to
"increase number of high-revenue customers" and then be further refined into a
goal to "increase number of high revenue customers in the 30-45 age bracket by
30% within 6 months".
As goals are analyzed they are converted into more descriptive, granular and
specific objectives, and linked to measures that make it possible to objectively
assess if the objective has been achieved. Objectives that are measurable enable
teams to know if needs were addressed and whether a change was effective.
Defining measurable objectives is often critical to justify completing the change
and might be a key component to a business case for the change. A common test
for assessing objectives is to ensure that they are SMART:
•  S pecific: describing something that has an observable outcome,
• Measurable: tracking and measuring the outcome,
• Achievable: testing the feasibility of the effort,
• R elevant: aligning with the enterprise’s vision, mission, and goals, and
• T ime-bounded: defining a time frame that is consistent with the need.



Define Future State
Strategy Analysis
114
.2 Scope of Solution Space
Decisions must be made about the range of solutions that will be considered to
meet the business goals and objectives. The scope of the solution space defines
which kinds of options will be considered when investigating possible solutions,
including changes to the organizational structure or culture, capabilities and
processes, technology and infrastructure, policies, products, or services, or even
creating or changing relationships with organizations currently outside the scope
of the extended enterprise. Solutions in each of these areas generally require
specific expertise from both the business analysis and the delivery team. The
analysis for this might happen on different levels in the enterprise, and the scope
of the solution space is not necessarily related to the size of the change. Even a
small change might require looking at the enterprise-level business objectives to
ensure alignment.
If multiple future states can meet the business needs, goals and objectives, it will
be necessary to determine which ones will be considered. This decision is typically
based on the value to be delivered to stakeholders and requires an understanding
of possible change strategies. The critical considerations for the decision are
dependent on the overall objectives of the enterprise, but will involve an
understanding of the quantitative and qualitative value of each option, the time
needed to achieve each future state, and the opportunity cost to the enterprise.
.3 Constraints
Constraints describe aspects of the current state, aspects of the planned future
state that may not be changed by the solution, or mandatory elements of the
design. They must be carefully examined to ensure that they are accurate and
justified.
Constraints may reflect any of the following:
• budgetary restrictions,
• time restrictions,
• technology,
• infrastructure,
• policies,
• limits on the number of resources available,
• restrictions based on the skills of the team and stakeholders,
• a requirement that certain stakeholders not be affected by the
implementation of the solution,
• compliance with regulations, and
• any other restriction.



Strategy Analysis
Define Future State
115
.4 Organizational Structure and Culture
The formal and informal working relationships that exist within the enterprise
may need to change to facilitate the desired future state. Changes to reporting
lines can encourage teams to work more closely together and facilitate alignment
of goals and objectives. Elements of the organizational structure and culture may
need to change to support the future state. Describing the components of the
future state provides insight into potential conflicts, impact, and limits.
.5 Capabilities and Processes
Identify new kinds of activities or changes in the way activities will be performed
to realize the future state. New or changed capabilities and processes will be
needed to deliver new products or services, to comply with new regulations, or to
improve the performance of the enterprise.
.6 Technology and Infrastructure
If current technology and infrastructure are insufficient to meet the business
need, the business analyst identifies the changes necessary for the desired future
state.
The existing technology may impose technical constraints on the design of the
solution. These may include development languages, hardware and software
platforms, and application software that must be used. Technical constraints may
also describe restrictions such as resource utilization, message size and timing,
software size, maximum number of and size of files, records, and data elements.
Technical constraints include any IT architecture standards that must be followed.
.7 Policies
If current polices are insufficient to meet the business need, the business analyst
identifies the changes necessary for the desired future state.
Policies are a common source of constraints on a solution or on the solution
space. Business policies may mandate what solutions can be implemented given
certain levels of approval, the process for obtaining approval, and the necessary
criteria a proposed solution must meet in order to receive funding. In some
instances, a change to an existing policy may open up alternative solutions that
would not otherwise be considered.
.8 Business Architecture
The elements of any future state must effectively support one another and all
contribute to meeting the business goals and objectives. In addition, they should
be integrated into the overall desired future state of the enterprise as a whole,
and support that future state.



Define Future State
Strategy Analysis
116
.9 Internal Assets
The analysis of resources might indicate that existing resources need to be
increased or require increased capabilities, or that new resources need to be
developed. When analyzing resources, business analysts examine the resources
needed to maintain the current state and implement the change strategy, and
determine what resources can be used as part of a desired future state. The
assessment of existing and needed resources is considered when performing a
feasibility analysis on possible solution approaches for the change strategy.
.10 Identify Assumptions
Most strategies are predicated on a set of assumptions that will determine
whether or not the strategy can succeed, particularly when operating in a highly
uncertain environment. It will often be difficult or impossible to prove that the
delivery of a new capability will meet a business need, even in cases where it
appears reasonable to assume that the new capability will have the desired effect.
These assumptions must be identified and clearly understood, so that appropriate
decisions can be made if the assumption later proves invalid. Change strategies in
uncertain environments can be structured in order to test these assumptions as
early as possible to support a redirection or termination of the initiative.
.11 Potential Value
Meeting the business objectives alone does not justify the transition to a future
state; the potential value must be evaluated to see if it is sufficient to justify a
change.
When defining the future state, business analysts identify the potential value of
the solution. The potential value of the future state is the net benefit of the
solution after operating costs are accounted for. A change must result in greater
value for the enterprise than would be achieved if no action was taken. However,
it is possible that the future state will represent a decrease in value from the
current state for some stakeholders or even for the enterprise as a whole. New
regulations or increased competition, for example, might need to be addressed
for the enterprise to remain operating but could still decrease the overall value
captured.
While determining the future state, business analysts consider increased or
decreased potential value from:
• external opportunities revealed in assessing external influences,
• unknown strengths of new partners,
• new technologies or knowledge,
• potential loss of a competitor in the market, and
• mandated adoption of a change component.
Business analysts identify the specific opportunities for potential alterations in
value, as well as the probability of those increases for the individual components



Strategy Analysis
Define Future State
117
of the proposed change. Business analysts estimate a total potential value by
aggregating across all opportunities.
The potential value, including the details of the expected benefit and costs and
the likely result if no change is made, is a key component to making a business
case for the change. Relating descriptions of potential value to measures of actual
value currently being achieved enables stakeholders to understand the expected
change in value. In most cases, the future state will not address all of the
opportunities for improvement. Any unaddressed opportunities might remain
valid after the solution is implemented and should be noted for future analysis in
other changes.
In addition to the potential value of the future state, this analysis should consider
the acceptable level of investment to reach the future state. While the actual
investment will depend on the change strategy, this information guides the
selection of possible strategies.
6.2.5
Guidelines and Tools
• Current State Description: provides the context within which the work needs
to be completed. It is often used as a starting point for the future state.
• Metrics and Key Performance Indicators (KPIs): the key performance
indicators and metrics which will be used to determine whether the desired
future state has been achieved.
• Organizational Strategy: describes the path, method, or approach an
enterprise or organization will take to achieve its desired future state. This can
be implicitly or explicitly stated.
6.2.6
Techniques
• Acceptance and Evaluation Criteria: used to identify what may make the
future state acceptable and/or how options may be evaluated.
• Balanced Scorecard: used to set targets for measuring the future state.
• Benchmarking and Market Analysis: used to make decisions about future
state business objectives.
• Brainstorming: used to collaboratively come up with ideas for the future state.
• Business Capability Analysis: used to prioritize capability gaps in relation to
value and risk.
• Business Cases: used to capture the desired outcomes of the change initiative.
• Business Model Canvas: used to plan strategy for the enterprise by mapping
out the needed infrastructure, target customer base, financial cost structure,
and revenue streams required to fulfill the value proposition to customers in the
desired future state.
• Decision Analysis: used to compare the different future state options and
understand which is the best choice.



Define Future State
Strategy Analysis
118
• Decision Modelling: used to model complex decisions regarding future state
options.
• Financial Analysis: used to estimate the potential financial returns to be
delivered by a proposed future state.
• Functional Decomposition: used to break down complex systems within the
future state for better understanding.
• Interviews: used to talk to stakeholders to understand their desired future
state, which needs they want to address, and what desired business objectives
they want to meet.
• Lessons Learned: used to determine which opportunities for improvement will
be addressed and how the current state can be improved upon.
• Metrics and Key Performance Indicators (KPIs): used to determine when
the organization has succeeded in achieving the business objectives.
• Mind Mapping: used to develop ideas for the future state and understand
relationships between them.
• Organizational Modelling: used to describe the roles, responsibilities, and
reporting structures that would exist within the future state organization.
• Process Modelling: used to describe how work would occur in the future
state.
• Prototyping: used to model future state options and could also help determine
potential value.
• Scope Modelling: used to define the boundaries of the enterprise in the future
state.
• Survey or Questionnaire: used to understand stakeholders' desired future
state, which needs they want to address, and what desired business objectives
they want to meet.
• SWOT Analysis: used to evaluate the strengths, weaknesses, opportunities,
and threats that may be exploited or mitigated by the future state.
• Vendor Assessment: used to assess potential value provided by vendor
solution options.
• Workshops: used to work with stakeholders to collaboratively describe the
future state.
6.2.7
Stakeholders
• Customer: might be targeted purchasers or consumers in a future state who
might or might not be ready or able to consume a new state.
• Domain Subject Matter Expert: provides insight into current state and
potential future states.
• End User: expected to use, or be a component of, a solution that implements
the future state.



Strategy Analysis
Define Future State
119
• Implementation Subject Matter Expert: provides information regarding the
feasibility of achieving the future state.
• Operational Support: directly involved in supporting the operations of the
enterprise and provides information on their ability to support the operation of
a proposed future state.
• Project Manager: might have input on what is a reasonable and manageable
desired future state.
• Regulator: ensures that laws, regulations, or rules are adhered to in the desired
future state. Interpretations of relevant regulations must be included in the
future state description in the form of business policies, business rules,
procedures, or role responsibilities.
• Sponsor: helps determine which business needs to address and sets the
business objectives that a future state will achieve. Authorizes and ensures
funding to support moving towards the future state.
• Supplier: might help define the future state if they are supporting delivery of
the change or deliver any part of the future state operation.
• Tester: responsible for ensuring an envisioned future state can be sufficiently
tested and can help set an appropriate level of quality to target.
6.2.8
Outputs
• Business Objectives: the desired direction that the business wishes to pursue
in order to achieve the future state.
• Future State Description: the future state description includes boundaries of
the proposed new, removed, and modified components of the enterprise and
the potential value expected from the future state. The description might
include the desired future capabilities, policies, resources, dependencies,
infrastructure, external influences, and relationships between each element.
• Potential Value: the value that may be realized by implementing the proposed
future state.



Assess Risks
Strategy Analysis
120
6.3
Assess Risks
6.3.1
Purpose
The purpose of Assess Risks is to understand the undesirable consequences of
internal and external forces on the enterprise during a transition to, or once in,
the future state. An understanding of the potential impact of those forces can be
used to make a recommendation about a course of action.
6.3.2
Description
Assessing risks includes analyzing and managing them. Risks might be related to
the current state, a desired future state, a change itself, a change strategy, or any
tasks being performed by the enterprise.
The risks are analyzed for the:
• possible consequences if the risk occurs,
• impact of those consequences,
• likelihood of the risk, and
• potential time frame when the risk might occur.
The collection of risks is used as an input for selecting or coordinating a change
strategy. A risk assessment can include choosing to accept a risk if either the
effort required to modify the risk or the level of risk outweighs the probable loss.
If the risks are understood and the change proceeds, then the risks can be
managed to minimize their overall impact to value.
Important
A number of methods include 'positive risk' as a way of managing opportunities.
Although the formal definition of risk in the BABOK® Guide doesn't preclude this
usage, 'opportunities' are captured as needs (and managed accordingly), and risk
is used for uncertain events that can produce negative outcomes.
6.3.3
Inputs
• Business Objectives: describing the desired direction needed to achieve the
future state can be used to identify and discuss potential risks.
• Elicitation Results (confirmed): an understanding of what the various
stakeholders perceive as risks to the realization of the desired future state.
• Influences: factors inside of the enterprise (internal) and factors outside of
the enterprise (external) which will impact the realization of the desired future
state.
• Potential Value: describing the value to be realized by implementing the
proposed future state provides a benchmark against which risks can be
assessed.
• Requirements (prioritized): depending on their priority, requirements will
influence the risks to be defined and understood as part of solution realization.



Strategy Analysis
Assess Risks
121
Figure 6.3.1: Assess Risks Input/Output Diagram
6.3.4
Elements
.1 Unknowns
When assessing a risk, there will be uncertainty in the likelihood of it occurring,
and the impact if it does occur. Business analysts collaborate with stakeholders to
assess risks based on current understanding. Even when it is not possible to know
all that will occur as a result of a particular change strategy, it is still possible to
estimate the impact of unknown or uncertain events or conditions occurring.
Business analysts consider other historical contexts from similar situations to
assess risks. The lessons learned from past changes and expert judgment from
Tasks Using This Output
Output
Business Analysis Approach
6.3
Risk Analysis
Results
4.5
Manage
Stakeholder
Collaboration
4.3
Elicitation Results
(confirmed)
Influences
(internal and
external)
Business Policies
Change Strategy
7.6
Analyze Potential
Value and
Recommend
Solution
8.2
Analyze
Performance
Measures
8.4
Assess Enterprise
Limitations
Current State Description
5.3
Designs
(prioritized)
Future State Description
Identified Risks
Stakeholder Engagement
Approach
6.2
Business
Objectives
6.2
Potential Value
6.4
Define Change
Strategy
8.3
Assess Solution
Limitations
5.3
Requirements
(prioritized)
Input
Guidelines and Tools
6.3
Assess Risks



Assess Risks
Strategy Analysis
122
stakeholders assist business analysts in guiding the team in deciding the impact
and likelihood of risks for the current change.
.2 Constraints, Assumptions, and Dependencies
Constraints, assumptions, and dependencies can be analyzed for risks and
sometimes should be managed as risks themselves. If the constraint, assumption,
or dependency is related to an aspect of a change, it can be restated as a risk by
identifying the event or condition and consequences that could occur because of
the constraint, assumption, or dependency.
.3 Negative Impact to Value
Risks are expressed as conditions that increase the likelihood or severity of a
negative impact to value. Business analysts clearly identify and express each risk
and estimate its likelihood and impact to determine the level of risk. Business
analysts estimate a total risk level from the aggregated set of risks, indicating the
overall potential impact for the risks being assessed. In some cases overall risk
level can be quantified in financial terms, or in an amount of time, effort, or other
measures.
.4 Risk Tolerance
How much uncertainty a stakeholder or an enterprise is willing to take on in
exchange for potential value is referred to as risk tolerance.
In general, there are three broad ways of describing attitude toward risk:
• Risk-aversion: An unwillingness to accept much uncertainty; there may be
a preference to either avoid a course of action which carries too high a level
of risk, or to invest more (and therefore accept a lower potential value) to
reduce the risks.
• Neutrality: some level of risk is acceptable, provided the course of action
does not result in a loss even if the risks occur.
• Risk-seeking: A willingness to accept or even take on more risk in return
for a higher potential value.
An individual or organization may exhibit different risk tolerances at different
times. If there is low tolerance for risk, there may be more effort on avoidance,
transfer or mitigation strategies. If the tolerance for risk is high, more risks are
likely to be accepted. Typically, the highest level risks are dealt with no matter
what the risk tolerance level.
.5 Recommendation
Based on the analysis of risks, business analysts recommend a course of action.
Business analysts work with stakeholders to understand the overall risk level and
their tolerance for risk.
The recommendation usually falls into one of the following categories:
• pursue the benefits of a change regardless of the risk,



Strategy Analysis
Assess Risks
123
• pursue the benefits of a change while investing in reducing risk (likelihood
and/or impact),
• seek out ways to increase the benefits of a change to outweigh the risk,
• identify ways to manage and optimize opportunities, and
• do not pursue the benefits of a change.
If the change proceeds with risks, stakeholders should be identified to monitor
the risks and consequences if the risk event occurs. The risk may alter the current
state of the enterprise and require revision of the change strategy. A plan of
action in this case may be developed before the risk materializes.
6.3.5
Guidelines and Tools
• Business Analysis Approach: guides how the business analyst analyzes risks.
• Business Policies: define the limits within which decisions must be made.
These may mandate or govern aspects of risk management.
• Change Strategy: provides the plan to transition from the current state to the
future state and achieve the desired business outcomes. This approach must be
assessed to understand risks associated with the change.
• Current State Description: provides the context within which the work needs
to be completed. It can be used to determine risks associated with the current
state.
• Future State Description: determines risks associated with the future state.
• Identified Risks: can be used as a starting point for more thorough risk
assessment. These can come from Risk Analysis Results, from elicitation
activities, from previous business analysis experience, or based on expert
opinion.
• Stakeholder Engagement Approach: understanding stakeholders and
stakeholder groups helps identify and assess the potential impact of internal
and external forces.
6.3.6
Techniques
• Brainstorming: used to collaboratively identify potential risks for assessment.
• Business Cases: used to capture risks associated with alternative change
strategies.
• Decision Analysis: used to assess problems.
• Document Analysis: used to analyze existing documents for potential risks,
constraints, assumptions, and dependencies.
• Financial Analysis: used to understand the potential effect of risks on the
financial value of the solution.
• Interviews: used to understand what stakeholders think might be risks and the
various factors of those risks.
• Lessons Learned: used as a foundation of past issues that might be risks.



Define Change Strategy
Strategy Analysis
124
• Mind Mapping: used to identify and categorize potential risks and understand
their relationships.
• Risk Analysis and Management: used to identify and manage risks.
• Root Cause Analysis: used to identify and address the underlying problem
creating a risk.
• Survey or Questionnaire: used to understand what stakeholders think might
be risks and the various factors of those risks.
• Workshops: used to understand what stakeholders think might be risks and
the various factors of those risks.
6.3.7
Stakeholders
• Domain Subject Matter Expert: provides input to the risk assessment based
on their knowledge of preparation required in their area of expertise.
• Implementation Subject Matter Expert: provides input to the risk
assessment based on their knowledge of preparation required in their area of
expertise.
• Operational Support: supports the operations of the enterprise and can
identify likely risks and their impact.
• Project Manager: helps to assess risk and is primarily responsible for managing
and mitigating risk to the project.
• Regulator: identifies any risks associated with adherence to laws, regulations,
or rules.
• Sponsor: needs to understand risks as part of authorizing and funding change.
• Supplier: there might be risk associated with using a supplier.
• Tester: identifies risks in the change strategy, from a validation or verification
perspective.
6.3.8
Outputs
Risk Analysis Results: an understanding of the risks associated with achieving the
future state, and the mitigation strategies which will be used to prevent those
risks, reduce the impact of the risk, or reduce the likelihood of the risk occurring.
6.4
Define Change Strategy
6.4.1
Purpose
The purpose of Define Change Strategy is to develop and assess alternative
approaches to the change, and then select the recommended approach.



Strategy Analysis
Define Change Strategy
125
6.4.2
Description
Developing a change strategy is simpler when the current state and the future
state are already defined because they provide some context for the change.
The change strategy clearly describes the nature of the change in terms of:
• context of the change,
• identified alternative change strategies,
• justification for why a particular change strategy is the best approach,
• investment and resources required to work toward the future state,
• how the enterprise will realize value after the solution is delivered,
• key stakeholders in the change, and
• transition states along the way.
The appropriate representation of a change strategy depends on the perspective
of the change team and their stakeholders. The change strategy might be
presented as part of a business case, Statement of Work (SOW), an enterprise’s
strategic plan, or in other formats.
Defining a change strategy usually involves identifying several strategies and
ultimately selecting the strategy that is most appropriate for the situation.
Change strategies can entail attaining only parts of a future state initially, and
therefore include only some components of a complete solution. For each
transition state along the path to reaching the future state, the change strategy
should clarify which parts of the solution are completed and which are not, as
well as which parts of the value can be realized and which cannot.
6.4.3
Inputs
• Current State Description: provides context about the current state, and
includes assessments of internal and external influences to the enterprise under
consideration.
• Future State Description: provides context about the desired future state.
• Risk Analysis Results: describe identified risks and exposure of each risk.
• Stakeholder Engagement Approach: understanding stakeholders'
communication and collaboration needs can help identify change-related
activities that need to be included as part of the change strategy.



Define Change Strategy
Strategy Analysis
126
Figure 6.4.1: Define Change Strategy Input/Output Diagram
Input
Guidelines and Tools
Tasks Using This Output
Business Analysis
Approach
6.4
Change Strategy
6.1
Current State
Description
3.2
Stakeholder
Engagement
Approach
Design Options
Solution
Recommendations
6.4
Solution Scope
3.2
Plan Stakeholder
Engagement
5.3
Prioritize
Requirements
5.4
Assess
Requirements
Changes
5.5
Approve
Requirements
6.3
Assess Risks
7.5
Define Design
Options
Tasks Using This Output
5.3
Prioritize
Requirements
6.3
Risk Analysis
Results
6.2
Future State
Description
5.4
Assess
Requirements
Changes
8.1
Measure Solution
Performance
8.2
Analyze
Performance
Measures
8.3
Assess Solution
Limitations
8.4
Assess Enterprise
Limitations
5.5
Approve
Requirements
7.1
Specify and Model
Requirements
7.3
Validate
Requirements
7.4
Define
Requirements
Architecture
7.5
Define Design
Options
7.6
Analyze Potential
Value and
Recommend
Solution
8.1
Measure Solution
Performance
8.2
Analyze
Performance
Measures
8.3
Assess Solution
Limitations
8.4
Assess Enterprise
Limitations
8.5
Recommend
Actions to Increase
Solution Value
Output
6.4
Define Change Strategy



Strategy Analysis
Define Change Strategy
127
6.4.4
Elements
.1 Solution Scope
The solution is the outcome of a change that allows an enterprise to satisfy a
need. Multiple solution options might be evaluated and, as part of a change
strategy, the best solution approach is justified and selected. The solution scope
defines the boundaries of the solution, and is described in enough detail to
enable stakeholders to understand which new capabilities the change will deliver.
It also describes how the proposed solution enables the future state's goals. The
solution scope might evolve throughout an initiative as more information is
discovered.
The solution scope might be described in different ways, including the use of:
• capabilities,
• technology,
• business rules,
• business decisions,
• data,
• processes,
• resources,
• knowledge and skills,
• models and descriptions of
markets,
• functions,
• locations,
• networks,
• organizational structures,
• workflows,
• events,
• sequence,
• motivations, or
• business logic.
The solution scope can also include descriptions of out-of-scope solution
components to provide clarity.
.2 Gap Analysis
A gap analysis identifies the difference between current state and future state
capabilities. To perform gap analysis, both current state and future state should
be defined. Using the same techniques to describe both current and future states
assists in gap analysis, as it simplifies the comparison.
Gap analysis can help identify the gaps that prevent the enterprise from meeting
needs and achieving goals. It can be used to determine if the enterprise can meet
its needs using its existing structure, resources, capabilities, and technology. If the
enterprise can meet the need with the current state capabilities, then the change
will likely be relatively small, or there may be no change at all. In any other case, a
change strategy is needed to create the missing capabilities or improve the
existing ones. The capabilities analyzed in a gap analysis can include:
• processes,
• functions,
• lines of business,
• organizational structures,
• staff competencies,
• knowledge and skills,
• training,
• facilities,



Define Change Strategy
Strategy Analysis
128
• locations,
• data and information,
• application systems, and
• technology infrastructure.
The gaps will need to be addressed in the transition and future states.
.3 Enterprise Readiness Assessment
Business analysts analyze the enterprise to assess its capacity to make the change
and to sustain the change in the future state. The readiness assessment considers
the enterprise’s capacity not only to make the change, but to use and sustain the
solution, and realize value from the solution. The assessment also factors in the
cultural readiness of the stakeholders and operational readiness in making the
change, the timeline from when the change is implemented to when value can be
realized, and the resources available to support the change effort.
.4 Change Strategy
A change strategy is a high-level plan of key activities and events that will be used
to transform the enterprise from the current state to the future state. Change
strategies may be a singular initiative composed of smaller changes which might
be structured as a set or sequence of projects, or as various continuous
improvement efforts. Each element of change might not completely address the
need, so multiple changes might be necessary.
During the course of the development of a change strategy, several options are
identified, explored, and described in enough detail to determine which options
are feasible. Alternatives can be identified through brainstorming and consulting
subject matter experts (SMEs). Sources of ideas can include historical ideas,
historical changes, other markets' strategies, and competitors' approaches.
A preferred change strategy is selected from this set of options and developed in
more detail. The preferred change strategy should be selected considering:
• organizational readiness to make the change,
• major costs and investments needed to make the change,
• timelines to make the change,
• alignment to the business objectives,
• timelines for value realization, and
• opportunity costs of the change strategy.
Business analysts may develop a business case for each potential change strategy
to support decision making. The opportunity cost of each change strategy also
needs to be considered. Opportunity cost refers to the benefits that could have
been achieved by selecting an alternative change strategy. The options considered
and rejected are an important component of the final strategy, providing
stakeholders with an understanding of the pros and cons of various approaches
to making the change.
When defining the change strategy, the investment to make the change to the
future state is also considered. The net benefits of a future state may be very high,



Strategy Analysis
Define Change Strategy
129
but if the investment is unbearable ("they just can't afford the change") the
enterprise may pass on the opportunity, and invest in something else.
The potential value, including the details of the expected benefit and costs, are
key components to making a business case for the change. Relating descriptions
of potential value to measures of actual value currently being achieved enables
stakeholders to understand the expected change in value. While every change
facilitated by business analysts is intended to increase value, some changes
decrease value in parts of an enterprise while increasing it in others.
.5 Transition States and Release Planning
In many cases, the future state will need to be achieved over time rather than
through a single change, meaning that the enterprise will have to operate in one
or more transition states. Release planning is concerned with determining which
requirements to include in each release, phase, or iteration of the change.
Business analysts help facilitate release planning discussions to help stakeholders
reach decisions. There are many factors that guide these decisions, such as the
overall budget, deadlines or time constraints, resource constraints, training
schedules, and the ability of the business to absorb changes within a defined time
frame. There may be organizational restraints or policies that must be adhered to
in any implementation. Business analysts assist in planning the timing of the
implementation in order to cause minimal disruption to business activities, and to
ensure all parties understand the impact to the organization.
6.4.5
Guidelines and Tools
• Business Analysis Approach: guides how the business analyst defines a
change strategy.
• Design Options: describe various ways to satisfy the business needs. Each
option will come with its own set of change challenges and the change strategy
will be impacted by the option selected as well as the specific change approach
that will be used.
• Solution Recommendations: identifying the possible solutions which can be
pursued in order to achieve the future state, which includes the
recommendations of various subject matter experts (SMEs), helps the business
analyst determine the types of changes to the organization.
6.4.6
Techniques
• Balanced Scorecard: used to define the metrics that will be used to evaluate
the effectiveness of the change strategy.
• Benchmarking and Market Analysis: used to make decisions about which
change strategy is appropriate.
• Brainstorming: used to collaboratively come up with ideas for change
strategies.
• Business Capability Analysis: used to prioritize capability gaps in relation to
value and risk.



Define Change Strategy
Strategy Analysis
130
• Business Cases: used to capture information about the recommended change
strategy and other potential strategies that were assessed but not
recommended.
• Business Model Canvas: used to define the changes needed in the current
infrastructure, customer base, and financial structure of the organization in
order to achieve the potential value.
• Decision Analysis: used to compare different change strategies and choose
which is most appropriate.
• Estimation: used to determine timelines for activities within the change
strategy.
• Financial Analysis: used to understand the potential value associated with a
change strategy, and evaluate strategies against targets set for return on
investments.
• Focus Groups: used to bring customers or end users together to solicit their
input on the solution and change strategy.
• Functional Decomposition: used to break down the components of the
solution into parts when developing a change strategy.
• Interviews: used to talk to stakeholders in order to fully describe the solution
scope and change scope, and to understand their suggestions for a change
strategy.
• Lessons Learned: used to understand what went wrong in past changes in
order to improve this change strategy.
• Mind Mapping: used to develop and explore ideas for change strategies.
• Organizational Modelling: used to describe the roles, responsibilities, and
reporting structures that are necessary during the change and are part of the
solution scope.
• Process Modelling: used to describe how work would occur in the solution
scope or during the change.
• Scope Modelling: used to define the boundaries on the solution scope and
change scope descriptions.
• SWOT Analysis: used to make decisions about which change strategy is
appropriate.
• Vendor Assessment: used to determine whether any vendors are part of the
change strategy, either to implement the change or to be part of the solution.
• Workshops: used in work with stakeholders to collaboratively develop change
strategies.
6.4.7
Stakeholders
• Customer: might be purchasing or consuming the solution that results from
the change. Customers can also be involved in a change as testers or focus



Strategy Analysis
Define Change Strategy
131
group members, whose input is considered in the enterprise readiness
assessment.
• Domain Subject Matter Expert: have expertise in some aspect of the change.
• End User: uses a solution, is a component of the solution, or is a user
temporarily during the change. End users could be customers or people who
work within the enterprise experiencing a change. Users might be involved in a
change as testers or focus group members, whose input is considered in the
enterprise readiness assessment.
• Implementation Subject Matter Expert: have expertise in some aspect of
the change.
• Operational Support: directly involved in supporting the operations of the
enterprise, and provide information on their ability to support the operation of
a solution during and after a change.
• Project Manager: responsible for managing change and planning the detailed
activities to complete a change. In a project, the project manager is responsible
for the project scope, which covers all the work to be performed by the project
team.
• Regulator: ensures adherence to laws, regulations, or rules during and at the
completion of the change. The regulator might have unique input to the
enterprise readiness assessment, as there might be laws and regulations that
must be complied with prior to or as a result of a planned or completed change.
• Sponsor: authorizes and ensures funding for solution delivery, and champions
the change.
• Supplier: might help implement the change or be part of the solution once the
change is completed.
• Tester: responsible for ensuring that the change will function within acceptable
parameters, accomplish the desired result, and deliver solutions that meet an
appropriate level of quality. The tester is often involved in validation of
components of a solution for which the results will be included in an enterprise
readiness assessment.
6.4.8
Outputs
• Change Strategy: the approach that the organization will follow to guide
change.
• Solution Scope: the solution scope that will be achieved through execution of
the change strategy.



Define Change Strategy
Strategy Analysis
132



133
7
Requirements Analysis and Design
Definition
The Requirements Analysis and Design Definition knowledge area describes the
tasks that business analysts perform to structure and organize requirements
discovered during elicitation activities, specify and model requirements and
designs, validate and verify information, identify solution options that meet
business needs, and estimate the potential value that could be realized for each
solution option. This knowledge area covers the incremental and iterative
activities ranging from the initial concept and exploration of the need through the
transformation of those needs into a particular recommended solution.
For more
information, see
Requirements and
Designs (p. 19).
Both requirements and designs are important tools used by business analysts to
define and guide change. The main difference between requirements and designs
is in how they are used and by whom. One person’s designs may be another
person’s requirements. Requirements and designs may be either high-level or very
detailed based upon what is appropriate to those consuming the information.
The business analyst's role in modelling needs, requirements, designs, and
solutions is instrumental in conducting thorough analysis and communicating
with other stakeholders. The form, level of detail, and what is being modelled are
all dependent on the context, audience, and purpose.
Business analysts analyze the potential value of both requirements and designs. In
collaboration with implementation subject matter experts, business analysts
define solution options that can be evaluated in order to recommend the best
solution option that meets the need and brings the most value.
The following image illustrates the spectrum of value as business analysis
activities progress from delivering potential value to actual value.



Requirements Analysis and Design Definition
134
Figure 7.0.1: Business Analysis Value Spectrum
The Requirements Analysis and Design Definition knowledge area includes the
following tasks:
• Specify and Model Requirements: describes a set of requirements or
designs in detail using analytical techniques.
• Verify Requirements: ensures that a set of requirements or designs has
been developed in enough detail to be usable by a particular stakeholder, is
internally consistent, and is of high quality.
• Validate Requirements: ensures that a set of requirements or designs
delivers business value and supports the organization's goals and
objectives.
• Define Requirements Architecture: structures all requirements and
designs so that they support the overall business purpose for a change and
that they work effectively as a cohesive whole.
• Define Solution Options: identifies, explores and describes different
possible ways of meeting the need.
• Analyze Potential Value and Recommend Solution: assesses the
business value associated with a potential solution and compares different
options, including trade-offs, to identify and recommend the solution
option that delivers the greatest overall value.
The Core Concept Model in Requirements Analysis
and Design Definition
The Business Analysis Core Concept Model™ (BACCM™) describes the
relationships among the six core concepts. The following table describes the
usage and application of each of the core concepts within the context of
Requirements Analysis and Design Definition.
Solution Evaluation
Potential
Requirements Analysis
& Design Definition
Strategy Analysis
Need
Solution
Scope
Requirements
Design
Proof of Concept/
Prototype
Pilot/Beta
Operating
Actual



Requirements Analysis and Design Definition
135
Table 7.0.1: The Core Concept Model in Requirements Analysis and Design
Definition
Core Concept
During Requirements Analysis and Design
Definition, business analysts...
Change: the act of transformation
in response to a need.
transform elicitation results into
requirements and designs in order to
define the change.
Need: a problem or opportunity to
be addressed.
analyze the needs in order to recommend
a solution that meets the needs.
Solution: a specific way of
satisfying one or more needs
within a context.
define solution options and recommend
the one that is most likely to address the
need and has the most value.
Stakeholder: a group or
individual with a relationship to
the change, the need, or the
solution.
tailor the requirements and designs so
that they are understandable and usable
by each stakeholder group.
Value: the worth, importance, or
usefulness of something to a
stakeholder within a context.
analyze and quantify the potential value
of the solution options.
Context: the circumstances that
influence, are influenced by, and
provide understanding of the
change.
model and describe the context in formats
that are understandable and usable by all
stakeholders.



Specify and Model Requirements
Requirements Analysis and Design Definition
136
Figure 7.0.2: Requirements Analysis and Design Definition Input/Output Diagram
7.1
Specify and Model Requirements
7.1.1
Purpose
The purpose of Specify and Model Requirements is to analyze, synthesize, and
refine elicitation results into requirements and designs.
7.1.2
Description
Specify and Model Requirements describes the practices for analyzing elicitation
Tasks
Output
7.3
Validate
Requirements
7.2
Verify
Requirements
7.1
Specify and Model
Requirements
7.4
Define
Requirements
Architecture
7.5
Define Design
Options
Requirements
(any state)
3.4
Information
Management
Approach
4.2, 4.3
Elicitation Results
(any state)
6.4
Change Strategy
6.4
Solution Scope
6.2
Potential Value
7.1
Requirements
(specified and
modelled)
7.2
Requirements
(verified)
7.3
Requirements
(validated)
7.5
Design Options
7.4
Requirements
Architecture
7.6
Analyze Potential
Value and
Recommend
Solution
7.6
Solution
Recommendation
Input



Requirements Analysis and Design Definition
Specify and Model Requirements
137
results and creating representations of those results. When the focus of the
specifying and modelling activity is on understanding the need, the outputs are
referred to as requirements. When the focus of the specifying and modelling
activity is on a solution, the outputs are referred to as designs.
Important
In many IT environments, the word 'design' is used specifically for technical
designs created by software developers, data architects, and other
implementation subject matter experts. All business deliverables are referred to as
'requirements'.
In addition to the models used to represent the requirements, this task also
includes capturing information about attributes or metadata about the
requirements. The specifying and modelling activities relate to all requirement
types.
7.1.3
Inputs
• Elicitation Results (any state): modelling can begin with any elicitation result
and may lead to the need for more elicitation to clarify or expand upon
requirements. Elicitation and modelling may occur sequentially, iteratively, or
concurrently.
Figure 7.1.1: Specify and Model Requirements Input/Output Diagram
Tasks Using This Output
Output
Modelling Notations/
Standards
7.1
Requirements
(specified and
modelled)
7.2
Verify
Requirements
4.2, 4.3
Elicitation Results
(any state)
Modelling Tools
Requirements Architecture
Requirements Life Cycle
Management Tools
Solution Scope
7.3
Validate
Requirements
Guidelines and Tools
7.1
Specify and Model
Requirements
Input



Specify and Model Requirements
Requirements Analysis and Design Definition
138
7.1.4
Elements
.1 Model Requirements
A model is a descriptive and visual way to convey information to a specific
audience in order to support analysis, communication, and understanding.
Models may also be used to confirm knowledge, identify information gaps that
the business analyst may have, and identify duplicate information.
Business analysts choose from one or more of the following modelling formats:
• Matrices: a matrix is used when the business analyst is modelling a
requirement or set of requirements that have a complex but uniform
structure, which can be broken down into elements that apply to every
entry in the table. Matrices may be used for data dictionaries, requirements
traceability, or for gap analysis. Matrices are also used for prioritizing
requirements and recording other requirements attributes and metadata.
• Diagrams: a diagram is a visual, often pictorial, representation of a
requirement or set of requirements. A diagram is especially useful to depict
complexity in a way that would be difficult to do with words. Diagrams can
also be used to define boundaries for business domains, to categorize and
create hierarchies of items, and to show components of objects such as
data and their relationships.
Using one or more of the model formats, business analysts determine specific
categories and specific models within categories to be used. Model categories can
include:
• People and Roles: models represent organizations, groups of people,
roles, and their relationships within an enterprise and to a solution.
Techniques used to represent people and their roles include Organizational
Modelling, Roles and Permissions Matrix and Stakeholder List, Map, or
Personas.
• Rationale: models represent the ‘why’ of a change. Techniques used to
represent the rationale include Decision Modelling, Scope Modelling,
Business Model Canvas, Root Cause Analysis, and Business Rules Analysis.
• Activity Flow: models represent a sequence of actions, events, or a course
that may be taken. Techniques used to represent activity flows include
Process Modelling, Use Cases and Scenarios, and User Stories.
• Capability: models focus on features or functions of an enterprise or a
solution. Techniques used to represent capabilities include Business
Capability Analysis, Functional Decomposition, and Prototyping.
• Data and Information: models represent the characteristics and the
exchange of information within an enterprise or a solution. Techniques used
to represent data and information include Data Dictionary, Data Flow
Diagrams, Data Modelling, Glossary, State Modelling, and Interface
Analysis.



Requirements Analysis and Design Definition
Specify and Model Requirements
139
Business analysts should use any combination of models best suited to meet
stakeholder needs in a given context. Each modelling technique has strengths
and weaknesses and provides unique insights into the business domain.
.2 Analyze Requirements
Business analysis information is decomposed into components to further examine
for:
• anything that must change to meet the business need,
• anything that should stay the same to meet the business need,
• missing components,
• unnecessary components, and
• any constraints or assumptions that impact the components.
The level of decomposition required, and the level of detail to be specified, varies
depending on the knowledge and understanding of the stakeholders, the
potential for misunderstanding or miscommunication, organizational standards,
and contractual or regulatory obligations, among other factors.
Analysis provides a basis for discussion to reach a conclusion about solution
options.
.3 Represent Requirements and Attributes
Business analysts identify information for requirements and their attributes as part
of the elicitation results. Requirements should be explicitly represented and
should include enough detail such that they exhibit the characteristics of
requirements and designs quality (see Verify Requirements (p. 141)). Various
attributes can be specified for each requirement or set of requirements. These
attributes are selected when planning for information management (see Plan
Business Analysis Information Management (p. 42)).
As part of specifying requirements, they can also be categorized according to the
schema described in task Requirements Classification Schema (p. 16). Typically
elicitation results contain information of different types, so it is natural to expect
that different types of requirements might be specified at the same time.
Categorizing requirements can help ensure the requirements are fully
understood, a set of any type is complete, and that there is appropriate
traceability between the types.
.4 Implement the Appropriate Levels of Abstraction
The level of abstraction of a requirement varies based on the type of requirement
and audience for the requirement. Not all stakeholders require or find value in the
complete set of requirements and models. It may be appropriate to produce
different viewpoints of requirements to represent the same need for different
stakeholders. Business analysts take special care to maintain the meaning and
intent of the requirements over all representations.
The business analysis approach may also influence the level of abstraction and
choice of models used when defining requirements.



Specify and Model Requirements
Requirements Analysis and Design Definition
140
7.1.5
Guidelines and Tools
• Modelling Notations/Standards: allow requirements and designs to be
precisely specified, as is appropriate for the audience and the purpose of the
models. Standard templates and syntax help to ensure that the right
information is provided about the requirements.
• Modelling Tools: software products that facilitate drawing and storing
matrices and diagrams to represent requirements. This functionality may or may
not be part of requirements life cycle management tools.
• Requirements Architecture: the requirements and interrelationships among
them can be used to ensure models are complete and consistent.
• Requirements Life Cycle Management Tools: software products that
facilitate recording, organizing, storing, and sharing requirements and designs.
• Solution Scope: the boundaries of the solution provide the boundaries for the
requirements and designs models.
7.1.6
Techniques
• Acceptance and Evaluation Criteria: used to represent the acceptance and
evaluation criteria attributes of requirements.
• Business Capability Analysis: used to represent features or functions of an
enterprise.
• Business Model Canvas: used to describe the rationale for requirements.
• Business Rules Analysis: used to analyze business rules so that they can be
specified and modelled alongside requirements.
• Concept Modelling: used to define terms and relationships relevant to the
change and the enterprise.
• Data Dictionary: used to record details about the data involved in the change.
Details may include definitions, relationships with other data, origin, format,
and usage.
• Data Flow Diagrams: used to visualize data flow requirements.
• Data Modelling: used to model requirements to show how data will be used
to meet stakeholder information needs.
• Decision Modelling: used to represent decisions in a model in order to show
the elements of decision making required.
• Functional Decomposition: used to model requirements in order to identify
constituent parts of an overall complex business function.
• Glossary: used to record the meaning of relevant business terms while
analyzing requirements.
• Interface Analysis: used to model requirements in order to identify and
validate inputs and outputs of the solution they are modelling.
• Non-Functional Requirements Analysis: used to define and analyze the
quality of service attributes.



Requirements Analysis and Design Definition
Verify Requirements
141
• Organizational Modelling: used to allow business analysts to model the
roles, responsibilities, and communications within an organization.
• Process Modelling: used to show the steps or activities that are performed in
the organization, or that must be performed to meet the desired change.
• Prototyping: used to assist the stakeholders in visualizing the appearance and
capabilities of a planned solution.
• Roles and Permissions Matrix: used to specify and model requirements
concerned with the separation of duties among users and external interfaces in
utilizing a solution.
• Root Cause Analysis: used to model the root causes of a problem as part of
rationale.
• Scope Modelling: used to visually show a scope boundary.
• Sequence Diagrams: used to specify and model requirements to show how
processes operate and interact with one another, and in what order.
• Stakeholder List, Map, or Personas: used to identify the stakeholders and
their characteristics.
• State Modelling: used to specify the different states of a part of the solution
throughout a life cycle, in terms of the events that occur.
• Use Cases and Scenarios: used to model the desired behaviour of a solution,
by showing user interactions with the solution, to achieve a specific goal or
accomplish a particular task.
• User Stories: used to specify requirements as a brief statement about what
people do or need to do when using the solution.
7.1.7
Stakeholders
• Any stakeholder: business analysts may choose to perform this task
themselves and then separately package and communicate the requirements to
stakeholders for their review and approval, or they might choose to invite some
or all stakeholders to participate in this task.
7.1.8
Outputs
• Requirements (specified and modelled): any combination of requirements
and/or designs in the form of text, matrices, and diagrams.
7.2
Verify Requirements
7.2.1
Purpose
The purpose of Verify Requirements is to ensure that requirements and designs
specifications and models meet quality standards and are usable for the purpose
they serve.



Verify Requirements
Requirements Analysis and Design Definition
142
7.2.2
Description
Verifying requirements ensures that the requirements and designs have been
defined correctly. Requirements verification constitutes a check by the business
analyst and key stakeholders to determine that the requirements and designs are
ready for validation, and provides the information needed for further work to be
performed.
A high-quality specification is well written and easily understood by its intended
audience. A high-quality model follows the formal or informal notation standards
and effectively represents reality.
The most important characteristic of quality requirements and designs is fitness
for use. They must meet the needs of stakeholders who will use them for a
particular purpose. Quality is ultimately determined by stakeholders.
7.2.3
Inputs
• Requirements (specified and modelled): any requirement, design, or set of
those may be verified to ensure that text is well structured and that matrices
and modelling notation are used correctly.
Figure 7.2.1: Verify Requirements Input/Output Diagram
Input
Tasks Using This Output
Output
7.2
Requirements
(verified)
5.5
Approve
Requirements
7.1
Requirements
(specified and
modelled)
Requirements Life Cycle
Management Tools
Guidelines and Tools
7.2
Verify Requirements



Requirements Analysis and Design Definition
Verify Requirements
143
7.2.4
Elements
.1 Characteristics of Requirements and Designs Quality
While quality is ultimately determined by the needs of the stakeholders who will
use the requirements or the designs, acceptable quality requirements exhibit
many of the following characteristics:
• Atomic: self-contained and capable of being understood independently of
other requirements or designs.
• Complete: enough to guide further work and at the appropriate level of
detail for work to continue. The level of completeness required differs
based on perspective or methodology, as well as the point in the life cycle
where the requirement is being examined or represented.
• Consistent: aligned with the identified needs of the stakeholders and not
conflicting with other requirements.
• Concise: contains no extraneous and unnecessary content.
• Feasible: reasonable and possible within the agreed-upon risk, schedule,
and budget, or considered feasible enough to investigate further through
experiments or prototypes.
• Unambiguous: the requirement must be clearly stated in such a way to
make it clear whether a solution does or does not meet the associated
need.
• Testable: able to verify that the requirement or design has been fulfilled.
Acceptable levels of verifying fulfillment depend on the level of abstraction
of the requirement or design.
• Prioritized: ranked, grouped, or negotiated in terms of importance and
value against all other requirements.
• Understandable: represented using common terminology of the audience.
.2 Verification Activities
Verification activities are typically performed iteratively throughout the
requirements analysis process.
Verification activities include:
• checking for compliance with organizational performance standards for
business analysis, such as using the right tools and methods,
• checking for correct use of modelling notation, templates, or forms,
• checking for completeness within each model,
• comparing each model against other relevant models, checking for
elements that are mentioned in one model but are missing in other models,
and verifying that the elements are referenced consistently,
• ensuring the terminology used in expressing the requirement is
understandable to stakeholders and consistent with the use of those terms
within the organization, and



Validate Requirements
Requirements Analysis and Design Definition
144
• adding examples where appropriate for clarification.
.3 Checklists
Checklists are used for quality control when verifying requirements and designs.
Checklists may include a standard set of quality elements that business analysts
use to verify the requirements, or they may be specifically developed to capture
issues of concern. The purpose of a checklist is to ensure that items determined to
be important are included in the final requirements deliverables, or that steps
required for the verification process are followed.
7.2.5
Guidelines and Tools
• Requirements Life Cycle Management Tools: some tools have functionality
to check for issues related to many of the characteristics, such as atomic,
unambiguous, and prioritized.
7.2.6
Techniques
• Acceptance and Evaluation Criteria: used to ensure that requirements are
stated clearly enough to devise a set of tests that can prove that the
requirements have been met.
• Item Tracking: used to ensure that any problems or issues identified during
verification are managed and resolved.
• Metrics and Key Performance Indicators (KPIs): used to identify how to
evaluate the quality of the requirements.
• Reviews: used to inspect requirements documentation to identify requirements
that are not of acceptable quality.
7.2.7
Stakeholders
• All stakeholders: the business analyst, in conjunction with the domain and
implementation subject matter experts, has the primary responsibility for
determining that this task has been completed. Other stakeholders may
discover problematic requirements during requirements communication.
Therefore, all stakeholders could be involved in this task.
7.2.8
Outputs
• Requirements (verified): a set of requirements or designs that is of sufficient
quality to be used as a basis for further work.
7.3
Validate Requirements
7.3.1
Purpose
The purpose of Validate Requirements is to ensure that all requirements and



Requirements Analysis and Design Definition
Validate Requirements
145
designs align to the business requirements and support the delivery of needed
value.
7.3.2
Description
Requirements validation is an ongoing process to ensure that stakeholder,
solution, and transition requirements align to the business requirements and that
the designs satisfy the requirements.
Understanding what the desired future state looks like for stakeholders after their
needs have been met is valuable to business analysts when validating
requirements. The overall goal of implementing the requirements is to achieve the
stakeholders' desired future state. In many cases, stakeholders have different,
conflicting needs and expectations that may be exposed through the validation
process.
7.3.3
Inputs
• Requirements (specified and modelled): any types of requirements and
designs can be validated. Validation activities may begin before requirements
are completely verified. However, validation activities cannot be completed
before requirements are completely verified.
Figure 7.3.1: Validate Requirements Input/Output Diagram
Input
Tasks Using This Output
Output
7.3
Validate Requirements
Business Objectives
7.3
Requirements
(validated)
7.5
Define Design
Options
7.1
Requirements
(specified and
modelled)
Future State Description
Potential Value
Solution Scope
8.1
Measure Solution
Performance
Guidelines and Tools



Validate Requirements
Requirements Analysis and Design Definition
146
7.3.4
Elements
.1 Identify Assumptions
If an organization is launching an unprecedented product or service, it may be
necessary to make assumptions about customer or stakeholder response, as there
are no similar previous experiences on which to rely. In other cases, it may be
difficult or impossible to prove that a particular problem derives from an identified
root cause. Stakeholders may have assumed that certain benefits will result from
the implementation of a requirement. These assumptions are identified and
defined so that associated risks can be managed.
.2 Define Measurable Evaluation Criteria
While the expected benefits are defined as part of the future state, the specific
measurement criteria and evaluation process may not have been included.
Business analysts define the evaluation criteria that will be used to evaluate how
successful the change has been after the solution is implemented. Baseline
metrics might be established based on the current state. Target metrics can be
developed to reflect the achievement of the business objectives or some other
measurement of success.
.3 Evaluate Alignment with Solution Scope
A requirement can be of benefit to a stakeholder and still not be a desirable part
of a solution. A requirement that does not deliver benefit to a stakeholder is a
strong candidate for elimination. When requirements do not align, either the
future state must be re-evaluated and the solution scope changed, or the
requirement removed from the solution scope.
If a design cannot be validated to support a requirement, there might be a
missing or misunderstood requirement, or the design must change.
7.3.5
Guidelines and Tools
• Business Objectives: ensure the requirements deliver the desired business
benefits.
• Future State Description: helps to ensure the requirements that are part of
the solution scope do help achieve the desired future state.
• Potential Value: can be used as a benchmark against which the value
delivered by requirements can be assessed.
• Solution Scope: ensures the requirements that provide benefit are within the
scope of the desired solution.
7.3.6
Techniques
• Acceptance and Evaluation Criteria: used to define the quality metrics that
must be met to achieve acceptance by a stakeholder.



Requirements Analysis and Design Definition
Validate Requirements
147
• Document Analysis: used to identify previously documented business needs in
order to validate requirements.
• Financial Analysis: used to define the financial benefits associated with
requirements.
• Item Tracking: used to ensure that any problems or issues identified during
validation are managed and resolved.
• Metrics and Key Performance Indicators (KPIs): used to select appropriate
performance measures for a solution, solution component, or requirement.
• Reviews: used to confirm whether or not the stakeholder agrees that their
needs are met.
• Risk Analysis and Management: used to identify possible scenarios that
would alter the benefit delivered by a requirement.
7.3.7
Stakeholders
• All stakeholders: the business analyst, in conjunction with the customer, end
users, and sponsors, has the primary responsibility for determining whether or
not requirements are validated. Other stakeholders may discover problematic
requirements during requirements communication. Therefore, virtually all
project stakeholders are involved in this task.
7.3.8
Outputs
• Requirements (validated): validated requirements and designs are those that
can be demonstrated to deliver benefit to stakeholders and align with the
business goals and objectives of the change. If a requirement or design cannot
be validated, it either does not benefit the organization, does not fall within the
solution scope, or both.



Define Requirements Architecture
Requirements Analysis and Design Definition
148
7.4
Define Requirements Architecture
7.4.1
Purpose
The purpose of Define Requirements Architecture is to ensure that the
requirements collectively support one another to fully achieve the objectives.
7.4.2
Description
Requirements architecture is the structure of all of the requirements of a change.
A requirements architecture fits the individual models and specifications together
to ensure that all of the requirements form a single whole that supports the
overall business objectives and produces a useful outcome for stakeholders.
Business analysts use a requirements architecture to:
• understand which models are appropriate for the domain, solution scope,
and audience,
• organize requirements into structures relevant to different stakeholders,
• illustrate how requirements and models interact with and relate to each
other, and show how the parts fit together into a meaningful whole,
• ensure the requirements work together to achieve the overall objectives,
and
• make trade-off decisions about requirements while considering the overall
objectives.
Requirements architecture is not intended to demonstrate traceability, but rather
to show how elements work in harmony with one another to support the
business requirements, and to structure them in various ways to align the
viewpoints of different stakeholders. Traceability is often used as the mechanism
to represent and manage these relationships (see Trace Requirements (p. 79)).
Traceability proves that every requirement links back to an objective and shows
how an objective was met. Traceability does not prove the solution is a cohesive
whole that will work.
7.4.3
Inputs
• Information Management Approach: defines how the business analysis
information (including requirements and models) will be stored and accessed.
• Requirements (any state): every requirement should be stated once, and only
once, and incorporated into the requirements architecture so that the entire set
may be evaluated for completeness.
• Solution Scope: must be considered to ensure the requirements architecture is
aligned with the boundaries of the desired solution.



Requirements Analysis and Design Definition
Define Requirements Architecture
149
Figure 7.4.1: Define Requirements Architecture Input/Output Diagram
7.4.4
Elements
.1 Requirements Viewpoints and Views
A viewpoint is a set of conventions that define how requirements will be
represented, how these representations will be organized, and how they will be
related. Viewpoints provide templates for addressing the concerns of particular
stakeholder groups.
Requirements viewpoints frequently include standards and guidelines for the:
• model types used for requirements,
• attributes that are included and consistently used in different models,
• model notations that are used, and
• analytical approaches used to identify and maintain relevant relationships
among models.
Tasks Using This Output
Output
7.4
Define Requirements
Architecture
Architecture Management
Software
7.4
Requirements
Architecture
5.3
Prioritize
Requirements
3.4
Information
Management
Approach
Requirements
(any state)
Legal/Regulatory
Information
Methodologies and
Framework
5.4
Assess
Requirements
Changes
7.1
Specify and Model
Requirements
7.5
Define Design
Options
6.4
Solution Scope
Input
Guidelines and Tools



Define Requirements Architecture
Requirements Analysis and Design Definition
150
No single viewpoint alone can form an entire architecture. Each viewpoint is
stronger for some aspects of the requirements, and weaker for others, as
different groups of stakeholders have different concerns. Trying to put too much
information into any one viewpoint will make it too complex and degrade its
purpose. Examples of viewpoints include:
• Business process models,
• Data models and information,
• User interactions, including use cases and/or user experience,
• Audit and security, and
• Business models.
Each of those viewpoints has different model notations and techniques, and each
is important to ensure a cohesive final solution. The solution would likely not be a
success if the business analyst only looked at the business process viewpoint.
Similarly, trying to put conventions from many viewpoints in one single viewpoint
would make it overwhelming to analyze and contain information irrelevant to
particular stakeholder groups.
The actual requirements and designs for a particular solution from a chosen
viewpoint are referred to as a view. A collection of views makes up the
requirements architecture for a specific solution. Business analysts align,
coordinate, and structure requirements into meaningful views for the various
stakeholders. This set of coordinated, complementary views provides a basis for
assessing the completeness and coherence of the requirements.
In short, the viewpoints tell business analysts what information they should
provide for each stakeholder group to address their concerns, while views
describe the actual requirements and designs that are produced.
.2 Template Architectures
An architectural framework is a collection of viewpoints that is standard across an
industry, sector, or organization. Business analysts can treat frameworks as
predefined templates to start from in defining their architecture. Similarly, the
framework can be populated with domain-specific information to form a
collection of views that is an even more useful template to build architecture from
if it is accurate because the information is already populated in it.
.3 Completeness
An architecture helps ensure that a set of requirements is complete. The entire set
of requirements should be able to be understood by the audience in way that it
can be determined that the set is cohesive and tells a full story. No requirements
should be missing from the set, inconsistent with others, or contradictory to one
another. The requirements architecture should take into account any
dependencies between requirements that could keep the objectives from being
achieved.
Structuring requirements according to different viewpoints helps ensure this



Requirements Analysis and Design Definition
Define Requirements Architecture
151
completeness. Iterations of elicitation, specification, and analysis activities can
help identify gaps.
.4 Relate and Verify Requirements Relationships
Requirements may be related to each other in several ways when defining the
requirements architecture. Business analysts examine and analyze the
requirements to define the relationships between them. The representation of
these relationships is provided by tracing requirements (see Trace Requirements
(p. 79)).
Business analysts examine each relationship to ensure that the relationships
satisfy the following quality criteria:
• Defined: there is a relationship and the type of the relationship is
described.
• Necessary: the relationship is necessary for understanding the
requirements holistically.
• Correct: the elements do have the relationship described.
• Unambiguous: there are no relationships that link elements in two
different and conflicting ways.
• Consistent: relationships are described in the same way, using the same set
of standard descriptions as defined in the viewpoints.
.5 Business Analysis Information Architecture
The structure of the business analysis information is also an information
architecture. This type of architecture is defined as part of the task Plan Business
Analysis Information Management (p. 42). The information architecture is a
component of the requirements architecture because it describes how all of the
business analysis information for a change relates. It defines relationships for
types of information such as requirements, designs, types of models, and
elicitation results. Understanding this type of information structure helps to
ensure that the full set of requirements is complete by verifying the relationships
are complete. It is useful to start defining this architecture before setting up
infrastructure such as requirements life cycle management tools, architecture
management software, or document repositories.
7.4.5
Guidelines and Tools
• Architecture Management Software: modelling software can help to
manage the volume, complexity, and versions of the relationships within the
requirements architecture.
• Legal/Regulatory Information: describes legislative rules or regulations that
must be followed. They may impact the requirements architecture or its
outputs. Additionally, contractual or standards-based constraints may also need
to be considered.



Define Design Options
Requirements Analysis and Design Definition
152
• Methodologies and Frameworks: a predetermined set of models, and
relationships between the models, to be used to represent different viewpoints.
7.4.6
Techniques
• Data Modelling: used to describe the requirements structure as it relates to
data.
• Functional Decomposition: used to break down an organizational unit,
product scope, or other elements into its component parts.
• Interviews: used to define the requirements structure collaboratively.
• Organizational Modelling: used to understand the various organizational
units, stakeholders, and their relationships which might help define relevant
viewpoints.
• Scope Modelling: used to identify the elements and boundaries of the
requirements architecture.
• Workshops: used to define the requirements structure collaboratively.
7.4.7
Stakeholders
• Domain Subject Matter Expert, Implementation Subject Matter Expert,
Project Manager, Sponsor, Tester: may assist in defining and confirming the
requirements architecture.
• Any stakeholder: may also use the requirements architecture to assess the
completeness of the requirements.
7.4.8
Outputs
• Requirements Architecture: the requirements and the interrelationships
among them, as well as any contextual information that is recorded.
7.5
Define Design Options
7.5.1
Purpose
The purpose of Define Design Options is to define the solution approach, identify
opportunities to improve the business, allocate requirements across solution
components, and represent design options that achieve the desired future state.
7.5.2
Description
When designing a solution, there may be one or more design options identified.
Each design option represents a way to satisfy a set of requirements. Design
options exist at a lower level than the change strategy, and are tactical rather than
strategic. As a solution is developed, tactical trade-offs may need to be made



Requirements Analysis and Design Definition
Define Design Options
153
among design alternatives. Business analysts must assess the effect these trade-
offs will have on the delivery of value to stakeholders. As initiatives progress and
requirements evolve, design options evolve as well.
7.5.3
Inputs
• Change Strategy: describes the approach that will be followed to transition to
the future state. This may have some impact on design decisions in terms of
what is feasible or possible.
• Requirements (validated, prioritized): only validated requirements are
considered in design options. Knowing the requirement priorities aids in the
suggestion of reasonable design options. Requirements with the highest
priorities might deserve more weight in choosing solution components to best
meet them as compared to lower priority requirements.
• Requirements Architecture: the full set of requirements and their
relationships is important for defining design options that can address the
holistic set of requirements.
Figure 7.5.1: Define Design Options Input/Output Diagram
Tasks Using This Output
Output
7.5
Define Design Options
Existing Solutions
7.5
Design Options
6.4
Define Change
Strategy
6.4
Change Strategy
5.3, 7.3
Requirements
(validated,
prioritized)
Future State Description
Requirements (traced)
7.6
Analyze Potential
Value and
Recommend
Solution
7.4
Requirements
Architecture
Solution Scope
Input
Guidelines and Tools



Define Design Options
Requirements Analysis and Design Definition
154
7.5.4
Elements
.1 Define Solution Approaches
The solution approach describes whether solution components will be created or
purchased, or some combination of both. Business analysts assess the merits of
the solution approaches for each design option.
Solution approaches include:
• Create: solution components are assembled, constructed, or developed by
experts as a direct response to a set of requirements. The requirements and
the design options have enough detail to make a decision about which
solution to construct. This option includes modifying an existing solution.
• Purchase: solution components are selected from a set of offerings that
fulfill the requirements. The requirements and design options have enough
detail to make a recommendation about which solution to purchase. These
offerings are usually products or services owned and maintained by third
parties.
• Combination of both: not all design options will fall strictly into one of
the categories above. Design options may include a combination of both
creation and purchase of components.
In all of these types of approaches, proposed integration of the components is
also considered within the design option.
.2 Identify Improvement Opportunities
When proposing design options, a number of opportunities to improve the
operation of the business may occur and are compared.
Some common examples of opportunities include:
• Increase Efficiencies: automate or simplify the work people perform by re-
engineering or sharing processes, changing responsibilities, or outsourcing.
Automation may also increase consistency of behaviour, reducing the
likelihood of different stakeholders performing the same function in
distinctly different fashions.
• Improve Access to Information: provide greater amounts of information
to staff who interface directly or indirectly with customers, thereby reducing
the need for specialists.
• Identify Additional Capabilities: highlight capabilities that have the
potential to provide future value and can be supported by the solution.
These capabilities may not necessarily be of immediate value to the
organization (for example, a software application with features the
organization anticipates using in the future).
.3 Requirements Allocation
Requirements allocation is the process of assigning requirements to solution
components and releases to best achieve the objectives. Allocation is supported



Requirements Analysis and Design Definition
Define Design Options
155
by assessing the trade-offs between alternatives in order to maximize benefits
and minimize costs. The value of a solution might vary depending on how
requirements are implemented and when the solution becomes available to
stakeholders. The objective of allocation is to maximize that value.
Requirements may be allocated between organizational units, job functions,
solution components, or releases of a solution. Requirements allocation typically
begins when a solution approach has been determined, and continues until all
valid requirements are allocated. Allocation typically continues through design
and implementation of a solution.
.4 Describe Design Options
Design options are investigated and developed while considering the desired
future state, and in order to ensure the design option is valid. Solution
performance measures are defined for each design option.
A design option usually consists of many design components, each described by a
design element. Design elements may describe:
• business policies and business rules,
• business processes to be performed and managed,
• people who operate and maintain the solution, including their job functions
and responsibilities,
• operational business decisions to be made,
• software applications and application components used in the solution, and
• organizational structures, including interactions between the organization,
its customers, and its suppliers.
7.5.5
Guidelines and Tools
• Existing Solutions: existing products or services, often third party, that are
considered as a component of a design option.
• Future State Description: identifies the desired state of the enterprise that
the design options will be part of, and helps to ensure design options are viable.
• Requirements (traced): define the design options that best fulfill known
requirements.
• Solution Scope: defines the boundaries when selecting viable design options.
7.5.6
Techniques
• Benchmarking and Market Analysis: used to identify and analyze existing
solutions and market trends.
• Brainstorming: used to help identify improvement opportunities and design
options.
• Document Analysis: used to provide information needed to describe design
options and design elements.



Define Design Options
Requirements Analysis and Design Definition
156
• Interviews: used to help identify improvement opportunities and design
options.
• Lessons Learned: used to help identify improvement opportunities.
• Mind Mapping: used to identify and explore possible design options.
• Root Cause Analysis: used to understand the underlying cause of the
problems being addressed in the change to propose solutions to address them.
• Survey or Questionnaire: used to help identify improvement opportunities
and design options.
• Vendor Assessment: used to couple the assessment of a third party solution
with an assessment of the vendor to ensure that the solution is viable and all
parties will be able to develop and maintain a healthy working relationship.
• Workshops: used to help identify improvement opportunities and design
options.
7.5.7
Stakeholders
• Domain Subject Matter Expert: provides the expertise within the business to
provide input and feedback when evaluating solution alternatives, particularly
for the potential benefits of a solution.
• Implementation Subject Matter Expert: use their expertise in terms of the
design options being considered to provide needed input about the constraints
of a solution and its costs.
• Operational Support: can help evaluate the difficulty and costs of integrating
proposed solutions with existing processes and systems.
• Project Manager: plans and manages the solution definition process,
including the solution scope and any risks associated with the proposed
solutions.
• Supplier: provides information on the functionality associated with a particular
design option.
7.5.8
Outputs
• Design Options: describe various ways to satisfy one or more needs in a
context. They may include solution approach, potential improvement
opportunities provided by the option, and the components that define the
option.



Requirements Analysis and Design Definition
Analyze Potential Value and Recommend Solution
157
7.6
Analyze Potential Value and Recommend Solution
7.6.1
Purpose
The purpose of Analyze Potential Value and Recommend Solution is to estimate
the potential value for each design option and to establish which one is most
appropriate to meet the enterprise’s requirements.
7.6.2
Description
Analyze Potential Value and Recommend Solution describes how to estimate and
model the potential value delivered by a set of requirements, designs, or design
options. Potential value is analyzed many times over the course of a change. This
analysis may be a planned event, or it may be triggered by a modification to the
context or scope of the change. The analysis of potential value includes
consideration that there is uncertainty in the estimates. Value can be described in
terms of finance, reputation, or even impact on the marketplace. Any change
may include a mix of increases and decreases in value.
Design options are evaluated by comparing the potential value of each option to
the other options. Each option has a mix of advantages and disadvantages to
consider. Depending on the reasons for the change, there may be no best option
to recommend, or there may be a clear best choice. In some cases this means the
best option may be to begin work against more than one design option, perhaps
to develop proofs of concept, and then measure the performance of each. In
other instances, all proposed designs may be rejected and more analysis may be
needed to define a suitable design. It is also possible that the best
recommendation is to do nothing.
7.6.3
Inputs
• Potential Value: can be used as a benchmark against which the value
delivered by a design can be evaluated.
• Design Options: need to be evaluated and compared to one another to
recommend one option for the solution.



Analyze Potential Value and Recommend Solution
Requirements Analysis and Design Definition
158
Figure 7.6.1: Analyze Potential Value and Recommend Solution Input/Output
Diagram
7.6.4
Elements
.1 Expected Benefits
Expected benefits describe the positive value that a solution is intended to deliver
to stakeholders. Value can include benefits, reduced risk, compliance with
business policies and regulations, an improved user experience, or any other
positive outcome. Benefits are determined based on the analysis of the benefit
that stakeholders desire and the benefit that is possible to attain. Expected
benefits can be calculated at the level of a requirement or set of requirements by
considering how much of an overall business objective the set of requirements
contribute to if fulfilled. The total expected benefit is the net benefit of all the
requirements a particular design option addresses. Benefits are often realized over
a period of time.
Input
Tasks Using This Output
Output
7.6
Analyze Potential Value and
Recommend Solution
Business Objectives
7.6
Solution
Recommendation
6.4
Define Change
Strategy
6.2
Potential Value
Current State Description
Future State Description
Risk Analysis Results
Solution Scope
7.5
Design Options
Guidelines and Tools



Requirements Analysis and Design Definition
Analyze Potential Value and Recommend Solution
159
.2 Expected Costs
Expected costs include any potential negative value associated with a solution,
including the cost to acquire the solution, any negative effects it may have on
stakeholders, and the cost to maintain it over time.
Expected costs can include:
• timeline,
• effort,
• operating costs,
• purchase and/or implementation
costs,
• maintenance costs,
• physical resources,
• information resources, and
• human resources.
Expected costs for a design option consider the cumulative costs of the design
components.
Business analysts also consider opportunity cost when estimating the expected
cost of a change. Opportunity costs are alternative results that might have been
achieved if the resources, time, and funds devoted to one design option had been
allocated to another design option. The opportunity cost of any design option is
equal to the value of the best alternative not selected.
.3 Determine Value
The potential value of a solution to a stakeholder is based on the benefits
delivered by that solution and the associated costs. Value can be positive (if the
benefits exceed the costs) or negative (if the costs exceed the benefits).
Business analysts consider potential value from the points of view of stakeholders.
Value to the enterprise is almost always more heavily weighted than value for any
individual stakeholder groups. There might be increases in value for one set of
stakeholders and decreases in value for another set, but an overall positive
increase in value for the enterprise as a whole justifies proceeding with the
change.
Potential value is uncertain value. There are always events or conditions that
could increase or decrease the actual value if they occur. Many changes are
proposed in terms of intangible or uncertain benefits, while costs are described as
tangible, absolute, and might grow. When benefits are described as intangible
and costs expressed as tangible, it may be difficult for decision makers to compare
their options. Business analysts define a complete estimate of the purpose-driven
and monetary effects of a proposed change by considering the tangible and
intangible costs alongside the tangible and intangible benefits. The estimate of
costs and benefits must take into account the degree of uncertainty pertaining at
the time the estimates are made.
.4 Assess Design Options and Recommend Solution
Each design option is assessed based on the potential value it is expected to
deliver. At any point in analyzing the design options, it may become necessary to
re-evaluate the initial allocation of design elements between components. The



Analyze Potential Value and Recommend Solution
Requirements Analysis and Design Definition
160
reasons for re-evaluation include better understanding of the cost to implement
each component and to determine which allocations have the best cost-to-
benefit ratio.
As costs and effort are understood for each solution component, business
analysts assess each design option to ensure that it represents the most effective
trade-offs. There are several factors to take into consideration:
• Available Resources: there may be limitations regarding the amount of
requirements that can be implemented based on the allocated resources. In
some instances, a business case can be developed to justify additional
investment.
• Constraints on the Solution: regulatory requirements or business
decisions may require that certain requirements be handled manually or
automatically, or that certain requirements be prioritized above all others.
• Dependencies between Requirements: some capabilities may in and of
themselves provide limited value to the organization, but need to be
delivered in order to support other high-value requirements.
Other considerations may include relationships with proposed vendors,
dependencies on other initiatives, corporate culture, and sufficient cash flow for
investment.
Business analysts recommend the option or options deemed to be the most
valuable solution to address the need. It is possible that none of the design
options are worthwhile and the best recommendation is to do nothing.
7.6.5
Guidelines and Tools
• Business Objectives: used to calculate the expected benefit.
• Current State Description: provides the context within which the work needs
to be completed. It can be used to identify and help quantify the value to be
delivered from a potential solution.
• Future State Description: describes the desired future state that the solution
will be part of in order to ensure the design options are appropriate.
• Risk Analysis Results: the potential value of design options includes an
assessment of the level of risk associated with the design options or initiative.
• Solution Scope: defines the scope of the solution that is being delivered so
that a relevant evaluation can be made that is within the scope boundaries.
7.6.6
Techniques
• Acceptance and Evaluation Criteria: used to express requirements in the
form of acceptance criteria to make them most useful when assessing proposed
solutions and determining whether a solution meets the defined business
needs.
• Backlog Management: used to sequence the potential value.



Requirements Analysis and Design Definition
Analyze Potential Value and Recommend Solution
161
• Brainstorming: used to identify potential benefits of the requirements in a
collaborative manner.
• Business Cases: used to assess recommendations against business goals and
objectives.
• Business Model Canvas: used as a tool to help understand strategy and
initiatives.
• Decision Analysis: used to support the assessment and ranking of design
options.
• Estimation: used to forecast the costs and efforts of meeting the requirements
as a step towards estimating their value.
• Financial Analysis: used to evaluate the financial return of different options
and choose the best possible return on investment.
• Focus Groups: used to get stakeholder input on which design options best
meet the requirements, and to evaluate a targeted, small group of stakeholders’
value expectations.
• Interviews: used to get stakeholder input on which design options best meet
the requirements, and to evaluate individual stakeholders’ value expectations.
• Metrics and Key Performance Indicators (KPIs): used to create and evaluate
the measurements used in defining value.
• Risk Analysis and Management: used to identify and manage the risks that
could affect the potential value of the requirements.
• Survey or Questionnaire: used to get stakeholder input on which design
options best meet the requirements, and to identify stakeholders’ value
expectations.
• SWOT Analysis: used to identify areas of strength and weakness that will
impact the value of the solutions.
• Workshops: used to get stakeholder input on which design options best meet
the requirements, and to evaluate stakeholders’ value expectations.
7.6.7
Stakeholders
• Customer: represents the market segments affected by the requirements and
solutions, and will be involved in analyzing the benefit of those requirements
and costs of the design options.
• Domain Subject Matter Expert: may be called upon for their domain
knowledge to assist in analyzing potential value and benefits, particularly for
those requirements where they are harder to identify.
• End User: provides an insight into the potential value of the change.
• Implementation Subject Matter Expert: may be called upon for their
expertise in implementing the design options in order to identify potential costs
and risks.



Analyze Potential Value and Recommend Solution
Requirements Analysis and Design Definition
162
• Project Manager: manages the selection process so that when effecting the
change they are aware of potential impacts on those supporting the change,
including the risks associated with the change.
• Regulator: may be involved in risk evaluation concerning outside regulatory
bodies or place constraints on the potential benefits.
• Sponsor: approves the expenditure of resources to purchase or develop a
solution and approve the final recommendation. The sponsor will want to be
kept informed of any changes in potential value or risk, as well as the resulting
opportunity cost, as he/she may prefer another course of action.
7.6.8
Outputs
• Solution Recommendation: identifies the suggested, most appropriate
solution based on an evaluation of all defined design options. The
recommended solution should maximize the value provided to the enterprise.



163
8
Solution Evaluation
The Solution Evaluation knowledge area describes the tasks that business analysts
perform to assess the performance of and value delivered by a solution in use by
the enterprise, and to recommend removal of barriers or constraints that prevent
the full realization of the value.
While there may be some similarities to the activities performed in Strategy
Analysis (p. 99), or Requirements Analysis and Design Definition (p. 133), an
important distinction between the Solution Evaluation knowledge area and other
knowledge areas is the existence of an actual solution. It may only be a partial
solution, but the solution or solution component has already been implemented
and is operating in some form. Solution Evaluation tasks that support the
realization of benefits may occur before a change is initiated, while current value
is assessed, or after a solution has been implemented.
Solution Evaluation tasks can be performed on solution components in varying
stages of development:
• Prototypes or Proofs of Concept: working but limited versions of a
solution that demonstrate value.
• Pilot or Beta releases: limited implementations or versions of a solution
used in order to work through problems and understand how well it
actually delivers value before fully releasing the solution.
• Operational releases: full versions of a partial or completed solution used
to achieve business objectives, execute a process, or fulfill a desired
outcome.
Solution Evaluation describes tasks that analyze the actual value being delivered,
identifies limitations which may be preventing value from being realized, and



Solution Evaluation
164
makes recommendations to increase the value of the solution. It may include any
combination of performance assessments, tests, and experiments, and may
combine both objective and subjective assessments of value. Solution Evaluation
generally focuses on a component of an enterprise rather than the entire
enterprise.
The following image illustrates the spectrum of value as business analysis
activities progress from delivering potential value to actual value.
Figure 8.0.1: Business Analysis Value Spectrum
The Solution Evaluation knowledge area includes the following tasks:
• Measure Solution Performance: determines the most appropriate way to
assess the performance of a solution, including how it aligns with enterprise
goals and objectives, and performs the assessment.
• Analyze Performance Measures: examines information regarding the
performance of a solution in order to understand the value it delivers to the
enterprise and to stakeholders, and determines whether it is meeting
current business needs.
• Assess Solution Limitations: investigates issues within the scope of a
solution that may prevent it from meeting current business needs.
• Assess Enterprise Limitations: investigates issues outside the scope of a
solution that may be preventing the enterprise from realizing the full value
that a solution is capable of providing.
• Recommend Actions to Increase Solution Value: identifies and defines
actions the enterprise can take to increase the value that can be delivered
by a solution.
The Core Concept Model in Solution Evaluation
The Business Analysis Core Concept Model™ (BACCM™) describes the
relationships among the six core concepts. The following table describes the
usage and application of each of the core concepts within the context of Solution
Evaluation.
Solution Evaluation
Potential
Requirements Analysis
& Design Definition
Strategy Analysis
Need
Solution
Scope
Requirements
Design
Proof of Concept/
Prototype
Pilot/Beta
Operating
Actual



Solution Evaluation
165
Table 8.0.1: : The Core Concept Model in Solution Evaluation
Core Concept
During Solution Evaluation, business
analysts...
Change: the act of transformation
in response to a need.
recommend a change to either a solution
or the enterprise in order to realize the
potential value of a solution.
Need: a problem or opportunity to
be addressed.
evaluate how a solution or solution
component is fulfilling the need.
Solution: a specific way of
satisfying one or more needs in a
context.
assess the performance of the solution,
examine if it is delivering the potential
value, and analyze why value may not be
realized by the solution or solution
component.
Stakeholder: a group or
individual with a relationship to
the change, the need, or the
solution.
elicit information from the stakeholders
about solution performance and value
delivery.
Value: the worth, importance, or
usefulness of something to a
stakeholder within a context.
determine if the solution is delivering the
potential value and examine why value
may not be being realized.
Context: the circumstances that
influence, are influenced by, and
provide understanding of the
change.
consider the context in determining
solution performance measures and any
limitations within the context that may
prohibit value from being realized.



Measure Solution Performance
Solution Evaluation
166
Figure 8.0.2: Solution Evaluation Input/Output Diagram
8.1
Measure Solution Performance
8.1.1
Purpose
The purpose of Measure Solution Performance is to define performance measures
and use the data collected to evaluate the effectiveness of a solution in relation to
the value it brings.
Tasks
Output
8.3
Assess Solution
Limitations
8.2
Analyze
Performance
Measures
8.1
Measure Solution
Performance
8.4
Assess Enterprise
Limitations
8.5
Recommend
Actions to Increase
Solution Value
Implemented Solution
(external)
6.1
Current State
Description
6.2
Business Objectives
6.2
Potential Value
8.1
Solution Performance
Measures
8.2
Solution Performance
Analysis
8.3
Solution Limitation
8.5
Recommend Actions
8.4
Enterprise Limitation
Input



Solution Evaluation
Measure Solution Performance
167
8.1.2
Description
Performance measures determine the value of a newly deployed or existing
solution. The measures used depend on the solution itself, the context, and how
the organization defines value. When solutions do not have built-in performance
measures, the business analyst works with stakeholders to determine and collect
the measures that will best reflect the performance of a solution. Performance
may be assessed through key performance indicators (KPIs) aligned with
enterprise measures, goals and objectives for a project, process performance
targets, or tests for a software application.
8.1.3
Inputs
• Business Objectives: the measurable results that the enterprise wants to
achieve. Provides a benchmark against which solution performance can be
assessed.
• Implemented Solution (external): a solution (or component of a solution)
that exists in some form. It may be an operating solution, a prototype, or a pilot
or beta solution.
Figure 8.1.1: Measure Solution Performance Input/Output Diagram
Tasks Using This Output
Output
8.1
Measure Solution Performance
Change Strategy
8.1
Solution
Performance
Measures
6.1
Analyze Current
State
Implemented
Solution
(external)
Future State Description
Requirements (validated)
Solution Scope
8.2
Analyze
Performance
Measures
6.2
Business
Objectives
Guidelines and Tools
Input



Measure Solution Performance
Solution Evaluation
168
8.1.4
Elements
.1 Define Solution Performance Measures
When measuring solution performance, business analysts determine if current
measures exist, or if methods for capturing them are in place. Business analysts
ensure that any existing performance measures are accurate, relevant and elicit
any additional performance measures identified by stakeholders.
Business goals, objectives, and business processes are common sources of
measures. Performance measures may be influenced or imposed by third parties
such as solution vendors, government bodies, or other regulatory organizations.
The type and nature of the measurements are considered when choosing the
elicitation method. Solution performance measures may be quantitative,
qualitative, or both, depending on the value being measured.
• Quantitative Measures: are numerical, countable, or finite, usually
involving amounts, quantities, or rates.
• Qualitative Measures: are subjective and can include attitudes,
perceptions, and any other subjective response. Customers, users, and
others involved in the operation of a solution have perceptions of how well
the solution is meeting the need.
.2 Validate Performance Measures
Validating performance measures helps to ensure that the assessment of solution
performance is useful. Business analysts validate the performance measures and
any influencing criteria with stakeholders. Specific performance measures should
align with any higher-level measures that exist within the context affecting the
solution. Decisions about which measures are used to evaluate solution
performance often reside with the sponsor, but may be made by any stakeholder
with decision-making authority.
.3 Collect Performance Measures
When defining performance measures, business analysts may employ basic
statistical sampling concepts.
When collecting performance measures, business analysts consider:
• Volume or Sample Size: a volume or sample size appropriate for the
initiative is selected. A sample size that is too small might skew the results
and lead to inaccurate conclusions. Larger sample sizes may be more
desirable, but may not be practical to obtain.
• Frequency and Timing: the frequency and timing with which
measurements are taken may have an effect on the outcome.
• Currency: measurements taken more recently tend to be more
representative than older data.
Using qualitative measures, business analysts can facilitate discussions to estimate
the value realized by a solution. Stakeholders knowledgeable about the operation



Solution Evaluation
Measure Solution Performance
169
and use of the solution reach a consensus based on facts and reasonable
assumptions, as perceived by them.
8.1.5
Guidelines and Tools
• Change Strategy: the change strategy used or in use to implement the
potential value.
• Future State Description: boundaries of the proposed new, removed, or
modified components of the enterprise, and the potential value expected from
the future state.
• Requirements (validated): a set of requirements that have been analyzed and
appraised to determine their value.
• Solution Scope: the solution boundaries to measure and evaluate.
8.1.6
Techniques
• Acceptance and Evaluation Criteria: used to define acceptable solution
performance.
• Benchmarking and Market Analysis: used to define measures and their
acceptable levels.
• Business Cases: used to define business objectives and performance measures
for a proposed solution.
• Data Mining: used to collect and analyze large amounts of data regarding
solution performance.
• Decision Analysis: used to assist stakeholders in deciding on suitable ways to
measure solution performance and acceptable levels of performance.
• Focus Groups: used to provide subjective assessments, insights, and
impressions of a solution’s performance.
• Metrics and Key Performance Indicators (KPIs): used to measure solution
performance.
• Non-Functional Requirements Analysis: used to define expected
characteristics of a solution.
• Observation: used either to provide feedback on perceptions of solution
performance or to reconcile contradictory results.
• Prototyping: used to simulate a new solution so that performance measures
can be determined and collected.
• Survey or Questionnaire: used to gather opinions and attitudes about
solution performance. Surveys and questionnaires can be effective when large
or disparate groups need to be polled.
• Use Cases and Scenarios: used to define the expected outcomes of a
solution.
• Vendor Assessment: used to assess which of the vendor’s performance
measures should be included in the solution’s performance assessment.



Analyze Performance Measures
Solution Evaluation
170
8.1.7
Stakeholders
• Customer: may be consulted to provide feedback on solution performance.
• Domain Subject Matter Expert: a person familiar with the domain who can
be consulted to provide potential measurements.
• End User: contributes to the actual value realized by the solution in terms of
solution performance. They may be consulted to provide reviews and feedback
on areas such as workload and job satisfaction.
• Project Manager: responsible for managing the schedule and tasks to perform
the solution measurement. For solutions already in operation, this role may not
be required.
• Sponsor: responsible for approving the measures used to determine solution
performance. May also provide performance expectations.
• Regulator: an external or internal group that may dictate or prescribe
constraints and guidelines that must be incorporated into solution performance
measures.
8.1.8
Outputs
• Solution Performance Measures: measures that provide information on how
well the solution is performing or potentially could perform.
8.2
Analyze Performance Measures
8.2.1
Purpose
The purpose of Analyze Performance Measures is to provide insights into the
performance of a solution in relation to the value it brings.
8.2.2
Description
The measures collected in the task Measure Solution Performance (p. 166) often
require interpretation and synthesis to derive meaning and to be actionable.
Performance measures themselves rarely trigger a decision about the value of a
solution.
In order to meaningfully analyze performance measures, business analysts require
a thorough understanding of the potential value that stakeholders hope to
achieve with the solution. To assist in the analysis, variables such as the goals and
objectives of the enterprise, key performance indicators (KPIs), the level of risk of
the solution, the risk tolerance of both stakeholders and the enterprise, and other
stated targets are considered.
8.2.3
Inputs
• Potential Value: describes the value that may be realized by implementing the
proposed future state. It can be used as a benchmark against which solution
performance can be evaluated.



Solution Evaluation
Analyze Performance Measures
171
• Solution Performance Measures: measures and provides information on
how well the solution is performing or potentially could perform.
Figure 8.2.1: Analyze Performance Measures Input/Output Diagram
8.2.4
Elements
.1 Solution Performance versus Desired Value
Business analysts examine the measures previously collected in order to assess
their ability to help stakeholders understand the solution’s value. A solution might
be high performing, such as an efficient online transaction processing system, but
contributes lower value than expected (or compared to what it had contributed in
the past). On the other hand, a low performing but potentially valuable solution,
such as a core process that is inefficient, can be enhanced to increase its
performance level. If the measures are not sufficient to help stakeholders
determine solution value, business analysts either collect more measurements or
treat the lack of measures as a solution risk.
.2 Risks
Performance measures may uncover new risks to solution performance and to the
enterprise. These risks are identified and managed like any other risks.
Input
Tasks Using This Output
Output
8.2
Analyze Performance
Measures
Change Strategy
8.2
Solution
Performance
Analysis
8.3
Assess Solution
Limitations
6.2
Potential Value
Future State Description
Risk Analysis Results
Solution Scope
8.4
Assess Enterprise
Limitations
8.1
Solution
Performance
Measures
Guidelines and Tools



Analyze Performance Measures
Solution Evaluation
172
.3 Trends
When analyzing performance data, business analysts consider the time period
when the data was collected to guard against anomalies and skewed trends. A
large enough sample size over a sufficient time period will provide an accurate
depiction of solution performance on which to make decisions and guard against
false signals brought about by incomplete data. Any pronounced and repeated
trends, such as a noticeable increase in errors at certain times or a change in
process speed when volume is increased, are noted.
.4 Accuracy
The accuracy of performance measures is essential to the validity of their analysis.
Business analysts test and analyze the data collected by the performance
measures to ensure their accuracy. To be considered accurate and reliable, the
results of performance measures should be reproducible and repeatable.
.5 Performance Variances
The difference between expected and actual performance represents a variance
that is considered when analyzing solution performance. Root cause analysis may
be necessary to determine the underlying causes of significant variances within a
solution. Recommendations of how to improve performance and reduce any
variances are made in the task Recommend Actions to Increase Solution Value
(p. 182).
8.2.5
Guidelines and Tools
• Change Strategy: the change strategy that was used or is in use to implement
the potential value.
• Future State Description: boundaries of the proposed new, modified, or
removed components of the enterprise and the potential value expected from
the future state.
• Risk Analysis Results: the overall level of risk and the planned approach to
modifying the individual risks.
• Solution Scope: the solution boundaries to measure and evaluate.
8.2.6
Techniques
• Acceptance and Evaluation Criteria: used to define acceptable solution
performance through acceptance criteria. The degree of variance from these
criteria will guide the analysis of that performance.
• Benchmarking and Market Analysis: used to observe the results of other
organizations employing similar solutions when assessing risks, trends, and
variances.
• Data Mining: used to collect data regarding performance, trends, common
issues, and variances from expected performance levels and understand
patterns and meaning in that data.



Solution Evaluation
Assess Solution Limitations
173
• Interviews: used to determine expected value of a solution and its perceived
performance from an individual or small group's perspective.
• Metrics and Key Performance Indicators (KPIs): used to analyze solution
performance, especially when judging how well a solution contributes to
achieving goals.
• Observation: used to observe a solution in action if the data collected does not
provide definitive conclusions.
• Risk Analysis and Management: used to identify, analyze, develop plans to
modify the risks, and to manage the risks on an ongoing basis.
• Root Cause Analysis: used to determine the underlying cause of performance
variance.
• Survey or Questionnaire: used to determine expected value of a solution and
its perceived performance.
8.2.7
Stakeholders
• Domain Subject Matter Expert: can identify risks and provide insights into
data for analyzing solution performance.
• Project Manager: within a project, responsible for overall risk management
and may participate in risk analysis for new or changed solutions.
• Sponsor: can identify risks, provide insights into data and the potential value of
a solution. They will make decisions about the significance of expected versus
actual solution performance.
8.2.8
Outputs
• Solution Performance Analysis: results of the analysis of measurements
collected and recommendations to solve performance gaps and leverage
opportunities to improve value.
8.3
Assess Solution Limitations
8.3.1
Purpose
The purpose of Assess Solution Limitations is to determine the factors internal to
the solution that restrict the full realization of value.
8.3.2
Description
Assessing solution limitations identifies the root causes for under-performing and
ineffective solutions and solution components.
Assess Solution Limitations is closely linked to the task Assess Enterprise
Limitations (p. 177). These tasks may be performed concurrently. If the solution



Assess Solution Limitations
Solution Evaluation
174
has not met its potential value, business analysts determine which factors, both
internal and external to the solution, are limiting value. This task focuses on the
assessment of those factors internal to the solution.
This assessment may be performed at any point during the solution life cycle. It
may occur on a solution component during its development, on a completed
solution prior to full implementation, or on an existing solution that is currently
working within an organization. Regardless of the timing, the assessment
activities are similar and involve the same considerations.
8.3.3
Inputs
• Implemented Solution (external): a solution that exists. The solution may or
may not be in operational use; it may be a prototype. The solution must be in
use in some form in order to be evaluated.
• Solution Performance Analysis: results of the analysis of measurements
collected and recommendations to solve for performance gaps and leverage
opportunities to improve value.
Figure 8.3.1: Assess Solution Limitations Input/Output Diagram
Input
Tasks Using This Output
Output
8.3
Assess Solution Limitations
Change Strategy
8.3
Solution Limitation
6.1
Analyze Current
State
Implemented
Solution (external)
Risk Analysis Results
Solution Scope
8.5
Recommend
Actions to Increase
Solution Value
8.2
Solution
Performance
Analysis
Guidelines and Tools



Solution Evaluation
Assess Solution Limitations
175
8.3.4
Elements
.1 Identify Internal Solution Component Dependencies
Solutions often have internal dependencies that limit the performance of the entire
solution to the performance of the least effective component. Assessment of the
overall performance of the solution or its components is performed in the tasks
Measure Solution Performance (p. 166) and Analyze Performance Measures
(p. 170). Business analysts identify solution components which have dependencies
on other solution components, and then determine if there is anything about those
dependencies or other components that limit solution performance and value
realization.
.2 Investigate Solution Problems
When it is determined that the solution is consistently or repeatedly producing
ineffective outputs, problem analysis is performed in order to identify the source
of the problem.
Business analysts identify problems in a solution or solution component by
examining instances where the outputs from the solution are below an
acceptable level of quality or where the potential value is not being realized.
Problems may be indicated by an inability to meet a stated goal, objective, or
requirement, or may be a failure to realize a benefit that was projected during the
tasks Define Change Strategy (p. 124) or Recommend Actions to Increase
Solution Value (p. 182).
.3 Impact Assessment
Business analysts review identified problems in order to assess the effect they may
have on the operation of the organization or the ability of the solution to deliver
its potential value. This requires determining the severity of the problem, the
probability of the re-occurrence of the problem, the impact on the business
operations, and the capacity of the business to absorb the impact. Business
analysts identify which problems must be resolved, which can be mitigated
through other activities or approaches, and which can be accepted.
Other activities or approaches may include additional quality control measures,
new or adjusted business processes, or additional support for exceptions to the
desired outcome.
In addition to identified problems, business analysts assess risks to the solution
and potential limitations of the solution. This risk assessment is specific to the
solution and its limitations.
8.3.5
Guidelines and Tools
• Change Strategy: the change strategy used or in use to implement the
potential value.



Assess Solution Limitations
Solution Evaluation
176
• Risks Analysis Results: the overall level of risk and the planned approach to
modifying the individual risks.
• Solution Scope: the solution boundaries to measure and evaluate.
8.3.6
Techniques
• Acceptance and Evaluation Criteria: used both to indicate the level at which
acceptance criteria are met or anticipated to be met by the solution and to
identify any criteria that are not met by the solution.
• Benchmarking and Market Analysis: used to assess if other organizations
are experiencing the same solution challenges and, if possible, determine how
they are addressing it.
• Business Rules Analysis: used to illustrate the current business rules and the
changes required to achieve the potential value of the change.
• Data Mining: used to identify factors constraining performance of the
solution.
• Decision Analysis: used to illustrate the current business decisions and the
changes required to achieve the potential value of the change.
• Interviews: used to help perform problem analysis.
• Item Tracking: used to record and manage stakeholder issues related to why
the solution is not meeting the potential value.
• Lessons Learned: used to determine what can be learned from the inception,
definition, and construction of the solution to have potentially impacted its
ability to deliver value.
• Risk Analysis and Management: used to identify, analyze, and manage risks,
as they relate to the solution and its potential limitations, that may impede the
realization of potential value.
• Root Cause Analysis: used to identify and understand the combination of
factors and their underlying causes that led to the solution being unable to
deliver its potential value.
• Survey or Questionnaire: used to help perform problem analysis.
8.3.7
Stakeholders
• Customer: is ultimately affected by a solution, and therefore has an important
perspective on its value. A customer may be consulted to provide reviews and
feedback.
• Domain Subject Matter Expert: provides input into how the solution should
perform and identifies potential limitations to value realization.



Solution Evaluation
Assess Enterprise Limitations
177
• End User: uses the solution, or is a component of the solution, and therefore
contributes to the actual value realized by the solution in terms of solution
performance. An end user may be consulted to provide reviews and feedback
on areas such as workload and job satisfaction.
• Regulator: a person whose organization needs to be consulted about the
planned and potential value of a solution, as that organization may constrain
the solution, the degree to which actual value is realized, or when actual value
is realized.
• Sponsor: responsible for approving the potential value of the solution, for
providing resources to develop, implement and support the solution, and for
directing enterprise resources to use the solution. The sponsor is also
responsible for approving a change to potential value.
• Tester: responsible for identifying solution problems during construction and
implementation; not often used in assessing an existing solution outside of a
change.
8.3.8
Outputs
• Solution Limitation: a description of the current limitations of the solution
including constraints and defects.
8.4
Assess Enterprise Limitations
8.4.1
Purpose
The purpose of Assess Enterprise Limitations is to determine how factors external
to the solution are restricting value realization.
8.4.2
Description
Solutions may operate across various organizations within an enterprise, and
therefore have many interactions and interdependencies. Solutions may also
depend on environmental factors that are external to the enterprise. Enterprise
limitations may include factors such as culture, operations, technical components,
stakeholder interests, or reporting structures.
Assessing enterprise limitations identifies root causes and describes how
enterprise factors limit value realization.
This assessment may be performed at any point during the solution life cycle. It
may occur on a solution component during its development or on a completed
solution prior to full implementation. It may also occur on an existing solution
that is currently working within an organization. Regardless of the timing, the
assessment activities are similar and require the same skills.



Assess Enterprise Limitations
Solution Evaluation
178
8.4.3
Inputs
• Current State Description: the current internal environment of the solution
including the environmental, cultural, and internal factors influencing the
solution limitations.
• Implemented (or Constructed) Solution (external): a solution that exists.
The solution may or may not be in operational use; it may be a prototype. The
solution must be in use in some form in order to be evaluated.
• Solution Performance Analysis: results of the analysis of measurements
collected and recommendations to solve performance gaps and leverage
opportunities to improve value.
Figure 8.4.1: Assess Enterprise Limitations Input/Output Diagram
8.4.4
Elements
.1 Enterprise Culture Assessment
Enterprise culture is defined as the deeply rooted beliefs, values, and norms
shared by the members of an enterprise. While these beliefs and values may not
be directly visible, they drive the actions taken by an enterprise.
Business analysts perform cultural assessments to:
Input
Tasks Using This Output
Output
8.4
Assess Enterprise Limitations
8.4
Enterprise
Limitation
6.1
Analyze Current
State
6.1
Current State
Description
Implemented or
Constructed
Solution (external)
8.5
Recommend
Actions to Increase
Solution Value
8.2
Solution
Performance
Analysis
Guidelines and Tools
Business Objectives
Change Strategy
Future State Description
Risk Analysis Results
Solution Scope



Solution Evaluation
Assess Enterprise Limitations
179
• identify whether or not stakeholders understand the reasons why a solution
exists,
• ascertain whether or not the stakeholders view the solution as something
beneficial and are supportive of the change, and
• determine if and what cultural changes are required to better realize value
from a solution.
The enterprise culture assessment evaluates the extent to which the culture can
accept a solution. If cultural adjustments are needed to support the solution, the
assessment is used to judge the enterprise’s ability and willingness to adapt to
these cultural changes.
Business analysts also evaluate internal and external stakeholders to:
• gauge understanding and acceptance of the solution,
• assess perception of value and benefit from the solution, and
• determine what communication activities are needed to ensure awareness
and understanding of the solution.
.2 Stakeholder Impact Analysis
A stakeholder impact analysis provides insight into how the solution affects a
particular stakeholder group.
When conducting stakeholder impact analysis, business analysts consider:
• Functions: the processes in which the stakeholder uses the solution, which
include inputs a stakeholder provides into the process, how the stakeholder
uses the solution to execute the process, and what outputs the stakeholder
receives from the process.
• Locations: the geographic locations of the stakeholders interacting with
the solution. If the stakeholders are in disparate locations, it may impact
their use of the solution and the ability to realize the value of the solution.
• Concerns: the issues, risks, and overall concerns the stakeholders have with
the solution. This may include the use of the solution, the perceptions of
the value of the solution, and the impact the solution has on a stakeholder’s
ability to perform necessary functions.
.3 Organizational Structure Changes
There are occasions when business analysts assess how the organization’s
structure is impacted by a solution.
The use of a solution and the ability to adopt a change can be enabled or blocked
by formal and informal relationships among stakeholders. The reporting structure
may be too complex or too simple to allow a solution to perform effectively.
Assessing if the organizational hierarchy supports the solution is a key activity. On
occasion, informal relationships within an organization, whether alliances,



Assess Enterprise Limitations
Solution Evaluation
180
friendships, or matrix-reporting, impact the ability of a solution to deliver
potential value. Business analysts consider these informal relationships in addition
to the formal structure.
.4 Operational Assessment
The operational assessment is performed to determine if an enterprise is able to
adapt to or effectively use a solution. This identifies which processes and tools
within the enterprise are adequately equipped to benefit from the solution, and if
sufficient and appropriate assets are in place to support it.
When conducting an operational assessment, business analysts consider:
• policies and procedures,
• capabilities and processes that enable other capabilities,
• skill and training needs,
• human resources practices,
• risk tolerance and management approaches, and
• tools and technology that support a solution.
8.4.5
Guidelines and Tools
• Business Objectives: are considered when measuring and determining
solution performance.
• Change Strategy: the change strategy used or in use to implement the
potential value.
• Future State Descriptions: boundaries of the proposed new, removed, or
modified components of the enterprise, as well as the potential value expected
from the future state.
• Risk Analysis Results: the overall level of risk and the planned approach to
modifying the individual risks.
• Solution Scope: the solution boundaries to measure and evaluate.
8.4.6
Techniques
• Benchmarking and Market Analysis: used to identify existing solutions and
enterprise interactions.
• Brainstorming: used to identify organizational gaps or stakeholder concerns.
• Data Mining: used to identify factors constraining performance of the
solution.
• Decision Analysis: used to assist in making an optimal decision under
conditions of uncertainty and may be used in the assessment to make decisions
about functional, technical, or procedural gaps.



Solution Evaluation
Assess Enterprise Limitations
181
• Document Analysis: used to gain an understanding of the culture, operations,
and structure of the organization.
• Interviews: used to identify organizational gaps or stakeholder concerns.
• Item Tracking: used to ensure that issues are not neglected or lost and that
issues identified by assessment are resolved.
• Lessons Learned: used to analyze previous initiatives and the enterprise
interactions with the solutions.
• Observation: used to witness the enterprise and solution interactions to
identify impacts.
• Organizational Modelling: used to ensure the identification of any required
changes to the organizational structure that may have to be addressed.
• Process Analysis: used to identify possible opportunities to improve
performance.
• Process Modelling: used to illustrate the current business processes and/or
changes that must be made in order to achieve the potential value of the
solution.
• Risk Analysis and Management: used to consider risk in the areas of
technology (if the selected technological resources provide required
functionality), finance (if costs could exceed levels that make the change
salvageable), and business (if the organization will be able to make the changes
necessary to attain potential value from the solution).
• Roles and Permissions Matrix: used to determine roles and associated
permissions for stakeholders, as well as stability of end users.
• Root Cause Analysis: used to determine if the underlying cause may be
related to enterprise limitations.
• Survey or Questionnaire: used to identify organizational gaps or stakeholder
concerns.
• SWOT Analysis: used to demonstrate how a change will help the organization
maximize strengths and minimize weaknesses, and to assess strategies
developed to respond to identified issues.
• Workshops: used to identify organizational gaps or stakeholder concerns.
8.4.7
Stakeholders
• Customer: people directly purchasing or consuming the solution who may
interact with the organization in the use of the solution.
• Domain Subject Matter Expert: provides input into how the organization
interacts with the solution and identifies potential limitations.
• End User: people who use a solution or who are a component of the solution.
Users could be customers or people who work within the organization.



Recommend Actions to Increase Solution Value
Solution Evaluation
182
• Regulator: one or many governmental or professional entities that ensure
adherence to laws, regulations, or rules; may have unique input to the
organizational assessment, as relevant regulations must be included in the
requirements. There may be laws and regulations that must be complied with
prior to (or as a result of) a planned or implemented change.
• Sponsor: authorizes and ensures funding for a solution delivery, and
champions action to resolve problems identified in the organizational
assessment.
8.4.8
Outputs
• Enterprise Limitation: a description of the current limitations of the enterprise
including how the solution performance is impacting the enterprise.
8.5
Recommend Actions to Increase Solution Value
8.5.1
Purpose
The purpose of Recommend Actions to Increase Solution Value is to understand
the factors that create differences between potential value and actual value, and
to recommend a course of action to align them.
8.5.2
Description
The various tasks in the Solution Evaluation knowledge area help to measure,
analyze, and determine causes of unacceptable solution performance. The task
Recommend Actions to Increase Solution Value (p. 182), focuses on
understanding the aggregate of the performed assessments and identifying
alternatives and actions to improve solution performance and increase value
realization.
Recommendations generally identify how a solution should be replaced, retired,
or enhanced. They may also consider long-term effects and contributions of the
solution to stakeholders. They may include recommendations to adjust the
organization to allow for maximum solution performance and value realization.
8.5.3
Inputs
• Enterprise Limitation: a description of the current limitations of the enterprise
including how the solution performance is impacting the enterprise.
• Solution Limitation: a description of the current limitations of the solution
including constraints and defects.



Solution Evaluation
Recommend Actions to Increase Solution Value
183
Figure 8.5.1: Recommend Actions to Increase Solution Value Input/Output Diagram
8.5.4
Elements
.1 Adjust Solution Performance Measures
In some cases, the performance of the solution is considered acceptable but may
not support the fulfillment of business goals and objectives. An analysis effort to
identify and define more appropriate measures may be required.
.2 Recommendations
While recommendations often describe ways to increase solution performance,
this is not always the case. Depending on the reason for lower than expected
performance, it may be reasonable to take no action, adjust factors that are
external to the solution, or reset expectations for the solution.
Some common examples of recommendations that a business analyst may make
include:
• Do Nothing: is usually recommended when the value of a change is low
relative to the effort required to make the change, or when the risks of
change significantly outweigh the risks of remaining in the current state. It
Input
Tasks Using This Output
Output
8.5
Recommend Actions to
Increase Solution Value
8.5
Recommended
Actions
4.5
Manage
Stakeholder
Collaboration
8.3
Solution Limitation
8.4
Enterprise
Limitation
Guidelines and Tools
Business Objectives
Current State Description
Solution Scope



Recommend Actions to Increase Solution Value
Solution Evaluation
184
may also be impossible to make a change with the resources available or in
the allotted time frame.
• Organizational Change: is a process for managing attitudes about,
perceptions of, and participation in the change related to the solution.
Organizational change management generally refers to a process and set of
tools for managing change at an organizational level. The business analyst
may help to develop recommendations for changes to the organizational
structure or personnel, as job functions may change significantly as the
result of work being automated. New information may be made available
to stakeholders and new skills may be required to operate the solution.
Possible recommendations that relate to organizational change include:
• automating or simplifying the work people perform. Relatively simple
tasks are prime candidates for automation. Additionally, work activities
and business rules can be reviewed and analyzed to determine
opportunities for re-engineering, changes in responsibilities, and
outsourcing.
• improving access to information. Change may provide greater amounts
of information and better quality of information to staff and decision
makers.
• Reduce Complexity of Interfaces: interfaces are needed whenever work
is transferred between systems or between people. Reducing their
complexity can improve understanding.
• Eliminate Redundancy: different stakeholder groups may have common
needs that can be met with a single solution, reducing the cost of
implementation.
• Avoid Waste: the aim of avoiding waste is to completely remove those
activities that do not add value and minimize those activities that do not
contribute to the final product directly.
• Identify Additional Capabilities: solution options may offer capabilities
to the organization above and beyond those identified in the requirements.
In many cases, these capabilities are not of immediate value to the
organization but have the potential to provide future value, as the solution
may support the rapid development or implementation of those capabilities
if they are required (for example, a software application may have features
that the organization anticipates using in the future).
• Retire the Solution: it may be necessary to consider the replacement of a
solution or solution component. This may occur because technology has
reached the end of its life, services are being insourced or outsourced, or
the solution is not fulfilling the goals for which it was created.
• Some additional factors that may impact the decision regarding the
replacement or retirement of a solution include:
• ongoing cost versus initial investment: it is common for the existing
solution to have increasing costs over time, while alternatives have a
higher investment cost upfront but lower maintenance costs.



Solution Evaluation
Recommend Actions to Increase Solution Value
185
• opportunity cost: represents the potential value that could be realized
by pursuing alternative courses of action.
• necessity: most solution components have a limited lifespan (due to
obsolescence, changing market conditions, and other causes). After a
certain point in the life cycle it will become impractical or impossible to
maintain the existing component.
• sunk cost: describes the money and effort already committed to an
initiative. The psychological impact of sunk costs may make it difficult
for stakeholders to objectively assess the rationale for replacement or
elimination, as they may feel reluctant to "waste" the effort or money
already invested. As this investment cannot be recovered, it is effectively
irrelevant when considering future action. Decisions should be based on
the future investment required and the future benefits that can be
gained.
8.5.5
Guidelines and Tools
• Business Objectives: are considered in evaluating, measuring, and
determining solution performance.
• Current State Description: provides the context within which the work needs
to be completed. It can be used to assess alternatives and better understand the
potential increased value that could be delivered. It can also help highlight
unintended consequences of alternatives that may otherwise remain
undetected.
• Solution Scope: the solution boundaries to measure and evaluate.
8.5.6
Techniques
• Data Mining: used to generate predictive estimates of solution performance.
• Decision Analysis: used to determine the impact of acting on any of the
potential value or performance issues.
• Financial Analysis: used to assess the potential costs and benefits of a change.
• Focus Groups: used to determine if solution performance measures need to be
adjusted and used to identify potential opportunities to improve performance.
• Organizational Modelling: used to demonstrate potential change within the
organization's structure.
• Prioritization: used to identify relative value of different actions to improve
solution performance.
• Process Analysis: used to identify opportunities within related processes.
• Risk Analysis and Management: used to evaluate different outcomes under
specific conditions.
• Survey or Questionnaire: used to gather feedback from a wide variety of
stakeholders to determine if value has been met or exceeded, if the metrics are



Recommend Actions to Increase Solution Value
Solution Evaluation
186
still valid or relevant in the current context, and what actions might be taken to
improve the solution.
8.5.7
Stakeholders
• Customer: people directly purchasing or consuming the solution and who may
interact with the organization in the use of the solution.
• Domain Subject Matter Expert: provides input into how to change the
solution and/or the organization in order to increase value.
• End User: people who use a solution or who are a component of the solution.
Users could be customers or people who work within the organization.
• Regulator: one or many governmental or professional entities that ensure
adherence to laws, regulations, or rules. Relevant regulations must be included
in requirements.
• Sponsor: authorizes and ensures funding for implementation of any
recommended actions.
8.5.8
Outputs
• Recommended Actions: recommendation of what should be done to improve
the value of the solution within the enterprise.



187
9
Underlying Competencies
The Underlying Competencies chapter provides a description of the behaviours,
characteristics, knowledge, and personal qualities that support the practice of
business analysis.
The underlying competencies described here are not unique to business analysis.
They are described here to ensure readers are aware of the range of fundamental
skills required and provide a basis for them to further investigate the skills and
knowledge that will enable them to be accomplished and adaptable business
analysts.
These competencies are grouped into six categories:
• Analytical Thinking and Problem Solving (p. 188),
• Behavioural Characteristics (p. 194),
• Business Knowledge (p. 199),
• Communication Skills (p. 203),
• Interaction Skills (p. 207), and
• Tools and Technology (p. 211).
Each underlying competency is defined with a purpose, definition, and
effectiveness measures.



Analytical Thinking and Problem Solving
Underlying Competencies
188
9.1
Analytical Thinking and Problem Solving
Analytical thinking and problem solving skills are required for business analysts to
analyze problems and opportunities effectively, identify which changes may
deliver the most value, and work with stakeholders to understand the impact of
those changes.
Business analysts use analytical thinking by rapidly assimilating various types of
information (for example, diagrams, stakeholder concerns, customer feedback,
schematics, user guides, and spreadsheets), and identifying which are relevant.
Business analysts should be able to quickly choose effective and adaptable
methods to learn and analyze the media, audiences, problem types, and
environments as each is encountered.
Business analysts utilize analytical thinking and problem solving as they facilitate
understanding of situations, the value of proposed changes, and other complex
ideas.
Possessing a sound understanding of the analytical thinking and problem solving
core competencies allows business analysts to identify the best ways to present
information to their stakeholders. For example, some concepts are more easily
understood when presented in diagrams and information graphics rather than by
paragraphs of text. Having this understanding assists business analysts when
planning their business analysis approach and enables them to communicate
business analysis information in a manner that suits the material being conveyed
to their audience.
Analytical Thinking and Problem Solving core competencies include:
• Creative Thinking,
• Decision Making,
• Learning,
• Problem Solving,
• Systems Thinking,
• Conceptual Thinking, and
• Visual Thinking.
9.1.1
Creative Thinking
.1 Purpose
Thinking creatively and helping others to apply creative thinking helps business
analysts to be effective in generating new ideas, approaches, and alternatives to
problem solving and opportunities.
.2 Definition
Creative thinking involves generating new ideas and concepts as well as finding
new or different associations between existing ideas and concepts. It helps



Underlying Competencies
Analytical Thinking and Problem Solving
189
overcome rigid approaches to problem solving by questioning conventional
approaches and encouraging new ideas and innovations that are appropriate to
the situation. Creative thinking may involve combining, changing, and reapplying
existing concepts or ideas. Business analysts can be effective in promoting
creative thinking in others by identifying and proposing alternatives, and by
asking questions and challenging assumptions.
.3 Effectiveness Measures
Measures of effective creative thinking include:
• generating and productively considering new ideas,
• exploring concepts and ideas that are new,
• exploring changes to existing concepts and ideas,
• generating creativity for self and others, and
• applying new ideas to resolve existing problems.
9.1.2
Decision Making
.1 Purpose
Business analysts must be effective in understanding the criteria involved in
making a decision, and in assisting others to make better decisions.
.2 Definition
When a business analyst or a group of stakeholders is faced with having to select
an option from a set of alternatives, a decision must be made on which is the
most advantageous for the stakeholders and the enterprise. Determining this
involves gathering the information that is relevant to the decision, analyzing the
relevant information, making comparisons and trade-offs between similar and
dissimilar options, and identifying the most desirable option. Business analysts
document decisions (and the rationale supporting those decisions) to use them as
a reference in the event a similar decision is required in the future or if they are
required to explain why a decision was made.
.3 Effectiveness Measures
Measures of effective decision making include:
• the appropriate stakeholders are represented in the decision-making
process,
• stakeholders understand the decision-making process and the rationale
behind the decision,
• the pros and cons of all available options are clearly communicated to
stakeholders,
• the decision reduces or eliminates uncertainty, and any remaining
uncertainty is accepted,



Analytical Thinking and Problem Solving
Underlying Competencies
190
• the decision made addresses the need or the opportunity at hand and is in
the best interest of all stakeholders,
• stakeholders understand all the conditions, environment, and measures in
which the decision will be made, and
• a decision is made.
9.1.3
Learning
.1 Purpose
The ability to quickly absorb new and different types of information and also
modify and adapt existing knowledge allows business analysts to work effectively
in rapidly changing and evolving environments.
.2 Definition
Learning is the process of gaining knowledge or skills. Learning about a domain
passes through a set of stages, from initial acquisition and learning of raw facts,
through comprehension of their meaning, to applying the knowledge in day-to-
day work, and finally analysis, synthesis, and evaluation. Business analysts must
be able to describe their level of understanding of the business domain and be
capable of applying that level of understanding to determine which analysis
activities need to be performed in a given situation. Once learning about a
domain has reached the point where analysis is complete, business analysts must
be able to synthesize the information to identify opportunities to create new
solutions and evaluate those solutions to ensure that they are effective.
Learning is improved when the learning technique is selected based on the
required learning outcomes.
Learning techniques to consider include:
• Visual: learning through the presentation of pictures, photographs,
diagrams, models, and videos.
• Auditory: learning through verbal and written language and text.
• Kinesthetic: learning by doing.
Most people experience faster understanding and longer retention of information
when more than one learning technique is used.
.3 Effectiveness Measures
Measures of effective learning include:
• understanding that learning is a process for all stakeholders,
• learning the concepts presented and then demonstrating an understanding
of them,
• demonstrating the ability to apply concepts to new areas or relationships,
• rapidly absorbing new facts, ideas, concepts, and opinions, and



Underlying Competencies
Analytical Thinking and Problem Solving
191
• effectively presenting new facts, ideas, concepts, and opinions to others.
9.1.4
Problem Solving
.1 Purpose
Business analysts define and solve problems in order to ensure that the real,
underlying root cause of a problem is understood by all stakeholders and that
solution options address that root cause.
.2 Definition
Defining a problem involves ensuring that the nature of the problem and any
underlying issues are clearly understood by all stakeholders. Stakeholder points of
view are articulated and addressed to understand any conflicts between the goals
and objectives of different groups of stakeholders. Assumptions are identified and
validated. The objectives that will be met once the problem is solved are clearly
specified, and alternative solutions are considered and possibly developed.
Alternatives are measured against the objectives to determine which possible
solution is best, and identify the value and trade-offs that may exist between
solutions.
.3 Effectiveness Measures
Measures of effective problem solving include:
• confidence of the participants in the problem solving process,
• selected solutions meet the defined objectives and solve the root cause of
the problem,
• new solution options can be evaluated effectively using the problem solving
framework, and
• the problem solving process avoids making decisions based on unvalidated
assumptions, preconceived notions, or other traps that may cause a sub-
optimal solution to be selected.
9.1.5
Systems Thinking
.1 Purpose
Understanding how the people, processes, and technology within an
organization interact allows business analysts to understand the enterprise from a
holistic point of view.
.2 Definition
Systems theory and systems thinking suggest that a system as a whole has
properties, behaviours, and characteristics that emerge from the interaction of
the components of that system. These factors are not predictable from an
understanding of the components alone. For example, just because a business



Analytical Thinking and Problem Solving
Underlying Competencies
192
analyst knows that a customer may return an item they purchased doesn't give
the business analyst the full picture. The analyst must analyze the impact the
return has on such items as inventory, finance, and store clerk training. In the
context of systems theory, the term system includes the people involved, the
interactions between them, the external forces affecting their behaviour, and all
other relevant elements and factors.
.3 Effectiveness Measures
Measures of effective use of systems thinking include:
• communicating how a change to a component affects the system as a
whole,
• communicating how a change to a system affects the environment it is in,
and
• communicating how systems adapt to internal and/or external pressures
and changes.
9.1.6
Conceptual Thinking
.1 Purpose
Business analysts routinely receive large amounts of detailed and potentially
disparate information. They apply conceptual thinking skills to find ways to
understand how that information fits into a larger picture and what details are
important, and to connect seemingly abstract information.
.2 Definition
Conceptual thinking is about understanding the linkage between contexts,
solutions, needs, changes, stakeholders, and value abstractly and in the big
picture. It involves understanding and connecting information and patterns that
may not be obviously related. Conceptual thinking involves understanding where
details fit into a larger context. It involves using past experiences, knowledge,
creativity, intuition, and abstract thinking to generate alternatives, options, and
ideas that are not easily defined or related.
Conceptual thinking in business analysis is specifically about linking factors not
easily defined to the underlying problem or opportunity, models, or frameworks
that help stakeholders understand and facilitate themselves and others through
change. It is needed to connect disparate information from a multitude of
stakeholders, objectives, risks, details, and other factors. With this information it
generates options and alternatives for a solution, and communicates this
information to others while encouraging them to generate ideas of their own.
.3 Effectiveness Measures
Measures of effective conceptual thinking include:
• connecting disparate information and acting to better understand the
relationship,



Underlying Competencies
Analytical Thinking and Problem Solving
193
• confirming the confidence and understanding of the concept being
communicated with stakeholders,
• formulating abstract concepts using a combination of information and
uncertainty, and
• drawing on past experiences to understand the situation.
9.1.7
Visual Thinking
.1 Purpose
The ability to communicate complex concepts and models into understandable
visual representations allows business analysts to engage stakeholders and help
them understand the concepts being presented.
.2 Definition
Visual thinking skills allow business analysts to create graphical representations of
the concepts or systems being discussed. The goal of these graphical
representations is to allow stakeholders to easily understand the concepts being
presented, and then provide input. Visual thinking requires that the analyst make
abstractions and then find suitable graphic devices to represent them.
Visual thinking is visualizing and creating simple visual concepts, graphics,
models, diagrams, and constructs to convey and integrate non-visual information.
In performing business analysis, large amounts of information and complex
connections between contexts, stakeholders, needs, solutions, changes, and
value are communicated. Visuals represent this information and its complexities,
allowing stakeholders and audiences to learn more quickly, process the
information, and connect points from each of their contexts.
Visual thinking also allows the audience to engage and connect concepts more
quickly and freely into their context, as well as understand and appreciate others’
contexts more clearly.
.3 Effectiveness Measures
Measures of effective visual thinking include:
• complex information is communicated in a visual model which is
understandable by stakeholders,
• visuals allow for comparisons, pattern finding, and idea mapping with
participants,
• productivity increases due to increased learning, quick memory, and follow
through from effective visuals,
• stakeholders are engaged at a deeper level than with text alone, and
• stakeholders understand critical information which may have been missed if
presented in textual content alone.



Behavioural Characteristics
Underlying Competencies
194
9.2
Behavioural Characteristics
Behavioural characteristics are not unique to business analysis but they have been
found to increase personal effectiveness in the practice of business analysis. These
characteristics exist at the core of every business analyst’s skill set. Each of the
behavioural characteristics described here can impact the outcome of the
practitioner's efforts.
The core competencies of behavioural characteristics focus on the skills and
behaviours that allow a business analyst to gain the trust and respect of
stakeholders. Business analysts do this by consistently acting in an ethical manner,
completing tasks on time and to expectations, efficiently delivering quality results,
and demonstrating adaptability to changing needs and circumstances.
Behavioural Characteristics core competencies include:
• Ethics (p. 194),
• Personal Accountability (p. 195),
• Trustworthiness (p. 195),
• Organization and Time Management (p. 196), and
• Adaptability (p. 197).
9.2.1
Ethics
.1 Purpose
Behaving ethically and thinking of ethical impacts on others allows business
analysts to earn the respect of the stakeholders. The ability to recognize when a
proposed solution or requirement may present ethical difficulties to an
organization or its stakeholders is an important consideration that business
analysts can use to help reduce exposure to risk.
.2 Definition
Ethics require an understanding and focus on fairness, consideration, and moral
behaviour through business analysis activities and relationships. Ethical behaviour
includes consideration of the impact that a proposed solution can have on all
stakeholder groups and working to ensure that those groups are treated as fairly
as possible. Fair treatment does not require that the outcome be beneficial to a
particular stakeholder group, but it does require that the affected stakeholders
understand the reasons for decisions. Awareness of ethical issues allows business
analysts to identify when ethical dilemmas occur and recommend resolutions to
these dilemmas.
.3 Effectiveness Measures
Measures of effective ethical behaviour include:
• prompt identification and resolution of ethical dilemmas,
• feedback from stakeholders confirming they feel decisions and actions are
transparent and fair,



Underlying Competencies
Behavioural Characteristics
195
• decisions made with consideration of the interests of all stakeholders,
• reasoning for decisions that is clearly articulated and understood,
• full and prompt disclosure of potential conflicts of interest, and
• honesty regarding one's abilities, the performance of one's work, and
accepting responsibility for failures or errors.
9.2.2
Personal Accountability
.1 Purpose
Personal accountability is important for a business analyst because it ensures
business analysis tasks are completed on time and to the expectations of
colleagues and stakeholders. It enables the business analyst to establish credibility
by ensuring that business analysis efforts meet the needs of the business.
.2 Description
Personal accountability includes effectively planning business analysis work to
achieve targets and goals, and ensuring that value delivered is aligned with
business needs. It involves chasing down all leads and loose ends to fully satisfy
the stakeholder’s needs. Following through on and fully completing business
analysis tasks produces complete, accurate, and relevant solutions traceable to a
need. Business analysts take responsibility for identifying and escalating risks and
issues. They also ensure that decision makers have the appropriate information in
order to assess impact.
.3 Effectiveness Measures
Measures of effective personal accountability include:
• work effort is planned and easily articulated to others,
• work is completed as planned or re-planned with sufficient reasoning and
lead time,
• status of both planned and unplanned work is known,
• stakeholders feel that work is organized,
• risks and issues are identified and appropriately acted on,
• completely traceable requirements are delivered on time, and stakeholder
needs are met.
9.2.3
Trustworthiness
.1 Purpose
Earning the trust of stakeholders helps business analysts elicit business analysis
information around sensitive issues and enables them to help stakeholders have
confidence that their recommendations will be evaluated properly and fairly.



Behavioural Characteristics
Underlying Competencies
196
.2 Description
Trustworthiness is the perception that one is worthy of trust. A business analyst
being considered trustworthy may offset the natural fear of change experienced
by many stakeholders.
Several factors can contribute to being considered trustworthy:
• intentionally and consistently completing tasks and deliverables on time,
within budget, and achieving expected results so that colleagues and
stakeholders consider the business analyst's behaviour dependable and
diligent,
• presenting a consistent attitude of confidence, so that colleagues and
stakeholders consider the business analyst's demeanor as strong,
• acting in an honest and straightforward manner, addressing conflict and
concerns immediately so that colleagues and stakeholders consider the
business analyst's morals as being honest and transparent, and
• maintaining a consistent schedule over a long period of time so that
colleagues and stakeholders consider the business analyst's availability
predictable and reliable.
.3 Effectiveness Measures
Measures of effective trustworthiness include:
• stakeholders involve the business analyst in discussions and decision
making,
• stakeholders bring issues and concerns to the business analyst,
• stakeholders are willing to discuss difficult or controversial topics with the
business analyst,
• stakeholders do not blame the business analyst when problems occur,
• stakeholders respect the business analyst's ideas and referrals, and
• stakeholders respond to the business analyst's referrals with positive
feedback.
9.2.4
Organization and Time Management
.1 Purpose
Organization and time management skills help business analysts perform tasks
effectively and use work time efficiently.
.2 Description
Organization and time management involves the ability to prioritize tasks,
perform them efficiently, and manage time effectively. Business analysts are
constantly acquiring and accumulating significant quantities of information, and



Underlying Competencies
Behavioural Characteristics
197
this information must be organized and stored in an efficient manner so that it
can be used and reused at a later date. Business analysts must also be able to
differentiate important information that should be retained from less important
information.
Effective time management requires the ability to prioritize tasks and deadlines.
Techniques of organization include establishing short- and long-term goals,
action plans, prioritizing tasks, and utilizing a checklist. Techniques for effective
time management include establishing time limits on non-critical tasks, focusing
more time on high risk and priority tasks, setting aside focus time, and managing
potential interruptions.
.3 Effectiveness Measures
Measures of effective organization and time management include:
• the ability to produce deliverables in a timely manner,
• stakeholders feel that the business analyst focuses on the correct tasks at
the right time,
• schedule of work effort and deadlines is managed and communicated to
stakeholders,
• stakeholders feel their time in meetings and in reading communications is
well spent,
• complete preparation for meetings, interviews, and requirements
workshops,
• relevant business analysis information is captured, organized, and
documented,
• adherence to the project schedule and the meeting of deadlines,
• provides accurate, thorough, and concise information in a logical manner
which is understood by stakeholders, and
• maintains up-to-date information on the status of each work item and all
outstanding work.
9.2.5
Adaptability
.1 Purpose
Business analysts frequently work in rapidly changing environments and with a
variety of stakeholders. They adjust their behavioural style and method of
approach to increase their effectiveness when interacting with different
stakeholders, organizations, and situations.
.2 Definition
Adaptability is the ability to change techniques, style, methods, and approach. By
demonstrating a willingness to interact with and complete tasks in a manner



Behavioural Characteristics
Underlying Competencies
198
preferable to the stakeholders, business analysts can maximize the quality of
service delivered and more efficiently help the organization achieve its goals and
objectives. Having the curiosity to learn what others need and possessing the
courage to try a different behaviour is adapting to situations and context.
Business analysts sometimes have to modify the way they interact with
stakeholders, such as the way they conduct interviews or the way they facilitate
workshops. Different stakeholders have different levels of comfort with
techniques that are in the business analysis tool kit. Some stakeholders are more
visual and respond better to information that is represented visually in models,
diagrams, and pictures. Other stakeholders are more verbal and prefer textual
descriptions. Being able to determine which techniques will work and which will
not, and then adapt accordingly increases the likelihood of a successful
interaction.
In the event that the goals and objectives of the organization change, business
analysts respond by accepting the changes and adapting to a new mandate.
Similarly, when circumstances arise or unanticipated problems occur, business
analysts adapt by altering their plans and identifying options that can be used to
deliver maximum value. The business analyst adapts when the business or
stakeholder needs change, or when the context of the goal or the objective
changes. When the need itself changes, the business analyst adapts by altering
the plans and the approach in order to ensure that value is provided and delivered
as part of the solution.
.3 Effectiveness Measures
Measures of effective adaptability include:
• demonstrating the courage to act differently from others,
• adapting to changing conditions and environments,
• valuing and considering other points of view and approaches,
• demonstrating a positive attitude in the face of ambiguity and change,
• demonstrating a willingness to learn new methods, procedures, or
techniques in order to accomplish goals and objectives,
• changing behaviour to perform effectively under changing or unclear
conditions,
• acquiring and applying new information and skills to address new
challenges,
• acceptance of having changes made to tasks, roles and project assignments
as organizational realities change,
• altering interpersonal style to highly diverse individuals and groups in a
range of situations, and
• evaluating what worked, what did not, and what could be done differently
next time.



Underlying Competencies
Business Knowledge
199
9.3
Business Knowledge
Business knowledge is required for the business analyst to perform effectively
within their business, industry, organization, solution, and methodology. Business
knowledge enables the business analyst to better understand the overarching
concepts that govern the structure, benefits, and value of the situation as it
relates to a change or a need.
Business Knowledge underlying competencies include:
• Business Acumen (p. 199),
• Industry Knowledge (p. 200),
• Organization Knowledge (p. 201),
• Solution Knowledge (p. 202), and
• Methodology Knowledge (p. 202).
9.3.1
Business Acumen
.1 Purpose
Business analysis requires an understanding of fundamental business principles
and best practices in order to ensure they are considered as solutions are
reviewed.
.2 Description
Business acumen is the ability to understand business needs using experience and
knowledge obtained from other situations. Organizations frequently share similar
practices, such as legal and regulatory requirements, finance, logistics, sales,
marketing, supply chain management, human resources, and technology.
Business acumen is the ability to understand and apply the knowledge based on
these commonalities within differing situations.
Understanding how other organizations have solved challenges may be useful
when seeking possible solutions. Being aware of the experiences or challenges
encountered in the past may assist a business analyst in determining which
information may be applicable to the current situation. Factors that may cause
differences in practices can include industry, location, size of organization,
culture, and the maturity of the organization.
.3 Effectiveness Measures
Measures of effective business acumen include:
• demonstrating the ability to recognize potential limitations and
opportunities,
• demonstrating the ability to recognize when changes to a situation may
require a change in the direction of an initiative or effort,



Business Knowledge
Underlying Competencies
200
• understanding the risks involved and the ability to make decisions on
managing risks,
• demonstrating the ability to recognize an opportunity to decrease expenses
and increase profits, and
• understanding the options available to address emerging changes in the
situation.
9.3.2
Industry Knowledge
.1 Purpose
Industry knowledge provides the business analyst with an understanding of
current practices and activities within an industry, and similar processes across
industries.
.2 Description
Industry knowledge is an understanding of:
• current trends,
• market forces,
• market drivers,
• key processes,
• services,
• products,
• definitions,
• customer segments,
• suppliers,
• practices,
• regulations, and
• other factors that impact or are
impacted by the industry and
related industries.
Industry knowledge is also an understanding of how a company is positioned
within an industry, and its impacts and dependencies, in regards to the market
and human resources.
When developing knowledge about a particular industry, competitor, or company
the following set of questions can provide guidance:
• Who are the top leaders in the industry?
• Which organizations promote or regulate the industry?
• What are the benefits of being involved with these organizations?
• Who is creating publicity releases, participating in conventions, and
delivering marketing materials?
• What are the comparisons of products and services?
• What are the satisfaction indicators/benchmarking projects that are
applicable?
• What are the suppliers, practices, equipment and tools used by each
company, and why do they use them?



Underlying Competencies
Business Knowledge
201
• What are the potential impacts of weather, political unrest, or natural
disasters?
• Who are the target customers and are they the same for the competition?
• What impacts the seasonal cycles for production, marketing, and sales?
Does it impact staffing or require changes in processes?
.3 Effectiveness Measures
Measures of effective industry knowledge include:
• being aware of activities within both the enterprise and the broader
industry,
• having knowledge of major competitors and partners,
• the ability to identify key trends shaping the industry,
• being familiar with the largest customer segments,
• having knowledge of common products and product types,
• being knowledgeable of sources of information about the industry,
including relevant trade organizations or journals,
• understanding of industry specific terms, standards, processes and
methodologies, and
• understanding of the industry regulatory environment.
9.3.3
Organization Knowledge
.1 Purpose
Organization knowledge provides an understanding of the management
structure and business architecture of the enterprise.
.2 Definition
Organization knowledge includes an understanding of how the enterprise
generates profits, accomplishes its goals, its organizational structure, the
relationships that exist between business units, and the persons who occupy key
stakeholder positions. Organization knowledge also includes understanding the
organization's formal and informal communication channels as well as an
awareness of the internal politics that influence decision making.
.3 Effectiveness Measures
Measures of effective organization knowledge include:
• the ability to act according to informal and formal communications and
authority channels,
• understanding of terminology or jargon used in the organization,
• understanding of the products or services offered by the organization,



Business Knowledge
Underlying Competencies
202
• the ability to identify subject matter experts (SMEs) in the organization, and
• the ability to navigate organizational relationships and politics.
9.3.4
Solution Knowledge
.1 Purpose
Solution knowledge allows business analysts to leverage their understanding of
existing departments, environments, or technology to efficiently identify the most
effective means of implementing a change.
.2 Definition
When the business analysis effort involves improving an existing solution,
business analysts apply knowledge and experience from the previous work on the
solution. Familiarity with the range of commercially available solutions or
suppliers can assist with the identification of possible alternatives. The business
analyst may leverage knowledge gained from prior experiences to expedite the
discovery of potential changes through elicitation or in-depth analysis.
.3 Effectiveness Measures
Measures of effective solution knowledge include:
• reduced time or cost to implement a required change,
• shortened time on requirements analysis and/or solution design,
• understanding when a larger change is, or is not, justified based on
business benefit, and
• understanding how additional capabilities that are present, but not
currently used, can be deployed to provide value.
9.3.5
Methodology Knowledge
.1 Purpose
Understanding the methodologies used by the organization provides the business
analyst with information regarding context, dependencies, opportunities, and
constraints used when developing a business analysis approach.
.2 Description
Methodologies determine the timing (big steps or small increments), the
approach, the role of those involved, the accepted risk level, and other aspects of
how a change is approached and managed. Organizations adopt or create their
own methodologies to fit varying levels of culture, maturity, adaptability, risk,
uncertainty, and governance.
Knowledge regarding a variety of methodologies allows the business analyst to
quickly adapt to, and perform in, new environments.



Underlying Competencies
Communication Skills
203
.3 Effectiveness Measures
Measures of effective methodology knowledge include:
• the ability to adapt to changes in methodologies,
• the willingness to use or learn a new methodology,
• the successful integration of business analysis tasks and techniques to
support the current methodology,
• familiarity with the terms, tools, and techniques prescribed by a
methodology, and
• the ability to play multiple roles within activities prescribed by a
methodology.
9.4
Communication Skills
Communication is the act of a sender conveying information to a receiver in a
method which delivers the meaning the sender intended. Active listening skills
help to deepen understanding and trust between the sender and the receiver.
Effective communication benefits all stakeholders.
Communication may be accomplished using a variety of delivery methods: verbal,
non-verbal, physical, and written. Most communication methods deal with
words, while some methods deal with movements and expressions. Words,
gestures, and phrases may have different meanings to different individuals.
Effective communication involves both the sender and receiver possessing the
same understanding of the information being communicated. A shared glossary
of terms and clear goals are effective tools to avoid misunderstandings and the
resulting complications.
Effective communication includes adapting communication styles and techniques
to the knowledge level and communication styles of recipients. Effective
communicators understand how tone, body language, and context change the
meaning of words. Gaining an understanding of the terms and concepts (prior to
the exchange) can provide fruitful benefits.
Planning effective communication includes the sender reviewing the information
that is known about the receiver. Differences between the sender and the
receiver, such as native language, culture, motivations, priorities, communication,
learning, and thinking styles may call for specific communication methods. Each
piece of information must be carefully crafted and packaged to ensure it is clear
and understood.
When planning to communicate information, the following considerations may
be helpful:
• consider what the receiver knows or does not know,
• structure the information in a logical, comprehensible manner,
• determine how to best present the information to convey the intended



Communication Skills
Underlying Competencies
204
meanings (for example, using visual aids, graphs, diagrams, or bullet
points), and
• understand the expectations of the recipients.
Communication Skills core competencies include:
• Verbal Communication (p. 204),
• Non-Verbal Communication (p. 205),
• Written Communication (p. 205), and
• Listening (p. 206).
9.4.1
Verbal Communication
.1 Purpose
Business analysts use verbal communication to convey ideas, concepts, facts, and
opinions to a variety of stakeholders.
.2 Description
Verbal communication uses spoken words to convey information from the sender
to the receiver. Verbal communication skills are used to express business analysis
information, ideas, concepts, facts, and opinions. It allows for the efficient
transfer of information, including emotional and other non-verbal cues. It can be
paired with both written and non-verbal communication.
Verbal communication deals specifically with the sender's choice of words and
the tone of voice. When the receiver is able to see the sender, the sender's non-
verbal communication impacts the meaning of the message being understood by
the receiver. When the sender is able to see the receiver, the receiver is providing
a response and both the sender and receiver are engaged in a dialogue, even
though the receiver may not be speaking verbally. Monitoring the receiver's non-
verbal communication allows the sender to consider adapting the message for
the receiver.
Having an understanding of the tone of the communication and how it can
positively or negatively influence the listener allows the business analyst to more
effectively communicate verbally. Effective verbal communication skills include
the ability to make one's meaning understood. The sender should partner verbal
communication with active listening to ensure that information presented is
being understood by the receiver.
.3 Effectiveness Measures
Measures of effective verbal communication include:
• restating concepts to ensure all stakeholders clearly understand the same
information,
• assisting conversations to reach productive conclusions,



Underlying Competencies
Communication Skills
205
• delivering effective presentations by designing and positioning content and
objectives appropriately, and
• communicating an issue's important points in a calm and rational manner,
and presenting solution options.
9.4.2
Non-Verbal Communication
.1 Purpose
Non-verbal communication skills enable the effective sending and receiving of
messages through—but not limited to—body movement, posture, facial
expressions, gestures, and eye contact.
.2 Definition
Communication is typically focused upon words that are written or spoken. Non-
verbal communication, however, is believed to convey much more meaning than
words alone. Moods, attitudes, and feelings impact body movement and facial
expressions. Non-verbal communication begins immediately when one person is
able to see another. The effective use of non-verbal communication skills can
present a trustworthy, confident, and capable demeanor. Being aware of non-
verbal communication provides the opportunity to be aware and address the
feelings of others that are not expressed verbally.
Observing gestures or expressions cannot provide a complete understanding of
the message being expressed by these non-verbal cues. These cues are indicators
of the feelings and intent of the communicator. For example, when a
stakeholder's non-verbal communication does not agree with their verbal
message, the business analyst may want to explore the conversation further to
uncover the source of this disagreement.
.3 Effectiveness Measures
Measures of effective non-verbal communication include:
• being aware of body language in others, but not assuming a complete
understanding through non-verbal communication,
• intentional awareness of personal non-verbal communication,
• improving trust and communication as a result of non-verbal
communication, and
• effectively addressing and resolving situations when a stakeholder's non-
verbal communication does not agree with their verbal message.
9.4.3
Written Communication
.1 Purpose
Business analysts use written communication to to convey ideas, concepts, facts,
and opinions to variety of stakeholders.



Communication Skills
Underlying Competencies
206
.2 Definition
Written communication is the practice of using text, symbols, models (formal or
informal), and sketches to convey and share information. An understanding of
the audience is beneficial to effectively use written communication. Presenting
information and ideas requires selecting the correct words so the audience will
understand the intended meaning. Written communication has the added
challenge of presenting information at a time or place that is remote from the
time and place it was created.
Effective written communication requires a broad vocabulary, strong grasp of
grammar and style, and an understanding of the terms which will be understood
by the audience. Written communication has the potential to convey a great deal
of information; however, conveying information effectively is a skill which must
be developed.
.3 Effectiveness Measures
Measures of effective written communication include:
• adjusting the style of writing for the needs of the audience,
• proper use of grammar and style,
• choosing words the audience will understand the intended meaning of, and
• ability of the reader to paraphrase and describe the content of the written
communication.
9.4.4
Listening
.1 Purpose
Effective listening allows the business analyst to accurately understand
information that is communicated verbally.
.2 Definition
Listening is the process of not just hearing words but understanding their
meaning in context. By exhibiting effective listening skills, business analysts not
only have a greater opportunity to accurately understand what is being
communicated, but also to demonstrate that they think what the speaker is
saying is important.
Active listening involves both listening and interpreting what the other person is
trying to communicate beyond the words used in order to understand the
essence of the message. Active listening includes summarizing and repeating
what was stated in different terms in order to ensure that both the listener and
the speaker have the same understanding.
.3 Effectiveness Measures
Measures of effective listening include:
• giving the speaker undivided attention,



Underlying Competencies
Interaction Skills
207
• acknowledging the speaker with verbal or non-verbal encouragement,
• providing feedback to the person or the group that is speaking to ensure
there is an understanding, and
• using active listening skills by deferring judgment and responding
appropriately.
9.5
Interaction Skills
Interaction skills are represented by the business analyst's ability to relate,
cooperate, and communicate with different kinds of people including executives,
sponsors, colleagues, team members, developers, vendors, learning and
development professionals, end users, customers, and subject matter experts
(SMEs).
Business analysts are uniquely positioned to facilitate stakeholder
communication, provide leadership, encourage comprehension of solution value,
and promote stakeholder support of the proposed changes.
Interaction Skills core competencies include:
• Facilitation (p. 207),
• Leadership and Influencing (p. 208),
• Teamwork (p. 209),
• Negotiation and Conflict Resolution (p. 210), and
• Teaching (p. 210).
9.5.1
Facilitation
.1 Purpose
Business analysts facilitate interactions between stakeholders in order to help
them make a decision, solve a problem, exchange ideas and information, or reach
an agreement regarding the priority and the nature of requirements. The business
analyst may also facilitate interactions between stakeholders for the purposes of
negotiation and conflict resolution (as discussed in Negotiation and Conflict
Resolution (p. 210)).
.2 Definition
Facilitation is the skill of moderating discussions within a group in order to enable
all participants to effectively articulate their views on a topic under discussion,
and to ensure that participants in the discussion are able to recognize and
appreciate the differing points of view that are articulated.



Interaction Skills
Underlying Competencies
208
.3 Effectiveness Measures
Measures of effective facilitation include:
• making it clear to the participants that the facilitator is a third party to the
process and not a decision maker nor the owner of the topic,
• encouraging participation from all attendees,
• remaining neutral and not taking sides, but at the same time being
impartial and intervening when required in order to make suggestions and
offer insights,
• establishing ground rules such as being open to suggestions, building on
what is there, not dismissing ideas, and allowing others to speak and
express themselves,
• ensuring that participants in a discussion correctly understand each other's
positions,
• using meeting management skills and tools to keep discussions focused
and organized,
• preventing discussions from being sidetracked onto irrelevant topics, and
• understanding and considering all parties’ interests, motivations, and
objectives.
9.5.2
Leadership and Influencing
.1 Purpose
Business analysts use leadership and influencing skills when guiding stakeholders
during the investigation of business analysis information and solution options.
They build consensus and encourage stakeholder support and collaboration
during change.
.2 Definition
Leadership and influencing involves motivating people to act in ways that enable
them to work together to achieve shared goals and objectives. Understanding the
individual motives, needs, and capabilities of each stakeholder and how those can
be effectively channeled assists business analysts in meeting the shared objectives
of the organization. The business analyst’s responsibility for defining, analyzing,
and communicating business analysis information provides opportunities for
leadership and influencing, whether or not there are people formally reporting to
the business analyst.
.3 Effectiveness Measures
Measures of effective leadership and influencing include:
• reduced resistance to necessary changes,
• articulation of a clear and inspiring vision of a desired future state,
• success in inspiring others to turn vision into action,



Underlying Competencies
Interaction Skills
209
• influence on stakeholders to understand mutual interests,
• effective use of collaboration techniques to influence others,
• influence on stakeholders to consider broader objectives over personal
motivations, and
• re-framing issues so alternate perspectives can be understood and
accommodated to influence stakeholders towards shared goals.
9.5.3
Teamwork
.1 Purpose
Teamwork skills allow business analysts to work productively with team members,
stakeholders, and any other vested partners so that solutions can be effectively
developed and implemented.
.2 Definition
Business analysts often work as part of a team with other business analysts,
project managers, stakeholders, and subject matter experts (SMEs). Relationships
with people in those roles are a critical part of the success of any project or
enterprise. It is important for the business analyst to understand how a team is
formed and how it functions. Recognizing team dynamics and how they play a
part as the team progresses through various stages of a project is also crucial.
Knowing and adapting to how and when a team is progressing through a
project's life cycle can lower the negative influences that impact a team.
Building and maintaining trust of teammates contributes to the integrity of the
team as a whole and helps the team perform at its fullest capacity. When team
members actively foster an environment for positive and trusting team dynamics,
difficult decisions and challenges become less complicated.
Team conflict is common. If handled well, the resolution of conflict can benefit
the team. Resolving conflict requires the team to focus on examining the
positions, assumptions, observations, and expectations of all team members.
Working through such problems can have the beneficial effect of strengthening
the foundation of the analysis and the solution.
.3 Effectiveness Measures
Measures of effective teamwork include:
• fostering a collaborative working environment,
• effectively resolving conflict,
• developing trust among team members,
• support among the team for shared high standards of achievement, and
• promoting a shared sense of ownership of the team goals.



Interaction Skills
Underlying Competencies
210
9.5.4
Negotiation and Conflict Resolution
.1 Purpose
Business analysts occasionally mediate negotiations between stakeholders in
order to reach a common understanding or an agreement. During this process,
business analysts help resolve conflicts and differences of opinion with the intent
of maintaining and strengthening working relationships among stakeholders and
team members.
.2 Definition
Negotiation and conflict resolution involves mediating discussions between
participants in order to help them recognize that there are differing views on the
topic, resolve differences, and reach conclusions that have the agreement of all
participants. Successful negotiation and conflict resolution includes identifying
the underlying interests of the parties, distinguishing those interests from their
stated positions, and helping the parties identify solutions that satisfy those
underlying interests. The business analyst accomplishes this while ensuring that
the outcome of the resolution aligns with the overall solution and the business
needs.
.3 Effectiveness Measures
Measures of effective negotiation and conflict resolution include:
• a planned approach to ensure that the negotiation takes into account the
tone of voice, the conveyed attitude, the methods used, and the concern
for the other side’s feelings and needs,
• the ability to recognize that the needs of the parties are not always in
opposition and that it is often possible to satisfy both parties without either
side losing,
• an objective approach to ensure the problem is separated from the person
so that the real issues are debated without damaging working relationships,
and
• the ability to recognize that effective negotiation and conflict resolution are
not always achieved in a single autonomous meeting, and that sometimes
several meetings are required in order to achieve the stated goals.
9.5.5
Teaching
.1 Purpose
Teaching skills help business analysts effectively communicate business analysis
information, concepts, ideas, and issues. They also help ensure that information is
understood and retained by stakeholders.
.2 Definition
Teaching is the process of leading others to gain knowledge. Business analysts are
responsible for confirming that the information communicated has been



Underlying Competencies
Tools and Technology
211
understood by stakeholders. Business analysts lead stakeholders to discover clarity
in ambiguity by helping them learn about the contexts and value of the needs
being investigated. This requires teaching skills in selecting the most appropriate
visual, verbal, written, and kinesthetic teaching approaches according to the
information or techniques being taught. The intent is to draw out stakeholder
engagement and collaborative learning to gain clarity. Business analysts
frequently elicit and learn new information, and then teach this information to
stakeholders in a meaningful way.
.3 Effectiveness Measures
Measures of effective teaching include:
• utilizing different methods to communicate information to be learned by
stakeholders,
• discovering new information through high levels of stakeholder
engagement,
• validating that audiences have a clear understanding of the key messages
that are intended to be learned, and
• verifying that the stakeholders can demonstrate the new knowledge, facts,
concepts, and ideas.
9.6
Tools and Technology
Business analysts use a variety of software applications to support communication
and collaboration, create and maintain requirements artifacts, model concepts,
track issues, and increase overall productivity.
Requirements documentation is often developed using word processing tools,
while the process of developing business requirements may require the use of
prototyping and simulation tools, as well as specialized tools for modelling and
diagramming.
Requirements management technologies support requirements workflow,
approvals, baselining, and change control. These technologies can also support
the traceability between requirements and assist in determining the impact of
changes to requirements.
Interacting with the stakeholders and team members may require the use of
communication and collaboration tools, as well as presentation software in order
to showcase ideas and generate discussion among stakeholders and team
members.
Business Analysis Tools and Technology core competencies include:
• Office Productivity Tools and Technology (p. 212),
• Business Analysis Tools and Technology (p. 213), and
• Communication Tools and Technology (p. 215).



Tools and Technology
Underlying Competencies
212
9.6.1
Office Productivity Tools and Technology
.1 Purpose
Business analysts use office productivity tools and technology to document and
track information and artifacts.
.2 Definition
Office productivity tools and technology provide business analysts with the ability
to organize, dissect, manipulate, understand, and communicate information
clearly. Utilizing these tools requires becoming familiar with available resources.
Understanding one software program may provide insights into comparable
abilities or operations in similar programs. Additionally, some programs are
designed to provide additional tools to other programs or exchange information,
such as e-mail or programs that can import/export files. Many organizations
utilize these tools to study, store, and distribute information.
Office productivity tools and technology include the following:
• Word processing and presentation programs: provide the ability to present
information in the form of a letter, newspaper, poster, research paper, slide
presentation, or animations. Word processors are commonly used to develop
and maintain requirements documents, allowing a great deal of control over
their formatting and presentation. Standard requirements documentation
templates are widely available for word processors. Most word processing tools
have a limited capability to track changes and record comments, and are not
designed for collaborative authoring; however, there are cloud solutions that
provide collaborative functionality.
• Presentation software: serves in the creation of training materials or to
present information to stimulate discussion among stakeholders. Some of these
applications can be used in a very limited way to capture requirements or create
a basic prototype.
• Spreadsheets: allow mathematical and logical manipulation. They are often
used to maintain lists (such as atomic requirements, features, actions, issues, or
defects). They are also used to capture and perform basic manipulation of
numeric data. They can support decision analysis, and are very effective at
summarizing complex scenarios. They support limited change tracking and can
be shared among multiple users in the same way as a word processing
document.
• Communication tools (e-mail and instant messaging programs): provide
the means to communicate with stakeholders who are remotely located, who
cannot respond to queries immediately, or who may need a longer-term record
of a discussion. They are generally available to almost all stakeholders and are
very easy to use. However, they are generally not effective for long-term
storage or retention of information. Their primary use is to facilitate
communication over time or distance.
• Collaboration and knowledge management tools: support the capturing
of knowledge distributed throughout an organization and make it as widely



Underlying Competencies
Tools and Technology
213
available as possible. They allow documents to be accessible by an entire team,
and facilitate collaboration. They also enable multiple users to work on a
document simultaneously, and generally support comments and discussion
about document content. These tools may take the form of a document
repository (which integrates with office productivity software), wikis (which
allow easy creation and linking of web pages), discussion forums, cloud
services, or other web-based tools.
• Hardware: allows for the replication and distribution of information to
facilitate communication with stakeholders. Tools such as printers and digital
projectors are often used to translate digital information generated on a
computer into physical information for ease of use. Photocopiers and scanners
copy physical documents and can provide the ability to share them
electronically.
.3 Effectiveness Measures
Measures of effective office productivity tools and technology include:
• increased efficiencies and streamlining of processes by exploring features
and functions of tools,
• awareness of available tools, their operation, and abilities,
• the ability to determine the tool that will best meet stakeholder needs, and
• the ability to clearly communicate the major features of available tools.
9.6.2
Business Analysis Tools and Technology
.1 Purpose
Business analysts use a variety of tools and technology to model, document, and
manage outputs of business analysis activities and deliverables to stakeholders.
.2 Definition
Tools that are specific to the field of business analysis provide specialized
capabilities in:
• modelling,
• diagramming,
• documenting,
• analyzing and mapping requirements,
• identifying relationships between requirements,
• tracking and storing requirements artifacts, and
• communicating with stakeholders.
Some business analysis tools and technologies focus solely on a single business
analysis activity and some integrate multiple business analysis functions into a
single tool. Tools specifically designed for business analysis may include such



Tools and Technology
Underlying Competencies
214
functionality as modelling, requirements management, issue tracking,
prototyping and simulation, computer aided software engineering (CASE), and
survey engines.
Modelling tools can provide functionality that assists business analysts with a
number of modelling related tasks, including:
• creating models and visuals to help align stakeholders and outline the
relationship of needs, entities, requirements, stakeholders, and context,
• tracing visuals to business rules, text requirements, scope statements, scope
visuals, data requirements, product needs, and other requirements context
and information, and
• creating an executable for a proprietary engine in order to execute the
model or generate an application code which can be enhanced by a
developer.
These tools frequently validate compliance with the notation. Some modelling
tools support the creation of executable models, such as business process
management systems (which allow for the creation of executable process models)
and business rules management systems (which allow for the evaluation of
captured business rules).
Requirements management technologies can provide functionality that assists
business analysts with a number of requirements management related tasks
including:
• requirements workflow including baselining, approvals and sign-off,
change control, and implementation status,
• traceability including backwards traceability, forwards traceability,
relationships between requirements, and impact analysis of requirements
change,
• configuration management of requirements and requirements artifacts, and
• verifying the quality of requirements through checking for defined
characteristics and relationships.
Issue tracking tools can provide functionality that assists business analysts with a
number of issue tracking related tasks such as:
• tracking requirements risks,
• tracking requirements conflicts and issues, and
• tracking defects.
Prototyping and simulation tools can provide functionality that assists business
analysts with prototyping or simulating the solution or pieces of the solution.
.3 Effectiveness Measures
Measures of effective business analysis tools and technology include:
• the ability to apply an understanding of one tool and other similar tools,



Underlying Competencies
Tools and Technology
215
• being able to identify major tools currently available and describe their
strengths, weaknesses, and how they may be used in any given situation,
• understanding of and the ability to use the major features of the tool,
• ability to select a tool or tools that support organizational processes,
• the ability to use the tools to complete requirements-related activities more
rapidly than otherwise possible, and
• the ability to track changes to the requirements and their impact on the
solution implementation, stakeholders, and value.
9.6.3
Communication Tools and Technology
.1 Purpose
Business analysts use communication tools and technology to perform business
analysis activities, manage teams, and collaborate with stakeholders.
.2 Definition
Communication tools are used to plan and complete tasks related to
conversational interactions and collaborative interactions. Communication tools
allow business analysts to work with virtual and co-located teams.
Understanding the options available with these tools—and knowing how to use
various communications tools to complete tasks and utilize various techniques in
a variety of collaboration environments—can enable more efficient and accurate
communication and more effective decision making. Business analysts select the
appropriate tool and technology for the situation and stakeholder group while
balancing cost, risk, and value.
Examples of conversation interaction tools include voice communications, instant
messaging, online chat, e-mail, blogging, and microblogging.
Examples of collaboration tools include video conferencing, electronic white
boarding, wikis, electronic calendars, online brainstorming tools, electronic
decision making, electronic voting, document sharing, and idea sharing.
.3 Effectiveness Measures
Measures of effective communication tools and technology include:
• the selection of appropriate and effective tools for the audience and
purpose,
• effectively choosing when to use communication technology and when not
to,
• the ability to identify tools to meet communication needs, and
• understanding of and the ability to use features of the tool.



Tools and Technology
Underlying Competencies
216



217
10
Techniques
The Techniques chapter provides a high-level overview of the techniques
referenced in the Knowledge Areas of the BABOK® Guide. Techniques are
methods business analysts use to perform business analysis tasks.
The techniques described in the BABOK® Guide are intended to cover the most
common and widespread techniques practiced within the business analysis
community. Business analysts apply their experience and judgment in determining
which techniques are appropriate to a given situation and how to apply each
technique. This may include techniques that are not described in the BABOK®
Guide. As the practice of business analysis evolves, techniques will be added,
changed, or removed from future iterations of the BABOK® Guide.
In a number of cases, a set of conceptually similar approaches have been grouped
into a single technique. Any approach within a technique may be used
individually or in combination to accomplish the technique's purpose.
10.1
Acceptance and Evaluation Criteria
10.1.1
Purpose
Acceptance criteria are used to define the requirements, outcomes, or conditions
that must be met in order for a solution to be considered acceptable to key
stakeholders. Evaluation criteria are the measures used to assess a set of
requirements in order to choose between multiple solutions.



Acceptance and Evaluation Criteria
Techniques
218
10.1.2
Description
Acceptance and evaluation criteria define measures of value attributes to be used
for assessing and comparing solutions and alternative designs. Measurable and
testable criteria allow for the objective and consistent assessment of solutions and
designs. The Acceptance and Evaluation Criteria technique can apply at all levels
of a project, from high-level to a more detailed level.
Acceptance criteria describe the minimum set of requirements that must be met
in order for a particular solution to be worth implementing. They may be used to
determine if a solution or solution component can meet a requirement.
Acceptance criteria are typically used when only one possible solution is being
evaluated, and are generally expressed as a pass or fail.
Evaluation criteria define a set of measurements which allow for ranking of
solutions and alternative designs according to their value for stakeholders. Each
evaluation criterion represents a continuous or discrete scale for measuring a
specific solution attribute such as cost, performance, usability, and how well the
functionality represents the stakeholders’ needs. Attributes that cannot be
measured directly are evaluated using expert judgment or various scoring
techniques.
Both evaluation and acceptance criteria may be defined with the same value
attributes. When evaluating various solutions, the solutions with lower costs and
better performance may be rated higher. When accepting a solution, the criteria
are written using minimum performance requirements and maximum cost limits
in contractual agreements and user acceptance tests.
10.1.3
Elements
.1 Value Attributes
Value attributes are the characteristics of a solution that determine or
substantially influence its value for stakeholders. They represent a meaningful and
agreed-upon decomposition of the value proposition into its constituent parts,
which can be described as qualities that the solution should either possess or
avoid.
Examples of value attributes include:
• ability to provide specific information,
• ability to perform or support specific operations,
• performance and responsiveness characteristics,
• applicability of the solution in specific situations and contexts,
• availability of specific features and capabilities, and
• usability, security, scalability, and reliability.



Techniques
Acceptance and Evaluation Criteria
219
Basing acceptance and evaluation criteria on value attributes ensures that they are
valid and relevant to stakeholder needs and should be considered when accepting
and evaluating the solution. Business analysts ensure that the definition of all
value attributes are agreed upon by all stakeholders. Business analysts may design
tools and instructions for performing the assessment as well as for recording and
processing its results.
Figure 10.1.1: Acceptance and Evaluation Criteria
.2 Assessment
In order to assess a solution against acceptance or evaluation criteria, it must be
constructed in a measurable format.
Testability
Acceptance criteria are expressed in a testable form. This may require breaking
requirements down into an atomic form so that test cases can be written to verify
the solution against the criteria. Acceptance criteria are presented in the form of
statements which can be verified as true or false. This is often achieved through
user acceptance testing (UAT).
Measures
Evaluation criteria provide a way to determine if features provide the value
necessary to satisfy stakeholder needs. The criteria are presented as parameters
that can be measured against a continuous or discrete scale. The definition of
each criterion allows the solution to be measured through various methods such
as benchmarking or expert judgment. Defining evaluation criteria may involve
designing tools and instructions for performing the assessment, as well as for
recording and processing its results.
Requirements
Pass or Fail
Solution Value
Ranking
Evaluation
Criteria
Value Attributes:
Cost
Performance
Usability
Functionality
Acceptance
Criteria
Value Attributes:
Cost
Performance
Usability
Functionality
Measure
Solutions
Test
Conduct
User Acceptance
Testing
Define
Measures
Criteria used to
assess value
delivered by
potential solutions
Define
Requirements
Requirements that
must be met in
order for a solution
to be considered
One Solution
Multiple Solutions



Backlog Management
Techniques
220
10.1.4
Usage Considerations
.1 Strengths
• Agile methodologies may require that all requirements be expressed in the form
of testable acceptance criteria.
• Acceptance criteria are necessary when the requirements express contractual
obligations.
• Acceptance criteria provide the ability to assess requirements based on agreed-
upon criteria.
• Evaluation criteria provide the ability to assess diverse needs based on agreed-
upon criteria, such as features, common indicators, local or global benchmarks,
and agreed ratios.
• Evaluation criteria assist in the delivery of expected return on investment (ROI)
or otherwise specified potential value.
• Evaluation criteria helps in defining priorities.
.2 Limitations
• Acceptance criteria may express contractual obligations and as such may be
difficult to change for legal or political reasons.
• Achieving agreement on evaluation criteria for different needs among diverse
stakeholders can be challenging.
10.2
Backlog Management
10.2.1
Purpose
The backlog is used to record, track, and prioritize remaining work items.
10.2.2
Description
A backlog occurs when the volume of work items to be completed exceeds the
capacity to complete them.
Backlog management refers to the planned approach to determine:
• what work items should be formally included in the backlog,
• how to describe the work items,
• how the work items should be tracked,
• how the work items should be periodically reviewed and prioritized in
relation to all other items in the backlog,
• how the work items are eventually selected to be worked on, and
• how the work items are eventually removed from the backlog.



Techniques
Backlog Management
221
In a managed backlog, the items at the top have the highest business value and
the highest priority. These are normally the next items to be selected to be worked
on.
Periodic review of the entire backlog should occur because changes in
stakeholder needs and priorities may necessitate changes to the priority of some
of the backlog items. In many environments, the backlog is reviewed at planned
intervals.
The changes to the number of items in the backlog are regularly monitored. The
root causes for these changes are investigated: a growing backlog could indicate
an increase in demand or a drop in productivity; a declining backlog could
indicate a drop in demand or improvements in the production process.
There may be more than one backlog. For example, one backlog may be used to
manage a global set of items, while a second backlog may be used to manage the
items that are due to be worked on within the very near future.
10.2.3
Elements
.1 Items in the Backlog
Backlog items may be any kind of item which may have work associated with it.
A backlog may contain, but is not limited to, any combination of the following
items:
• use cases,
• user stories,
• functional requirements,
• non-functional requirements,
• designs,
• customer orders,
• risk items,
• change requests,
• defects,
• planned rework,
• maintenance,
• conducting a presentation, or
• completing a document.
An item is added to the backlog if it has value to a stakeholder. There may be one
person with the authority to add new items to the backlog, or there could be a
committee which adds new items based on a consensus. In some cases, the
responsibility for adding new items may be delegated to the business analyst.
There may also be policies and rules which dictate what is to be added and when,
as may be the case with major product defects.
.2 Prioritization
Items in the backlog are prioritized relative to each other. Over time, these
priorities will change as stakeholders’ priorities change, or as dependencies
between backlog items emerge. Rules on how to manage the backlog may also
impact priority.
A multi-phased prioritization approach can also be used. When items are first
added to the backlog, the prioritization may be very broad, using categories such



Backlog Management
Techniques
222
as high, medium, or low. The high priority items tend to be reviewed more
frequently since they are likely candidates for upcoming work. To differentiate
between the high priority items, a more granular approach is used to specify the
relative priority to other high priority items, such as a numerical ranking based on
some measure of value.
.3 Estimation
The level of detail used to describe each backlog item may vary considerably.
Items near the top of the backlog are usually described in more detail, with a
correspondingly accurate estimate about their relative size and complexity that
would help to determine the cost and effort to complete them. When an item is
first added, there may be very little detail included, especially if the item is not
likely to be worked on in the near term.
A minimal amount of work is done on each item while it is on the backlog; just
enough to be able to understand the work involved to complete it. As the work
progresses on other items in the backlog, an individual item’s relative priority may
rise, leading to a need to review it and possibly further elaborate or decompose it
to better understand and estimate its size and complexity.
Feedback from the production process about the cost and effort to complete
earlier items can be used to refine the estimates of items still in the backlog.
.4 Managing Changes to the Backlog
Items make their way to the top of the backlog based on their relative priority to
other items in the backlog. When new or changed requirements are identified,
they are added to the backlog and ordered relative to the other items already
there.
Whenever work capacity becomes available the backlog is reviewed and items are
selected based on the available capacity, dependencies between items, current
understanding of the size, and complexity.
Items are removed from the backlog when they are completed, or if a decision
has been made to not do any more work on them. However, removed items can
be re-added to the backlog for a variety of reasons, including:
• stakeholder needs could change significantly,
• it could be more time-consuming than estimated,
• other priority items could take longer to complete than estimated, or
• the resulting work product might have defects.
10.2.4
Usage Considerations
.1 Strengths
• An effective approach to responding to changing stakeholder needs and
priorities because the next work items selected from the backlog are always



Techniques
Balanced Scorecard
223
aligned with current stakeholder priorities.
• Only items near the top of the backlog are elaborated and estimated in detail;
items near the bottom of the backlog reflect lower priorities and receive less
attention and effort.
• Can be an effective communication vehicle because stakeholders can
understand what items are about to be worked on, what items are scheduled
farther out, and which ones may not be worked on for some time.
.2 Limitations
• Large backlogs may become cumbersome and difficult to manage.
• It takes experience to be able to break down the work to be done into enough
detail for accurate estimation.
• A lack of detail in the items in the backlog can result in lost information over
time.
10.3
Balanced Scorecard
10.3.1
Purpose
The balanced scorecard is used to manage performance in any business model,
organizational structure, or business process.
10.3.2
Description
The balanced scorecard is a strategic planning and management tool used to
measure organizational performance beyond the traditional financial measures. It
is outcome focused and provides a balanced view of an enterprise by
implementing the strategic plan as an active framework of objectives and
performance measures. The underlying premise of the balanced scorecard is that
the drivers of value creation are understood, measured, and optimized in order to
create sustainable performance.
The balanced scorecard is composed of four dimensions:
• Learning and Growth,
• Business Process,
• Customer, and
• Financial.
The balanced scorecard includes tangible objectives, specific measures, and
targeted outcomes derived from an organization's vision and strategy. Balanced
business scorecards can be used at multiple levels within an organization. This
includes at an enterprise-wide level (macro level), departmental or function level,
and even at the level of a project or initiative.



Balanced Scorecard
Techniques
224
Figure 10.3.1: Balanced Scorecard
10.3.3
Elements
.1 Learning and Growth Dimension
The Learning and Growth dimension includes measures regarding employee
training and learning, product and service innovation, and corporate culture.
Metrics guide the use of training funds, mentoring, knowledge sharing, and
technology improvements.
.2 Business Process Dimension
The Business Process dimension includes metrics that indicate how well the
enterprise is operating and if their products meet customer needs.
.3 Customer Dimension
The Customer dimension includes metrics on customer focus, satisfaction and
delivery of value. These metrics capture how well customer needs are met, how
satisfied they are with products and services, whether the delivery of those
products and services meet their quality expectations, and their overall experience
with the enterprise.
To satisfy our
shareholders and
customers, what
business processes
must we excel at?
To achieve our vision, how will we sustain our
ability to change and improve?
To achieve our
vision, how should
we appear to our
customers?
To succeed financially, how should we
appear to our shareholders?
Vision
and
Strategy
Internal Business Process
Objectives
Measures
Targets
Initiatives
Customer
Financial
Learning and Growth
Objectives
Measures
Targets
Initiatives
Objectives
Measures
Targets
Initiatives
Objectives
Measures
Targets
Initiatives



Techniques
Balanced Scorecard
225
.4 Financial Dimension
The Financial dimension identifies what is financially necessary to realize the
strategy. Examples of financial measures indicate profitability, revenue growth,
and added economic value.
.5 Measures or Indicators
There are two basic types of measures or indicators: lagging indicators that
provide results of actions already taken and leading indicators that provide
information about future performance.
Objectives tend to have lagging indicators, but using related leading indicators
can provide more real-time performance information.
10.3.4
Usage Considerations
In order for measures to be meaningful they should be quantitative, linked to
strategy, and easily understood by all stakeholders. When defining measures,
business analysts consider other relevant measures that are in place and ensure
that any new or changed measures do not adversely impact any existing ones. At
any time, any dimension of the balanced scorecard may be active, changing, and
evolving. Each dimension affects and is affected by the others. The balanced
scorecard allows the organization to establish monitoring and measuring of
progress against objectives and to adapt strategy as needed.
Because scorecards are used to assess the performance of the enterprise or a
business unit within the enterprise, changes to the measures can have wide
reaching implications and must be clearly communicated and carefully managed.
.1 Strengths
• Facilitates holistic and balanced planning and thinking.
• Short-, medium-, and long-term goals can be harmonized into programs with
incremental success measures.
• Strategic, tactical, and operational teams are more easily aligned in their work.
• Encourages forward thinking and competitiveness.
.2 Limitations
• A lack of a clear strategy makes aligning the dimensions difficult.
• Can be seen as the single tool for strategic planning rather than just one tool to
be used in a suite of strategic planning tools.
• Can be misinterpreted as a replacement for strategic planning, execution, and
measurement.



Benchmarking and Market Analysis
Techniques
226
10.4
Benchmarking and Market Analysis
10.4.1
Purpose
Benchmarking and market analysis are conducted to improve organizational
operations, increase customer satisfaction, and increase value to stakeholders.
10.4.2
Description
Benchmark studies are conducted to compare organizational practices against
the best-in-class practices. Best practices may be found in competitor enterprises,
in government, or from industry associations. The objective of benchmarking is to
evaluate enterprise performance and ensure that the enterprise is operating
efficiently. Benchmarking may also be performed against standards for
compliance purposes. The results from the benchmark study may initiate change
within an organization.
Market analysis involves researching customers in order to determine the
products and services that they need or want, the factors that influence their
decisions to purchase, and the competitors that exist in the market. The objective
of market analysis is to acquire this information in order to support the various
decision-making processes within an organization. Market analysis can also help
determine when to exit a market. It may be used to determine if partnering,
merging, or divesting are viable alternatives for an enterprise.
10.4.3
Elements
.1 Benchmarking
Benchmarking includes:
• identifying the areas to be studied,
• identifying enterprises that are leaders in the sector (including competitors),
• conducting a survey of selected enterprises to understand their practices,
• using a Request for Information (RFI) to gather information about
capabilities,
• arranging visits to best-in-class organizations,
• determining gaps between current and best practices, and
• developing a project proposal to implement best practices.
.2 Market Analysis
Market Analysis requires that business analysts:
• identify customers and understand their preferences,
• identify opportunities that may increase value to stakeholders,
• identify competitors and investigate their operations,



Techniques
Brainstorming
227
• look for trends in the market, anticipate growth rate, and estimate potential
profitability,
• define appropriate business strategies,
• gather market data,
• use existing resources such as company records, research studies, and
books and apply that information to the questions at hand, and
• review data to determine trends and draw conclusions.
10.4.4
Usage Considerations
.1 Strengths
• Benchmarking provides organizations with information about new and
different methods, ideas, and tools to improve organizational performance.
• An organization may use benchmarking to identify best practices by its
competitors in order to meet or exceed its competition.
• Benchmarking identifies why similar companies are successful and what
processes they used to become successful.
• Market analysis can target specific groups and can be tailored to answer
specific questions.
• Market analysis may expose weaknesses within a certain company or industry.
• Market analysis may identify differences in product offerings and services that
are available from a competitor.
.2 Limitations
• Benchmarking is time-consuming; organizations may not have the expertise to
conduct the analysis and interpret useful information.
• Benchmarking cannot produce innovative solutions or solutions that will
produce a sustainable competitive advantage because it involves assessing
solutions that have been shown to work elsewhere with the goal of
reproducing them.
• Market analysis can be time-consuming and expensive, and the results may not
be immediately available.
• Without market segmentation, market analysis may not produce the expected
results or may provide incorrect data about a competitor's products or services.
10.5
Brainstorming
10.5.1
Purpose
Brainstorming is an excellent way to foster creative thinking about a problem. The
aim of brainstorming is to produce numerous new ideas, and to derive from them
themes for further analysis.



Brainstorming
Techniques
228
10.5.2
Description
Brainstorming is a technique intended to produce a broad or diverse set of
options.
It helps answer specific questions such as (but not limited to):
• What options are available to resolve the issue at hand?
• What factors are constraining the group from moving ahead with an
approach or option?
• What could be causing a delay in activity 'A'?
• What can the group do to solve problem 'B'?
Brainstorming works by focusing on a topic or problem and then coming up with
many possible solutions to it. This technique is best applied in a group as it draws
on the experience and creativity of all members of the group. In the absence of a
group, one could brainstorm on one's own to spark new ideas. To heighten
creativity, participants are encouraged to use new ways of looking at things and
freely associate in any direction. When facilitated properly, brainstorming can be
fun, engaging, and productive.
Figure 10.5.1: Brainstorming
Define Area
of Interest
Determine Time
Limit
Identify
Participants
Establish
Evaluation Criteria

## Wrap-up


Share Ideas
Record Ideas
Build on each
others ideas
Elicit as many
ideas as possible
Create List
Rate Ideas
Distribute
Final List
Discuss
and Evaluate



Techniques
Brainstorming
229
10.5.3
Elements
.1 Preparation
• Develop a clear and concise definition of the area of interest.
• Determine a time limit for the group to generate ideas; the larger the group,
the more time required.
• Identify the facilitator and participants in the session (aim for six to eight
participants who represent a range of backgrounds and experience with the
topic).
• Set expectations with participants and get their buy-in to the process.
• Establish the criteria for evaluating and rating the ideas.
.2 Session
• Share new ideas without any discussion, criticism, or evaluation.
• Visibly record all ideas.
• Encourage participants to be creative, share exaggerated ideas, and build on
the ideas of others.
• Don't limit the number of ideas as the goal is to elicit as many as possible
within the time period.
.3 Wrap-up
• Once the time limit is reached, discuss and evaluate the ideas using the
predetermined evaluation criteria.
• Create a condensed list of ideas, combine ideas where appropriate, and
eliminate duplicates.
• Rate the ideas, and then distribute the final list of ideas to the appropriate
parties.
10.5.4
Usage Considerations
.1 Strengths
• Ability to elicit many ideas in a short time period.
• Non-judgmental environment enables creative thinking.
• Can be useful during a workshop to reduce tension between participants.
.2 Limitations
• Participation is dependent on individual creativity and willingness to participate.
• Organizational and interpersonal politics may limit overall participation.
• Group participants must agree to avoid debating the ideas raised during
brainstorming.



Business Capability Analysis
Techniques
230
10.6
Business Capability Analysis
10.6.1
Purpose
Business capability analysis provides a framework for scoping and planning by
generating a shared understanding of outcomes, identifying alignment with
strategy, and providing a scope and prioritization filter.
10.6.2
Description
Business capability analysis describes what an enterprise, or part of an enterprise,
is able to do. Business capabilities describe the ability of an enterprise to act on or
transform something that helps achieve a business goal or objective. Capabilities
may be assessed for performance and associated risks to identify specific
performance gaps and prioritize investments. Many product development efforts
are an attempt to improve the performance of an existing business capability or
to deliver a new one. As long as an enterprise continues to perform similar
functions, the capabilities required by the enterprise should remain
constant—even if the method of execution for those capabilities undergoes
significant change.
10.6.3
Elements
.1 Capabilities
Capabilities are the abilities of an enterprise to perform or transform something
that helps achieve a business goal or objective. Capabilities describe the purpose
or outcome of the performance or transformation, not how the performance or
transformation is performed. Each capability is found only once on a capability
map, even if it is possessed by multiple business units.
.2 Using Capabilities
Capabilities impact value through increasing or protecting revenue, reducing or
preventing cost, improving service, achieving compliance, or positioning the
company for the future. Not all capabilities have the same level of value. There are
various tools that can be used to make value explicit in a capability assessment.
.3 Performance Expectations
Capabilities can be assessed to identify explicit performance expectations. When
a capability is targeted for improvement, a specific performance gap can be
identified. The performance gap is the difference between the current
performance and the desired performance, given the business strategy.
.4 Risk Model
Capabilities alone do not have risks—the risks are in the performance of the
capability, or in the lack of performance.



Techniques
Business Capability Analysis
231
These risks fall into the usual business categories:
• business risk,
• technology risk,
• organizational risk, and
• market risk.
.5 Strategic Planning
Business capabilities for the current state and future state of an enterprise can be
used to determine where that enterprise needs to go in order to accomplish its
strategy. A business capability assessment can produce a set of recommendations
or proposals for solutions. This information forms the basis of a product roadmap
and serves as a guide for release planning. At the strategic level, capabilities
should support an enterprise in establishing and maintaining a sustainable
competitive advantage and a distinct value proposition.
.6 Capability Maps
Capability maps provide a graphical view of elements involved in business
capability analysis. The following examples demonstrate one element of a
capability map that would be part of a larger capabilities grid.
There is no set standard for the notation of capabilities maps. The following
images show two different methods for creating a capability map. The first two
images are the first example and the third image is the second example.
Figure 10.6.1: Sample Capability Map Example 1 Cell
Key
High Performance Gap
Medium Performance Gap
Low Performance Gap
High Risk
Medium Risk
Low Risk
High Value
Medium Value
Low Value
An Outcome
Explicit Performance Gaps
Risk
Business Risk
Technology Risk
Organizational Risk
Business
Value
Customer
Value



Business Capability Analysis
Techniques
232
Figure 10.6.2: Sample Capability Map Example 1
Organizational
Analysis
Project
Analysis
Professional
Development
Management
Business Value Analysis Centre of Excellence
High Value
Medium Value
Low Value
High Performance Gap
Medium Performance Gap
Low Performance Gap
Key
High Risk
Medium Risk
Low Risk
Requirements
Elicitation
Organizational
Analysis
Consulting
Performance
Management
Capability
Analysis
Employee
Development
Planning
Training
Requirements
Communication
Process
Analysis
Root Cause
Analysis
Requirements
Management
Project
Analysis
Consulting
Resource
Allocations
Roadmap
Construction
Usability
Testing
Templates &
Resources
Maintenance
User
Acceptance
Testing
Stakeholder
Analysis
Mentoring



Techniques
Business Capability Analysis
233
Figure 10.6.3: Sample Capability Map Example 2
10.6.4
Usage Considerations
.1 Strengths
• Provides a shared articulation of outcomes, strategy, and performance, which
help create very focused and aligned initiatives.
• Helps align business initiatives across multiple aspects of the organization.
• Useful when assessing the ability of an organization to offer new products and
services.
.2 Limitations
• Requires an organization to agree to collaborate on this model.
ORGANIZATIONAL
ANALYSIS
Business Value
Customer Value
Performance Gap
Risk
High
Med
Low
High
Med
Low
High
Med
Low
High
Med
Low
Capability Analysis












Root Cause Analysis












Process Analysis












Stakeholder Analysis












Roadmap Construction













PROJECT ANALYSIS
Business Value
Customer Value
Performance Gap
Risk
High
Med
Low
High
Med
Low
High
Med
Low
High
Med
Low
Requirements Elicitation












Requirements Management












Requirements Communication












User Acceptance Testing




Usability Testing





PROFESSIONAL
DEVELOPMENT
Business Value
Customer Value
Performance Gap
Risk
High
Med
Low
High
Med
Low
High
Med
Low
High
Med
Low
Organizational Consulting












Project Analysis Consulting




Training




Mentoring












Resources Maintenance













MANAGEMENT
Business Value
Customer Value
Performance Gap
Risk
High
Med
Low
High
Med
Low
High
Med
Low
High
Med
Low
Performance Management




Resource Allocations












Employee Dev Planning
















Business Cases
Techniques
234
• When created unilaterally or in a vacuum it fails to deliver on the goals of
alignment and shared understanding.
• Requires a broad, cross–functional collaboration in defining the capability
model and the value framework.
10.7
Business Cases
10.7.1
Purpose
A business case provides a justification for a course of action based on the
benefits to be realized by using the proposed solution, as compared to the cost,
effort, and other considerations to acquire and live with that solution.
10.7.2
Description
A business case captures the rationale for undertaking a change. A business case
is frequently presented in a formal document, but may also be presented through
informal methods. The amount of time and resources spent on the business case
should be proportional to the size and importance of its potential value. The
business case provides sufficient detail to inform and request approval without
providing specific intricacies about the method and/or approach to the
implementation. It may also be the catalyst for one or many initiatives in order to
implement the change.
A business case is used to:
• define the need,
• determine the desired outcomes,
• assess constraints, assumptions, and risks, and
• recommend a solution.
10.7.3
Elements
.1 Need Assessment
The need is the driver for the business case. It is the relevant business goal or
objective that must be met. Objectives are linked to a strategy or the strategies of
the enterprise. The need assessment identifies the problem or the potential
opportunity. Throughout the development of the business case, different
alternatives to solve the problem or take advantage of the opportunity will be
assessed.
.2 Desired Outcomes
The desired outcomes describe the state which should result if the need is
fulfilled. They should include measurable outcomes that can be utilized to
determine the success of the business case or the solution. Desired outcomes



Techniques
Business Cases
235
should be revisited at defined milestones and at the completion of the initiative
(or initiatives) to fulfill the business case. They should also be independent of the
recommended solution. As solution options are assessed, their ability to achieve
the desired outcomes will help determine the recommended solution.
.3 Assess Alternatives
The business case identifies and assesses various alternative solutions.
Alternatives may include (but are not limited to) different technologies, processes,
or business models. Alternatives may also include different ways of acquiring
these and different timing options. They will be affected by constraints such as
budget, timing, and regulatory. The ‘do-nothing’ alternative should be assessed
and considered for the recommended solution.
Each alternative should be assessed in terms of:
• Scope: defines the alternative being proposed. Scope can be defined using
organizational boundaries, system boundaries, business processes, product
lines or geographic regions. Scope statements clearly define what will be
included and what will be excluded. The scope of various alternatives may
be similar or have overlap but may also differ based on the alternative.
• Feasibility: The organizational and technical feasibility should be assessed
for each alternative. It includes organizational knowledge, skills, and
capacity, as well as technical maturity and experience in the proposed
technologies.
• Assumptions, Risks, and Constraints: Assumptions are agreed-to facts
that may have influence on the initiative. Constraints are limitations that
may restrict the possible alternatives. Risks are potential problems that may
have a negative impact on the solution. Agreeing to and documenting
these factors facilitates realistic expectations and a shared understanding
amongst stakeholders.
For more
information, see
Financial Analysis
(p. 274).
• Financial Analysis and Value Assessment: The financial analysis and
value assessment includes an estimate of the costs to implement and
operate the alternative, as well as a quantified financial benefit from
implementing the alternative. Benefits of a non-financial nature (such as
improved staff morale, increased flexibility to respond to change, improved
customer satisfaction, or reduced exposure to risk) are also important and
add significant value to the organization. Value estimates are related back
to strategic goals and objectives.
.4 Recommended Solution
The recommended solution describes the most desirable way to solve the
problem or leverage the opportunity. The solution is described in sufficient detail
for decision makers to understand the solution and determine if the
recommendation will be implemented. The recommended solution may also
include some estimates of cost and duration to implement the solution.
Measurable benefits/outcomes will be identified to allow stakeholders to assess



Business Model Canvas
Techniques
236
the performance and success of the solution after implementation and during
operation.
10.7.4
Usage Considerations
.1 Strengths
• Provides an amalgamation of the complex facts, issues, and analysis required to
make decisions regarding change.
• Provides a detailed financial analysis of cost and benefits.
• Provides guidance for ongoing decision making throughout the initiative.
.2 Limitations
• May be subject to the biases of authors.
• Frequently not updated once funding for the initiative is secured.
• Contains assumptions regarding costs and benefits that may prove invalid upon
further investigation.
10.8
Business Model Canvas
10.8.1
Purpose
A business model canvas describes how an enterprise creates, delivers, and
captures value for and from its customers.
10.8.2
Description
A business model canvas is comprised of nine building blocks that describe how
an organization intends to deliver value:
• Key Partnerships,
• Key Activities,
• Key Resources,
• Value Proposition,
• Customer Relationships,
• Channels,
• Customer Segments,
• Cost Structure, and
• Revenue Streams.
These building blocks are arranged on a business canvas that shows the
relationship between the organization's operations, finance, customers, and
offerings. The business model canvas also serves as a blueprint for implementing
a strategy.



Techniques
Business Model Canvas
237
Figure 10.8.1: Business Model Canvas
A business model canvas can be used as a diagnostic and planning tool regarding
strategy and initiatives. As a diagnostic tool, the various elements of the canvas
are used as a lens into the current state of the business, especially with regards to
the relative amounts of energy, time, and resources the organization is currently
investing in various areas. As a planning and monitoring tool, the canvas can be
used as a guideline and framework for understanding inter-dependencies and
priorities among groups and initiatives.
A business model canvas allows for the mapping of programs, projects, and other
initiatives (such as recruitment or talent retention) to the strategy of the
enterprise. In this capacity, the canvas can be used to view where the enterprise is
investing, where a particular initiative fits, and any related initiatives.
A business model canvas can also be used to demonstrate where the efforts of
various departments and work groups fit and align to the overall strategy of the
enterprise.
.1 Elements
Key Partnerships
Key partnerships frequently involve some degree of sharing of proprietary
information, including technologies. An effective key partnership can, in some
cases, lead to more formalized relationships such as mergers and acquisitions.
The benefits in engaging in key partnerships include:
• optimization and economy,
• reduction of risk and uncertainty,
• acquisition of particular resources and activities, and
• lack of internal capabilities.
Value
Proposition
Key
Activities
Customer
Segments
Customer
Relationships
Key
Partnerships
Key Resources
Channels
Cost Structure
Revenue Streams



Business Model Canvas
Techniques
238
Key Activities
Key activities are those that are critical to the creation, delivery, and maintenance
of value, as well as other activities that support the operation of the enterprise.
Key activities can be classified as:
• Value-add: characteristics, features, and business activities for which the
customer is willing to pay.
• Non-value-add: aspects and activities for which the customer is not willing
to pay.
• Business non-value-add: characteristics that must be included in the
offering, activities performed to meet regulatory and other needs, or costs
associated with doing business, for which the customer is not willing to pay.
Key Resources
Resources are the assets needed to execute a business model. Resources may be
different based on the business model.
Resources can be classified as:
• Physical: applications, locations, and machines.
• Financial: what is needed to fund a business model, such as cash and lines
of credit.
• Intellectual: any proprietary aspects that enable a business model to thrive,
such as knowledge, patents and copyrights, customer databases, and
branding.
• Human: the people needed to execute a particular business model.
Value Proposition
A value proposition represents what a customer is willing to exchange for having
their needs met. The proposition may consist of a single product or service, or
may be comprised of a set of goods and services that are bundled together to
address the needs of a customer or customer segment to help them solve their
problem.
Customer Relationships
In general, customer relationships are classified as customer acquisition and
customer retention. The methods used in establishing and maintaining customer
relationships vary depending on the level of interaction desired and the method
of communication. For example, some relationships can be highly personalized,
while others are automated and promote a self-serve approach. The relationships
can also be formal or informal.
Organizations interact with their customers in different ways depending on the
relationship they want to establish and maintain.



Techniques
Business Model Canvas
239
Channels
Channels are the different ways an enterprise interacts with and delivers value to
its customers. Some channels are very communication-oriented (for example,
marketing channel), and some are delivery-oriented (for example, distribution
channel). Other examples include sales channels and partnering channels.
Enterprises use channels to:
• raise awareness about their offerings,
• help customers evaluate the value proposition,
• allow customers to purchase a good or service,
• help the enterprise deliver on the value proposition, and
• provide support.
Understanding channels involves identifying the processes, procedures,
technologies, inputs, and outputs (and their current impact), as well as
understanding the relationship of the various channels to the strategies of the
organization.
Customer Segments
Customer segments group customers with common needs and attributes so that
the enterprise can more effectively and efficiently address the needs of each
segment.
An organization within an enterprise may consider defining and targeting distinct
customer segments based on:
• different needs for each segment,
• varying profitability between segments,
• different distribution channels, and
• formation and maintenance of customer relationships.
Cost Structure
Every entity, product, or activity within an enterprise has an associated cost.
Enterprises seek to reduce, minimize, or eliminate costs wherever possible.
Reducing costs may increase the profitability of an organization and allow those
funds to be used in other ways to create value for the organization and for
customers. Therefore, it is important to understand the type of business models,
the differences in the types of costs and their impact, and where the enterprise is
focusing its efforts to reduce costs.
Revenue Streams
A revenue stream is a way or method by which revenue comes into an enterprise
from each customer segment in exchange for the realization of a value
proposition. There are two basic ways revenue is generated for an enterprise:



Business Rules Analysis
Techniques
240
revenue resulting from a one-time purchase of a good or service and recurring
revenue from periodic payments for a good, service, or ongoing support.
Some types of revenue streams include:
• Licensing or Subscription fees: the customer pays for the right to access
a particular asset, either as a one-time fee or as a recurring cost.
• Transaction or Usage fees: the customer pays each time they use a good
or service.
• Sales: the customer is granted ownership rights to a specific product.
• Lending, Renting, or Leasing: the customer has temporary rights to use
an asset.
.2 Usage Considerations
Strengths
• It is a widely used and effective framework that can be used to understand and
optimize business models.
• It is simple to use and easy to understand.
Limitations
• Does not account for alternative measures of value such as social and
environmental impacts.
• The primary focus on value propositions does not provide a holistic insight for
business strategy.
• Does not include the strategic purpose of the enterprise within the canvas.
10.9
Business Rules Analysis
10.9.1
Purpose
Business rules analysis is used to identify, express, validate, refine, and organize
the rules that shape day-to-day business behaviour and guide operational
business decision making.
10.9.2
Description
Business policies and rules guide the day-to-day operation of the business and its
processes, and shape operational business decisions. A business policy is a
directive concerned with broadly controlling, influencing, or regulating the
actions of an enterprise and the people in it. A business rule is a specific, testable
directive that serves as a criterion for guiding behaviour, shaping judgments, or
making decisions. A business rule must be practicable (needing no further



Techniques
Business Rules Analysis
241
interpretation for use by people in the business) and is always under the control
of the business.
Analysis of business rules involves capturing business rules from sources,
expressing them clearly, validating them with stakeholders, refining them to best
align with business goals, and organizing them so they can be effectively
managed and reused. Sources of business rules may be explicit (for example,
documented business policies, regulations, or contracts) or tacit (for example,
undocumented stakeholder know-how, generally accepted business practices, or
norms of the corporate culture). Business rules should be explicit, specific, clear,
accessible, and single sourced. Basic principles for business rules include:
• basing them on standard business vocabulary to enable domain subject
matter experts to validate them,
• expressing them separately from how they will be enforced,
• defining them at the atomic level and in declarative format,
• separating them from processes they support or constrain,
• mapping them to decisions the rule supports or constrains, and
• maintaining them in a manner such that they can be monitored and
adapted as business circumstances evolve over time.
A set of rules for making an operational business decision may be expressed as a
decision table or decision tree, as described in Decision Analysis (p. 261). The
number of rules in such a set can be quite large, with a high level of complexity.
10.9.3
Elements
Business rules require consistent use of business terms, a glossary of definitions
for the underlying business concepts, and an understanding of the structural
connections among the concepts. Reuse of existing terminology from external
industry associations or internal business glossaries is often advised. Sometimes
definitions and structures from data dictionaries or data models can be helpful
(see Data Dictionary (p. 247) and Data Modelling (p. 256)). Business rules should
be expressed and managed independently of any implementation technology
since they need to be available for reference by business people. In addition, they
sometimes will be implemented in multiple platforms or software components.
There are frequently exceptions to business rules; these should be treated simply
as additional business rules. Existing business rules should be challenged to
ensure they align with business goals and remain relevant, especially when new
solutions emerge.
.1 Definitional Rules
Definitional rules shape concepts, or produce knowledge or information. They
indicate something that is necessarily true (or untrue) about some concept,
thereby supplementing its definition. In contrast to behavioural rules, which are
about the behaviour of people, definitional rules represent operational



Business Rules Analysis
Techniques
242
knowledge of the organization. Definitional rules cannot be violated but they can
be misapplied. An example of a definitional rule is:
A customer must be considered a Preferred Customer if they place more
than 10 orders per month.
Definitional rules often prescribe how information may be derived, inferred or
calculated based on information available to the business. An inference or
calculation may be the result of multiple rules, each building on something
inferred or calculated by some other(s). Sets of definitional rules are often used to
make operational business decisions during some process or upon some event.
An example of a calculation rule is:
An order's local jurisdiction tax amount must be calculated as (sum of the
prices of all the order's taxable ordered items) × local jurisdiction tax rate
amount.
.2 Behavioural Rules
Behavioural rules are people rules–even if the behaviour is automated.
Behavioural rules serve to shape (govern) day-to-day business activity. They do so
by placing some obligation or prohibition on conduct, action, practice, or
procedure.
Behavioural rules are rules the organization chooses to enforce as a matter of
policy, often to reduce risk or enhance productivity. They frequently make use of
the information or knowledge produced by definitional rules (which are about
shaping knowledge or information). Behavioural rules are intended to guide the
actions of people working within the organization, or people who interact with it.
They may oblige individuals to perform actions in a certain way, prevent them
from carrying out actions, or prescribe the conditions under which something can
be correctly done. An example of a behavioural rule is:
An order must not be placed when the billing address provided by the
customer does not match the address on file with the credit card provider.
In contrast to definitional rules, behavioural rules are rules that can be violated
directly. By definition, it is always possible to violate a behavioural rule—even if
there are no circumstances under which the organization would approve that,
and despite the fact that the organization takes extraordinary precautions in its
solution to prevent it. Because of this, further analysis should be conducted to
determine how strictly the rule needs to be enforced, what kinds of sanctions
should be imposed when it is violated, and what additional responses to a
violation might be appropriate. Such analysis often leads to specification of
additional rules.
Various levels of enforcement may be specified for a behavioural rule. For
example:
• Allow no violations (strictly enforced).
• Override by authorized actor.



Techniques
Collaborative Games
243
• Override with explanation.
• No active enforcement.
A behavioural rule for which there is no active enforcement is simply a guideline
that suggests preferred or optimal business behaviour.
10.9.4
Usage Considerations
.1 Strengths
• When enforced and managed by a single enterprise-wide engine, changes to
business rules can be implemented quickly.
• A centralized repository creates the ability to reuse business rules across an
organization.
• Business rules provide structure to govern business behaviours.
• Clearly defining and managing business rules allows organizations to make
changes to policy without altering processes or systems.
.2 Limitations
• Organizations may produce lengthy lists of ambiguous business rules.
• Business rules can contradict one another or produce unanticipated results
when combined unless validated against one another.
• If available vocabulary is insufficiently rich, not business-friendly, or poorly
defined and organized, resulting business rules will be inaccurate or
contradictory.
10.10
Collaborative Games
10.10.1
Purpose
Collaborative games encourage participants in an elicitation activity to collaborate
in building a joint understanding of a problem or a solution.
10.10.2
Description
Collaborative games refer to several structured techniques inspired by game play
and are designed to facilitate collaboration. Each game includes rules to keep
participants focused on a specific objective. The games are used to help the
participants share their knowledge and experience on a given topic, identify
hidden assumptions, and explore that knowledge in ways that may not occur
during the course of normal interactions. The shared experience of the
collaborative game encourages people with different perspectives on a topic to
work together in order to better understand an issue and develop a shared model



Collaborative Games
Techniques
244
of the problem or of potential solutions. Many collaborative games can be used
to understand the perspectives of various stakeholder groups.
Collaborative games often benefit from the involvement of a neutral facilitator
who helps the participants understand the rules of the game and enforces those
rules. The facilitator's job is to keep the game moving forward and to help ensure
that all participants play a role. Collaborative games usually involve a strong visual
or tactile element. Activities such as moving sticky notes, scribbling on
whiteboards, or drawing pictures help people to overcome inhibitions, foster
creative thinking, and think laterally.
10.10.3
Elements
.1 Game Purpose
Each different collaborative game has a defined purpose—usually to develop a
better understanding of a problem or to stimulate creative solutions—that is
specific to that type of game. The facilitator helps the participants in the game
understand the purpose and work toward the successful realization of that
purpose.
.2 Process
Each type of collaborative game has a process or set of rules that, when followed,
keeps the game moving toward its goal. Each step in the game is often limited by
time.
Games typically have at least three steps:
Step 1.
an opening step, in which the participants get involved, learn the
rules of the game, and start generating ideas,
Step 2.
the exploration step, in which participants engage with one
another and look for connections between their ideas, test those
ideas, and experiment with new ideas, and
Step 3.
a closing step, in which the ideas are assessed and participants
work out which ideas are likely to be the most useful and
productive.
.3 Outcome
At the end of a collaborative game, the facilitator and participants work through
the results and determine any decisions or actions that need to be taken as a
result of what the participants have learned.
.4 Examples of Collaborative Games
There are many types of collaborative games available, including (but not limited
to) the following:



Techniques
Concept Modelling
245
10.10.4
Usage Considerations
.1 Strengths
• May reveal hidden assumptions or differences of opinion.
• Encourages creative thinking by stimulating alternative mental processes.
• Challenges participants who are normally quiet or reserved to take a more
active role in team activities.
• Some collaborative games can be useful in exposing business needs that aren't
being met.
.2 Limitations
• The playful nature of the games may be perceived as silly and make participants
with reserved personalities or cultural norms uncomfortable.
• Games can be time-consuming and may be perceived as unproductive,
especially if the objectives or outcomes are unclear.
• Group participation can lead to a false sense of confidence in the conclusions
reached.
10.11
Concept Modelling
10.11.1
Purpose
A concept model is used to organize the business vocabulary needed to
consistently and thoroughly communicate the knowledge of a domain.
Table 10.10.1:  Examples of Collaborative Games
Game
Description
Objective
Product
Box
Participants construct a box for the
product as if it was being sold in a retail
store.
Used to help identify
features of a product
that help drive interest
in the marketplace.
Affinity
Map
Participants write down features on
sticky notes, put them on a wall, and
then move them closer to other features
that appear similar in some way.
Used to help identify
related or similar
features or themes.
Fishbowl
Participants are divided into two groups.
One group of participants speaks about
a topic, while the other group listens
intently and documents their
observations.
Used to identify hidden
assumptions or
perspectives.



Concept Modelling
Techniques
246
10.11.2
Description
A concept model starts with a glossary, which typically focuses on the core noun
concepts of a domain. Concept models put a premium on high-quality, design-
independent definitions that are free of data or implementation biases. Concept
models also emphasize rich vocabulary.
A concept model identifies the correct choice of terms to use in communications,
including all business analysis information. It is especially important where high
precision and subtle distinctions need to be made.
Concept models can be effective where:
• the enterprise seeks to organize, retain, build-on, manage, and
communicate core knowledge,
• the initiative needs to capture large numbers of business rules,
• there is resistance from stakeholders about the perceived technical nature
of data models, class diagrams, or data element nomenclature and
definition,
• innovative solutions are sought when re-engineering business processes or
other aspects of business capability, and
• the enterprise faces regulatory or compliance challenges.
A concept model differs from a data model. The goal of a concept model is to
support the expression of natural language statements, and supply their
semantics. Concept models are not intended to unify, codify, and simplify data.
Therefore the vocabulary included in a concept model is far richer, as suits
knowledge-intensive domains. Concept models are often rendered graphically.
10.11.3
Elements
.1 Noun Concepts
The most basic concepts in a concept model are the noun concepts of the
domain, which are simply ‘givens’ for the space.
.2 Verb Concepts
Verb concepts provide basic structural connections between noun concepts.
These verb concepts are given standard wordings, so they can be referenced
unambiguously. These wordings by themselves are not necessarily sentences;
rather, they are the building blocks of sentences (such as business rule
statements). Sometimes verb concepts are derived, inferred, or computed by
definitional rules. This is how new knowledge or information is built up from
more basic facts.
.3 Other Connections
Since concept models must support rich meaning (semantics), other types of
standard connections are used besides verb concepts.



Techniques
Data Dictionary
247
These include but are not limited to:
• categorizations,
• classifications,
• partitive (whole-part) connections, and
• roles.
10.11.4
Usage Considerations
.1 Strengths
• Provide a business-friendly way to communicate with stakeholders about
precise meanings and subtle distinctions.
• Is independent of data design biases and the often limited business vocabulary
coverage of data models.
• Proves highly useful for white-collar, knowledge-rich, decision-laden business
processes.
• Helps ensure that large numbers of business rules and complex decision tables
are free of ambiguity and fit together cohesively.
.2 Limitations
• May set expectations too high about how much integration based on business
semantics can be achieved on relatively short notice.
• Requires a specialized skill set based on the ability to think abstractly and non-
procedurally about know-how and knowledge.
• The knowledge-and-rule focus may be foreign to stakeholders.
• Requires tooling to actively support real-time use of standard business
terminology in writing business rules, requirements, and other forms of
business communication.
10.12
Data Dictionary
10.12.1
Purpose
A data dictionary is used to standardize a definition of a data element and enable
a common interpretation of data elements.
10.12.2
Description
A data dictionary is used to document standard definitions of data elements, their
meanings, and allowable values. A data dictionary contains definitions of each
data element and indicates how those elements combine into composite data
elements. Data dictionaries are used to standardize usage and meanings of data
elements between solutions and between stakeholders.



Data Dictionary
Techniques
248
Data dictionaries are sometimes referred to as metadata repositories and are used
to manage the data within the context of a solution. As organizations adopt data
mining and more advanced analytics, a data dictionary may provide the metadata
required by these more complex scenarios. A data dictionary is often used in
conjunction with an entity relationship diagram (see Data Modelling (p. 256)) and
may be extracted from a data model.
Data dictionaries can be maintained manually (as a spreadsheet) or via automated
tools.
Figure 10.12.1: Example of a Data Dictionary
10.12.3
Elements
.1 Data Elements
Data dictionaries describe data element characteristics including the description of
the data element in the form of a definition that will be used by stakeholders. Data
dictionaries include standard definitions of data elements, their meanings, and
allowable values. A data dictionary contains definitions of each primitive data
element and indicates how those elements combine into composite data elements.
.2 Primitive Data Elements
The following information must be recorded about each data element in the data
Primitive Data
Elements
First Name
Data Element
1
Data Element
2
Data Element
3
Alias
Alternate name
referenced by
stakeholders
Values/Meanings
Enumerated list
or description of
data element
Description
Definition
Customer Name = First Name + Middle Name + Family Name
Middle Name
Last Name
Given Name
Minimum 2
characters
First Name
Composite
Middle Name
Can be omitted
Middle Name
Surname
Minimum 2
characters
Family Name
Name
Name referenced
by data elements



Techniques
Data Dictionary
249
dictionary:
• Name: a unique name for the data element, which will be referenced by
the composite data elements.
• Aliases: alternate names for the data element used by various
stakeholders.
• Values/Meanings: a list of acceptable values for the data element. This
may be expressed as an enumerated list or as a description of allowed
formats for the data (including information such as the number of
characters). If the values are abbreviated this will include an explanation of
the meaning.
• Description: the definition of the data element in the context of the
solution.
.3 Composite Elements
Composite data elements are built using data elements to build composite
structures, which may include:
• Sequences: required ordering of primitive data elements within the
composite structure. For example, a plus sign indicates that one element is
followed by or concatenated with another element: Customer Name = First
Name+Middle Name+Family Name.
• Repetitions: whether one or more data elements may be repeated
multiple times.
• Optional Elements: may or may not occur in a particular instance of the
composite element.
10.12.4
Usage Considerations
.1 Strengths
• Provides all stakeholders with a shared understanding of the format and
content of relevant information.
• A single repository of corporate metadata promotes the use of data throughout
the organization in a consistent manner.
.2 Limitations
• Requires regular maintenance, otherwise the metadata could become obsolete
or incorrect.
• All maintenance is required to be completed in a consistent manner in order to
ensure that stakeholders can quickly and easily retrieve the information they
need. This requires time and effort on the part of the stewards responsible for
the accuracy and completeness of the data dictionary.
• Unless care is taken to consider the metadata required by multiple scenarios, it
may have limited value across the enterprise.



Data Flow Diagrams
Techniques
250
10.13
Data Flow Diagrams
10.13.1
Purpose
Data flow diagrams show where data comes from, which activities process the
data, and if the output results are stored or utilized by another activity or external
entity.
10.13.2
Description
Data flow diagrams portray the transformation of data. They are useful for
depicting a transaction-based system and illustrating the boundaries of a physical,
logical, or manual system.
A data flow diagram illustrates the movement and transformation of data
between externals (entities) and processes. The output from one external or
process is the input to another. The data flow diagram also illustrates the
temporary or permanent repositories (referred to as data stores or terminators)
where data is stored within a system or an organization. The data defined should
be described in a data dictionary (see Data Dictionary (p. 247)).
Data flow diagrams can consist of multiple layers of abstraction. The highest level
diagram is a context diagram which represents the entire system. Context
diagrams show the system in its entirety, as a transformation engine with
externals as the source or consumer of data.
Figure 10.13.1: Context Diagram Gane-Sarson Notation
The next level of data flow diagrams is the level 1 diagram. Level 1 diagrams
illustrate the processes related to the system with the respective input data,
output transformed data, and data stores.
External
Agent
Noun
Data Process
Verb/Noun
Phrase Naming
External
Agent
Noun
External
Agent
Noun
External
Agent
Noun
Input Data
Input Data
Input Data
Output Data
Output Data
Input Data
Output Data
Output Data



Techniques
Data Flow Diagrams
251
Figure 10.13.2: Level 1 Diagram Yourdon Notation
Further levels of the data flow diagram (level 2, level 3 and so forth) break down
the major processes from the level 1 diagram. Level 1 diagrams are useful to show
the internal partitioning of the work and the data that flows between the
partitions, as well as the stored data used by each of the partitions. Each of the
partitions can be further decomposed if needed. The externals remain the same
and additional flows and stores are defined.
Logical data flow diagrams represent the future or essential state—that is, what
transformations need to occur regardless of the current physical limitations.
Physical data flow diagrams model all of the data stores, printers, forms, devices,
and other manifestations of data. The physical diagram can show either the
current state or how it will be implemented.
10.13.3
Elements
.1 Externals (Entity, Source, Sink)
An external (entity, source, sink) is a person, organization, automated system, or any
device capable of producing data or receiving data. An external is an object which is
outside of the system under analysis. Externals are the sources and/or destinations
(sinks) of the data. Each external must have at least one data flow going to or
coming from it. Externals are represented by using a noun inside a rectangle and are
found within context-level diagrams as well as lower levels of abstraction.
External
Agent
Noun
Data
Process
Verb/Noun
External
Agent
Noun
External
Agent
Noun
External
Agent
Noun
Input Data
Noun
Input Data
Noun
Output Data
Noun
Data
Process
Verb/Noun
Data
Process
Verb/Noun
Noun
Input Data
Noun
Transformed
Output Data
Data Store



Data Flow Diagrams
Techniques
252
.2 Data Store
A data store is a collection of data where data may be read repeatedly and where
it can be stored for future use. In essence, it is data at rest. Each data store must
have at least one data flow going to or coming from it. A data store is
represented as either two parallel lines or as an open-ended rectangle with a
label.
.3 Process
A process can be a manual or automated activity performed for a business
reason. A process transforms the data into an output. Naming standards for a
process should contain a verb and a noun. Each process must have at least one
data flow going to it and one data flow coming from it. A data process is
represented as a circle or rectangle with rounded corners.
.4 Data Flow
The movement of data between an external, a process, and a data store is
represented by data flows. The data flows hold processes together. Every data
flow will connect to or from a process (transformation of the data). Data flows
show the inputs and outputs of each process. Every process transforms an input
into an output. Data flows are represented as a line with an arrow displayed
between processes. The data flow is named using a noun.
Figure 10.13.3: Data Flow Diagram Gane-Sarson Notation
Figure 10.13.4: Data Flow Diagram Yourdon Notation
Output Data
Input Data
Input Data from
parent diagram
(System Input 1)
Data Store
Output Data from
parent diagram
(System Output 1)
1
Process 1
Verb/Noun
Phrase Naming
2
Process 2
Verb/Noun
Phrase Naming
Input
Data
External
Agent
Data Process
Output
Data
Data Store



Techniques
Data Mining
253
10.13.4
Usage Considerations
.1 Strengths
• May be used as a discovery technique for processes and data or as a Technique
for the verification of functional decompositions or data models.
• Are excellent ways to define the scope of a system and all of the systems,
interfaces, and user interfaces that attach to it. Allows for estimation of the
effort needed to study the work.
• Most users find these data flow diagrams relatively easy to understand.
• Helps to identify duplicated data elements or misapplied data elements.
• Illustrates connections to other systems.
• Helps define the boundaries of a system.
• Can be used as part of system documentation.
• Helps to explain the logic behind the data flow within a system.
.2 Limitations
• Using data flow diagrams for large-scale systems can become complex and
difficult for stakeholders to understand.
• Different methods of notation with different symbols could create challenges
pertaining to documentation.
• Does not illustrate a sequence of activities.
• Data transformations (processes) say little about the process or stakeholder.
10.14
Data Mining
10.14.1
Purpose
Data mining is used to improve decision making by finding useful patterns and
insights from data.
10.14.2
Description
Data mining is an analytic process that examines large amounts of data from
different perspectives and summarizes the data in such a way that useful patterns
and relationships are discovered.
The results of data mining techniques are generally mathematical models or
equations that describe underlying patterns and relationships. These models can
be deployed for human decision making through visual dashboards and reports,
or for automated decision-making systems through business rule management
systems or in-database deployments.



Data Mining
Techniques
254
Data mining can be utilized in either supervised or unsupervised investigations. In
a supervised investigation, users can pose a question and expect an answer that
can drive their decision making. An unsupervised investigation is a pure pattern
discovery exercise where patterns are allowed to emerge, and then considered for
applicability to business decisions.
Data mining is a general term that covers descriptive, diagnostic, and predictive
techniques:
• Descriptive: such as clustering make it easier to see the patterns in a set of
data, such as similarities between customers.
• Diagnostic: such as decision trees or segmentation can show why a
pattern exists, such as the characteristics of an organization's most
profitable customers.
• Predictive: such as regression or neural networks can show how likely
something is to be true in the future, such as predicting the probability that
a particular claim is fraudulent.
In all cases it is important to consider the goal of the data mining exercise and to
be prepared for considerable effort in securing the right type, volume, and quality
of data with which to work.
10.14.3
Elements
.1 Requirements Elicitation
The goal and scope of data mining is established either in terms of decision
requirements for an important identified business decision, or in terms of a
functional area where relevant data will be mined for domain-specific pattern
discovery. This top-down versus a bottom-up mining strategy allows analysts to
pick the correct set of data mining techniques.
Formal decision modelling techniques (see Decision Modelling (p. 265)) are used
to define requirements for top-down data mining exercises. For bottom-up
pattern discovery exercises it is useful if the discovered insight can be placed on
existing decision models, allowing rapid use and deployment of the insight.
Data mining exercises are productive when managed as an agile environment.
They assist rapid iteration, confirmation, and deployment while providing project
controls.
.2 Data Preparation: Analytical Dataset
Data mining tools work on an analytical dataset. This is generally formed by
merging records from multiple tables or sources into a single, wide dataset.
Repeating groups are typically collapsed into multiple sets of fields. The data may
be physically extracted into an actual file or it may be a virtual file that is left in the
database or data warehouse so it can be analyzed. Analytical datasets are split
into a set to be used for analysis, a completely independent set for confirming
that the model developed works on data not used to develop it, and a validation
set for final confirmation. Data volumes can be very large, sometimes resulting in



Techniques
Data Mining
255
the need to work with samples or to work in-datastore so that the data does not
have to be moved around.
.3 Data Analysis
Once the data is available, it is analyzed. A wide variety of statistical measures are
typically applied and visualization tools used to see how data values are
distributed, what data is missing, and how various calculated characteristics
behave. This step is often the longest and most complex in a data mining effort
and is increasingly the focus of automation. Much of the power of a data mining
effort typically comes from identifying useful characteristics in the data. For
instance, a characteristic might be the number of times a customer has visited a
store in the last 80 days. Determining that the count over the last 80 days is more
useful than the count over the last 70 or 90 is key.
.4 Modelling Techniques
There are a wide variety of data mining techniques.
Some examples of data mining techniques are:
• classification and regression trees (CART), C5 and other decision tree
analysis techniques,
• linear and logistic regression,
• neural networks,
• support sector machines, and
• predictive (additive) scorecards.
The analytical dataset and the calculated characteristics are fed into these
algorithms which are either unsupervised (the user does not know what they are
looking for) or supervised (the user is trying to find or predict something specific).
Multiple techniques are often used to see which is most effective. Some data is
held out from the modelling and used to confirm that the result can be replicated
with data that was not used in the initial creation.
.5 Deployment
Once a model has been built, it must be deployed to be useful. Data mining
models can be deployed in a variety of ways, either to support a human decision
maker or to support automated decision-making systems. For human users, data
mining results may be presented using visual metaphors or as simple data fields.
Many data mining techniques identify potential business rules that can be
deployed using a business rules management system. Such executable business
rules can be fitted into a decision model along with expert rules as necessary.
Some data mining techniques—especially those described as predictive analytic
techniques—result in mathematical formulas. These can also be deployed as
executable business rules but can also be used to generate SQL or code for
deployment. An increasingly wide range of in-database deployment options allow
such models to be integrated into an organization's data infrastructure.



Data Modelling
Techniques
256
10.14.4
Usage Considerations
.1 Strengths
• Reveal hidden patterns and create useful insight during analysis—helping
determine what data might be useful to capture or how many people might be
impacted by specific suggestions.
• Can be integrated into a system design to increase the accuracy of the data.
• Can be used to eliminate or reduce human bias by using the data to determine
the facts.
.2 Limitations
• Applying some techniques without an understanding of how they work can
result in erroneous correlations and misapplied insight.
• Access to big data and to sophisticated data mining tool sets and software may
lead to accidental misuse.
• Many techniques and tools require specialist knowledge to work with.
• Some techniques use advanced math in the background and some
stakeholders may not have direct insights into the results. A perceived lack of
transparency can cause resistance from some stakeholders.
• Data mining results may be hard to deploy if the decision making they are
intended to influence is poorly understood.
10.15
Data Modelling
10.15.1
Purpose
A data model describes the entities, classes or data objects relevant to a domain,
the attributes that are used to describe them, and the relationships among them
to provide a common set of semantics for analysis and implementation.
10.15.2
Description
A data model usually takes the form of a diagram that is supported by textual
descriptions. It visually represents the elements that are important to the business
(for example, people, places, things, and business transactions), the attributes
associated with those elements, and the significant relationships among them.
Data models are frequently used in elicitation and requirements analysis and
design, as well as to support implementation and continuous improvement.
There are several variations of data models:
• Conceptual data model: is independent of any solution or technology
and can be used to represent how the business perceives its information. It



Techniques
Data Modelling
257
can be used to help establish a consistent vocabulary describing business
information and the relationships within that information.
• Logical data model: is an abstraction of the conceptual data model that
incorporates rules of normalization to formally manage the integrity of the
data and relationships. It is associated with the design of a solution.
• Physical data model: is used by implementation subject matter experts to
describe how a database is physically organized. It addresses concerns like
performance, concurrency, and security.
The conceptual, logical, and physical data models are developed for different
purposes and may be significantly different even when depicting the same
domain.
At the conceptual level, different data modelling notations are likely to produce
broadly similar results and can be thought of as a single technique (as presented
here). Logical and physical data models include elements specific to the solutions
they support, and are generally developed by stakeholders with expertise in
implementing particular technical solutions. For instance, logical and physical
entity-relationship diagrams (ERDs) would be used to implement a relational
database, whereas a logical or physical class diagram would be used to support
object-oriented software development.
Object diagrams can be used to illustrate particular instances of entities from a
data model. They can include actual sample values for the attributes, making
object diagrams more concrete and more easily understood.
10.15.3
Elements
.1 Entity or Class
In a data model, the organization keeps data on entities (or classes or data
objects). An entity may represent something physical (such as a Warehouse),
something organizational (such as a Sales Area), something abstract (such as a
Product Line), or an event (such as an Appointment). An entity contains attributes
and has relationships to other entities in the model.
In a class diagram, entities are referred to as classes. Like an entity in a data
model, a class contains attributes and has relationships with other classes. A class
also contains operations or functions that describe what can be done with the
class, such as generating an invoice or opening a bank account.
Each instance of an entity or class will have a unique identifier that sets it apart
from other instances.
.2 Attribute
An attribute defines a particular piece of information associated with an entity,
including how much information can be captured in it, its allowable values, and
the type of information it represents. Attributes can be described in a data
dictionary (see Data Dictionary (p. 247)). Allowable values may be specified
through business rules (see Business Rules Analysis (p. 240)).



Data Modelling
Techniques
258
Attributes can include such values as:
• Name: a unique name for the attribute. Other names used by stakeholders
may be captured as aliases.
• Values/Meanings: a list of acceptable values for the attribute. This may be
expressed as an enumerated list or as a description of allowed formats for
the data (including information such as the number of characters). If the
values are abbreviated this will include an explanation of the meaning.
• Description: the definition of the attribute in the context of the solution.
.3 Relationship or Association
The relationships between entities provide structure for the data model,
specifically indicating which entities relate to which others and how.
Specifications for a relationship typically indicate the number of minimum and
maximum occurrences allowed on each side of that relationship (for example,
every customer is related to exactly one sales area, while a sales area may be
related to zero, one, or many customers). The term cardinality is used to refer to
the minimum and maximum number of occurrences to which an entity may be
related. Typical cardinality values are zero, one, and many.
The relationship between two entities may be read in either direction, using this
format:
Each occurrence (of this entity) is related to (minimum, maximum) (of this
other entity).
In a class model, the term association is used instead of relationship and
multiplicity is used instead of cardinality.
.4 Diagrams
Both data models and class models may have one or more diagrams that show
entities, attributes, and relationships.
The diagram in a data model is called an entity-relationship diagram (ERD). In a
class model, the diagram is called a class diagram.



Techniques
Data Modelling
259
Figure 10.15.1: Entity-Relationship Diagram (Crow's Foot Notation)
Each entity is shown as a
rectangle with the entity
name.
The unique identifier of the
entity is shown under the
entity name.
relationship left to right
relationship right to left
Entity 1
Unique Identifier
Attribute
Entity 2
Unique Identifier
Attribute
Entity 3
Unique Identifier
Attribute 1
Attribute 2
The attributes of the entity
are listed below the unique
identifier.
Relationships are indicated by
a line, which is annotated to
show cardinality.
Entity 4
Unique Identifier
Attribute
Cardinality
Any number (zero
to many)
Zero to One
Only One
Any number
from one to
many
Entity
Entity
Entity
Entity



Data Modelling
Techniques
260
Figure 10.15.2: Class Diagram (UML®)
.5 Metadata
A data model optionally contains metadata describing what the entities
represent, when and why they were created or changed, how they should be
used, how often they are used, when, and by whom. There could be restrictions
on their creation or use, as well as security, privacy, and audit constraints on
specific entities or whole groups of entities.
10.15.4
Usage Considerations
.1 Strengths
• Can be used to define and communicate a consistent vocabulary used by
domain subject matter experts and implementation subject matter experts.
• Review of a logical data model helps to ensure that the logical design of
persistent data correctly represents the business need.
• Provides a consistent approach to analyzing and documenting data and its
relationships.
The name of the class is listed here. It
may optionally have a stereotype which
defines additional properties.
Relationships are indicated
by a line, which may also show
multiplicity.
1
The attributes of the class are
listed in a box below the name.
Operations are listed below the
attributes.
Multiplicity
Any number
(zero to many)
Must be exactly X
Any number
from X to Y
Any number from
one to many
0..*
<<stereotype>>
Class 1
Attribute 1: Attribute Type
Attribute 2: Attribute Type
Operation 1
Operation 2
Operation 3
Class 2
Attribute 1
Attribute 2
Attribute 3
Attribute 4
1..*
X..Y
X
*
Class
Class
Class
Class



Techniques
Decision Analysis
261
• Offers the flexibility of different levels of detail, which provides just enough
information for the respective audience.
• Formal modelling of the information held by the business may expose new
requirements as inconsistencies are identified.
.2 Limitations
• Following data modelling standards too rigorously may lead to models that are
unfamiliar to people without a background in IT.
• May extend across multiple functional areas of the organization, and so beyond
the business knowledge base of individual stakeholders.
10.16
Decision Analysis
10.16.1
Purpose
Decision analysis formally assesses a problem and possible decisions in order to
determine the value of alternate outcomes under conditions of uncertainty.
10.16.2
Description
Decision analysis examines and models the possible consequences of different
decisions about a given problem. A decision is the act of choosing a single course
of action from several uncertain outcomes with different values. The outcome
value may take different forms depending on the domain, but commonly include
financial value, scoring, or a relative ranking dependent on the approach and
evaluation criteria used by the business analyst.
Decisions are often difficult to assess when:
• the problem is poorly defined,
• the action leading to a desired outcome is not fully understood,
• the external factors affecting a decision are not fully understood, or
• the value of different outcomes is not understood or agreed upon by the
various stakeholders and does not allow for direct comparison.
Decision analysis helps business analysts evaluate different outcome values under
conditions of uncertainty or in highly complex situations. A variety of decision
analysis approaches are available. The appropriate approach depends on the level
of uncertainty, risk, quality of information, and available evaluation criteria.
Effective decision analysis requires an understanding of:
• the values, goals, and objectives that are relevant to the decision problem,
• the nature of the decision that must be made,
• the areas of uncertainty that affect the decision, and
• the consequences of each potential decision.



Decision Analysis
Techniques
262
Decision analysis approaches use the following activities:

## Define Problem Statement: clearly describe the decision problem to be


addressed.

## Evaluate Alternatives: determine a logical approach to analyze the


alternatives. An agreement of evaluation criteria can also be determined
at the beginning of this activity.

## Choose Alternative to Implement: the stakeholders responsible for


making the decision choose which alternative will be implemented based
on the decision analysis results.

## Implement Choice: implement the chosen alternative.


There are a number of decision analysis tools available to assist the business
analyst and decision makers in making objective decisions. Some of the tools and
techniques are best for deciding between two alternatives, while others handle
multiple alternatives.
Some general decision analysis tools and techniques include:
• pro versus con considerations,
• force field analysis,
• decision tables,
• decision trees,
• comparison analysis,
• analytical hierarchy process (AHP),
• totally-partially-not (TPN),
• multi-criteria decision analysis (MCDA), and
• computer-based simulations and algorithms.
10.16.3
Elements
.1 Components of Decision Analysis
General components of decision analysis include:
• Decision to be Made or Problem Statement: a description of what the
decision question or problem is about.
• Decision Maker: person or people responsible for making the final
decision.
• Alternative: a possible proposition or course of action.
• Decision Criteria: evaluation criteria used to evaluate the alternatives.



Techniques
Decision Analysis
263
.2 Decision Matrices
The tables below provide examples of a a simple decision matrix and a weighted
decision matrix.
A simple decision matrix checks whether or not each alternate meets each
criterion being evaluated, and then totals the number of criteria matched for each
alternate. In this example, Alternate 1 would likely be selected because it matches
the most criteria.
A weighted decision matrix assesses options in which each criterion is weighted
based on importance. The higher the weighting, the more important the
criterion. In this example, the criteria are weighted on a scale of 1-5, where 5
indicates the most important. The alternates are ranked per criterion on a scale of
1-5, where 5 indicates the best match. In this example, Alternate 3 would likely
be selected due to its high weighted score.
.3 Decision Trees
For more
information on
decision trees, see
Decision
Modelling
(p. 265).
A decision tree is a method of assessing the preferred outcome where multiple
sources of uncertainty may exist. A decision tree allows for assessment of
responses to uncertainty to be factored across multiple strategies.
Decision trees include:
• Decision Nodes: that include different strategies.
• Chance Nodes: that define uncertain outcomes.
• Terminator or End Nodes: that identify a final outcome of the tree.
Table 10.16.1: Simple Decision Matrix
Alternate 1
Alternate 2
Alternate 3
Criterion 1
Meets criterion
n/a
n/a
Criterion 2
Meets criterion
Meets criterion
Meets criterion
Criterion 3
n/a
Meets criterion
Meets criterion
Criterion 4
Meets criterion
n/a
n/a
Score
3
2
2
Table 10.16.2: Weighted Decision Matrix
Criterion
Weighting
Alternate 1
Alt 1
Value
Alternate 2
Alt 2
Value
Alternate 3
Alt 3
Value
Criterion 1
1
Rank = 1*3
3
Rank = 1*5
5
Rank = 1*2
2
Criterion 2
1
Rank = 1*5
5
Rank = 1*4
4
Rank = 1*3
8
Criterion 3
3
Rank = 3*5
15
Rank = 3*1
3
Rank = 3*5
15
Criterion 4
5
Rank = 5*1
5
Rank = 5*5
25
Rank = 5*3
15
Weighted
Score
28
37
40



Decision Analysis
Techniques
264
.4 Trade-offs
Trade-offs become relevant whenever a decision problem involves multiple,
possibly conflicting, objectives. Because more than one objective is relevant, it is
not sufficient to simply find the maximum value for one variable (such as the
financial benefit for the organization). When making trade-offs, effective
methods include:
• Elimination of dominated alternatives: a dominated alternative is any
option that is clearly inferior to some other option. If an option is equal to
or worse than some other option when rated against the objectives, the
other option can be said to dominate it. In some cases, an option may also
be dominated if it only offers very small advantages but has significant
disadvantages.
• Ranking objectives on a similar scale: one method of converting
rankings to a similar scale is proportional scoring. Using this method, the
best outcome is assigned a rating of 100, the worst a rating of 0, and all
other outcomes are given a rating based on where they fall between those
two scores. If the outcomes are then assigned weights based on their
relative importance, a score can be assigned to each outcome and the best
alternative assigned using a decision tree.
10.16.4
Usage Considerations
.1 Strengths
• Provides business analysts with a prescriptive approach for determining
alternate options, especially in complex or uncertain situations.
• Helps stakeholders who are under pressure to assess options based on criteria,
thus reducing decisions based on descriptive information and emotions.
• Requires stakeholders to honestly assess the importance they place on different
alternate outcomes in order to help avoid false assumptions.
• Enables business analysts to construct appropriate metrics or introduce relative
rankings for outcome evaluation in order to directly compare both the financial
and non-financial outcome evaluation criteria.
.2 Limitations
• The information to conduct proper decision analysis may not be available in
time to make the decision.
• Many decisions must be made immediately, without the luxury of employing a
formal or even informal decision analysis process.
• The decision maker must provide input to the process and understand the
assumptions and model limitations. Otherwise, they may perceive the results
provided by the business analyst as more certain than they are.
• Analysis paralysis can occur when too much dependence is placed on the
decision analysis and in determining probabilistic values.



Techniques
Decision Modelling
265
• Some decision analysis models require specialized knowledge (for example,
mathematical knowledge in probability and strong skills with decision analysis
tools).
10.17
Decision Modelling
10.17.1
Purpose
Decision modelling shows how repeatable business decisions are made.
10.17.2
Description
Decision models show how data and knowledge are combined to make a specific
decision. Decision models can be used for both straightforward and complex
decisions. Straightforward decision models use a single decision table or decision
tree to show how a set of business rules that operate on a common set of data
elements combine to create a decision. Complex decision models break down
decisions into their individual components so that each piece of the decision can
be separately described and the model can show how those pieces combine to
make an overall decision. The information that needs to be available to make the
decision and any sub-decisions can be decomposed. Each sub-decision is
described in terms of the business rules required to make that part of the
decision.
A comprehensive decision model is an overarching model that is linked to
processes, performance measures, and organizations. It shows where the
business rules come from and represents decisions as analytical insight.
The business rules involved in a given decision may be definitional or behavioural.
For instance, a decision 'Validate order' might check that the tax amount is
calculated correctly (a definitional rule) and that the billing address matches the
credit card provided (a behavioural rule).
Decision tables and decision trees define how a specific decision is made. A
graphical decision model can be constructed at various levels. A high-level model
may only show the business decisions as they appear in business processes, while
a more detailed model might show as-is or to-be decision making in enough
detail to act as a structure for all the relevant business rules.
10.17.3
Elements
.1 Types of Models and Notations
There are several different approaches to decision modelling. Decision tables
represent all the rules required to make an atomic decision. Decision trees are
common in some industries, but are generally used much less often than decision
tables. Complex decisions require the combination of multiple simple decisions
into a network. This is shown using dependency or requirements notations.



Decision Modelling
Techniques
266
All of these approaches involve three key elements:
• decision,
• information, and
• knowledge.
Decision Tables
Business decisions use a specific set of input values to determine a particular
outcome by using a defined set of business rules to select one from the available
outcomes. A decision table is a compact, tabular representation of a set of these
rules. Each row (or column) is a rule and each column (or row) represents one of
the conditions of that rule. When all the conditions in a particular rule evaluate to
true for a set of input data, the outcome or action specified for that rule is
selected.
Decision tables generally contain one or more condition columns that map to
specific data elements, as well as one or more action or outcome columns. Each
row can contain a specific condition in each condition column. These are
evaluated against the value of the data element being considered. If all the cells in
a rule are either blank or evaluate to true, the rule is true and the result specified
in the action or outcome column occurs.
Figure 10.17.1: Decision Table
Decision Trees
Decision trees are also used to represent a set of business rules. Each path on a
decision tree leaf node is a single rule. Each level in the tree represents a specific
data element; the downstream branches represent the different conditions that
must be true to continue down that branch. Decision trees can be very effective
for representing certain kinds of rule sets, especially those relating to customer
segmentation.
As with decision tables, a decision tree selects one of the available actions or
outcomes (a leaf node shown on the far right or bottom of the tree) based on the
Loan Amount
<=1000
Eligibility Rules
Age
Eligibility
>18
Eligible
1000–2000
>21
Eligible
>2000
>=25
Eligible
<=18
Ineligible
<=21
Ineligible
<25
Ineligible



Techniques
Decision Modelling
267
specific values passed to it by the data elements that represent the branching
nodes.
In the following decision tree, the rules in the tree share conditions (represented
by earlier nodes in the tree).
Figure 10.17.2: Decision Tree
Decision Requirements Diagrams
A decision requirements diagram is a visual representation of the information,
knowledge, and decision making involved in a more complex business decision.
Decision requirement diagrams contain the following elements:
• Decisions: shown as rectangles. Each decision takes a set of inputs and
selects from a defined set of possible outputs by applying business rules and
other decision logic.
• Input Data: shown as ovals, representing data that must be passed as an
input to a decision on the diagram.
• Business Knowledge Models: shown as a rectangle with the corners cut
off, representing sets of business rules, decision tables, decision trees, or
even predictive analytic models that describe precisely how to make a
decision.
• Knowledge Sources: shown as a document, representing the original
source documents or people from which the necessary decision logic can be
or has been derived.
These nodes are linked together into a network to show the decomposition of
complex decision making into simpler building blocks. Solid arrows show the
information requirements for a decision. These information requirements might
link input data to a decision, to show that this decision requires that data to be
available, or might link two decisions together.
Business knowledge models which describe how to make a specific decision can
be linked to that decision with dashed arrows to display knowledge requirements.
Knowledge sources can be linked to decisions with a dashed, rounded arrow to
show that a knowledge source (for example, a document or person) is an
authority for the decision. This is called an authority requirement.
Amount
<=1000
1000-2000
>2000
>18
<=18
>=25
<25
>21
<=21
Age
Age
Age
Eligible
Ineligible
Eligible
Ineligible
Eligible
Ineligible



Decision Modelling
Techniques
268
Figure 10.17.3: Decision Requirements Diagram
10.17.4
Usage Considerations
.1 Strengths
• Decision models are easy to share with stakeholders, facilitate a shared
understanding, and support impact analysis.
• Multiple perspectives can be shared and combined, especially when a diagram
is used.
• Simplifies complex decision making by removing business rules management
from the process.
• Assists with managing large numbers of rules in decision tables by grouping
rules by decision. This also helps with reuse.
• These models work for rules-based automation, data mining, and predictive
analytics, as well as for manual decisions or business intelligence projects.
.2 Limitations
• Adds a second diagram style when modelling business processes that contain
decisions.This may add unnecessary complexity if the decision is simple and
tightly coupled with the process.
• May limit rules to those required by known decisions and so limit the capture of
rules not related to a known decision.
• Defining decision models may allow an organization to think it has a standard
way of making decisions when it does not. May lock an organization into a
current-state decision-making approach.
• Cuts across organizational boundaries, which can make it difficult to acquire
any necessary sign-off.
• May not address behavioural business rules in a direct fashion.
Knowledge
Source
Input Data
Decision
Input Data
Decision
Business
Knowledge
Business
Knowledge



Techniques
Document Analysis
269
• Business terminology must be clearly defined and shared definitions developed
to avoid data quality issues affecting automated decisions.
10.18
Document Analysis
10.18.1
Purpose
Document analysis is used to elicit business analysis information, including
contextual understanding and requirements, by examining available materials
that describe either the business environment or existing organizational assets.
10.18.2
Description
Document analysis may be used to gather background information in order to
understand the context of a business need, or it may include researching existing
solutions to validate how those solutions are currently implemented. Document
analysis may also be used to validate findings from other elicitation efforts such as
interviews and observations. Data mining is one approach to document analysis
that is used to analyze data in order to determine patterns, group the data into
categories, and determine opportunities for change. The purpose, scope, and
topics to be researched through document analysis are determined based on the
business analysis information being explored. When performing document
analysis, business analysts methodically review the materials and determine
whether the information should be recorded within a work product.
Background research gathered through document analysis may include reviewing
materials such as marketing studies, industry guidelines or standards, company
memos, and organizational charts. By researching a wide variety of source
materials, the business analyst can ensure the need is fully understood in terms of
the environment in which it exists. Document analysis about an existing solution
may include reviewing business rules, technical documentation, training
documentation, problem reports, previous requirements documents, and
procedure manuals in order to validate both how the current solution works and
why it was implemented in its current form. Document analysis can also help
address information gaps that may occur when the subject matter experts (SMEs)
for the existing solution are no longer present or will not be available for the
duration of the elicitation process.
10.18.3
Elements
.1 Preparation
Document analysis materials may originate from public or proprietary sources.
When assessing source documents for analysis, business analysts consider:
• whether or not the source’s content is relevant, current, genuine, and
credible,



Document Analysis
Techniques
270
• whether or not the content is understandable and can be easily conveyed
to stakeholders as needed, and
• defining both the data to be mined (based on the classes of data needed)
and the data clusters that provide items grouped by logical relationships.
.2 Document Review and Analysis
Performing document analysis includes:
• Conducting a detailed review of each document’s content and recording
relevant notes associated with each topic. Notes can be recorded using a
document analysis chart that includes the topic, type, source, verbatim
details, a paraphrased critique, and any follow-up issues or actions for each
document that is reviewed.
• Identifying if any notes conflict or are duplicates.
• Noting any gaps in knowledge in which the findings about certain topics
are limited. It may be necessary to perform additional research to revisit
these topics, or to drill down at a sub-topic level.
.3 Record Findings
When the information elicited through document analysis is used in a work
product, the business analyst considers:
• if the content and level of detail is appropriate for the intended audience,
and
• if the material should be transformed into visual aids such as graphs,
models, process flows, or decision tables in order to help improve
understanding.
10.18.4
Usage Considerations
.1 Strengths
• Existing source material may be used as a basis for analysis.
• The business analyst does not need to create content.
• Existing sources, although possibly outdated, can be used as a point of
reference to determine what is current and what has changed.
• Results can be used to validate against the results of other requirements
elicitation techniques.
• Findings can be presented in formats that permit ease of review and reuse.
.2 Limitations
• Existing documentation may be out of date or invalid (incorrect, missing
information, unreadable, unreviewed or unapproved).
• Authors may not be available for questions.



Techniques
Estimation
271
• Primarily helpful only for evaluating the current state, via review of as-is
documentation.
• If there is a wide range of sources, the effort may be very time-consuming and
lead to information overload and confusion.
10.19
Estimation
10.19.1
Purpose
Estimation is used by business analysts and other stakeholders to forecast the cost
and effort involved in pursuing a course of action.
10.19.2
Description
Estimation is used to support decision making by predicting attributes such as:
• cost and effort to pursue a
course of action,
• expected solution benefits,
• project cost,
• business performance,
• potential value anticipated from
a solution, and
• costs of creating a solution,
• costs of operating a solution,
• potential risk impact.
The result of estimation is sometimes expressed as a single number. Representing
the results of estimation as a range, with minimum and maximum values along
with probability, may present a higher degree of effectiveness for stakeholders.
This range is referred to as a confidence interval and serves as a measure of the
level of uncertainty. The less information that is available to the estimator, the
wider the confidence interval will be.
Estimation is an iterative process. Estimates are reviewed as more information
becomes available, and are also revised (if appropriate). Many estimation
techniques rely on historical performance records from the organization in order
to calibrate estimates against prior experience. Each estimate can include an
assessment of its associated level of uncertainty.
10.19.3
Elements
.1 Methods
Various methods of estimation are used for specific situations. In each case it is
important for the estimators to have an agreed-upon description of the elements
to be estimated, often in the form of a work breakdown structure or some other
decomposition of all the work being estimated. When developing and delivering
an estimate, constraints and assumptions also need to be clearly communicated.
Common estimation methods include:
• Top-down: examining the components at a high level in a hierarchical
breakdown.



Estimation
Techniques
272
• Bottom-up: using the lowest-level elements of a hierarchical breakdown to
examine the work in detail and estimate the individual cost or effort, and
then summing across all elements to provide an overall estimate.
• Parametric Estimation: use of a calibrated parametric model of the
element attributes being estimated. It is important that the organization
uses its own history to calibrate any parametric model, since the attribute
values reflect the skills and abilities of both its staff and the processes used
to do work.
• Rough Order of Magnitude (ROM): a high-level estimate, generally
based on limited information, which may have a very wide confidence
interval.
• Rolling Wave: repeated estimates throughout an initiative or project,
providing detailed estimates for near-term activities (such as an iteration of
the work) extrapolated for the remainder of the initiative or project.
• Delphi: uses a combination of expert judgment and history. There are
several variations on this process, but they all include individual estimates,
sharing the estimates with experts, and having several rounds of estimation
until consensus is reached. An average of the three estimates is used.
• PERT: each component of the estimate is given three values: (1) Optimistic
value, representing the best-case scenario, (2) Pessimistic value,
representing the worst-case scenario, (3) Most Likely value. Then a PERT
value for each estimated component is computed as a weighted average:
(Optimistic + Pessimistic + (4 times Most Likely))/6.
.2 Accuracy of the Estimate
The accuracy of an estimate is a measure of uncertainty that evaluates how close
an estimate is to the actual value measured later. It can be calculated as a ratio of
the width of the confidence interval to its mean value and then expressed as a
percentage. When there is little information, such as early in the development of
a solution approach, a Rough Order of Magnitude (ROM) estimate is delivered,
which is expected to have a wide range of possible values and a high level of
uncertainty.
ROM estimates are often no more than +50% to -50% accurate. A definitive
estimate, which is much more accurate, can be made as long as more real-world
data is collected. Definitive estimates that are used for predicting timelines, final
budgets, and resource needs should ideally be accurate within 10% or less.
Teams can combine the use of ROM estimates and definitive estimates
throughout a project or initiative using rolling wave estimates. A team creates a
definitive estimate for the next iteration or phase (for which they have adequate
information), while the remainder of the work is given a ROM estimate. As the
end of the iteration or phase approaches, a definitive estimate is made for the
work of the next iteration or phase and the ROM estimate for remaining activities
is refined.



Techniques
Estimation
273
.3 Sources of Information
Estimators consider available information from prior experience along with the
attributes being estimated.
Some common sources of information include:
• Analogous Situations: using an element (project, initiative, risk, or other)
that is like the element being estimated.
• Organization History: previous experiences of the organization with
similar work. This is most helpful if the prior work was done by the same or
a similarly-skilled team and by using the same techniques.
• Expert Judgment: leveraging the knowledge of individuals about the
element being estimated. Estimating often relies on the expertise of those
who have performed the work in the past, internal or external to the
organization. When using external experts, estimators take into account the
relevant skills and abilities of those doing the work being estimated.
.4 Precision and Reliability of Estimates
When multiple estimates are made for a particular attribute, the precision of the
resulting estimate is a measure of agreement between the estimates (how close
they are to each other). By examining measures of imprecision such as variance or
standard deviation, estimators can determine their level of agreement.
The reliability of an estimate (its repeatability) is reflected in the variation of
estimates made by different methods of estimating or by different estimators.
To illustrate the level of reliability and precision, an estimate is often expressed as
a range of values with an associated confidence level. That is, for a given
summary estimate value and confidence level, the range of values is the expected
range of possible values based on the estimates provided. For example, if a team
estimated that some task would take 40 hours, a 90% confidence interval might
be 36 to 44 hours, depending on what they gave as individual estimates. A 95%
confidence interval might be 38 to 42 hours. In general, the higher the
confidence level in the estimate, the narrower the range would be.
To provide estimates with a particular level of confidence, estimators can use a
technique such as PERT. Using the multiple estimates for each component of the
estimate, a probability distribution can be constructed. This distribution provides a
way to compute an overall estimate (incorporating all of the estimated elements)
as a range of values, with an associated level of confidence.
.5 Contributors to Estimates
The estimators of an element are frequently those responsible for that element.
The estimate of a team is usually more accurate than the estimate of one
individual, since it incorporates the expertise of all team members.
In some cases, an organization has a group that performs estimation for much of
the work of the organization. This is done with care, so that the estimate reflects
the likely context of the element being estimated.



Financial Analysis
Techniques
274
When an organization needs a high level of confidence in the estimate of some
critical element, it may call on an external expert to perform or review the
estimate. The organization may compare an independent estimate against their
internal estimate to determine what adjustments may be needed.
10.19.4
Usage Considerations
.1 Strengths
• Estimates provide a rationale for an assigned budget, time frame, or size of a
set of elements.
• Without an estimate, teams making a change may be provided an unrealistic
budget or schedule for their work.
• Having a small team of knowledgeable individuals provide an estimate by
following a defined technique generally results in a closer predictor of the
actual value than if an estimate was made by one individual.
• Updating an estimate throughout a work cycle, in which the estimated
elements are refined over time, incorporates knowledge and helps ensure
success.
.2 Limitations
• Estimates are only as accurate as the level of knowledge about the elements
being estimated. Without organization or local knowledge, estimates can vary
widely from the actual values determined later.
• Using just one estimation method may lead stakeholders to have unrealistic
expectations.
10.20
Financial Analysis
10.20.1
Purpose
Financial analysis is used to understand the financial aspects of an investment, a
solution, or a solution approach.
10.20.2
Description
Financial analysis is the assessment of the expected financial viability, stability, and
benefit realization of an investment option. It includes a consideration of the
tbbotal cost of the change as well as the total costs and benefits of using and
supporting the solution.
Business analysts use financial analysis to make a solution recommendation for an
investment in a specific change initiative by comparing one solution or solution
approach to others, based on analysis of the:
• initial cost and the time frame in which those costs are incurred,
• expected financial benefits and the time frame in which they will be incurred,
• ongoing costs of using the solution and supporting the solution,



Techniques
Financial Analysis
275
• risks associated with the change initiative, and
• ongoing risks to business value of using that solution.
A combination of analysis techniques are typically used because each provides a
different perspective. Executives compare the financial analysis results of one
investment option with that of other possible investments to make decisions
about which change initiatives to support.
Financial analysis deals with uncertainty, and as a change initiative progresses
through its life cycle, the effects of that uncertainty become better understood.
Financial analysis is continuously applied during the initiative to determine if the
change is likely to deliver enough business value such that it should continue. A
business analyst may recommend that a change initiative be adjusted or stopped
if new information causes the financial analysis results to no longer support the
initial solution recommendation.
10.20.3
Elements
.1 Cost of the Change
The cost of a change includes the expected cost of building or acquiring the
solution components and the expected costs of transitioning the enterprise from
the current state to the future state. This could include the costs associated with
changing equipment and software, facilities, staff and other resources, buying
out existing contracts, subsidies, penalties, converting data, training,
communicating the change, and managing the roll out. These costs may be
shared between organizations within the enterprise.
.2 Total Cost of Ownership (TCO)
The total cost of ownership (TCO) is the cost to acquire a solution, the cost of
using the solution, and the cost of supporting the solution for the foreseeable
future, combined to help understand the potential value of a solution. In the case
of equipment and facilities, there is often a generally agreed to life expectancy.
However, in the case of processes and software, the life expectancy is often
unknown. Some organizations assume a standard time period (for example, three
to five years) to understand the costs of ownership of intangibles like processes
and software.
.3 Value Realization
Value is typically realized over time. The planned value could be expressed on an
annual basis, or could be expressed as a cumulative value over a specific time period.
.4 Cost-Benefit Analysis
Cost-benefit analysis (sometimes called benefit-cost analysis) is a prediction of the
expected total benefits minus the expected total costs, resulting in an expected
net benefit (the planned business value).
Assumptions about the factors that make up the costs and benefits should be
clearly stated in the calculations so they can be reviewed, challenged and



Financial Analysis
Techniques
276
approved. The costs and benefits will often be estimated based on those
assumptions, and the estimating methodology should be described so that it can
be reviewed and adjusted if necessary.
The time period of a cost-benefit analysis should look far enough into the future
that the solution is in full use, and the planned value is being realized. This will
help to understand which costs will be incurred and when, and when the
expected value should be realized.
Some benefits may not be realized until future years. Some project and operating
costs may be recognized in future years. The cumulative net benefits could be
negative for some time until the future.
In some organizations, all or part of the costs associated with the change may be
amortized over several years, and the organization may require the cost-benefit
Table 10.20.1: Example of a Cost-Benefit Analysis
Year 0
Year 1
Year 2
Year 3
Expected Benefits
Revenue
$XXXX
$XXXX
$XXXX
Reduced operating costs
$XXXX
$XXXX
$XXXX
Time savings
$XXXX
$XXXX
$XXXX
Reduced cost of errors
$XXXX
$XXXX
$XXXX
Increased customer
satisfaction
$XXXX
$XXXX
$XXXX
Decreased cost of
compliance
$XXXX
$XXXX
$XXXX
Other
$XXXX
$XXXX
$XXXX
Total Annual benefits
$0
$XXXX
$XXXX
$XXXX
Costs
Project costs
$XXXX
$XXXX
$0
$0
Ongoing support
$0
$XXXX
$XXXX
$XXXX
New facilities
$XXXX
$0
$0
$XXXX
Licensing
$0
$XXXX
$XXXX
$XXXX
Infrastructure renewal
$XXXX
$0
$XXXX
$0
Other
$0
$XXXX
$0
$XXXX
Total Costs
$XXXX
$XXXX
$XXXX
$XXXX
Net Benefits
-$XXXX
$XXXX
$XXXX
$XXXX
Cumulative Net Benefits
-$XXXX
-$XXXX
-$XXXX
$XXXX



Techniques
Financial Analysis
277
analysis to reflect this.
During a change initiative, as the expected costs become real costs, the business
analyst may re-examine the cost-benefit analysis to determine if the solution or
solution approach is still viable.
.5 Financial Calculations
Organizations use a combination of standard financial calculations to understand
different perspectives about when and how different investments deliver value.
These calculations take into consideration the inherent risks in different
investments, the amount of upfront money to be invested compared to when the
benefits will be realized, a comparison to other investments the organization
could make, and the amount of time it will take to recoup the original
investment.
Financial software, including spreadsheets, typically provide pre-programmed
functions to correctly perform these financial calculations.
Return on Investment
The return on investment (ROI) of a planned change is expressed as a percentage
measuring the net benefits divided by the cost of the change. One change
initiative, solution, or solution approach may be compared to that of others to
determine which one provides the greater overall return relative to the amount of
the investment.
The formula to calculate ROI is:
Return on Investment = (Total Benefits – Cost of the Investment) / Cost of
the Investment.
The higher the ROI, the better the investment.
When making a comparison between potential investments, the business analyst
should use the same time period for both.
Discount Rate
The discount rate is the assumed interest rate used in present value calculations. In
general, this is similar to the interest rate that the organization would expect to
earn if it invested its money elsewhere. Many organizations use a standard
discount rate, usually determined by its finance officers, to evaluate potential
investments such as change initiatives using the same assumptions about expected
interest rates. Sometimes a larger discount rate is used for time periods that are
more than a few years into the future to reflect greater uncertainty and risk.
Present Value
Different solutions and different solution approaches could realize benefits at
different rates and over a different time. To objectively compare the effects of
these different rates and time periods, the benefits are calculated in terms of



Financial Analysis
Techniques
278
present-day value. The benefit to be realized sometime in the future is reduced by
the discount rate to determine its worth today.
The formula to calculate present value is:
Present Value = Sum of (Net Benefits in that period / (1 + Discount Rate for
that period)) for all periods in the cost-benefit analysis.
Present value is expressed in currency. The higher the present value, the greater
the total benefit.
Present value does not consider the cost of the original investment.
Net Present Value
Net present value (NPV) is the present value of the benefits minus the original cost
of the investment. In this way, different investments, and different benefit
patterns can be compared in terms of present day value. The higher the NPV, the
better the investment.
The formula to calculate net present value is:
Net Present Value = Present Value – Cost of Investment
Net present value is expressed in currency. The higher the NPV, the better the
investment.
Internal Rate of Return
The internal rate of return (IRR) is the interest rate at which an investment breaks
even, and is usually used to determine if the change, solution or solution
approach is worth investing in. The business analyst may compare the IRR of one
solution or solution approach to a minimum threshold that the organization
expects to earn from its investments (called the hurdle rate). If the change
initiative’s IRR is less than the hurdle rate, then the investment should not be
made.
Once the planned investment passes the hurdle rate, it could be compared to
other investments of the same duration. The investment with the higher IRR
would be the better investment. For example, the business analyst could compare
two solution approaches over the same time period, and would recommend the
one with the higher IRR.
The IRR is internal to one organization since it does not consider external
influencers such as inflation or fluctuating interest rates or a changing business
context.
The IRR calculation is based on the interest rate at which the NPV is 0:
Net Present Value = (-1 x Original Investment) + Sum of (net benefit for
that period / (1 + IRR) for all periods) = 0.



Techniques
Focus Groups
279
Payback Period
The payback period provides a projection on the time period required to generate
enough benefits to recover the cost of the change, irrespective of the discount
rate. Once the payback period has passed the initiative would normally show a
net financial benefit to the organization, unless operating costs rise. There is no
standard formula for calculating the payback period. The time period is usually
expressed in years or years and months.
10.20.4
Usage Considerations
.1 Strengths
• Financial analysis allows executive decision makers to objectively compare very
different investments from different perspectives.
• Assumptions and estimates built into the benefits and costs, and into the
financial calculations, are clearly stated so that they may be challenged or
approved.
• It reduces the uncertainty of a change or solution by requiring the identification
and analysis of factors that will influence the investment.
• If the context, business need, or stakeholder needs change during a change
initiative, it allows the business analyst to objectively re-evaluate the
recommended solution.
.2 Limitation
• Some costs and benefits are difficult to quantify financially.
• Because financial analysis is forward looking, there will always be some
uncertainty about expected costs and benefits
• Positive financial numbers may give a false sense of security—they may not
provide all the information required to understand an initiative.
10.21
Focus Groups
10.21.1
Purpose
A focus group is a means to elicit ideas and opinions about a specific product,
service, or opportunity in an interactive group environment. The participants,
guided by a moderator, share their impressions, preferences, and needs.
10.21.2
Description
A focus group is composed of pre-qualified participants whose objective is to
discuss and comment on a topic within a context. The participants share their
perspectives and attitudes about a topic and discuss them in a group setting. This



Focus Groups
Techniques
280
sometimes leads participants to re-evaluate their own perspectives in light of
others' experiences. A trained moderator manages the preparation of the session,
assists in selecting participants, and facilitates the session. If the moderator is not
the business analyst, he/she may work with the business analyst to analyze the
results and produce findings that are reported to the stakeholders. Observers may
be present during the focus group session, but do not typically participate.
A focus group can be utilized at various points in an initiative to capture
information or ideas in an interactive manner. If the group’s topic is a product
under development, the group’s ideas are analyzed in relationship to the stated
requirements. This may result in updating existing requirements or uncovering
new requirements. If the topic is a completed product that is ready to be
launched, the group’s report could influence how to position the product in the
market. If the topic is a product in production, the group’s report may provide
direction on the revisions to the next release of requirements. A focus group may
also serve as a means to assess customer satisfaction with a product or service.
A focus group is a form of qualitative research. The activities are similar to that of
a brainstorming session, except that a focus group is more structured and focused
on the participants’ perspectives concerning a specific topic. It is not a interview
session conducted as a group; rather, it is a discussion during which feedback is
collected on a specific subject. The session results are usually analyzed and
reported as themes and perspectives rather than numerical findings.
10.21.3
Elements
.1 Focus Group Objective
A clear and specific objective establishes a defined purpose for the focus group.
Questions are formulated and discussions are facilitated with the intent of
meeting the objective.
.2 Focus Group Plan
The focus group plan ensures that all stakeholders are aware of the purpose of
the focus group and agree on the expected outcomes, and that the session meets
the objectives.
The focus group plan defines activities that include:
• Purpose: creating questions that answer the objective, identifying key
topics to be discussed, and recommending whether or not discussion
guides will be used.
• Location: identifying whether the session will be in-person or online, as
well as which physical or virtual meeting place will be used.
• Logistics: identifying the size and set up of the room, other facilities that
may be required, public transportation options, and the time of the session.
• Participants: identifying the demographics of those actively engaged in
the discussion, if any observers are required, and who the moderators and



Techniques
Focus Groups
281
recorders will be. Consideration may also be given to incentives for
participants.
• Budget: outlining the costs of the session and ensuring that resources are
allocated appropriately.
• Timelines: establishing the period of time when the session or sessions will
be held, as well as when any reports or analysis resulting from the focus
group are expected.
• Outcomes: identifying how the results will be analyzed and communicated
and the intended actions based on the results.
.3 Participants
A successful focus group session has participants who are willing to both offer
their insights and perspectives on a specific topic and listen to the opinions of the
other participants. A focus group typically has 6 to 12 attendees. It may be
necessary to invite additional individuals to compensate for those who do not
attend the session due to scheduling conflicts, emergencies, or other reasons. If
many participants are needed, it may be necessary to run more than one focus
group. Often participants of a focus group are paid for their time.
The demographics of the participants are determined based on the objective of
the focus group.
.4 Discussion Guide
A discussion guide provides the moderator with a prepared script of specific
questions and topics for discussion that meet the objective of the session.
Discussion guides also include the structure or framework that the moderator will
follow. This includes obtaining general feedback and comments before delving
into specifics. Discussion guides also remind the moderator to welcome and
introduce the participants, as well as to explain the objectives of the session, how
the session will be conducted, and how the feedback will be used.
.5 Assign a Moderator and Recorder
The moderator is both skilled at keeping the session on track and knowledgeable
about the initiative. Moderators are able to engage all participants and are
adaptable and flexible. The moderator is an unbiased representative of the
feedback process.
The recorder takes notes to ensure the participant’s opinions are accurately
recorded.
The business analyst can fill the role of either the moderator or the recorder. The
moderator and recorder are not considered active participants in the focus group
session and do not submit feedback.
.6 Conduct the Focus Group
The moderator guides the group’s discussion, follows a prepared script of specific
issues, and ensures that the objectives are met. However, the group discussion



Focus Groups
Techniques
282
should appear free-flowing and relatively unstructured to the participants. A
session is typically one to two hours in length. A recorder captures the group’s
comments.
.7 After the Focus Group
The results of the focus group are transcribed as soon as possible after the session
has ended. The business analyst analyzes and documents the participants’
agreements and disagreements, looks for trends in the responses, and creates a
report that summarizes the results.
10.21.4
Usage Considerations
.1 Strengths
• The ability to elicit data from a group of people in a single session saves both
time and costs as compared to conducting individual interviews with the same
number of people.
• Effective for learning people's attitudes, experiences, and desires.
• Active discussion and the ability to ask others questions creates an environment
in which participants can consider their personal view in relation to other
perspectives.
• An online focus group is useful when travel budgets are limited and
participants are distributed geographically.
• Online focus group sessions can be recorded easily for playback.
.2 Limitations
• In a group setting, participants may be concerned about issues of trust or may
be unwilling to discuss sensitive or personal topics.
• Data collected about what people say may not be consistent with how people
actually behave.
• If the group is too homogeneous their responses may not represent the
complete set of requirements.
• A skilled moderator is needed to manage group interactions and discussions.
• It may be difficult to schedule the group for the same date and time.
• Online focus groups limit interaction between participants.
• It is difficult for the moderator of an online focus group to determine attitudes
without being able to read body language.
• One vocal participant could sway the results of the focus group.



Techniques
Functional Decomposition
283
10.22
Functional Decomposition
10.22.1
Purpose
Functional decomposition helps manage complexity and reduce uncertainty by
breaking down processes, systems, functional areas, or deliverables into their
simpler constituent parts and allowing each part to be analyzed independently.
10.22.2
Description
Functional decomposition approaches the analysis of complex systems and
concepts by considering them as a set of collaborating or related functions,
effects, and components. This isolation helps reduce the complexity of the
analysis. Breaking down larger components into sub-components allows scaling,
tracking, and measuring work effort for each of them. It also facilitates evaluation
of the success of each sub-component as it relates to other larger or smaller
components.
The depth of decomposition may vary depending on the nature of components
and objectives. Functional decomposition assumes that sub-components can and
do completely describe their parent components. Any sub-component can have
only one parent component when developing the functional hierarchy.
The diagram below provides an example of how a function can be broken down
to manageable, measurable sub-components.
Figure 10.22.1: Functional Decomposition Diagram
Process 1.1
Activity 1.1.3
Function
Subfunction
1
Process 1.3
Process 1.2
Activity 1.2.1
Activity 1.1.1
Activity 1.1.2
Activity 1.2.2
Subfunction
2
Process 2.1
Process 2.2
Process 2.3
Process 2.4
Process 2.1.1
Process 2.2.2



Functional Decomposition
Techniques
284
10.22.3
Elements
.1 Decomposition Objectives
Objectives of functional decomposition both drive the process of decomposition
and define what to decompose, how to decompose, and how deeply to
decompose.
The objectives may include:
• Measuring and Managing: to isolate specific manageable factors that
contribute to the overall result, or to identify important metrics and
indicators.
• Designing: to simplify a design problem by reducing and isolating the
object of design.
• Analyzing: to study the essential properties and behaviours of an artifact
or phenomenon in isolation from its encompassing environment.
• Estimating and Forecasting: to decrease the level of uncertainty by
breaking down a complex value into its constituent factors.
• Reusing: to create a reusable solution building block that serves a specific
function for various processes.
• Optimization: to detect or alleviate a bottleneck, reduce function cost, or
improve process quality.
• Substitution: to make a specific implementation of a solution component
or a function easily replaceable without impacting the system as a whole.
• Encapsulation: combining elements to make one element.
.2 Subjects of Decomposition
Functional decomposition applies to a wide variety of versatile subjects, such as:
• Business Outcomes: for example, income, profit, expenses, volume of
service, or volume of production.
• Work to be Done: this decomposition (known as a Work Breakdown
Structure or WBS) breaks endeavours into phases, milestones, work
activities, tasks, work items, and deliverables.
• Business Process: to identify its constituent parts for the purposes of
measuring, managing, optimizing, or reusing the process or its
components.
• Function: to enable its optimization or implementation.
• Business Unit: to enable its reverse engineering and design.
• Solution Component: to enable its design, implementation, or change.
• Activity: to enable its implementation, modification, optimization,
measurement, and estimation.
• Products and Services: to design, implement, and improve them.



Techniques
Functional Decomposition
285
• Decisions: for enabling, improving, or supporting them by identifying their
inputs, underlying models, dependencies, and outcomes.
.3 Level of Decomposition
The appropriate level of functional decomposition defines where, why, and when
to stop decomposing the subject in order to meet the analysis objectives. The
process of functional decomposition continues until the business analyst has just
enough understanding and detail to proceed and can apply the results of
decomposition in the execution of other tasks.
.4 Representation of Decomposition Results
Representations of functional decomposition results allow business analysts to
both validate and verify the results and to use them to solve other tasks. The
results can be expressed as a combination of plain textual descriptions,
hierarchical lists, descriptions using special formal notations (for example,
mathematical formulas, Business Process Execution Language, or programming
languages), and visual diagrams. A wide variety of diagramming techniques can
be used to represent functional decomposition, including:
• Tree diagrams: represent hierarchical partitioning of work, activities, or
deliverables.
• Nested diagrams: illustrate hierarchical part-to-whole relationships
between decomposition results.
• Use Case diagrams: represent decomposition of a higher-level use case.
• Flow diagrams: depict results of a process or function decomposition.
• State Transition diagrams: explain the behaviour of an object inside its
composite state.
• Cause-Effect diagrams: elaborate on events, conditions, activities, and
effects involved in producing a complex outcome or phenomenon.
• Decision Trees: detail the structure of a complex decision and its potential
outcomes.
• Mind Maps: represent information in categories.
• Component diagram: depicts how components are wired together to
form larger components and/or software systems.
• Decision Model and Notation: is used to analyze the business logic to
ensure that it has inferential and business integrity.
10.22.4
Usage Considerations
.1 Strengths
• Makes complex endeavours possible by breaking down complex problems into
feasible parts.



Glossary
Techniques
286
• Provides a structured approach to building a shared understanding of complex
matters among a diverse group of stakeholders.
• Simplifies measurement and estimation of the amount of work involved in
pursuing a course of action, defining scope of work, and defining process
metrics and indicators.
.2 Limitations
• Missing or incorrect information at the time decomposition is performed may
later cause a need to revise the results of decomposition partially or entirely.
• Many systems cannot be fully represented by simple hierarchical relationships
between components because the interactions between components cause
emergent characteristics and behaviours.
• Every complex subject allows multiple alternative decompositions. Exploring all
alternatives can be a challenging and time-consuming task, while sticking with
a single alternative may disregard important opportunities and result in a sub-
optimal solution.
• Performing functional decomposition may involve deep knowledge of the
subject and extensive collaboration with diverse stakeholders.
10.23
Glossary
10.23.1
Purpose
A glossary defines key terms relevant to a business domain.
10.23.2
Description
Glossaries are used to provide a common understanding of terms that are used by
stakeholders. A term may have different meanings for any two people. A list of
terms and established definitions provides a common language that can be used
to communicate and exchange ideas. A glossary is organized and continuously
accessible to all stakeholders.
10.23.3
Elements
A glossary is a list of terms in a particular domain with definitions for those terms
and their common synonyms. Organizations or industries may use a term
differently than how it is generally understood.
A term is included in the glossary when:
• the term is unique to a domain,
• there are multiple definitions for the term,
• the definition implied is outside of the term's common use, or
• there is a reasonable chance of misunderstanding.



Techniques
Interface Analysis
287
The creation of a glossary should take place in the early stages of a project in
order to facilitate knowledge transfer and understanding. A point of contact
responsible for the maintenance and distribution of the glossary throughout the
initiative is identified. Organizations that maintain glossaries often find additional
uses for this information and are able to leverage the glossary for future
initiatives.
Consider the following when developing a glossary:
• definitions should be clear, concise, and brief,
• acronyms should be spelled out if used in a definition,
• stakeholders should have easy and reliable access to glossaries, and
• the editing of a glossary should be limited to specific stakeholders.
10.23.4
Usage Considerations
.1 Strengths
• A glossary promotes common understanding of the business domain and
better communication among all stakeholders.
• Capturing the definitions as part of an enterprise's documentation provides a
single reference and encourages consistency.
• Simplifies the writing and maintenance of other business analysis information
including but not limited to requirements, business rules, and change strategy.
.2 Limitations
• A glossary requires an owner to perform timely maintenance, otherwise it
becomes outdated and may be ignored.
• It may be challenging for different stakeholders to agree on a single definition
for a term.
10.24
Interface Analysis
10.24.1
Purpose
Interface analysis is used to identify where, what, why, when, how, and for whom
information is exchanged between solution components or across solution
boundaries.
10.24.2
Description
An interface is a connection between two components or solutions. Most
solutions require one or more interfaces to exchange information with other
solution components, organizational units, or business processes.



Interface Analysis
Techniques
288
Interface types include:
• user interfaces, including human users directly interacting with the solution
within the organization,
• people external to the solution such as stakeholders or regulators,
• business processes,
• data interfaces between systems,
• application programming interfaces (APIs), and
• any hardware devices.
Interface analysis defines and clarifies the following:
• who will use the interface,
• what information is being exchanged through the interface, as well as the
volume of the data,
• when information will be exchanged and how frequently,
• where the information exchange will occur,
• why the interface is needed, and
• how the interface is or should be implemented.
The early identification of interfaces allows the business analyst to provide the
context for eliciting more detailed stakeholder requirements, thus determining
adequate functional coverage of the solution to meet stakeholder needs. Early
identification of interfaces reveals which stakeholders will benefit from or
depend on the various components of the solution, which can help the business
analyst determine which stakeholders should be present for other elicitation
techniques.
Figure 10.24.1: Interface Analysis
10.24.3
Elements
.1 Preparing for Identification
The business analyst can leverage other techniques, such as document analysis,
observation, scope modelling, and interviews, in order to understand which
interfaces need to be identified. A context diagram can reveal high-level
Input
Solution
Output
Solution
Validation
or
Transformation
Interface
Message
Message



Techniques
Interface Analysis
289
interfaces between human actors, organizational units, business processes, or
other solution components. The results of this analysis can reveal how frequently
any existing interfaces are being used and any problems with them that may
strengthen the case for change. The results may also help identify any key issues
that need to be resolved in order for an interface solution to be created.
.2 Conduct Interface Identification
Business analysts identify what interfaces are needed in the future state for each
stakeholder or system that interacts with the system. The relationship between
stakeholders and interfaces can be many-to-many or, in some cases, one-to-one.
Some interfaces may be less obvious or less frequent such as an interface used
for regulatory functions or auditing, or for employee training. Identified
interfaces can include interfaces from solutions other than the operational
solution.
For each interface, business analysts:
• describe the function of the interface,
• assess the frequency of the interface usage,
• evaluate which type of interface may be appropriate, and
• elicit initial details about the interface.
.3 Define Interfaces
Requirements for an interface are primarily focused on describing the inputs to
and outputs from that interface, any validation rules that govern those inputs and
outputs, and events that might trigger interactions. There may be a large number
of possible interaction types, each of which needs to be specified. Interactions
may be triggered by the typical or alternate flow of inputs and outputs in the
business solution, or by exceptional events such as failures.
Business analysts consider who will use the interface, what information is passed
over the interface, and when and where the interface takes place. The interface
defines user workflow between systems, user roles and privileges, and any
management objectives for the interface. Interface definition is dependent upon
usability guidelines, such as accessibility requirements or general workflow
requirements.
In order to identify any major design issues, interfaces between solution or
process components and people require detailed analysis of the interface to be
conducted upfront. Interface definition includes:
• the name of the interface,
• the coverage or span of the interface,
• the exchange method between the two entities,
• the message format, and
• the exchange frequency.



Interviews
Techniques
290
10.24.4
Usage Considerations
.1 Strengths
• By engaging in interface analysis early on, increased functional coverage is
provided.
• Clear specification of the interfaces provides a structured means of allocating
requirements, business rules, and constraints to the solution.
• Due to its broad application, it avoids over analysis of fine detail.
.2 Limitations
• Does not provide insight into other aspects of the solution since the analysis
does not assess the internal components.
10.25
Interviews
10.25.1
Purpose
An interview is a systematic approach designed to elicit business analysis
information from a person or group of people by talking to the interviewee(s),
asking relevant questions, and documenting the responses. The interview can
also be used for establishing relationships and building trust between business
analysts and stakeholders in order to increase stakeholder involvement or build
support for a proposed solution.
10.25.2
Description
The interview is a common technique for eliciting requirements. It involves direct
communication with individuals or groups of people who are part of an initiative.
In an interview, the interviewer directs questions to stakeholders in order to
obtain information. One-on-one interviews are the most common. In a group
interview (with more than one interviewee in attendance), the interviewer is
careful to elicit responses from each participant.
There are two basic types of interviews used to elicit business analysis
information:
• Structured Interview: in which the interviewer has a predefined set of
questions.
• Unstructured Interview: in which the interviewer does not have a
predetermined format or order of questions. Questions may vary based on
interviewee responses and interactions.
In practice, business analysts may use a combination of the two types by adding,
dropping, and varying the order of questions as needed.



Techniques
Interviews
291
Successful interviewing depends on factors such as:
• level of understanding of the domain by the interviewer,
• experience of the interviewer in conducting interviews,
• skill of the interviewer in documenting discussions,
• readiness of the interviewee to provide the relevant information and the
interviewer to conduct the interview,
• degree of clarity in the interviewee’s mind about the goal of the interview,
and
• rapport of the interviewer with the interviewee.
10.25.3
Elements
.1 Interview Goal
When planning interviews, business analysts consider:
• the overall purpose of performing a set of interviews, based on a business
need, and
• the individual goals for each interview, based on what the interviewee can
provide.
The goals are to be clearly expressed and communicated to each interviewee.
.2 Potential Interviewees
Potential interviewees are identified with the help of the project manager, project
sponsors, and other stakeholders, based on the goals for the interview.
.3 Interview Questions
Interview questions are designed according to the interview goals, such as:
• collecting data,
• researching the stakeholder’s view of the change or proposed solution,
• developing a proposed solution, or
• building rapport with or support for the proposed solution from the
interviewee.
Open-ended questions are used to elicit a dialogue or series of steps and cannot
be answered in a yes or no fashion. Open-ended questions are a good tool to
allow the interviewee to provide information of which the interviewer may be
unaware.
Closed questions are used to elicit a single response such as yes, no, or a specific
number. Closed questions can be used to clarify or confirm a previous answer.
The interview questions are often organized based on priority and significance.
Examples of question order include general to specific, start to finish, and detailed
to summary. Questions can also be organized based on factors such as the
interviewee's level of knowledge and the subject of the interview.



Interviews
Techniques
292
Interview questions may be customized when the purpose of the interview is to
gather information that is unique to the perspective of the interviewee.
Standardized questions may be used when the interview results will be
summarized and analyzed, such as when interview results will be tallied using a
check sheet.
Interview questions can be compiled in an interview guide, which includes the
interview questions, proposed timing, and follow-up questions. This will all be
based on the interview type, according to the interview goals, mode of
communication, and duration. The interview guide can be a document where the
interviewee’s responses are easily recorded. The interview guide should identify
which interview questions may be omitted based upon time constraints.
.4 Interview Logistics
Ensuring a successful interview requires attention to logistics that include:
• The location for the interview. The interview is adapted to the schedule and
availability of the interviewee and the mode of communication (in-person,
phone, or online conferencing).
• Whether or not to record the interview, which may require the use of a
scribe.
• Whether or not to send the questions to the interviewees in advance.
Sending questions in advance is advisable only when the interviewee needs
to collect information to prepare for the interview.
• Whether the interview results will be confidential and, if so, how the results
will be summarized to avoid identifying individual interviewees.
.5 Interview Flow
Opening the interview includes:
• describing the purpose of the interview, including why the interviewees'
time is needed,
• confirming the interviewees' roles and addressing any initial concerns raised
by the interviewees, and
• explaining how information from the interview will be recorded and shared
with the interviewees and other stakeholders during the project.
During the interview, the interviewer:
• maintains focus on the established goals and predefined questions, and
adapts based upon the information provided and non-verbal
communication from the interviewees,
• considers both the willingness of the interviewees to participate in the
interview and to provide the required information,
• considers that several meetings might be required to conduct the entire
interview,
• manages concerns raised by the interviewees by addressing them during
the interview or documenting them for follow-up,



Techniques
Interviews
293
• practices active listening to confirm what the interviewer has said, and
• takes written notes or records the interview as appropriate.
Closing the interview includes:
• asking the interviewees for areas that may have been overlooked in the
session,
• providing contact information for the interviewees to follow up with
additional information after the meeting as needed,
• summarizing the session,
• outlining the process for how the interview results will be used, and
• thanking the interviewees for their time.
.6 Interview Follow-Up
It is important for the interviewer to organize the information and confirm results
with the interviewees as soon as possible after the interview. Sharing the
information that has been learned allows the interviewees to point out any
missed or incorrectly recorded items.
10.25.4
Usage Considerations
.1 Strengths
• Encourages participation by and establishes rapport with stakeholders.
• Simple, direct technique that can be used in a variety of situations.
• Allows the interviewer and participant to have full discussions and explanations
of the questions and answers.
• Enables observations of non-verbal behaviour.
• The interviewer can ask follow-up and probing questions to confirm their own
understanding.
• Maintains focus through the use of clear objectives for the interview that are
agreed upon by all participants and can be met in the time allotted.
• Allows interviewees to express opinions in private that they may be reluctant to
express in public, especially when interview results are kept confidential.
.2 Limitations
• Significant time is required to plan for and conduct interviews.
• Requires considerable commitment and involvement of the participants.
• Training is required to conduct effective interviews.
• Based on the level of clarity provided during the interview, the resulting
documentation may be subject to the interviewer's interpretation.
• There is a risk of unintentionally leading the interviewee.



Item Tracking
Techniques
294
10.26
Item Tracking
10.26.1
Purpose
Item tracking is used to capture and assign responsibility for issues and
stakeholder concerns that pose an impact to the solution.
10.26.2
Description
Item tracking is an organized approach used by business analysts to address
stakeholder concerns. Stakeholders may identify such item types as actions,
assumptions, constraints, dependencies, defects, enhancements, and issues.
When a stakeholder concern is first raised, it is assessed to determine if it is viable.
If viable, the concern is classified as a specific item type so that it can be better
tracked and controlled by a process that works towards the item’s closure. During
its life cycle, an item is assigned to one or more stakeholders who are responsible
for its resolution.
Item tracking tracks the item from the initial recording of the concern and its
degree of impact to its agreed-upon closure. The item tracking record may be
shared with stakeholders to ensure transparency and visibility into the status and
progress of items in the record.
10.26.3
Elements
.1 Item Record
Each recorded item may contain all or any of the following attributes for item
tracking. These items may be recorded using various software applications or
manually catalogued for sharing between an agreed set of stakeholders.
• Item Identifier: a unique identifier that distinguishes one item from
another.
• Summary: a brief description of the item.
• Category: a grouping of items with similar properties.
• Type: the kind of item raised.
• Date Identified: the date the item was raised as a concern.
• Identified By: the person who initially raised the concern.
• Impact: the possible consequences if the item is not resolved by the
resolution due date. Impact can be assessed in relation to the initiative’s
time, cost, scope, or quality.
• Priority: the importance of this item to the impacted stakeholders.
• Resolution Date: the date by which the item must be resolved (or closed).
• Owner: the stakeholder assigned to manage the item to its closure.



Techniques
Item Tracking
295
• Resolver: the stakeholder assigned to resolve the item.
• Agreed Strategy: agreed-upon strategy for the item. Examples include
accept, pursue, ignore, mitigate, and avoid.
• Status: the current status of the item within its life cycle. Examples include
open, assigned, resolved, and cancelled.
• Resolution Updates: a running log of details about how the item’s
resolution is proceeding towards closure, as well as approval of its
completion.
• Escalation Matrix: a level of escalation in case the item is not resolved by
the given due date.
.2 Item Management
Each item’s resolution is undertaken as prescribed by stakeholder needs and
according to any organizational process standards. In some cases, one item may
cause another item to be recorded and tracked. In these situations, close
attention is needed so that item resolution efforts are not duplicated and are
progressing in coordination. Each item must be tracked to its closure or
resolution.
.3 Metrics
All stakeholders benefit from the detailed information that is maintained about
any item and its progress. These items can be looked at individually for resolution
or even used to define key performance indicators tailored to the item tracking
process.
By reviewing this output, stakeholders can determine how well:
• items are being resolved by the proper resources,
• the initiative is progressing, and
• the item tracking process is being utilized.
10.26.4
Usage Considerations
.1 Strengths
• Ensures concerns around stakeholder requirements are captured, tracked, and
resolved to the stakeholder’s satisfaction.
• Allows stakeholders to rank the importance of outstanding items.
.2 Limitations
• If not careful, the copious recording of data about items may outweigh any
benefits realized.
• It may use time that could be better spent on other efforts and stakeholders
could become mired in details and statistics.



Lessons Learned
Techniques
296
10.27
Lessons Learned
10.27.1
Purpose
The purpose of the lessons learned process is to compile and document
successes, opportunities for improvement, failures, and recommendations for
improving the performance of future projects or project phases.
10.27.2
Description
A lessons learned session (also known as a retrospective) helps identify either
changes to business analysis processes and deliverables or successes that can be
incorporated into future work. These techniques can also be beneficial at the
close of any milestone within the effort.
Lessons learned sessions can include any format or venue that is acceptable to the
key stakeholders and can be either formal facilitated meetings with set agendas
and meeting roles or informal working sessions. If there are noteworthy
successes, a celebration may be included in a lessons learned session.
10.27.3
Elements
Sessions can include a review of:
• business analysis activities or deliverables,
• the final solution, service, or product,
• automation or technology that was introduced or eliminated,
• impact to organizational processes,
• performance expectations and results,
• positive or negative variances,
• root causes impacting performance results, and
• recommendations for behavioural approaches.
10.27.4
Usage Considerations
.1 Strengths
• Useful in identifying opportunities or areas of improvement.
• Assists in building team morale after a difficult period.
• Reinforces positive experiences and successes.
• Reduces risks for future actions.
• Provides tangible value or metrics as a result of the effort.
• Recognizes strengths or shortcomings with the project structure, methodology,
or tools that were used.



Techniques
Metrics and Key Performance Indicators (KPIs)
297
.2 Limitations
• Honest discussion may not occur if participants try to assign blame during these
sessions.
• Participants may be reluctant to document and discuss problems.
• Proactive facilitation may be required to ensure that the discussions remain
focused on solutions and improvement opportunities.
10.28
Metrics and Key Performance Indicators (KPIs)
10.28.1
Purpose
Metrics and key performance indicators measure the performance of solutions,
solution components, and other matters of interest to stakeholders.
10.28.2
Description
A metric is a quantifiable level of an indicator that an organization uses to
measure progress. An indicator identifies a specific numerical measurement that
represents the degree of progress toward achieving a goal, objective, output,
activity, or further input. A key performance indicator (KPI) is one that measures
progress towards a strategic goal or objective. Reporting is the process of
informing stakeholders of metrics or indicators in specified formats and at
specified intervals.
Metrics and reporting are key components of monitoring and evaluation.
Monitoring is a continuous process of data collection used to determine how well
a solution has been implemented as compared to the expected results. Evaluation
is the systematic and objective assessment of a solution both to determine its
status and effectiveness in meeting objectives over time and to identify ways to
improve the solution to better meet objectives. The top priorities of a monitoring
and evaluation system are the intended goals and effects of a solution, as well as
inputs, activities, and outputs.
10.28.3
Elements
.1 Indicators
An indicator displays the result of analyzing one or more specific measures for
addressing a concern about a need, value, output, activity, or input in a table or
graphical form. Each concern requires at least one indicator to measure it
properly, but some may require several.
A good indicator has six characteristics:
• Clear: precise and unambiguous.
• Relevant: appropriate to the concern.



Metrics and Key Performance Indicators (KPIs)
Techniques
298
• Economical: available at reasonable cost.
• Adequate: provides a sufficient basis on which to assess performance.
• Quantifiable: can be independently validated.
• Trustworthy and Credible: based on evidence and research.
In addition to these characteristics, stakeholder interests are also important.
Certain indicators may help stakeholders perform or improve more than others.
Over time, weaknesses in some indicators can be identified and improved.
Not all factors can be measured directly. Proxies can be used when data for direct
indicators are not available or when it is not feasible to collect at regular intervals.
For example, in the absence of a survey of client satisfaction, an organization
might use the proportion of all contracts renewed as an indicator.
When establishing an indicator, business analysts will consider its source, method
of collection, collector, and the cost, frequency, and difficulty of collection.
Secondary sources of data may be the most economical, but to meet the other
characteristics of a good indicator, primary research such as surveys, interviews, or
direct observations may be necessary. The method of data collection is the key
driver of a monitoring, evaluation, and reporting system's cost.
.2 Metrics
Metrics are quantifiable levels of indicators that are measured at a specified point
in time. A target metric is the objective to be reached within a specified period. In
setting a metric for an indicator, it is important to have a clear understanding of
the baseline starting point, resources that can be devoted to improving the
factors covered by the indicator, and political concerns.
A metric can be a specific point, a threshold, or a range. A range can be useful if
the indicator is new. Depending on the need, the scope of time to reach the
target metric can be multi-year, annual, quarterly, or even more frequent.
.3 Structure
Establishing a monitoring and evaluation system requires a data collection
procedure, a data analysis procedure, a reporting procedure, and the collection of
baseline data. The data collection procedure covers units of analysis, sampling
procedures, data collection instruments to use, collection frequency, and
responsibility for collection. The analysis method specifies both the procedures for
conducting the analysis and the data consumer, who may have strong interests in
how the analysis is conducted. The reporting procedure covers the report
templates, recipients, frequency, and means of communication. Baseline
information is the data provided immediately before or at the beginning of a
period to measure. Baseline data is used both to learn about recent performance
and to measure progress from that point forward. It needs to be collected,
analyzed, and reported for each indicator.
There are three key factors in assessing the quality of indicators and their metrics:
reliability, validity, and timeliness. Reliability is the extent to which the data
collection approach is stable and consistent across time and space. Validity is the



Techniques
Mind Mapping
299
extent to which data clearly and directly measures the performance the
organization intends to measure. Timeliness is the fit of the frequency and latency
of data to the management’s need.
.4 Reporting
Typically, reports compare the baseline, current metrics, and target metrics with
calculations of the differences presented in both absolute and relative terms. In
most situations, trends are more credible and important than absolute metrics.
Visual presentations tend to be more effective than tables, particularly when
using qualitative text to explain the data.
10.28.4
Usage Considerations
.1 Strengths
• Establishing a monitoring and evaluation system allows stakeholders to
understand the extent to which a solution meets an objective, as well as how
effective the inputs and activities of developing the solution (outputs) were.
• Indicators, metrics, and reporting also facilitate organizational alignment,
linking goals to objectives, supporting solutions, underlying tasks, and
resources.
.2 Limitations
• Gathering excessive amounts of data beyond what is needed will result in
unnecessary expense in collecting, analyzing, and reporting. It will also distract
project members from other responsibilities. On Agile projects, this will be
particularly relevant.
• A bureaucratic metrics program fails from collecting too much data and not
generating useful reports that will allow timely action. Those charged with
collecting metric data must be given feedback to understand how their actions
are affecting the quality of the project results.
• When metrics are used to assess performance, the individuals being measured
are likely to act to increase their performance on those metrics, even if this
causes sub-optimal performance on other activities.
10.29
Mind Mapping
10.29.1
Purpose
Mind mapping is used to articulate and capture thoughts, ideas, and information.
10.29.2
Description
Mind mapping is a form of note taking that captures thoughts, ideas, and
information in a non-linear diagram. Mind maps use images, words, colour, and



Mind Mapping
Techniques
300
connected relationships to apply structure and logic to thoughts, ideas, and
information. A mind map has a central main idea supported by secondary ideas
(or topics), followed by as many layers of ideas (or sub-topics) as necessary to fully
capture and articulate the concept. Connections are made between ideas by
branches that typically have a single keyword associated with them that explain
the connection.
Mind maps can be developed individually or as a collaboration exercise. They can
be created on paper or with the use of specialized software.
Business analysts use mind maps to:
• think through and generate ideas on complex concepts or problems,
• explore relationships between the various facets of a problem in a way that
inspires creative and critical thinking, and
• present a consolidated view of complex concepts or problems.
There is no standardized format for a mind map. The intent of a mind map is to
capture information in a fashion closely resembling how our minds process
information. The following image is intended to illustrate the general structure
and usage of mind maps.
Figure 10.29.1: The Taxonomy of a Mind Map
Topic 1
Topic 3
Topic 2
Topic 4
Sub-topic 1.1
Sub-topic 1.2
Sub-topic 3.1
Sub-topic 3.2
Branches
Sub-topic 4.1
Sub-topic 4.2
Sub-topic 4.3
Sub-topic 4.3.1
Sub-topic 2.2
Sub-topic 2.2.1
Sub-topic 2.2.2
Sub-topic 2.1
Branches
Keyword
Keyword
Keyword
Keyword
Keyword
Keyword
Keyword
Keyword
Keyword
Keyword
Keyword
Keyword
Keyword
Keyword
Main Topic
Keyword



Techniques
Mind Mapping
301
10.29.3
Elements
.1 Main Topic
The main topic of a mind map is the thought or concept that is being articulated.
The main topic is positioned in the centre of the images so that multiple topics
and associations can branch off. Images are frequently used as the main topic
because they contain a great deal of information and can be useful in stimulating
associated topics.
.2 Topics
Topics are thoughts or concepts that expound upon or further articulate the main
topic. Their association with the main topic is expressed through a branch
(connected line) that has a keyword associated with it. There can be as many or as
few topics as required to fully explore the thought or concept of the main topic.
.3 Sub-topics
Sub-topics are thoughts or concepts that expound upon or further articulate the
topic and directly relate to the main topic. Their association with the topic is
expressed through a branch (connected line) that has a keyword associated with
it. There can be as many or as few sub-topics as required to fully explore the
thought or concept of the main topic.
.4 Branches
Branches are the associations between the main topic, topics, and sub-topics.
Branches include a keyword that clearly articulates the nature of the association.
.5 Keywords
Keywords are single words used to articulate the nature of the association of
topics or sub-topics connected by a branch. The keywords are useful for both
categorizing topics and for triggering additional associations.
.6 Colour
Colour may be used to categorize, prioritize, and analyze topics, sub-topics, and
their associations. There is no defined colour coding standard for mind maps.
Each mind map creator applies colour in a way that best suits their mode of
thinking.
.7 Images
Images can be used in mind maps to express larger volumes of information that
are unable to be expressed in short topic headings. Images are useful in
stimulating creativity and innovation by generating additional thoughts, ideas,
and associations.



Non-Functional Requirements Analysis
Techniques
302
10.29.4
Usage Considerations
.1 Strengths
• Can be used as an effective collaboration and communication tool.
• Summarizes complex thoughts, ideas, and information in a way that shows the
overall structure.
• Associations and sub-topics facilitate understanding and decision making.
• Enable creative problem solving by articulating associations and generating
new associations.
• Can be helpful in preparing and delivering presentations.
.2 Limitations
• Can be misused as a brainstorming tool, and the related documenting of ideas
and creating associations may inhibit idea generation.
• A shared understanding of a mind map can be difficult to communicate.
10.30
Non-Functional Requirements Analysis
10.30.1
Purpose
Non-functional requirements analysis examines the requirements for a solution
that define how well the functional requirements must perform. It specifies
criteria that can be used to judge the operation of a system rather than specific
behaviours (which are referred to as the functional requirements).
10.30.2
Description
Non-functional requirements (also known as quality attributes or quality of service
requirements) are often associated with system solutions, but they also apply
more broadly to both process and people aspects of solutions. They augment the
functional requirements of a solution, identify constraints on those requirements,
or describe quality attributes a solution must exhibit when based on those
functional requirements.
Non-functional requirements are generally expressed in textual formats as
declarative statements or in matrices. Declarative non-functional requirements
statements will typically have a constraining factor to them. For example, errors
must not exceed X per use of the process, transactions must be at least X%
processed after S seconds, or the system must be available X% of the time.



Techniques
Non-Functional Requirements Analysis
303
10.30.3
Elements
.1 Categories of Non-Functional Requirements
Common categories of non-functional requirements include:
• Availability: degree to which the solution is operable and accessible when
required for use, often expressed in terms of percent of time the solution is
available.
• Compatibility: degree to which the solution operates effectively with other
components in its environment, such as one process with another.
• Functionality: degree to which the solution functions meet user needs,
including aspects of suitability, accuracy, and interoperability.
• Maintainability: ease with which a solution or component can be
modified to correct faults, improve performance or other attributes, or
adapt to a changed environment.
• Performance Efficiency: degree to which a solution or component
performs its designated functions with minimum consumption of resources.
Can be defined based on the context or period, such as high-peak, mid-
peak or off-peak usage.
• Portability: ease with which a solution or component can be transferred
from one environment to another.
• Reliability: ability of a solution or component to perform its required
functions under stated conditions for a specified period of time, such as
mean time to failure of a device.
• Scalability: degree with which a solution is able to grow or evolve to
handle increased amounts of work.
• Security: aspects of a solution that protect solution content or solution
components from accidental or malicious access, use, modification,
destruction, or disclosure.
• Usability: ease with which a user can learn to use the solution.
• Certification: constraints on the solution that are necessary to meet certain
standards or industry conventions.
• Compliance: regulatory, financial, or legal constraints which can vary based
on the context or jurisdiction.
• Localization: requirements dealing with local languages, laws, currencies,
cultures, spellings, and other characteristics of users, which requires
attention to the context.
• Service Level Agreements: constraints of the organization being served
by the solution that are formally agreed to by both the provider and the
user of the solution.
• Extensibility: the ability of a solution to incorporate new functionality.



Non-Functional Requirements Analysis
Techniques
304
.2 Measurement of Non-Functional Requirements
Non-functional requirements often describe quality characteristics in vague terms,
such as “the process must be easy to learn", or “the system must respond
quickly”. To be useful to developers of a solution and to be verifiable, non-
functional requirements must be quantified whenever possible. Including an
appropriate measure of success provides the opportunity for verification.
For example:
• "The process must be easy to learn" can be expressed as "90% of
operators must be able to use the new process after no more than six hours
of training", and
• "The system must respond quickly" can be expressed as "The system must
provide 90% of responses in no more than two seconds".
Measurement of the other categories of non-functional requirements is guided by
the source of the requirement.
For example:
• certification requirements are generally specified in measurable detail by the
organization setting the standard or convention, such as ISO Certification
standards,
• compliance requirements and localization requirements are set in
measurable detail by their providers,
• effective service level agreements state clearly the measures of success
required, and
• an organization’s enterprise architecture generally defines the solution
environment requirements and specifies exactly which platform or other
attribute of the environment is required.
.3 Context of Non-Functional Requirements
Depending on the category of non-functional requirements, the context may
have to be considered. For example, a regulatory agency may impose context-
impacting compliance and security requirements, or an organization that is
expanding operations abroad may have to consider localization and scalability
requirements. Determining the optimal portfolio of non-functional requirements
in a given organizational context is central to delivering value to stakeholders.
The assessment of a non-functional requirement, such as localization or
maintainability, may impose contextual pressures on other non-functional
requirements. For instance, regulations or resources in one jurisdiction may affect
the maintainability of a solution in that region, and so it may justify a lower
performance efficiency or reliability measure of success than in another jurisdiction.
Context is dynamic by nature and non-functional requirements may need to be
adjusted or removed outright. Business analysts consider the relative stability of
the context when evaluating non-functional requirements.



Techniques
Observation
305
10.30.4
Usage Considerations
.1 Strengths
• Clearly states the constraints that apply to a set of functional requirements.
• Provides measurable expressions of how well the functional requirements must
perform, leaving it to the functional requirements to express what the solution
must do or how it must behave. This will also have a strong influence on
whether the solution is accepted by the users.
.2 Limitations
• The clarity and usefulness of a non-functional requirement depends on what
the stakeholders know about the needs for the solution and how well they can
express those needs.
• Expectations of multiple users may be quite different, and getting agreement
on quality attributes may be difficult because of the users' subjective perception
of quality. For example, what might be 'too fast' to one user might be 'too
slow' to another.
• A set of non-functional requirements may have inherent conflicts and require
negotiation. For example, some security requirements may require
compromises on performance requirements.
• Overly strict requirements or constraints can add more time and cost to the
solution, which may have negative impacts and weaken adoption by users.
• Many non-functional requirements are qualitative and therefore may be
difficult to be measured on a scale, and may garner a degree of subjectivity by
the users as to how they believe the particular requirements ultimately meet
their needs.
10.31
Observation
10.31.1
Purpose
Observation is used to elicit information by viewing and understanding activities
and their context. It is used as a basis for identifying needs and opportunities,
understanding a business process, setting performance standards, evaluating
solution performance, or supporting training and development.
10.31.2
Description
Observation of activities, also known as job shadowing, involves examining a
work activity firsthand as it is performed. It can be conducted in either natural
work environments or specially constructed laboratory conditions. The objectives
of the observation dictate how it is planned for and methodically conducted.



Observation
Techniques
306
There are two basic approaches for observation:
• Active/Noticeable: while observing an activity the observer asks any
questions as they arise. Despite this interruption to the work flow, the
observer can more quickly understand the rationale and hidden processes
underlying the activity, such as decision making. A variation of this method
may involve even stronger intervention into actors' activities by stimulating
them to perform specific tasks. This kind of facilitated observation allows
focus on the observer's objectives in order to shorten observation time or
elicit specific information.
• Passive/Unnoticeable: during the activity the observer does not interrupt
the work. Any concerns are raised once the observation is over. This allows
observation of a natural flow of events without intervention by the
observer, as well as measurement of the time and quality of work. A
variation of this method is video recording the activity and then reviewing it
with the person being observed so they may provide further clarification.
Inspection of a person's work environment helps in discovering any tools and
information assets involved in performing their activities. This supports
understanding of the activities, especially with the purpose of identifying needs
and opportunities. This kind of observation is an important part of the
technique's variation, and is known as Contextual Inquiry.
10.31.3
Elements
.1 Observation Objectives
A clear and specific objective establishes a defined purpose of the observation
session.
Objectives of an observation session may include:
• understanding the activity and its elements such as tasks, tools, events, and
interactions,
• identifying opportunities for improvement,
• establishing performance metrics, or
• assessing solutions and validating assumptions.
.2 Prepare for Observation
Preparing for an observation session involves planning the observation approach
based on the objectives and deciding who should be viewed performing which
activities at what times. While preparing for an observation session, business
analysts consider the skill and experience levels of participants, the frequency of
the activities being observed, and any existing documentation and analysis related
to the work activity. Preparing for observation also includes creating a schedule of
observations.
The plan for observation ensures that all stakeholders are aware of the purpose of
the observation session, they agree on the expected outcomes, and that the
session meets their expectations.



Techniques
Observation
307
.3 Conduct the Observation Session
Before the observation session:
• explain why the observation is being conducted,
• reassure the participant that their personal performance is not being judged
and that the results of this observation, among others, will be evaluated as
a whole,
• inform the participant that they can stop the observation at any time, and
• recommend the sharing of any reasoning or concerns while performing the
activity or soon afterwards.
During the observation session:
• attentively watch the person perform the activity and note typical and
atypical tasks or steps, the manner in which any tools are used, and
information content,
• record what is seen, the time taken to perform the work, its quality, any
process anomalies, and the observer's own concerns or questions, and
• ask probing questions either while the work is being performed or soon
after the observation session.
.4 Confirm and Present Observation Results
After the observation session, business analysts review the notes and data
recorded from the observation and follow up with the participant to obtain
answers to any remaining questions or to fill any gaps. Sharing these notes and
data with participants may be helpful in obtaining answers to any questions or
easing any concerns the participant may have.
The validated notes and data are collated with other related observations to
identify similarities, differences, and trends. Findings are aggregated,
summarized, and analyzed against the objectives of the session. Needs and
opportunities for improvement are communicated to stakeholders.
10.31.4
Usage Considerations
.1 Strengths
• Observers can gain realistic and practical insight about the activities and their
tasks within an overall process.
• Instances of informally performed tasks as well as any workarounds can be
identified.
• Productivity can be viewed firsthand and realistically compared against any
established performance standards or metrics.
• Recommendations for improvement are supported by objective and
quantitative evidence.



Organizational Modelling
Techniques
308
.2 Limitations
• May be disruptive to the performance of the participant and the overall
organization.
• Can be threatening and intrusive to the person being observed.
• While being observed, a participant may alter their work practices.
• Significant time is required to plan for and conduct observations.
• Not suitable for evaluating knowledge-based activities since these are not
directly observable.
10.32
Organizational Modelling
10.32.1
Purpose
Organizational modelling is used to describe the roles, responsibilities, and
reporting structures that exist within an organization and to align those structures
with the organization's goals.
10.32.2
Description
An organizational model defines how an organization or organizational unit is
structured. The purpose of an organizational unit is to bring together a group of
people to fulfill a common purpose. The group may be organized because the
people share a common set of skills and knowledge or to serve a particular
market.
An organizational model is a visual representation of the organizational unit
which defines:
• the boundaries of the group (who is in the group),
• the formal relationships between members (who reports to whom),
• the functional role for each person, and
• the interfaces (interaction and dependencies) between the unit and other
units or stakeholders.
10.32.3
Elements
.1 Types of Organizational Models
There are three pre-eminent organizational models:
• Functionally-oriented: group staff together based on shared skills or
areas of expertise and generally encourage a standardization of work or
processes within the organization. Functional organizations are beneficial
because they seem to facilitate cost management and reduce duplication of



Techniques
Organizational Modelling
309
work, but are prone to develop communication and cross-functional
coordination problems (known informally as "silos").
Figure 10.32.1: Functionally-oriented Organizational Model
• Market-oriented: may be intended to serve particular customer groups,
geographical areas, projects, or processes rather than grouping employees
by common skills or expertise. Market-oriented structures permit the
organization to meet the needs of its customers, but are prone to
developing inconsistencies in how work is performed. Some may discover
they are performing duplicate work in multiple areas.
Figure 10.32.2: Market-oriented Organizational Model
Executive Function
Incumbent Name
Management Function
Incumbent Name
Management Function
Incumbent Name
Management Function
Incumbent Name
Business Area Management
Function (no staff)
Function
Vacancy
Staff Function
Incumbent Name
Staff Function
Incumbent Name
Staff Function
Incumbent Name
President/CEO
Market 1
Market 2
Market 3
Finance
(Shared Support)
Staff
Research &
Development
Manufacturing
Marketing & Sales
Research &
Development
Manufacturing
Marketing & Sales
Research &
Development
Manufacturing
Marketing & Sales
Accounting
Planning



Organizational Modelling
Techniques
310
• The Matrix Model: has separate managers for each functional area and
for each product, service, or customer group. Employees report to a line
manager, who is responsible for the performance of a type of work and for
identifying opportunities for efficiency in the work, and to a market (or
product, service, or project) manager, who is responsible for managing the
product or service across multiple functional areas. A challenge of the
matrix model is that each employee has two managers (who are focused on
different goals) and accountability is difficult to maintain.
Figure 10.32.3: Matrix Organizational Model
.2 Roles
An organizational unit includes a number of defined roles. Each role requires a
certain set of skills and knowledge, has specific responsibilities, performs certain
kinds of work, and has defined relationships with other roles in the organization.
.3 Interfaces
Each organizational unit has interfaces with other organizational units. Interfaces
(interactions) may be in the form of communication with people in other roles
and work packages that the organizational unit receives from or delivers to other
units.
.4 Organizational Charts
The fundamental diagram used in organizational modelling is the organizational
chart (org chart).
There is no recognized standard for org charts, although there are some
conventions that most org charts follow:
• A box depicts:
• Organizational Unit: people, teams, departments, or divisions. An org
Area 1
Area 2
Line Manager
Line Manager
Area 3
Line Manager
Employee
Project Manager
Process Manager
Product Manager
Employee
Employee
Employee
Employee
Employee
Employee
Employee
Employee



Techniques
Prioritization
311
chart may mix organizational units and show a mix of people, teams,
and higher-level divisions.
• Roles and People: the roles within an organization and the people
assigned to each role.
• A line depicts:
• Lines of Reporting: accountability and control between units. A solid
line typically denotes direct authority, while a dotted line indicates
information transfer or situational authority. Lines of reporting depict
the relationship between a manager and an organizational unit
.5 Influencers
Organizational charts are the primary tool for beginning organizational
modelling. Organizational charts represent the formal structure of the organization.
Business analysts also identify informal lines of authority, influence, and
communication which may not directly align with the formal organizational chart.
Determining all of the influencers is important in planning communication and
making provisions for user acceptance. One method of identifying influencers
may be to ask stakeholders, “Who can I ask…” and note the answers. An
influencer may be a person everyone goes to for information, direction, and
advice. Another method is to note who speaks for the group in meetings.
10.32.4
Usage Considerations
.1 Strengths
• Organizational models are common in most organizations.
• Including an organizational model in business analysis information allows team
members to provide support. Future projects may benefit from knowing who
was involved in this project and what their role entailed.
.2 Limitations
• Organizational models are sometimes out of date.
• Informal lines of authority, influence, and communication not reflected in the
org chart are more difficult to identify and may conflict with the organizational
chart.
10.33
Prioritization
10.33.1
Purpose
Prioritization provides a framework for business analysts to facilitate stakeholder
decisions and to understand the relative importance of business analysis
information.



Prioritization
Techniques
312
10.33.2
Description
Prioritization is a process used to determine the relative importance of business
analysis information. The importance may be based on value, risk, difficulty of
implementation, or other criteria. These priorities are used to determine which
business analysis information should be targeted for further analysis, which
requirements should be implemented first, or how much time or detail should be
allocated to the requirements.
There are many approaches to prioritization. For the purpose of this technique,
prioritization is classified into one of four approaches:
• Grouping,
• Ranking,
• Time boxing/Budgeting, and
• Negotiation.
When choosing a prioritization approach, business analysts consider the
audience, their needs, and their opinions on the value a requirement or business
analysis information brings to a stakeholder's respective area.
Business analysts revisit priorities and utilize different approaches when changes
occur in the business environment, to the stakeholders, and to the business
analysis information.
Figure 10.33.1: Approaches to Prioritization
Consider audience needs and opinions
Choose approach(es)
Budgeting/
Time Boxing
BA information
based on allocation of
a fixed resource
(time or money)
Negotiation
Stakeholder
consensus on
requirements to be
prioritized
Grouping
BA information
classified high,
medium, low priority
Ranking
BA information
ordered from most to
least important
Approaches to Prioritization
Determine importance of business analysis information based on
value, risk, difficulty of implementation, or other criteria.



Techniques
Prioritization
313
10.33.3
Elements
.1 Grouping
Grouping consists of classifying business analysis information according to
predefined categories such as high, medium, or low priority. Many requirements
management tools support listing the priority category as an attribute of a
requirement.
.2 Ranking
Ranking consists of ordering business analysis information from most to least
important. Some adaptive approaches involve the explicit sequencing of
requirements in an ordered list (a product backlog).
.3 Time Boxing/Budgeting
Time boxing or budgeting prioritizes business analysis information based on the
allocation of a fixed resource. It is frequently used when the solution approach
has been determined. Time boxing is used to prioritize requirements based on the
amount of work that the project team is capable of delivering in a set period of
time. Budgeting is used when the project team has been allocated a fixed amount
of money. This approach is most often used when a fixed deadline must be met
or for solutions that are enhanced on a regular and frequent basis.
.4 Negotiation
The negotiation approach involves establishing a consensus among stakeholders
as to which requirements will be prioritized.
10.33.4
Usage Considerations
.1 Strengths
• Facilitates consensus building and trade-offs and ensures that solution value is
realized and initiative timelines are met.
.2 Limitations
• Some stakeholders may attempt to avoid difficult choices and fail to recognize
the necessity for making trade-offs.
• The solution team may intentionally or unintentionally try to influence the result
of the prioritization process by overestimating the difficulty or complexity of
implementing certain requirements.
• Metrics and key performance indicators are often not available when
prioritizing business analysis information; therefore, a stakeholder’s perspective
of the importance may be subjective.



Process Analysis
Techniques
314
10.34
Process Analysis
10.34.1
Purpose
Process analysis assesses a process for its efficiency and effectiveness, as well as its
ability to identify opportunities for change.
10.34.2
Description
Process analysis is used for various purposes including:
• recommending a more efficient or effective process,
• determining the gaps between the current and future state of a process,
• understanding factors to be included in a contract negotiation,
• understanding how data and technology are used in a process, and
• analyzing the impact of a pending change to a process.
A number of frameworks and methodologies exist that focus on process analysis
and improvement methods, such as Six Sigma and Lean. Methods for process
improvement include value stream mapping, statistical analysis and control,
process simulation, benchmarking, and process frameworks.
Common changes made to processes in order to improve them include:
• reducing the time required to complete a task or tasks in the process,
• modifying interfaces or hand-offs between roles and organizational units to
remove errors, including the reduction or elimination of bottlenecks,
• automating steps that are more routine or predictable, and
• increasing the degree of automation in the decision making required by the
process.
When analyzing a process, business analysts look for:
• how the process adds or creates value for the organization,
• how the process aligns to organizational goals and strategy,
• to what degree the process is and needs to be efficient, effective, repeated,
measured, controlled, used, and transparent, and
• how the requirements for a solution cover the future state process and its
external stakeholders, including customers.
10.34.3
Elements
.1 Identify Gaps and Areas to Improve
Identifying gaps and areas to improve helps to identify what areas are in scope for
analysis. Industry-specific models and process frameworks may be helpful in this



Techniques
Process Analysis
315
regard. When identifying gaps and areas to improve, business analysts:
• identify gaps between the current and desired future state,
• identify what gaps and areas are value and non-value added,
• understand pain points and the challenges of the process from multiple
points of view,
• understand opportunities to improve the process from multiple points of
view,
• align the gaps and areas to improve with the strategic direction of the
organization, and
• understand the relationship of the gaps and areas to improve to changes in
the enterprise.
.2 Identify Root Cause
Identifying the root cause of the gaps and improvement areas ensures that the
solution addresses the right gap and area.
When identifying the root cause, business analysts understand:
• there may be multiple root causes,
• the inputs leading to the gap or area of improvement,
• who the right people are to identify the root cause, and
• the current measurements and motivators in place for those owning or
performing the process.
.3 Generate and Evaluate Options
Generating options and alternative solutions to solve for the gap or area of
improvement helps the team evaluate and see different points of view for
improving the process. It is important for stakeholders to be involved in
identifying the impact, feasibility, and value of the proposed solution relative to
alternative options.
.4 Common Methods
SIPOC
SIPOC is a process analysis method that originates in the Six Sigma methodology
and has been more commonly adopted as a process analysis method outside of
Six Sigma.
It is used to look at the process and understand the Suppliers, Inputs, Process,
Outputs and Customers of the process being analyzed.
A SIPOC provides a simple overview of the process. It also shows the complexity
of who and what is involved in creating inputs to the process and shows who
receives outputs from the process. A SIPOC is a powerful tool used to create



Process Analysis
Techniques
316
dialogue about problems, opportunities, gaps, root cause, and options and
alternatives during process analysis.
Figure 10.34.1: SIPOC Model
Value Stream Mapping (VSM)
Value stream mapping (VSM) is a process analysis method used in Lean
methodologies.
Value stream mapping involves the diagramming and monitoring of inputs and
application points for processing those inputs, starting from the front-end of the
supply chain. At each stage, the value stream map gauges the wait time for the
inputs and the actual processing times at the application points (also known as
conversion times). At the end of the supply chain, the value stream map depicts
the logistics or distribution process to the customer.
The value stream map provides a one-page picture of all the steps involved in the
end-to-end process, including both value-adding (the value stream) and non-
value-adding (waste) elements.
Suppliers
Inputs
Process
Outputs
Customers
Customer (buyer)
Credit Card Bureau
PayPal
Customer (buyer)
Order Warehouse
Credit Bureau
PayPal
Delivery Service
Step 1
Step 2
Step 3
Step 4
Step 5
Purchase
Create Profile
Select Items To
Purchase
Confirm
Payment
Information
Confirm
Delivery
Information
View Receipt
Customer Information
Inventory Information
Payment Method &
Details
Order Details
Receipt
Product Purchased



Techniques
Process Analysis
317
Figure 10.34.2: Value Stream Map
10.34.4
Usage Considerations
.1 Strengths
• Ensures solutions address the right issues, minimizing waste.
• Many different techniques and methodologies can be used and provide teams
with great flexibility in approach.
.2 Limitations
• Can be time-consuming.
• There are many techniques and methodologies in process analysis. It can be
challenging to decipher which to use and how rigorously to follow them, given
the scope and purpose.
• May prove ineffective at process improvement in knowledge or decision-
intensive processes.
Shipment
Shipment
Supplier
Documents
(Manual
Information)
Customer
Time
Time
Time
Time
Total elapsed time
Time
Data
Process
Activity/Tasks
Process
Activity/Tasks
Data
Non-value adding time
Value-adding time
Time
Wait time
Processing/
Conversion time
Process
Activity/Tasks
Data
Process
Activity/Tasks
Data
Time
Electronic Information Flow



Process Modelling
Techniques
318
10.35
Process Modelling
10.35.1
Purpose
Process modelling is a standardized graphical model used to show how work is
carried out and is a foundation for process analysis.
10.35.2
Description
Process models describe the sequential flow of work or activities. A business
process model describes the sequential flow of work across defined tasks and
activities through an enterprise or part of an enterprise. A system process model
defines the sequential flow of control among programs or units within a
computer system. A program process flow shows the sequential execution of
program statements within a software program. A process model can also be
used in documenting operational procedures.
A process model can be constructed on multiple levels, each of which can be
aligned to different stakeholder points of view. These levels exist to progressively
decompose a complex process into component processes, with each level
providing increasing detail and precision. At a high (enterprise or context) level,
the model provides a general understanding of a process and its relationship to
other processes. At lower (operational) levels, it can define more granular
activities and identify all outcomes, including exceptions and alternative paths. At
the lowest (system) level, the model can be used as a basis for simulation or
execution.
Process models can be used to:
• describe the context of the solution or part of the solution,
• describe what actually happens, or is desired to happen, during a process,
• provide an understandable description of a sequence of activities to an
external observer,
• provide a visual to accompany a text description, and
• provide a basis for process analysis.
The business analyst can use a process model to define the current state of a
process (also known as an as-is model) or a potential future state (also known as
a to-be model). A model of the current state can provide understanding and
agreement as to what happens now. A model of the future state can provide
alignment with what is desired to happen in the future.
Process models generally include:
• the participants in the process,
• the business event that triggers the process,
• the steps or activities of the process (both manual and automated),
• the paths (flows) and decision points that logically link those activities, and



Techniques
Process Modelling
319
• the results of the process.
The most basic process model includes: a trigger event, a sequence of activities,
and a result.
A more comprehensive process model can include other elements, such as data/
materials, inputs and outputs, and call-out descriptions that supplement the
graphical representation.
10.35.3
Elements
.1 Types of Process Models and Notations
Many different notations are used in process modelling.
The most commonly used notations include the following:
• Flowcharts and Value Stream Mapping (VSM): used in the business
domain.
• Data Flow diagrams and Unified Modelling Language™ (UML®)
diagrams: used in the information technology domain.
• Business Process Model and Notation (BPMN): used across both
business and information technology domains; is increasingly adopted as an
industry standard.
• Integrated DEFinition (IDEF) notation and Input, Guide, Output,
Enabler (IGOE) diagrams: used for establishing scope.
• SIPOC and Value Stream Analysis: used for process modelling.
Process models typically contain some or all of the following key elements:
• Activity: an individual step or piece of work that forms part of the business
process. It may be a single task or may be further decomposed into a sub-
process (with its own activities, flow, and other process elements).
• Event: a zero-time occurrence which initiates, interrupts, or terminates an
activity or task within a process or the process itself. It may be a message
received, the passage of time, or the occurrence of a condition as defined in
the business rules.
• Directional Flow: a path that indicates the logical sequence of the
workflow. In general, diagrams are drawn to show the passage of time in a
consistent fashion (typically in the direction that text would be read).
• Decision Point: a point in the process where the flow of work splits into
two or more flows (paths), which may be mutually exclusive alternatives or
parallels. A decision can also be used to locate rules where separate flows
merge together.
• Link: a connection to other process maps.
• Role: a type of person or group involved in the process. Its definitions
typically match those in the organizational model.



Process Modelling
Techniques
320
Flowchart
Flowcharts are used commonly with non-technical audiences and are good for
gaining both alignment with what the process is and context for a solution. A
flowchart can be simple, displaying just the sequence of activities, or it can be
more comprehensive, using swimlanes. A swimlane is a partitioned area
(horizontal or vertical) that segregates those activities in the process that are
carried out by a particular role.
Figure 10.35.1: Flowchart
Business Process Model and Notation (BPMN)
Business Process Model and Notation (BPMN) provides an industry-standard
language for modelling business processes in a form that is accessible by both
business users and technical developers. BPMN is designed to cover many types of
modelling, including both internal (private) processes and collaborative (public)
processes. It can be the input to process automation technologies.
A key feature of BPMN is its ability to distinguish the activities of different
participants in a process with pools and swimlanes. When the flow of work
crosses the boundary of a swimlane, responsibility for the work then passes to
Swimlane for Role 1
Swimlane for Role 2
Task 1
Start
Flow merge
into a task.
Task 2A
Task 2B
Stop
Task 3
Sub-Process
A sub-process embeds
another process model.
Input/Output
The flow of work splits.
Tasks are executed in
parallel.
Swimlanes are an unofficial, but common,
extension to the flowcharting standard.
Decision
True
False



Techniques
Process Modelling
321
another role within the organization. Swimlanes are part of a pool. A pool is a
self-regulating (free-standing) business entity, typically an organization or a
system. A pool may include a number of swimlanes, each of which represents a
role. Commonly, a process includes one pool for the customer and a second pool
for the organization under study, although it is possible for a process to include
any number of pools.
Figure 10.35.2: Business Process Model and Notation
Activity Diagram
The activity diagram is one of the use case realization diagrams defined in the
Unified Modelling Language™ (UML®). Originally designed to elaborate on a
single use case, the activity diagram has been adopted for more general process
modelling purposes, including business process modelling. While similar in
appearance to a flowchart, the activity diagram typically employs swimlanes to
show responsibilities, synchronization bars to show parallel processing, and
multiple exit decision points.
Lane 1
Lane 2
X
End Event
Task 1
Task 2B
Task 2A
*nput/Output
Task
Task 3
Data Store
Parallel Split
Parallel Join
Sub-process
successful?
The flow of work splits.
Tasks are executed in
parallel.
A sub-process embeds
another process model.
The flow of work
merges. The join must
be explicit.
Exclusive Gateway. The
decision is not made at
the gateway. It is made
in a preceding task.
Sub-Process
Start Event



Process Modelling
Techniques
322
Figure 10.35.3: Activity Diagram
10.35.4
Usage Considerations
.1 Strengths
• Appeals to the basic human understanding of sequential activities.
• Most stakeholders are comfortable with the concepts and basic elements of a
process model.
• The use of levels can accommodate the different perspectives of various
stakeholder groups.
• Effective at showing how to handle a large number of scenarios and parallel
branches.
• Can help identify any stakeholder groups that may have otherwise been
overlooked.
• Facilitates the identification of potential improvements by highlighting “pain
points” in the process structure (i.e. process visualization).
Partition for Role 1
Partition for Role 2
The flow of work splits.
Tasks are executed in
parallel.
Task 1
Task 2A
Task 2B
Task (I/O)
A sub-process embeds
another process model.
Task 3
Sub-Process
Flow merges.
Decision
[True]
[False]



Techniques
Prototyping
323
• Likely to have value in its own right. They provide documentation for
compliance purposes and can be used by business stakeholders for training and
coordination of activities.
• Can be used as a baseline for continuous improvement.
• Ensures labelling consistency across artifacts.
• Provides transparency and clarity to process owners and participants on activity
responsibilities, sequence and hand-overs.
.2 Limitations
• To many people in IT, a formal process model tends to reflect an older and more
document-heavy approach to software development. Therefore, project time is
not allocated to developing a process model, especially of the current state or
problem domain.
• Can become extremely complex and unwieldy if not structured carefully. This is
especially true if business rules and decisions are not managed separately from
the process.
• Complex processes can involve many activities and roles; this can make them
almost impossible for a single individual to understand and ‘sign off’.
• Problems in a process cannot always be identified by looking at a high-level
model. A more detailed model with reference to metadata (such as path
frequency, cost, and time factors) is usually required. It is often necessary to
engage with stakeholders directly to find the operational problems they have
encountered while working with a process.
• In a highly dynamic environment where things change quickly, process models
can become obsolete.
• May prove difficult to maintain if the process model only serves as
documentation, as stakeholders may alter the process to meet their needs
without updating the model.
10.36
Prototyping
10.36.1
Purpose
Prototyping is used to elicit and validate stakeholder needs through an iterative
process that creates a model or design of requirements. It is also used to optimize
user experience, to evaluate design options, and as a basis for development of the
final business solution.
10.36.2
Description
Prototyping is a proven method for product design. It works by providing an early
model of the final result, known as a prototype. Prototyping is used to identify
both missing or improperly specified requirements and unsubstantiated



Prototyping
Techniques
324
assumptions by demonstrating what the product looks like and how it acts in the
early stages of design.
Prototypes can be non-working models, working representations, or digital
depictions of a solution or a proposed product. They can be used to mock up
websites, serve as a partially working construct of the product, or describe
processes through a series of diagrams (such as workflow). Business rules and
data prototypes can be used to discover desired process flow and business rules.
Data prototyping can be used for data cleansing and transformation.
10.36.3
Elements
.1 Prototyping Approach
There are two common approaches to prototyping:
• Throw-away: prototypes are generated with simple tools (such as paper
and pencil, a whiteboard, or software) to serve the goal of uncovering and
clarifying requirements. The prototype may be updated or evolve during the
course of discussion and development, but does not become workable
code or get maintained as a deliverable once the final system or process is
implemented. This method is helpful for identifying functionality or
processes that are not easily elicited by other techniques, have conflicting
points of view, or are difficult to understand. These prototypes can be an
inexpensive tool to uncover or confirm requirements that go beyond an
interface including requirements related to processes, data, and business
rules.
• Evolutionary or Functional: prototypes are created to extend initial
requirements into a functioning solution as requirements are further
defined through stakeholder use. This approach produces a working
solution and usually requires a specialized prototyping tool or language.
These prototypes may be used in the final solution. If specialized software is
used, business processes, rules, and data can be simulated to evaluate the
impact of changes and validate desired outcomes.
.2 Prototyping Examples
There are many forms of prototyping in use today.
Each of the following can be considered a form of prototyping:
• Proof of Principle or Proof of Concept: is a model created to validate the
design of a system without modelling the appearance, materials used in the
creation of work, or processes/workflows ultimately used by the
stakeholders.
• Form Study Prototype: is used to explore the basic size, look, and feel of
a product that will be manufactured, without creating actual functionality.
It is used to assess ergonomic and visual factors using a sculptural
representation of the product made from inexpensive materials. This type of
prototype may also be used to model a workflow or navigation at a high



Techniques
Prototyping
325
level in order to identify gaps or inconsistencies in the possible solution of
the properties (for example, appearance, configuration).
• Usability Prototype: is a product model created to test how the end user
interacts with the system without including any of the properties (for
example, appearance, configuration).
• Visual Prototype: is a product model created to test the visual aspects of
the solution without modelling the complete functionality.
• Functional Prototype: is a model created to test software functionality,
qualities of the system for the user (for example, appearance), and
workflow. It is also referred to as a working model and is used both to
simulate business processes and business rules and to evaluate software
function calls.
.3 Prototyping Methods
The following is a list of commonly used methods for prototyping:
• Storyboarding: is used to visually and textually detail the sequence of
activities by summing up different user interactions with the solution or
enterprise.
• Paper Prototyping: uses paper and pencil to draft an interface or process.
• Workflow Modelling: depicts a sequence of operations that are
performed and usually focuses solely on the human aspect.
• Simulation: is used to demonstrate solutions or components of a solution.
It may test various processes, scenarios, business rules, data, and inputs.
10.36.4
Usage Considerations
.1 Strengths
• Provides a visual representation for the future state.
• Allows for stakeholders to provide input and feedback early in the design
process.
• When using throw-away or paper prototyping methods, users may feel more
comfortable being critical of the mock-up because it is not polished and
release-ready.
• A narrow yet deep vertical prototype can be used for technical feasibility
studies, proof of concept efforts, or to uncover technology and process gaps.
.2 Limitations
• If the system or process is highly complex, the prototyping process may become
bogged down with discussion of 'how' rather than 'what', which can make the
process take considerable time, effort, and facilitation skill.
• Underlying technology may need to be understood or assumed in order to
initiate prototyping.



Reviews
Techniques
326
• If the prototype is deeply elaborate and detailed, stakeholders may develop
unrealistic expectations for the final solution. These can range from assumed
completion dates to higher expectations of performance, reliability, and
usability.
• Stakeholders may focus on the design specifications of the solution rather than
the requirements that any solution must address. This can, in turn, constrain
the solution design. Developers may believe that they must provide a user
interface that precisely matches the prototype, even if more elegant technology
and interface approaches exist.
10.37
Reviews
10.37.1
Purpose
Reviews are used to evaluate the content of a work product.
10.37.2
Description
Different types of reviews are conducted for business analysis work products.
Each is tailored to the needs of the organization and business analyst, and uses
these dimensions:
• Objectives: defining the purpose of the review.
• Techniques: identifying either a formal or informal way to perform the
review.
• Participants: identifying who should take part in the review activity.
Each review is focused on a work product, not the skills or actions of the
participants. The work product may be a package of several deliverables, a single
deliverable, a portion of a deliverable, or work in process. For a completed work
product, the objective of the review is usually to remove defects or inform the
reviewers about the content. For work in process, the review may be conducted
to resolve an issue or question.
Each review includes the business analyst as a participant. Reviewers may be
peers, especially for work in process, or stakeholders, who validate that the work
product is complete and correct. The review steps depend on the technique used.
Reviews can include:
• an overview of the work product and review objectives,
• checklists and reference materials that can be used by reviewers,
• reviewing the work product and documenting the findings, and
• verifying any rework.
Using feedback from reviewers, the business analyst updates the work product.



Techniques
Reviews
327
10.37.3
Elements
.1 Objectives
Objectives are clearly communicated to all participants prior to the review.
Objectives may include one or more goals, for example:
• to remove defects,
• to ensure conformance to specifications or standards,
• to ensure the work product is complete and correct,
• to establish consensus on an approach or solution,
• to answer a question, resolve an issue, or explore alternatives,
• to educate reviewers about the work product, and
• to measure work product quality.
.2 Techniques
Reviews can be formal or informal. The techniques used during a review are
selected to support the objectives of the review.
The following techniques are commonly used by business analysts when
conducting reviews:
• Inspection: a formal technique that includes an overview of the work
product, individual review, logging the defects, team consolidation of
defects, and follow-up to ensure changes were made. The focus is to
remove defects and create a high quality work product. While usually
performed by peers, it can also be used for stakeholder reviews.
• Formal Walkthrough (also known as Team Review): a formal
technique that uses the individual review and team consolidation activities
often seen in inspection. Walkthroughs are used for peer reviews and for
stakeholder reviews.
• Single Issue Review (also known as Technical Review): a formal
technique focused on either one issue or a standard in which reviewers
perform a careful examination of the work product prior to a joint review
session held to resolve the matter in focus.
• Informal Walkthrough: an informal technique in which the business
analyst runs through the work product in its draft state and solicits
feedback. Reviewers may do minimal preparation before the joint review
session.
• Desk Check: an informal technique in which a reviewer who has not been
involved in the creation of the work product provides verbal or written
feedback.
• Pass Around: an informal technique in which multiple reviewers provide
verbal or written feedback. The work product may be reviewed in a
common copy of the work product or passed from one person to the next.



Reviews
Techniques
328
• Ad hoc: an informal technique in which the business analyst seeks informal
review or assistance from a peer.
.3 Participants
Participant roles involved in any particular review depend on the objectives of the
review, the selected technique, and any organizational standards that may be in
place.
In some situations, a supervisor or manager may be one of the reviewers because
of their expertise. In these situations, the moderator is careful to avoid adversely
affecting the level of candour of other participants or inappropriately affecting
decisions of the team.
10.37.4
Usage Considerations
.1 Strengths
• Can help identify defects early in the work product life cycle, eliminating the
need for expensive removal of defects discovered later in the life cycle.
• All parties involved in a review become engaged with the final outcome; they
have a vested interest in a quality result.
Table 10.37.1: Review Roles
Role
Description
Responsibility
Applicable
Techniques
Author
Author of the
work product.
Answers questions about the work product and
listens to suggestions and comments.
Incorporates changes into the work product after
the review.
All
Reviewer
A peer or
stakeholder.
Examines the work product according to the
review objectives. For defect detection reviews,
the reviewer examines the work product prior to
a review session and keeps track of both defects
found and suggestions for improvement.
All
Facilitator
A neutral
facilitator
(should not be
the author in
order to avoid
compromising
the review).
Facilitates the review session, keeps participants
focused on the objectives of the review and
ensures that each relevant section of the work
product is covered. Validates that reviewers have
examined the work product before the session
begins and ensures that all reviewers participate
in the review session.
• Inspection
• Formal
walkthrough
• May be helpful
for single issue
review
Scribe
A neutral
participant with
strong
communication
skills.
Documents all defects, suggestions, comments,
issues, concerns, and outstanding questions that
are raised during a review session. Familiarity with
the subject matter enables the scribe to capture
items clearly.
• Inspection
• Formal and
informal
walkthrough



Techniques
Risk Analysis and Management
329
• Desk checks and pass around reviews can be performed by a reviewer at a
convenient time, rather than interrupting work in progress to attend a meeting.
.2 Limitations
• Rigorous team reviews take time and effort. Thus, only the most critical work
products might be reviewed using inspection or formal walkthrough
techniques.
• Informal reviews by one or two reviewers are practical in terms of the effort
required, but they provide less assurance of removing all significant defects
than using a larger team and more formal process.
• For desk checks and pass around reviews it may be difficult for the author to
validate that an independent review was done by each participant.
• If review comments are shared and discussed via e-mail there may be many
messages to process, which makes it difficult for the author to resolve
disagreements or differences in suggested changes.
10.38
Risk Analysis and Management
10.38.1
Purpose
Risk analysis and management identifies areas of uncertainty that could
negatively affect value, analyzes and evaluates those uncertainties, and develops
and manages ways of dealing with the risks.
10.38.2
Description
Failure to identify and manage risks may negatively affect the value of the
solution. Risk analysis and management involves identifying, analyzing, and
evaluating risks. Where sufficient controls are not already in place, business
analysts develop plans for avoiding, reducing, or modifying the risks, and when
necessary, implementing these plans.
Risk management is an ongoing activity. Continuous consultation and
communication with stakeholders helps to both identify new risks and to monitor
identified risks.
10.38.3
Elements
.1 Risk Identification
Risks are discovered and identified through a combination of expert judgment,
stakeholder input, experimentation, past experiences, and historical analysis of
similar initiatives and situations. The goal is to identify a comprehensive set of
relevant risks and to minimize the unknowns. Risk identification is an ongoing
activity.



Risk Analysis and Management
Techniques
330
A risk event could be one occurrence, several occurrences, or even a non-
occurrence. A risk condition could be one condition or a combination of
conditions. One event or condition may have several consequences, and one
consequence may be caused by several different events or conditions.
Each risk can be described in a risk register that supports the analysis of those risks
and plans for addressing them.
.2 Analysis
Analysis of a risk involves understanding the risk, and estimating the level of a
risk. Sometimes controls may already be in place to deal with some risks, and
these should be taken into account when analyzing the risk.
Figure 10.38.1: Example of a Risk Register
#
Risk Event or
Condition
Consequence
Probability
Impact
Risk
Level
Risk
Modification
Plan
Risk
Owner
Residual Risk
Probability
Impact
Risk
Level
1 If the union
does not
agree with
changes to
job
descriptions
then planned
staff changes
will not be
able to occur
Medium
Medium
Medium Begin
consultations
with the union
no later than
next month
Marta
Low
Low
Low
2 If subject
matter
experts are
not available
for
requirements
elicitation
then scope
and quality
will be
reduced, and
the delivery
date will be
pushed back
Medium
High
High
Develop a plan
for when the
SME’s are
required, hold
on-site
workshops and
obtain
agreement
from the
sponsor about
their
participation
Deepak
Low
Medium
Low
3 If an
insufficient
number of
customers
reply to our
survey
then we will
not have a
representative
sample of
customer
requirements
Medium
High
High
Contract with
a firm that
specializes in
survey
management
to develop and
run the survey
François
Low
Medium
Low
4 If the
organizationa
l structure
does not
adjust to the
new business
processes
then the
enterprise will
not be able to
achieve the
planned
efficiencies
and the
business need
will not be
met
High
High
High
The business
sponsor must
approve the
organizational
changes prior
to deployment,
and the
changes must
occur prior to
deployment
Jiahui
Medium
Low
Medium



Techniques
Risk Analysis and Management
331
The likelihood of occurrence could be expressed either as a probability on a
numerical scale or with values such as Low, Medium, and High.
The consequences of a risk are described in terms of their impact on the potential
value. The impact of any risk can be described in terms of cost, duration, solution
scope, solution quality, or any other factor agreed to by the stakeholders such as
reputation, compliance, or social responsibility.
While an enterprise may have a standard or baseline risk impact scale, the
categories like cost, effort, and reputation, and the thresholds may be adjusted to
consider the potential value and the level of risk that is acceptable. Typically, three
to five broad categories of level are used to describe how to interpret the
potential impact.
The level of a given risk may be expressed as a function of the probability of
occurrence and the impact. In many cases, it is a simple multiplication of
probability and impact. The risks are prioritized relative to each other according to
their level. Risks which could occur in the near term may be given a higher priority
than risks which are expected to occur later. Risks in some categories such as
reputation or compliance may be given higher priority than others.
.3 Evaluation
The risk analysis results are compared with the potential value of the change or of
the solution to determine if the level of risk is acceptable or not. An overall risk
level may be determined by adding up all the individual risk levels.
Table 10.38.1: Example of a Risk Impact Scale
Scope
Quality
Cost
Effort
Duration
Reputation
Social
Responsibility
Low
Impact
Minor areas
of scope are
affected
Minor
quality
problems
Less than
1% cost
impact
Less than
2% extra
days
effort
Delay of
up to
3%
Very minor
impact to
enterprise’s
reputation
Minor
impediment
Medium
Impact
Major areas
of scope are
affected, but
workarounds
are feasible
Significant
quality
issues, but
the
product is
still usable
More
than 1%
but less
than 3%
impact
2% -10%
extra days
effort
Delay of
3%-
10%
Moderate
impact to
enterprise’s
reputation
Major
impediment
High
Impact
The product
does not
meet the
business
need
The
product is
not usable
More
than 3%
impact
More
than 10%
extra days
effort
Delay of
more
than
10%
Severe
impact to
enterprise’s
reputation
Severe
impediment



Risk Analysis and Management
Techniques
332
.4 Treatment
Some risks may be acceptable, but for other risks it may be necessary to take
measures to reduce the risk.
One or more approaches for dealing with a risk may be considered, and any
combination of approaches could be used to address a risk:
• Avoid: either the source of the risk is removed, or plans are adjusted to
ensure that the risk does not occur.
• Transfer: the liability for dealing with the risk is moved to, or shared with, a
third party.
• Mitigate: reduce the probability of the risk occurring or the possible
negative consequences if the risk does occur.
• Accept: decide not to do anything about the risk. If the risk does occur, a
workaround will be developed at that time.
• Increase: decide to take on more risk to pursue an opportunity.
Once the approach for dealing with a specific risk is selected, a risk response plan
is developed and assigned to a risk owner with responsibility and authority for
that risk. In the case of risk avoidance, the risk owner takes steps to ensure that
the probability or the impact of the risk is reduced to nil. For those risks which
cannot be reduced to nil, the risk owner is responsible for monitoring the risk, and
for implementing a risk mitigation plan.
The risk is re-analyzed to determine the residual risk which is the new probability
and new impact as a result of the measures taken to modify the risk. There could
be a cost-benefit analysis done to determine if the cost and effort of the measures
reduces the level of risk enough to make it worthwhile. The risks may be re-
evaluated in terms of the residual risk.
Stakeholders should be informed of the plans for modifying the risks.
10.38.4
Usage Considerations
.1 Strengths
• Can be applied to strategic risks which affect long-term value of the enterprise,
tactical risks which affect the value of a change, and operational risks which
affect the value of a solution once the change is made.
• An organization typically faces similar challenges on many of its initiatives. The
successful risk responses on one initiative can be useful lessons learned for
other initiatives.
• The risk level of a change or of a solution could vary over time. Ongoing risk
management helps to recognize that variation, and to re-evaluate the risks and
the suitability of the planned responses.



Techniques
Roles and Permissions Matrix
333
.2 Limitations
• The number of possible risks to most initiatives can easily become
unmanageably large. It may only be possible to manage a subset of potential
risks.
• There is the possibility that significant risks are not identified.
10.39
Roles and Permissions Matrix
10.39.1
Purpose
A roles and permissions matrix is used to ensure coverage of activities by denoting
responsibility, to identify roles, to discover missing roles, and to communicate
results of a planned change.
10.39.2
Description
Role and permission allocation involves identifying roles, associating these with
solution activities, and then denoting authorities who can perform these
activities. A role is a label for a group of individuals who share common functions.
Each function is portrayed as one or more solution activities. A single activity can
be associated with one or more roles by designating authorities. Each individual
that is assigned this authority can perform the associated activity.
The following is an example of a roles and permissions matrix for a software
system.
Figure 10.39.1: Roles and Permissions Matrix
Roles and Permissions
Matrix
Role Group 1
Administrator
Manager
Role Group 2
Sales
Customer
Activity
Create new account
X
X


X
Modify account
X
X

X
Create order
X
X
X
X
View reports
X
X
X

Create reports
X
X
X




Roles and Permissions Matrix
Techniques
334
10.39.3
Elements
.1 Identifying Roles
To identify roles for either internal or external stakeholders, business analysts:
• review any organizational models, job descriptions, procedure manuals, and
system user guides, and
• meet with stakeholders to uncover additional roles.
Through this review and discussion, the business analyst considers both that
individuals with the same job title may have different roles and that individuals
with different job titles may have the same roles.
When identifying roles, business analysts look for common functions that are
performed by individuals with similar needs.
.2 Identifying Activities
Business analysts frequently use functional decomposition to break down each
function into sub-parts, process modelling to better understand the workflow
and division of work among users, and use cases to represent tasks. By
performing these techniques, the business analyst can ensure that all functions
are accounted for and their activities are identified among various use case
scenarios.
There may be different levels of abstraction for roles and permission matrices
based on the business analysis perspective. Initiative level roles and responsibilities
may be identified in a RACI (Responsible, Accountable, Consulted, Informed)
matrix. Specific information technology system roles and responsibilities may be
identified in a CRUD (Create, Read, Update, and Delete) matrix.
.3 Identifying Authorities
Authorities are actions that identified roles are permitted to perform. For each
activity, the business analyst identifies the authorities for each role. When
identifying authorities, business analysts consider the level of security needed and
how the work flows through the process. Business analysts collaborate with
stakeholders to validate identified authorities.
.4 Refinements
Delegations
The business analyst may also identify which authorities can be delegated by one
individual to another on a short-term or permanent basis.
Inheritances
Stakeholders may request that when an individual is assigned an authority at an
organizational hierarchy level that this assignment pertain to only that user’s
organizational level and any subsidiary organizational unit levels.



Techniques
Root Cause Analysis
335
10.39.4
Usage Considerations
.1 Strengths
• Provides procedural checks and balances, as well as data security, by restricting
individuals from performing certain actions.
• Promotes improved review of transaction history, in that audit logs can capture
details about any assigned authorities at the time.
• Provides documented roles and responsibilities for activities.
.2 Limitations
• Need to recognize the required level of detail for a specific initiative or activity;
too much detail can be time-consuming and not provide value, too little detail
can exclude necessary roles or responsibilities.
10.40
Root Cause Analysis
10.40.1
Purpose
Root cause analysis is used to identify and evaluate the underlying causes of a
problem.
10.40.2
Description
Root cause analysis is a systematic examination of a problem or situation that
focuses on the problem's origin as the proper point of correction rather than
dealing only with its effects. It applies an iterative analysis approach in order to
take into account that there might be more than one root cause contributing to
the effects. Root cause analysis looks at the main types of causes such as people
(human error, lack of training), physical (equipment failure, poor facility), or
organizational (faulty process design, poor structure).
Root cause analysis helps organize the information in a framework, which allows
for deeper analysis if needed. Root cause analysis can be used for:
• Reactive Analysis: identifying the root cause(s) of an occurring problem
for corrective action, or
• Proactive Analysis: identifying potential problem areas for preventive
action.
Root cause analysis uses four main activities:
• Problem Statement Definition: describes the issue to be addressed.
• Data Collection: gathers information about the nature, magnitude,
location, and timing of the effect.
• Cause Identification: investigates the patterns of effects to discover the
specific actions that contribute to the problem.



Root Cause Analysis
Techniques
336
• Action Identification: defines the corrective action that will prevent or
minimize recurrence.
10.40.3
Elements
.1 The Fishbone Diagram
A fishbone diagram (also known as an Ishikawa or cause-and-effect diagram) is
used to identify and organize the possible causes of a problem. This tool helps to
focus on the cause of the problem versus the solution and organizes ideas for
further analysis. The diagram serves as a map that depicts possible cause-and-
effect relationships.
Steps to develop a fishbone diagram include:
Step 1.
Capturing the issue or problem under discussion in a box at the
top of the diagram.
Step 2.
Drawing a line from the box across the paper or whiteboard
(forming the spine of the fishbone).
Step 3.
Drawing diagonal lines from the spine to represent categories of
potential causes of the problem. The categories may include
people, processes, tools, and policies.
Step 4.
Drawing smaller lines to represent deeper causes.
Step 5.
Brainstorming categories and potential causes of the problem and
capturing them under the appropriate category.
Step 6.
Analyzing the results. Remember that the group has identified
only potential causes of the problem. Further analysis is needed to
validate the actual cause, ideally with data.
Step 7.
Brainstorming potential solutions once the actual cause has been
identified.
Figure 10.40.1: Fishbone Diagram
Category 1
Primary Cause
Tertiary Cause
Secondary Cause
Category 2
Effect
Category N
Category 3



Techniques
Root Cause Analysis
337
.2 The Five Whys
The five whys is a question asking process to explore the nature and cause of a
problem. The five whys approach repeatedly asks questions in an attempt to get
to the root cause of the problem. This is one of the simplest facilitation tools to
use when problems have a human interaction component.
To use this technique:
Step 1.
Write the problem on a flip chart or whiteboard.
Step 2.
Ask "Why do you think this problem occurs?" and capture the
idea below the problem.
Step 3.
Ask "Why?" again and capture that idea below the first idea.
Continue with step 3 until you are convinced the actual root cause has been
identified. This may take more or less than five questions—the technique is called
the five whys because it often takes that many to reach the root cause, not
because the question must be asked five times.
The five whys can be used alone or as part of the fishbone diagram technique.
Once all ideas are captured in the diagram, use the five whys approach to drill
down to the root causes.
10.40.4
Usage Considerations
.1 Strengths
• Helps to maintain an objective perspective when performing cause-and-effect
analysis.
• Enables stakeholders to specify an effective solution at the appropriate points
for corrective action.
.2 Limitations
• Works best when the business analyst has formal training to ensure the root
causes, not just symptoms of the problem, are identified.
• May be difficult with complex problems; the potential exists to lead to a false
trail and/or dead–end conclusion.



Scope Modelling
Techniques
338
10.41
Scope Modelling
10.41.1
Purpose
Scope models define the nature of one or more limits or boundaries and place
elements inside or outside those boundaries.
10.41.2
Description
Scope models are commonly used to describe the boundaries of control, change,
a solution, or a need. They may also be used to delimit any simple boundary (as
distinct from horizons, emergent properties, and recursive systems).
These models may show elements that include:
• In-scope: the model identifies a boundary as seen from inside, as well as
the elements contained by that boundary (for example, functional
decomposition).
• Out-of-scope: the model identifies a boundary as seen from outside, as
well as the elements that are not contained by that boundary (for example,
context diagram).
• Both: the model identifies a boundary as seen from both sides, as well as
elements on both sides of the boundary (for example, venn diagram or use
case model).
Scope models provide the basis for understanding the boundaries of:
• Scope of Control: what is being analyzed, roles and responsibilities, and
what is internal and external to the organization.
• Scope of Need: stakeholder needs, value to be delivered, functional areas,
and organizational units to be explored.
• Scope of Solution: requirements met, value delivered, and impact of
change.
• Scope of Change: actions to be taken, stakeholders affected or involved,
and events to cause or prevent.
Scope models are typically represented as a combination of diagrams, matrices,
and textual explanations. If the scope is implemented in phases or iterations, the
scope model should be described per each phase or iteration.
10.41.3
Elements
.1 Objectives
Scope models are typically used to clarify the:
• span of control,
• relevance of elements, and
• where effort will be applied.



Techniques
Scope Modelling
339
Depending on the action or stakeholder needs the model supports, a business
analyst determines the types of models to be used and selects boundaries and
elements.
.2 Scope of Change and Context
Typically, business analysts are concerned with elements that will be altered as
part of a change, as well as external elements that are relevant to the change. For
elements inside the scope of change, the business analyst is involved in
establishing the ways those elements are modified. For elements outside the
scope of change but relevant to the change, the business analyst is involved in
establishing the interactions between the change, the current and proposed
solutions, and the context.
The business analyst often determines:
• business processes to be defined or modified,
• business functions to be added, changed, optimized, or re-assigned,
• new capabilities to be built or existing capabilities to be changed,
• external and internal events to be responded to,
• use cases and situations to be supported,
• technologies to be changed or replaced,
• informational assets to be acquired, produced, or processed,
• stakeholders and organizational roles impacted by the change,
• external and internal agents and entities impacted by the change,
• organizations and organizational units (departments, teams, groups)
impacted by the change, and
• systems, components, tools, and physical assets required for the change or
impacted by the change.
.3 Level of Detail
The purpose of analysis defines the appropriate level of abstraction at which
scope elements are described. A proper level of detail provides a meaningful
reduction of uncertainty while preventing 'analysis paralysis' at a scope definition
stage. The elements of the final scope model can be described by enumerating
them, by referring to a specific level of their decomposition hierarchy, or by
grouping them into logically bound sets. For example, a subject of change can be
defined as a list of specific business processes, as a high-level business process
encompassing all of them, or as a generic business function. Similarly,
stakeholders included in the scope can be defined by enumerating specific titles
or by referring to their common organizational role.



Scope Modelling
Techniques
340
.4 Relationships
Exploring relationships between potential scope elements helps to ensure
completeness and integrity of the scope model by identifying their dependencies
or by discovering other elements involved in or impacted by the change.
Various diagramming techniques are available for exploring relationships of
specific types, including:
• Parent-Child or Composition-Subset: relates elements of the same type
by way of hierarchical decomposition. Relationships of this type appear as
an organization chart, in a class or entity-relationship diagram, as sub-
processes in a business process model, or as composite states on a state
diagram.
• Function-Responsibility: relates a function with the agent (stakeholder,
organizational unit, or solution component) that is responsible for its
execution. Relationships of this type appear on business process models and
on collaboration, sequence, and use case diagrams.
• Supplier-Consumer: relates elements by way of the transmission of
information or materials between them. Elements can be processes,
systems, solution components, and organizational units, for both internal
and external entities. Relationships of this type occur in data flow diagrams,
business process models, and in collaboration, sequence, and robustness
diagrams.
• Cause-Effect: relates elements by logical contingency in order to identify
chains of associated elements that are involved in or impacted by the
change. Relationships of this type appear in fishbone (Ishikawa) diagrams
and other cause-effect diagrams.
• Emergent: in most complex systems, several elements can interact to
produce results that cannot be predicted or understood based on the
components alone.
.5 Assumptions
At a time of scope modelling, the validity of the model heavily relies on
assumptions such as the definition of needs, causality of outcomes, impact of
changes, applicability, and feasibility of the solution. The resulting scope model
should include explicit statements of critical assumptions and their implications.
.6 Scope Modelling Results
Results of scope modelling can be represented as:
• textual descriptions of elements, including criteria for making in-scope or
out-of-scope decisions,
• diagrams illustrating relationships of scope elements, and
• matrices depicting dependencies between scope elements.



Techniques
Sequence Diagrams
341
10.41.4
Usage Considerations
.1 Strengths
• A scope model facilitates agreement as a basis for:
• defining contractual obligations,
• estimating the project effort,
• justifying in-scope/out-of-scope decisions in requirements analysis, and
• assessing the completeness and impact of solutions.
.2 Limitations
• An initial, high-level model can lack a sufficient level of granularity, particularly
for boundary elements, that is needed to ensure clear scope identification.
• Once a scope is defined, changing it may be difficult due to political reasons
and contractual obligations. Meanwhile, many factors can affect the scope
validity before the targets are achieved. Such factors as wrong initial
assumptions, situation change, evolution of stakeholder needs, or technology
innovations may cause a need for revising the scope partially or entirely.
• Traditional scope models cannot address common complex boundaries, such as
a horizon (a boundary that is completely dependent on the position of the
stakeholder).
10.42
Sequence Diagrams
10.42.1
Purpose
Sequence diagrams are used to model the logic of usage scenarios by showing
the information passed between objects in the system through the execution of
the scenario.
10.42.2
Description
A sequence diagram shows how processes or objects interact during a scenario.
The classes required to execute the scenario and the messages they pass to one
another (triggered by steps in the use case) are displayed on the diagram. The
sequence diagram shows how objects used in the scenario interact, but not how
they are related to one another. Sequence diagrams are also often used to show
how user interface components or software components interact.
The diagram represents information in a horizontal and vertical alignment. The
objects that send messages to each other are represented as boxes that are
aligned at the top of the page from the left to the right, with each object
occupying a column of space on the page bordered by a vertical line stretching
down to the bottom of the page. The messages that are sent from one object to



Sequence Diagrams
Techniques
342
the next are represented as horizontal arrows. The order of the messages is
represented in a top-down and left-to-right sequence beginning with the first
message at the top left of the page and subsequent messages occurring to the
right and below. Sequence diagrams are sometimes called event diagrams.
The standard notation for sequence diagrams is defined as part of the Unified
Modelling Language™ (UML®) specification.
10.42.3
Elements
.1 Lifeline
A lifeline represents the lifespan of an object during the scenario being modelled
in a sequence diagram. The example below shows the object order. A lifeline is
drawn as a dashed line that vertically descends from each object box to the
bottom of the page.
Figure 10.42.1: Lifeline
.2 Activation Box
An activation box represents the period during which an operation is executed. A
call to activate is represented by an arrow with a solid arrowhead leading to the
activation object. The lifeline can be terminated with an X.
Figure 10.42.2: Activation Box



Techniques
Sequence Diagrams
343
.3 Message
A message is an interaction between two objects. A message is shown as an
arrow coming from the activation box of the object that sends the message to the
activation box of the object that receives the message.
The name of the message is placed on top of the arrowed line. There are different
types of messages:
• Synchronous Call: transfers control to the receiving object. The sender
cannot act until a return message is received.
• Asynchronous Call: (also known as a signal) allows the object to continue
with its own processing after sending the signal. The object may send many
signals simultaneously, but may only accept one signal at a time.
Figure 10.42.3: Message
10.42.4
Usage Considerations
.1 Strengths
• Shows the interaction between the objects of a system in the chronological
order that the interactions occur.
• Shows the interaction between the objects in a visual manner that allows the
logic to be validated by stakeholders with relative ease.
• Use cases can be refined into one or more sequence diagrams in order to
provide added detail and a more in-depth understanding of a business process.
.2 Limitations
• Time and effort can be wasted creating a complete set of sequence diagrams
for each use case of a system, which may not be necessary.
• Have historically been used for modelling system flows and may be considered
too technical in other circumstances.
Object 2
Object 3
X
Destruction
Execution
Specification
Lifeline
Call
Response
Asynchronous
Message
Object 1
Synchronous
Message



Stakeholder List, Map, or Personas
Techniques
344
10.43
Stakeholder List, Map, or Personas
10.43.1
Purpose
Stakeholder lists, maps, and personas assist the business analyst in analyzing
stakeholders and their characteristics. This analysis is important in ensuring that
the business analyst identifies all possible sources of requirements and that the
stakeholder is fully understood so decisions made regarding stakeholder
engagement, collaboration, and communication are the best choices for the
stakeholder and for the success of the initiative.
10.43.2
Description
Stakeholder analysis involves identifying the stakeholders that may be affected by
a proposed initiative or that share a common business need. Stakeholder analysis
notes, considers, and analyzes the various characteristics of the identified
stakeholders.
Common types of stakeholder characteristics that are worth identifying and
analyzing include:
• level of authority within the domain of change and within the organization,
• attitudes toward or interest in the change being undertaken,
• attitudes toward the business analysis work and role, and
• level of decision-making authority.
For details on the work involved in conducting a thorough stakeholder analysis,
see Plan Stakeholder Engagement (p. 31).
When analyzing stakeholders, business analysts utilize one or more techniques to
draw out a list of stakeholders and analyze them. Stakeholder lists, maps, and
personas are three tools that can be utilized when conducting this work.
10.43.3
Elements
.1 Stakeholder Lists
A business analyst may apply a number of techniques to generate a stakeholder
list. Brainstorming and interviews are two common techniques that can be used.
The goal is to ensure a thorough list is produced because this list is central to both
stakeholder analysis activities and the planning work the business analyst
performs for elicitation, collaboration, and communication.
Stakeholder lists may become quite lengthy. As the analysis is conducted, the
business analyst categorizes and adds structure to the list. It is important to have
an exhaustive list to ensure that no important stakeholder or stakeholder group
has been overlooked, which opens up the risk that requirements will be missed
later on.



Techniques
Stakeholder List, Map, or Personas
345
.2 Stakeholder Map
Stakeholder maps are diagrams that depict the relationship of stakeholders to the
solution and to one another.
There are many forms of stakeholder maps, but two common ones include:
• Stakeholder Matrix: maps the level of stakeholder influence against the
level of stakeholder interest.
• Onion Diagram: indicates how involved the stakeholders are with the
solution, which stakeholders will directly interact with the solution or
participate in a business process, which are part of the larger organization,
and which are outside the organization.
The business analyst typically starts their stakeholder analysis by reviewing the
proposed scope of the solution and then analyzing which groups will be
impacted. At the start of this analysis, the business analyst may produce a
stakeholder matrix to identify each stakeholder and their role as it pertains to the
development of the requirements. Throughout a project, a stakeholder’s position
on the matrix can change due to organizational, environmental, or requirement
scope changes. Due to these potential changes, stakeholder analysis is considered
iterative and reviewed frequently by the business analyst.
Figure 10.43.1: Stakeholder Matrix
• High Influence/High Impact: the stakeholders are key players in the
change effort. The business analyst should focus their efforts and engage
this group regularly.
• High Influence/Low Impact: the stakeholders have needs that should be
met. The business analyst should engage and consult with them, while also
attempting to engage them and increase their level of interest with the
change activity.
• Low Influence/High Impact: the stakeholders are supporters of and
potential goodwill ambassadors for the change effort. The business analyst
should engage this group for their input and show interest in their needs.
Work closely with
stakeholder to ensure that
they are in agreement with
and support the change.
Keep informed; stakeholder
is likely to be very concerned
and may feel anxious about
lack of control.
Monitor to ensure
stakeholders interest or
influence do not change.
Ensure stakeholder
remains satisfied.
Impact on
Stakeholder
High
Low
Influence of
Stakeholder
Low
High



Stakeholder List, Map, or Personas
Techniques
346
• Low Influence/Low Impact: the stakeholders can be kept informed using
general communications. Additional engagement may move them into the
goodwill ambassador quadrant, which can help the effort gain additional
support.
Figure 10.43.2: Stakeholder Onion Diagram
.3 Responsibility (RACI) Matrix
Another popular stakeholder matrix is the responsibility (RACI) matrix. RACI
stands for the four types of responsibility that a stakeholder may hold on the
initiative: Responsible, Accountable, Consulted, and Informed. When completing
a RACI matrix, it is important to ensure that all stakeholders or stakeholder groups
have been identified. Further analysis is then conducted to assign the RACI
designation in order to specify the level of responsibility expected from each
stakeholder and/or group. It is common practice to define each term so that a
consistent understanding of the assignment and associated roles are understood
by any stakeholders utilizing the RACI matrix.
• Responsible (R): the persons who will be performing the work on the task.
• Accountable (A): the person who is ultimately held accountable for
successful completion of the task and is the decision maker. Only one
stakeholder receives this assignment.
• Consulted (C): the stakeholder or stakeholder group who will be asked to
provide an opinion or information about the task. This assignment is often
provided to the subject matter experts (SMEs).
• Informed (I): a stakeholder or stakeholder group that is kept up to date on
the task and notified of its outcome. Informed is different from Consulted
as with Informed the communication is one-direction (business analyst to
stakeholder) and with Consulted the communication is two-way.
Customers, suppliers,
regulators, and others.
Sponsors, executives,
domain SMEs, and
others who interact with
the affected group.
End users, help desk,
and others whose work
changes when the
solution is delivered.
Project team and others
directly involved with
creating the solution.
Affected External Stakeholders
Organization or Enterprise
Affected Organizational Unit
Solution Delivery



Techniques
Stakeholder List, Map, or Personas
347
Figure 10.43.3: RACI Matrix
.4 Personas
A persona is defined as a fictional character or archetype that exemplifies the way
a typical user interacts with a product. Personas are helpful when there is a desire
to understand the needs held by a group or class of users. Although the user
groups are fictional, they are built to represent actual users. Research is
conducted to understand the user group, and the personas are then created
based upon knowledge rather than opinion. A number of elicitation techniques
can be utilized to conduct this research. Interviews and surveys/questionnaires are
two techniques commonly used to elicit this information. The persona is written
in narrative form and focuses on providing insight into the goals of the group.
This allows the reader to see the story from the point of view of the stakeholder
group. Personas help bring the user to life, which in turn makes the needs feel
real to those who design and build solutions.
10.43.4
Usage Considerations
.1 Strengths
• Identifies the specific people who must be engaged in requirements elicitation
activities.
• Helps the business analyst plan collaboration, communication, and facilitation
activities to engage all stakeholder groups.
• Useful to understand changes in impacted groups over time.
Other Stakeholders
Subject Matter Expert (SME)
Solution Owner
Information Architect
Business Architect
Infrastructure Analyst
Database Analyst (DBA)
Data Modeller
Tester
Developer
Business Analyst
Executive Sponsor
Project Manager
Application Architect
Trainer
A
R
C
C
I
I
C
C
C
C
R
C
C
C
R
C
I
(varies)
Change Request Process
RACI



State Modelling
Techniques
348
.2 Limitations
• Business analysts who are continuously working with the same teams may not
utilize the stakeholder analysis and management technique because they
perceive change as minimal within their respective groups.
• Assessing information about a specific stakeholder representative, such as
influence and interest, can be complicated and may feel politically risky.
10.44
State Modelling
10.44.1
Purpose
State modelling is used to describe and analyze the different possible states of an
entity within a system, how that entity changes from one state to another, and
what can happen to the entity when it is in each state.
10.44.2
Description
An entity is an object or concept within a system. An entity may be used in several
processes. The life cycle of every entity has a beginning and an end.
In a state model (also sometimes called a state transition model), a state is a
formal representation of a status. It is used when it is necessary to have a precise
and consistent understanding of an entity that has complex behaviour and
complex rules about that behaviour.
A state model describes:
• a set of possible states for an entity,
• the sequence of states that the entity can be in,
• how an entity changes from one state to another,
• the events and conditions that cause the entity to change states, and
• the actions that can or must be performed by the entity in each state as it
moves through its life cycle.
While a process model can show all of the entities that are used in or affected by
that process, a state model shows a complementary view: what happens to one
entity across all the processes that affect it or use it.
10.44.3
Elements
.1 State
An entity has a finite number of states during its life cycle, although it can be in
more than one state at a time. Each state is described with a name and the
activities that could be performed while in that state. There may be rules about
which activities must or can be performed and which events it can respond to or
trigger.



Techniques
State Modelling
349
A complex state can be decomposed into sub-states.
.2 State Transition
How the entity changes or transitions from one state to another could be
determined by the steps of a process, by business rules, or by information
content. The sequence of states of an entity are not always linear; an entity could
skip over several states or revert to a previous state, perhaps more than once.
A transition may be conditional (triggered by a specific event or a condition being
reached) or automatic (triggered by the completion of the required activities while
in the previous state or by the passage of time). It may also be recursive, leaving
one state and returning back to the same state. A transition is described in terms
of the event that causes the transition, conditions which determine whether or
not the entity must respond to that event, and actions that occur in association
with the event.
.3 State Diagram
A state diagram shows the life cycle of one entity, beginning when the entity first
comes into existence and moving through all of the different states that the entity
may have until it is discarded and no longer of use.
A state on a state diagram is shown as a rectangle with rounded corners. There
may be any number of states. A state may be decomposed into sub-states.
The transition from one state to another state is shown with a one-directional
arrow pointing from the start state to the destination state, optionally labelled
with the name of the event that causes the entity’s state to change from one state
to another, and optionally with conditions and actions.
The beginning and end of the entity’s life cycle are shown with special symbols for
both the initial state, which indicates that the entity has come into existence, and
the final state, which indicates that the entity is discarded and the life cycle is
complete.
Figure 10.44.1: State Transition Diagram
Transition
Final State
Initial State
State 1
State 2
State 3



Survey or Questionnaire
Techniques
350
.4 State Tables
A state table is a two-dimensional matrix showing states and the transitions
between them. It can be used during elicitation and analysis either as an
alternative, a precursor, or a complement to a state diagram. It is a simple way to
get started on a state model in order to elicit the state names and event names
from the domain subject matter experts.
Each row shows a starting state, the transition, and the end state. If one state
could respond to several transitions, there will be a separate row for each
transition.
A state that appears as an end state in one row could be a start state in another
row.
10.44.4
Usage Considerations
.1 Strengths
• Identifies business rules and information attributes that apply to the entity
being modelled.
• Identifies and describes the activities that apply to the entity at different states
of the entity.
• Is a more effective documentation and communication tool than plain text,
especially if the entity being described has more than a few states, transitions,
and conditions governing those transitions.
.2 Limitations
• Is usually only used to understand and communicate about information entities
that are perceived to be complex; simple entities may be understood without
the time and effort required to build a state model.
• Building a state model appears simple at the start, but achieving a consensus
among domain SMEs about the details required by the model can be difficult
and time-consuming.
• A high degree of precision about states and transitions is required to build a
state diagram; some domain SMEs and business analysis practitioners are
uncomfortable trying to describe such a level of detail.
10.45
Survey or Questionnaire
10.45.1
Purpose
A survey or questionnaire is used to elicit business analysis information—including
information about customers, products, work practices, and attitudes—from a
group of people in a structured way and in a relatively short period of time.



Techniques
Survey or Questionnaire
351
10.45.2
Description
A survey or questionnaire presents a set of questions to stakeholders and subject
matter experts (SMEs), whose responses are then collected and analyzed in order
to formulate knowledge about the subject matter of interest. The questions can
be submitted in written form or can be administered in person, over the
telephone, or using technology that can record responses.
There are two types of questions used in a survey or questionnaire:
• Close-ended: the respondent is asked to select from a list of predefined
responses, such as a Yes/No response, a multiple-choice selection, a rank/
order decision, or a statement requiring a level of agreement. This is useful
when the anticipated range of user responses is fairly well defined and
understood. The responses to close-ended questions are easier to analyze
than those gained from open-ended questions because they can be tied to
numerical coefficients.
• Open-ended: the respondent is asked to answer questions in a free form
without having to select an answer from a list of predefined responses.
Open-ended questions are useful when the issues are known and the range
of user responses is not. Open-ended questions may result in more detail
and a wider range of responses than closed-ended questions. The
responses to open-ended questions are more difficult and time-consuming
to categorize, quantify, and summarize as they are unstructured and often
include subjective language with incomplete or superfluous content.
Questions should be asked in a way that does not influence the response data.
They should be expressed in neutral language and should not be structured or
sequenced to condition the respondent to provide perceived desirable answers.
10.45.3
Elements
.1 Prepare
An effective survey or questionnaire requires detailed planning in order to ensure
that the needed information is obtained in an efficient manner.
When preparing for a survey or questionnaire, business analysts do the following:
• Define the objective: a clear and specific objective establishes a defined
purpose of the survey or questionnaire. Questions are formulated with the
intent of meeting the objective.
• Define the target survey group: identifying the group to be surveyed in
terms of population size and any perceived variations (for example, culture,
language, or location) helps identify factors that can impact survey design.
• Choose the appropriate survey or questionnaire type: the objective of
the survey or questionnaire determines the appropriate combination of
close-ended questions and open-ended questions to elicit the information
required.



Survey or Questionnaire
Techniques
352
• Select the sample group: consider both the survey or questionnaire type
and the number of people in the identified user group in order to determine
if it is necessary and feasible to survey the entire group. It may be important
to survey all members—even of a large group—if their demographics
indicate a wide variance due to geographic distribution, regulatory
differences, or lack of standardization in job function or business process. If
the population is large and the survey type is open-ended, it may be
necessary to identify a subset of users to engage in the questionnaire
process. Using a statistical sampling method will help ensure that the
sample selected is representative of the population so that the survey results
can be reliably generalized.
• Select the distribution and collection methods: determine the
appropriate communication mode for each sample group.
• Set the target level and timeline for response: determine what
response rate is acceptable and when it should be closed or considered
complete. If the actual response rate is lower than the acceptable threshold,
the use of the survey results may be limited.
• Determine if the survey or questionnaire should be supported with
individual interviews: as a survey or questionnaire does not provide the
depth of data that can be obtained from individual interviews, consider
either pre- or post-survey or questionnaire interviews.
• Write the survey questions: ensure that all the questions support the
stated objectives.
• Test the survey or questionnaire: a usability test on the survey identifies
errors and opportunities for improvement.
.2 Distribute the Survey or Questionnaire
When distributing the survey or questionnaire it is important to communicate the
survey's objectives, how its results will be used, as well as any arrangements for
confidentiality or anonymity that have been made.
When deciding on a method of distribution (for example, in-person, e-mail, or
survey tool), business analysts consider:
• the urgency of obtaining the results,
• the level of security required, and
• the geographic distribution of the respondents.
.3 Document the Results
When documenting the results of the survey or questionnaire, business analysts:
• collate the responses,
• summarize the results,
• evaluate the details and identify any emerging themes,



Techniques
SWOT Analysis
353
• formulate categories for encoding the data, and
• break down the data into measurable increments.
10.45.4
Usage Considerations
.1 Strengths
• Quick and relatively inexpensive to administer.
• Easier to collect information from a larger audience than other techniques such
as interviews.
• Does not typically require significant time from the respondents.
• Effective and efficient when stakeholders are geographically dispersed.
• When using closed-ended questions, surveys can be effective for obtaining
quantitative data for use in statistical analysis.
• When using open-ended questions, survey results may yield insights and
opinions not easily obtained through other elicitation techniques.
.2 Limitations
• To achieve unbiased results, specialized skills in statistical sampling methods are
needed when surveying a subset of potential respondents.
• The response rates may be too low for statistical significance.
• Use of open-ended questions requires more analysis.
• Ambiguous questions may be left unanswered or answered incorrectly.
• May require follow-up questions or more survey iterations depending on the
answers provided.
10.46
SWOT Analysis
10.46.1
Purpose
SWOT analysis is a simple yet effective tool used to evaluate an organization's
strengths, weaknesses, opportunities, and threats to both internal and external
conditions.
10.46.2
Description
SWOT analysis is used to identify the overall state of an organization both
internally and externally.
The language used in a SWOT analysis is brief, specific, realistic, and supported by
evidence. SWOT analysis serves as an evaluation of an organization against
identified success factors. SWOT can be performed at any scale from the



SWOT Analysis
Techniques
354
enterprise as a whole to a division, a business unit, a project, or even an
individual. By performing SWOT in a disciplined way, stakeholders can have a
clearer understanding of the impact of an existing set of conditions on a future
set of conditions.
A SWOT analysis can be used to:
• evaluate an organization's current environment,
• share information learned with stakeholders,
• identify the best possible options to meet an organization’s needs,
• identify potential barriers to success and create action plans to overcome
barriers,
• adjust and redefine plans throughout a project as new needs arise,
• identify areas of strength that will assist an organization in implementing
new strategies,
• develop criteria for evaluating project success based on a given set of
requirements,
• identify areas of weakness that could undermine project goals, and
• develop strategies to address outstanding threats.
10.46.3
Elements
SWOT is an acronym for Strengths, Weaknesses, Opportunities, and Threats:
• Strengths (S): anything that the assessed group does well. May include
experienced personnel, effective processes, IT systems, customer
relationships, or any other internal factor that leads to success.
• Weaknesses (W): actions or functions that the assessed group does poorly
or not at all.
• Opportunities (O): external factors of which the assessed group may be
able to take advantage. May include new markets, new technology,
changes in the competitive marketplace, or other forces.
• Threats (T): external factors that can negatively affect the assessed group.
They may include factors such as the entrance into the market of a new
competitor, economic downturns, or other forces.
Beginning a SWOT analysis with opportunities and threats sets the context to
identify strengths and weaknesses.



Techniques
SWOT Analysis
355
Figure 10.46.1: SWOT Matrix
10.46.4
Usage Considerations
.1 Strengths
• Is a valuable tool to aid in understanding the organization, product, process, or
stakeholders.
• Enables business analysts to direct the stakeholders’ focus to the factors that
are important to the business.
.2 Limitations
• The results of a SWOT analysis provide a high-level view; more detailed analysis
is often needed.
• Unless a clear context is defined for the SWOT analysis the result may be
unfocused and contain factors which are not relevant to the current situation.
Threats
Opportunities
SO Strategies
ST Strategies
WO Strategies
WT Strategies
How can the group's
strength be used to exploit
potential opportunities?
SO strategies are fairly
straightforward to
implement.
How can the group use its
strengths to ward off
potential threats? Can the
threats be turned into
opportunities?
Can the group use an
opportunity to eliminate or
mitigate a weakness?
Does the opportunity
warrant the development
of new capabilities?
Can the group restructure
itself to avoid the threat?
Should the group consider
getting out of this market?
WT strategies involve
worst-case scenarios.
Opportunity
Opportunity
Opportunity
Threat
Threat
Threat
Strengths
Strength
Strength
Strength
Weaknesses
Weakness
Weakness
Weakness



Use Cases and Scenarios
Techniques
356
10.47
Use Cases and Scenarios
10.47.1
Purpose
Use cases and scenarios describe how a person or system interacts with the
solution being modelled to achieve a goal.
10.47.2
Description
Use cases describe the interactions between the primary actor, the solution, and
any secondary actors needed to achieve the primary actor's goal. Use cases are
usually triggered by the primary actor, but in some methods may also be triggered
by another system or by an external event or timer.
A use case describes the possible outcomes of an attempt to accomplish a
particular goal that the solution will support. It details different paths that can be
followed by defining primary and alternative flows. The primary or basic flow
represents the most direct way to accomplish the goal of the use case. Special
circumstances and exceptions that result in a failure to complete the goal of the
use case are documented in alternative or exception flows. Use cases are written
from the point of view of the actor and avoid describing the internal workings of
the solution.
Use case diagrams are a graphical representation of the relationships between
actors and one or more use cases supported by the solution.
Some use case approaches distinguish between business use cases and system
use cases, with business use cases describing how actors interact with a particular
process or business function, and system use cases describing the interaction
between an actor and a software application.
A scenario describes just one way that an actor can accomplish a particular goal.
Scenarios are written as a series of steps performed by actors or by the solution
that enable an actor to achieve a goal. A use case describes several scenarios.
10.47.3
Elements
There is no fixed, universal format for use cases. The following elements are
frequently captured in a use case description.
.1 Use Case Diagram
A use case diagram visually depicts the scope of the solution, by showing the
actors who interact with the solution, which use cases they interact with, and any
relationships between the use cases. Unified Modelling Language™ (UML®)
describes the standard notation for a use case diagram.



Techniques
Use Cases and Scenarios
357
Relationships
Relationships between actors and use cases are called associations. An association
line indicates that an actor has access to the functionality represented by the use
case. Associations do not represent input, output, time, or dependency.
There are two commonly used relationships between use cases:
• Extend: allows for the insertion of additional behavior into a use case. The
use case that is being extended must be completely functional in its own
right and must not depend on the extending use case for its successful
execution. This relationship may be used to show that an alternate flow has
been added to an existing use case (representing new requirements).
• Include: allows for the use case to make use of functionality present in
another use case. The included use case does not need to be a complete
use case in its own right if it is not directly triggered by an actor. This
relationship is most often used either when some shared functionality is
required by several use cases or to abstract out a complex piece of logic.
Figure 10.47.1: Use Case Diagram
.2 Use Case Description
Name
The use case has a unique name. The name generally includes a verb that
describes the action taken by the actor and a noun that describes either what is
being done or the target of the action.
Goal
The goal is a brief description of a successful outcome of the use case from the
perspective of the primary actor. This acts as a summary of the use case.
Actor 1
Actor 2
Use Case 2
Extension points:
Call Use Case 3
Use Case 4
Use Case 3
Use Case 1
System
<<include>>
<<extend>>



Use Cases and Scenarios
Techniques
358
Actors
An actor is any person or system external to the solution that interacts with that
solution. Each actor is given a unique name that represents the role they play in
interactions with the solution. Some use case authoring approaches recommend
against the use of systems or events as actors.
A use case is started by an actor, referred to as the primary actor for that use case.
Other actors who participate in the use case in a supporting role are called
secondary actors.
Preconditions
A precondition is any fact that must be true before the use case can begin. The
precondition is not tested in the use case but acts as a constraint on its execution.
Trigger
A trigger is an event that initiates the flow of events for a use case. The most
common trigger is an action taken by the primary actor.
A temporal event (for example, time) can initiate a use case. This is commonly
used to trigger a use case that must be executed based on the time of day or a
specific calendar date, such as an end-of-day routine or an end-of-month
reconciliation of a system.
Flow of Events
The flow of events is the set of steps performed by the actor and the solution
during the execution of the use case. Most use case descriptions separate out a
basic, primary, or main success flow that represents the shortest or simplest
successful path that accomplishes the goal of the actor.
Use cases may also include alternative and exception flows. Alternative flows
describe other paths that may be followed to allow the actor to successfully
achieve the goal of the use case. Exception flows describe the desired response by
the solution when the goal is unachievable and the use case cannot be
successfully completed.
Post-conditions or Guarantees
A post-condition is any fact that must be true when the use case is complete. The
post-conditions must be true for all possible flows through the use case, including
both the primary and alternative flows. The use case may describe separate post-
conditions that are true for successful and unsuccessful executions of the use
case. These can be called guarantees; the success guarantee describes the post-
conditions for success. Minimal guarantees describe the conditions that are
required to be true, even if the actor’s goal is not achieved, and may address
concerns such as security requirements or data integrity.



Techniques
User Stories
359
10.47.4
Usage Considerations
.1 Strengths
• Use case diagrams can clarify scope and provide a high-level understanding of
requirements.
• Use case descriptions are easily understood by stakeholders due to their
narrative flow.
• The inclusion of a desired goal or outcome ensures that the business value of
the use case is articulated.
• Use case descriptions articulate the functional behaviour of a system.
.2 Limitations
• The flexibility of the use case description format may lead to information being
embedded that would be better captured using other techniques such as user
interface interactions, non-functional requirements, and business rules.
• Decisions and the business rules that define them should not be recorded
directly in use cases, but managed separately and linked from the appropriate
step.
• The flexible format of use cases may result in capturing inappropriate or
unnecessary detail in the attempt to show every step or interaction.
• Use cases intentionally do not relate to the design of the solution and as a
result, significant effort may be required in development to map use case steps
to software architecture.
10.48
User Stories
10.48.1
Purpose
A user story represents a small, concise statement of functionality or quality
needed to deliver value to a specific stakeholder.
10.48.2
Description
User stories capture the needs of a specific stakeholder and enable teams to
define features of value to a stakeholder using short, simple documentation. They
can serve as a basis for identifying needs and allow for the prioritizing, estimating,
and planning of solutions. A user story is typically a sentence or two that
describes who has the need addressed by the story, the goal the user is trying to
accomplish, and any additional information that may be critical to understanding
the scope of the story. With a focus on stakeholder value, user stories invite



User Stories
Techniques
360
exploration of the requirements by promoting additional conversations with
stakeholders and grouping functional requirements for delivery.
User stories can be used:
• to capture stakeholder needs and prioritize development of solutions,
• as a basis of estimating and planning solution delivery,
• as a basis for generating user acceptance tests,
• as a metric for measuring the delivery of value,
• as a unit for tracing related requirements,
• as a basis for additional analysis, and
• as a unit of project management and reporting.
10.48.3
Elements
.1 Title (optional)
The title of the story describes an activity the stakeholder wants to carry out with
the system. Typically, it is an active-verb goal phrase similar to the way use cases
are titled.
.2 Statement of Value
There is no mandatory structure for user stories.
The most popular format includes three components:
• Who: a user role or persona.
• What: a necessary action, behaviour, feature, or quality.
• Why: the benefit or value received by the user when the story is
implemented.
For example, "As a <who>, I need to <what>, so that <why>."
"Given...When...Then" is another common format.
.3 Conversation
User stories help teams to explore and understand the feature described in the
story and the value it will deliver to the stakeholder. The story itself doesn't
capture everything there is to know about the stakeholder need and the
information in the story is supplemented by further modelling as the story is
delivered.
.4 Acceptance Criteria
A user story may be supported through the development of detailed acceptance
criteria (see Acceptance and Evaluation Criteria (p. 217)). Acceptance criteria
define the boundaries of a user story and help the team to understand what the



Techniques
Vendor Assessment
361
solution needs to provide in order to deliver value for the stakeholders.
Acceptance criteria may be supplemented with other analysis models as needed.
10.48.4
Usage Considerations
.1 Strengths
• Easily understandable by stakeholders.
• Can be developed through a variety of elicitation techniques.
• Focuses on value to stakeholders.
• A shared understanding of the business domain is enhanced through
collaboration on defining and exploring user stories.
• Tied to small, implementable, and testable slices of functionality, which
facilitates rapid delivery and frequent customer feedback.
.2 Limitations
In general, user stories are intended as a tool for short-term capture and
prioritization of requirements and not for long-term knowledge retention or to
provide a detailed analysis. Neglecting this principle can lead to the following
issues:
• This conversational approach can challenge the team since they do not have all
the answers and detailed specifications upfront.
• Requires context and visibility; the team can lose sight of the big picture if
stories are not traced back through validation or supplemented with higher-
level analysis and visual artifacts.
• May not provide enough documentation to meet the need for governance, a
baseline for future work, or stakeholder expectations. Additional
documentation may be required.
10.49
Vendor Assessment
10.49.1
Purpose
A vendor assessment assesses the ability of a vendor to meet commitments
regarding the delivery and the consistent provision of a product or service.
10.49.2
Description
When solutions are in part provided by external vendors (who may be involved in
design, construction, implementation, or maintenance of the solution or solution
components), or when the solution is outsourced, there may be specific
requirements in regard to the involvement of a third party. There may be a need
to ensure that the supplier is financially secure, capable of maintaining specific



Vendor Assessment
Techniques
362
staffing levels, compliant with standards, and able to commit appropriate skilled
staff to support the solution. Non-functional requirements can be used to define
the service levels expected of a third party, due diligence may be conducted, or
certification from an independent authority may be requested.
A vendor assessment is conducted to ensure that the vendor is reliable and that
the product and service meet the organization's expectations and requirements.
The assessment may be formal through the submission of a Request for
Information (RFI), Request for Quote (RFQ), Request for Tender (RFT), or Request
for Proposal (RFP). It may also be very informal through word of mouth and
recommendations. The standards of the organization, the complexity of the
initiative, and the criticality of the solution may influence the level of formality in
which vendors are assessed.
10.49.3
Elements
.1 Knowledge and Expertise
A common reason for using third-party vendors is that they can provide
knowledge and expertise not available within the organization. It may be
desirable to target vendors with expertise in particular methodologies or
technologies with the goal of having that expertise transferred to people within
the enterprise.
.2 Licensing and Pricing Models
The licensing or pricing model is taken into account in cases where a solution or
solution component is purchased from or outsourced to a third party vendor. In
many cases, solutions that offer similar functionality may differ greatly in their
licensing models, which then requires analysis of different usage scenarios to
determine which option will provide the best cost-benefit ratio under the
scenarios likely to be encountered in the enterprise.
.3 Vendor Market Position
It is important to be able to compare each vendor with the competitors and
decide with which market players the organization wants to get involved. The
comparison of the organization’s profile with each vendor’s customer community
may also be a factor in the assessment. The dynamics of the vendors’ market
position are also very important, especially if the organization intends to establish
a long-term partnership with that vendor.
.4 Terms and Conditions
Terms and conditions refer to the continuity and integrity of the provided
products and services. The organization investigates whether the vendor's
licensing terms, intellectual property rights and technology infrastructure are
likely to turn into challenges if the organization later chooses to transition to
another supplier. There may also be considerations regarding the vendor's use of,
and responsibility for protecting, the organization's confidential data. The terms
under which customizations of the product will be executed, as well as the



Techniques
Workshops
363
availability of a regular update schedule and roadmap of features that are
planned for delivery, are considered.
.5 Vendor Experience, Reputation, and Stability
Vendors' experience with other customers may provide valuable information on
how likely it is that they will be able to meet their contractual and non-
contractual obligations. Vendors can also be evaluated for conformance and
compliance with external relevant standards for quality, security, and
professionalism. It may be necessary to request that steps be taken to ensure
there are no risks if a vendor encounters financial difficulties, and that it will be
possible to maintain and enhance the solution even if the vendor's situation
changes radically.
10.49.4
Usage Considerations
.1 Strengths
• Increases the chances of the organization to develop a productive and fair
relationship with a suitable and reliable vendor, and to improve long-term
satisfaction with the decision.
.2 Limitations
• May be consuming in regards to time and resources.
• Does not prevent risk of failure as the partnership evolves.
• Subjectivity may bias the evaluation outcome.
10.50
Workshops
10.50.1
Purpose
Workshops bring stakeholders together in order to collaborate on achieving a
predefined goal.
10.50.2
Description
A workshop is a focused event attended by key stakeholders and subject matter
experts (SMEs) for a concentrated period of time. A workshop may be held for
different purposes including planning, analysis, design, scoping, requirements
elicitation, modelling, or any combination of these. A workshop may be used to
generate ideas for new features or products, to reach consensus on a topic, or to
review requirements or designs.
Workshops generally include:
• a representative group of stakeholders,
• a defined goal,



Workshops
Techniques
364
• interactive and collaborative work,
• a defined work product, and
• a facilitator.
Workshops can promote trust, mutual understanding, and strong communication
among the stakeholders and produce deliverables that structure and guide future
work efforts.
The workshop is ideally facilitated by an experienced, neutral facilitator; however,
a team member may also serve as the facilitator. A scribe documents the decisions
reached and any outstanding issues. A business analyst may be the facilitator or
the scribe in these workshops. In situations where the business analyst is a subject
matter expert on the topic, they may serve as a workshop participant. This must
be approached with caution as it can confuse others as to the role of the business
analyst.
10.50.3
Elements
.1 Prepare for the Workshop
When preparing for a workshop, business analysts:
• define the purpose and desired outcomes,
• identify key stakeholders to participate,
• identify the facilitator and scribe,
• create the agenda,
• determine how the outputs will be captured,
• schedule the session and invite the participants,
• arrange room logistics and equipment,
• send the agenda and other materials in advance to prepare the attendees
and increase productivity at the meeting, and
• if appropriate, conduct pre-workshop interviews with participants.
.2 Workshop Roles
There are several roles involved in a successful workshop:
• Sponsor: frequently not a participant in the workshop, but does have
ultimate accountability for its outcome.
• Facilitator: establishes a professional and objective tone for the workshop,
introduces the goals and agenda for the workshop, enforces structure and
ground rules, keeps activities focused on the purpose and desired
outcomes, facilitates decision making and conflict resolution, and ensures
that all participants have an opportunity to be heard.



Techniques
Workshops
365
• Scribe: documents the decisions in the format determined prior to the
workshop and keeps track of any items or issues that are deferred during
the session.
• Timekeeper: may be used to keep track of the time spent on each agenda
item.
• Participants: includes key stakeholders and subject matter experts. They
are responsible for providing their input and views, listening to other views,
and discussing the issues without bias.
.3 Conduct the Workshop
To ensure that all participants have a common understanding, facilitators
generally begin the workshop with a statement of its purpose and desired
outcomes. Some workshops may also start with an easy or fun task to break the
ice and get the participants comfortable working together.
Establishing agreed-upon ground rules can be an effective method for
establishing a productive environment for collaboration. Ground rules can
include:
• respect the opinions of others,
• everyone is expected to contribute,
• discussion that is off-topic should be limited to a specific set time,
• discuss the issues, not the people, and
• an agreement on how decisions are made.
Throughout the workshop, the facilitator maintains focus by frequently validating
the session’s activities with the workshop’s purpose and outcomes.
.4 Post Workshop Wrap-up
After the workshop, the facilitator follows up on any open action items that were
recorded at the workshop, completes the documentation, and distributes it to the
workshop attendees and any stakeholders who need to be kept informed of the
work done.
10.50.4
Usage Considerations
.1 Strengths
• Can be a means to achieve agreement in a relatively short period of time.
• Provides a means for stakeholders to collaborate, make decisions, and gain a
mutual understanding.
• Costs are often lower than the cost of performing multiple interviews.
• Feedback on the issues or decisions can be provided immediately by the
participants.



Workshops
Techniques
366
.2 Limitations
• Stakeholder availability may make it difficult to schedule the workshop.
• The success of the workshop is highly dependent on the expertise of the
facilitator and knowledge of the participants.
• Workshops that involve too many participants can slow down the workshop
process. Conversely, collecting input from too few participants can lead to the
overlooking of needs or issues that are important to some stakeholders, or to
the arrival at decisions that don't represent the needs of the majority of the
stakeholders.



367
11
Perspectives
Perspectives are used within business analysis work to provide focus to tasks and
techniques specific to the context of the initiative. Most initiatives are likely to
engage one or more perspectives. The perspectives included in the BABOK®
Guide are:
• Agile,
• Business Intelligence,
• Information Technology,
• Business Architecture, and
• Business Process Management.
These perspectives do not presume to represent all the possible perspectives from
which business analysis is practiced. The perspectives discussed in the BABOK®
Guide represent some of the most common views of business analysis at the time
of writing.
Any given initiative includes one, many, or all of these perspectives. For example,
an initiative may have a technology component (Information Technology
Perspective), the technology component may mean business process changes
(Business Process Management Perspective), the initiative may decide to do part,
or all of the work with an agile approach (Agile Perspective). Another initiative
may merge two organizations and need to look at the business capabilities and
how the transformation impacts those capabilities (Business Architecture
Perspective), and the business leaders need updated information for decision
making and analysis (Business Intelligence Perspective). Large or complex
initiatives will likely employ all perspectives.



The Agile Perspective
Perspectives
368
While the business analysis tasks detailed in the BABOK® Guide are intended to
be applicable across all areas of business analysis, they are also pertinent to each
specific business analysis perspective. Perspectives provide ways to approach
business analysis work in a more focused manner suitable to the context. The
perspectives help interpret and understand the knowledge areas and tasks in the
BABOK® Guide from the lens in which one is currently working.
For more
information
regarding this
structure, see
Perspectives
(p. 9).
Each perspective follows a common structure:
• Change Scope,
• Business Analysis Scope,
• Methodologies, Approaches, and Techniques,
• Underlying Competencies, and
• Impact on Knowledge Areas.
11.1
The Agile Perspective
The Agile Perspective highlights the unique characteristics of business analysis
when practiced in the context of agile environments.
Agile is about having a flexible mindset, embodied in a set of values and principles
and exhibited by a variety of complementary practices. Agile initiatives involve
constant change. Business analysts working on agile initiatives continually
reassess, adapt, and adjust their efforts and tactics. Business analysts conduct
analysis and deliver work products at the last responsible moment to continually
allow flexibility for change; detailed analysis work is not done ahead of time, but
just in time to be effectively utilized by the agile team.
Agile business analysis ensures that information is available to the agile team at
the right level of detail at the right time. Business analysts help agile teams
answer these questions:
• What need are we trying to satisfy?
• Is that need worth satisfying?
• Should we deliver something to satisfy that need?
• What is the right thing to do to deliver that need?
Business analysis work is performed continuously throughout an agile initiative
and relies heavily on interpersonal skills such as communication, facilitation,
coaching, and negotiation. Business analysts are active members of an agile team
and often facilitate planning, analyzing, testing, and demonstrating activities. In
an agile team, business analysis may be performed by a product manager/owner,
business analyst, or by other defined team roles. Business analysts help the team
identify modifications in assumptions and other project variations that emerge.
Refer to the Agile Extension to the BABOK® Guide for an expanded treatment of
the role, mindset, and practices of business analysis in agile approaches, as well as
details on the values and principles of the Agile Manifesto
(www.agilemanifesto.org).



Perspectives
The Agile Perspective
369
11.1.1
Change Scope
Business analysts working on agile initiatives engage with the business sponsor
on a strategic level and assist with defining how the proposed product or feature
aligns with the organization's objectives. They collaborate with various
stakeholders and the change team to break the product vision down into a
prioritized list of desired work items to be completed. The prioritized items (or
prioritized backlog list) usually focus on the capabilities needed in the resultant
product, with emphasis on the highest value items first.
Business analysts may act as a stakeholder proxy, or work directly with the
sponsor or product owner.
In agile environments, change and rapid response to change is expected. Agile
teams deliver small, incremental changes and commit to prioritized work items
for only one iteration at a time. This allows the agile team to handle emerging
changes for the upcoming iteration with minimal impact. An iteration is an
agreed period of work time.
Requirements are developed through continual exploration and analysis of the
business needs. It is important to note that though most agile approaches are
iterative, not all iterative approaches are agile. There are also several agile
approaches that are not iterative, such as the kanban method.
During agile initiatives, scope is constantly evolving. This is managed by the
backlog list which is continually reviewed and re-prioritized. This process
contributes to the refinement and redefinition of scope in order to meet the
evolving and emerging business need.
If a major change emerges that significantly impacts the overall value and goals
for the project, the project can be adjourned and reassessed.
.1 Breadth of Change
Agile approaches are used to address a variety of needs in an enterprise. The most
common use of agile practices is in software development projects. However,
many organizations have started to apply agile principles to non-software related
change such as process engineering and business improvement. Initiatives using
agile approaches can be undertaken within a single department or can span
across multiple teams, departments, and divisions of an organization.
For organizations new to the agile mindset and practices, a focus on continuous
improvement, ongoing changing behaviour, and making progress enables the
organization to move towards culturally adopting the agile mindset. Adopting the
agile mindset refers to the cultural adoption of agile principles as opposed to the
organization considering agile as a methodology or practice to be implemented.
.2 Depth of Change
Initiatives using an agile approach are frequently part of a larger program of
work, which can include organizational transformation and change, business
process re-engineering, or business process change. The agile work stream is
frequently, but not always, centered on software development. The other



The Agile Perspective
Perspectives
370
elements of the program can be developed using agile or another methodology
that is appropriate for the need. Agile principles and practices are often
successfully applied in initiatives where:
• there is a clear commitment from the customer and engagement by
empowered subject matter experts (SMEs),
• the business need or proposed solution is complex or complicated, and
• business needs are changing or unknown and are still emerging.
Agile approaches can be used for initiatives that are developing a solution for the
first time, or for maintaining and enhancing an existing solution. For example, if
the change is mission critical then processes can be added to address regulatory
requirements and to deal with the mission critical aspects of the project.
.3 Value and Solutions Delivered
The value and solutions delivered in an agile initiative are similar to any other
initiative. The difference with an agile approach is the emphasis on delivering
value early in a highly collaborative manner, using adaptive planning that has a
focus on continuous improvement.
An agile initiative provides value by virtue of the approach taken by an agile team
through ongoing review and feedback of the work performed. Stakeholders get
the opportunity to frequently review the product, which allows them to identify
any missed requirements early. The solution evolves over time with an expectation
of rapid and flexible response to change. Clarity and visibility of all
communications is of the utmost importance to ensure the agile team’s efforts
align with the organization’s needs and expectations.
In a new team, the business analyst often plays a central role in building rapport
and trust amongst the agile team members and external stakeholders to help
enable ongoing collaborative discussions and engagement. This interaction
enables the agile team to accurately deliver value that meets evolving stakeholder
needs.
.4 Delivery Approach
Agile approaches focus on people interactions, transparent communications, and
ongoing delivery of valuable change to stakeholders.
Each agile approach has its own unique set of characteristics that allows teams to
select an approach that best suits the initiative at hand. Some agile teams have
found that a hybrid or combination of approaches is necessary to work within the
constraints of their environment.
Refer to the Agile Extension to the BABOK® Guide for a description of different
agile delivery approaches.
.5 Major Assumptions
The assumptions in place in agile environments frequently include:
• Changing requirements are welcome, even late in development.



Perspectives
The Agile Perspective
371
• The business problem can be reduced to a set of needs that can be met
using some combination of technology and business process change.
• Agile initiatives have fully engaged customers and empowered SMEs with
complete buy-in to the agile approach.
• Ideally, team membership is constant and members are not continually
being moved to other teams.
• There is a preference for multidisciplinary and co-located teams
encouraging more efficient and effective face-to-face conversation.
However, agile approaches can work well with distributed teams provided
appropriate support and communication channels are in place.
• Team members may perform more than one role within the team if it is
required, and provided that the team has the appropriate skills (for
example, cross-functional teams).
• Team members have a mindset for continuous improvement and successful
value delivery through regular inspection.
• Agile teams are empowered and self-organizing.
11.1.2
Business Analysis Scope
.1 Change Sponsor
It is important that a sponsor of an agile initiative be familiar with the agile
philosophy, mindset, and approaches, and also be open to the constant feedback
that will require trade-offs from the stakeholders.
An agile sponsor understands and accepts the:
• use of adaptive planning over predictive planning,
• use and value of a fixed period of time for a work cycle, and
• need and value of the sponsor’s involvement.
The sponsor’s (or empowered SME's) active involvement with the agile team is
critical to providing the sponsor with the ability to preview and understand the
product being developed, as well as allowing an opportunity for the sponsor to
provide continuous feedback to the team and adjust the product as needs
change.
.2 Change Targets and Agents
Agile approaches are most successful when the organizational culture and
working environments lend themselves to intensive collaboration, frequent
communication, and a strong disposition towards incremental delivery of
appropriate solution value.
Agile teams are frequently either small or around teams of small teams. The
simpler and flatter structure doesn’t change the fact that the deliverables may
affect a large group of stakeholders. The change agent, also considered a



The Agile Perspective
Perspectives
372
stakeholder, is not different because the project uses agile. The primary agents for
a change using an agile approach can include:
• Agile team leader: the facilitator of the work of the team. An agile team
leader frequently shares the same soft skill set of a project manager, but
completely delegates the tasks of planning, scheduling, and prioritization to
the team. Rather than traditional command-and-control management,
servant leadership is preferred in all the agile approaches. Depending on the
approach, this role may be called scrum master, iteration manager, team
leader, or coach.
• Customer representative or product owner: the active team member
responsible for ensuring that the change being developed addresses the
requirements for which it has been mandated. In Scrum this role is called
the product owner. The dynamic systems development method (DSDM)
refers to this role as that of a visionary, and extreme programming (XP)
refers to it as a customer representative.
• Team members: the specialists or domain experts that include both
technical and customer representation. Depending on size and particular
context of the initiative, individuals within a team have different specialties.
Usability experts, technical architects, and database administrators are just a
sample of such specialized roles that provide support to the team as
needed.
• External stakeholders: all of the remaining stakeholders who may not be
considered team members, but are an interested party in the outcome of
the project or simply required for its completion, playing what can be
considered a supporting role in the team.
.3 Business Analyst Position
An agile team may have one or more team members with business analysis skills
who may or may not have the job title of business analyst. This recognition of
cross-skilled team members expands the practice of business analysis beyond that
of a single specialist role.
On agile teams, business analysis activities can be performed by one or a
combination of:
• a business analyst working on the team,
• the customer representative or product owner, or
• distributing these activities throughout the team.
Refer to the Agile Extension to the BABOK® Guide for more details.
.4 Business Analysis Outcomes
In an agile environment, business analysis brings people together and ensures
that the right stakeholders are involved with the agile team at the right time.
Open communication and collaboration is one of the principal outcomes of
successful business analysis in an agile project.



Perspectives
The Agile Perspective
373
Business analysts ensure that the project's vision and direction are in strategic
alignment to the organizational goals and business need. The business analyst
holds shared responsibility in defining strategic criteria for project completion and
during the project assists with defining acceptance criteria. They also facilitate the
articulation of the product vision statement. The product vision statement is a
common initial deliverable.
Documentation rigour and style is highly dependent on the purpose and the
context in which it is produced. Agile approaches favour just enough and just-in-
time documentation rather than establishing predefined models for
documentation to be delivered. This documentation approach allows for the
documents to incorporate as much of the change introduced as possible while
keeping the cost of change low. Mandatory documentation, such as that required
for auditing or compliance reporting, are still produced as part of each delivery
cycle. It is important that documents address an identified need and deliver more
value than the cost incurred to produce and maintain them.
11.1.3
Approaches and Techniques
.1 Approaches
Agile is an umbrella term for a variety of approaches. All agile approaches practice
business analysis but only a few explicitly define the business analysis role. The
primary characteristic of any agile approach is its alignment to the values and
principles of the Agile Manifesto. An agile team may implement or evolve to use
a combination of approaches which enables them to deliver value more
effectively given their project type and work environment.
Table 11.1.1: Agile Approaches
Approach
Brief description
Crystal Clear
Part of a family of Crystal methodologies which are defined
based on hardness and colour. The hardness refers to the
business criticality or potential for causing harm, which
amounts to more rigour and predictive planning being
required as the criticality increases. Colour refers to the
heaviness of the project across a number of dimensions
including number of people required and risk elements in
the project.
Disciplined Agile
Delivery (DAD)
A decision process framework which incorporates ideas
from a variety of other agile approaches. It is intended to
support a project from initiation through delivery. DAD is
not prescriptive and allows for teams to customize their
own life cycles and approaches.



The Agile Perspective
Perspectives
374
Dynamic Systems
Development
Method (DSDM)
A project delivery framework which focuses on fixing cost,
quality, and time at the beginning while contingency is
managed by varying the features to be delivered. MoSCoW
prioritization technique is used for scope management.
Time boxes, or short focused periods of time with clearly
defined outcomes, are used to manage the work.
Evolutionary
Project
Management
(Evo)
A project management method for developing and
delivering a system incrementally. It has a strong focus on
quantifying value for multiple stakeholders and planning
increments based on delivery of that value (which can be
measured). It uses impact estimation tables as a formal
technique for assessing solutions for their ability to deliver
value to multiple stakeholders for a given cost.
Extreme
Programming (XP)
Named for the concept of taking beneficial software
engineering techniques to the extreme. This concept
focuses on the technical development processes and
features pair-programming, test-driven development, and
other craftsmanship approaches to the technical practices.
XP technical practices are often used in conjunction with
one of the agile management frameworks.
Feature Driven
Development
(FDD)
Focuses on a client valued functionality perspective to
develop working software. For example, following a high-
level scoping exercise, a feature list is identified and all
planning, design, and development are performed based
on feature sets.
Kanban
Does not require fixed iterations. Work moves through the
development process as a continuous flow of activity. A key
feature is to limit the amount of work underway at any one
time (referred to as the work in progress limit or WIP). The
team works only on a fixed number of items at any one
time and work may begin on a new item only when it is
required to maintain flow downstream and after the
previous item has been completed.
Scaled Agile
Framework®
(SAFe™)
A framework for implementing agile practices at enterprise
scale. It highlights the individual roles, teams, activities and
artifacts necessary to scale agile from the team to program
to the enterprise level.
Scrum
A lightweight process management framework based on
empirical process control. Work is performed in a series of
fixed length iterations, called Sprints, which last one month
or less. At the end of each sprint the team must produce
working software of a high enough quality that it could
potentially be shipped or otherwise delivered to a
customer.
Table 11.1.1: Agile Approaches (Continued)
Approach
Brief description



Perspectives
The Agile Perspective
375
.2 Techniques
The following table lists techniques commonly used within agile approaches.
Refer to the Agile Extension to the BABOK® Guide for a more detailed description
of these techniques.
Table 11.1.2: Techniques used within Agile Approaches
Technique
Brief Description
Behaviour Driven
Development
(BDD)
An approach that enhances the communication between
stakeholders and team members by expressing product
needs as concrete examples.
Kano Analysis
A technique for understanding which product features will
help drive customer satisfaction.
Lightweight
Documentation
A principle that governs all documentation produced on
an agile project. The purpose is to ensure that all
documentation is intended to fulfill an impending need,
has clear value for stakeholders, and does not create
unnecessary overhead. For example, a system overview
document may be written towards the end of a project
based on stable content and acceptance tests written as
part of the product testing.
MoSCoW
Prioritization
A method to prioritize stories (or other elements) in
incremental and iterative approaches. MoSCoW (must
have, should have, could have, won’t have) provides a way
to reach a common understanding on relative importance
of delivering a story or other piece of value in the product.
Personas
Fictional characters or archetypes that exemplify the way
that typical users interact with a product.
Planning
Workshop
A collaborative workshop that is used to allow an agile
team to determine what value can be delivered over a time
period such as a release.
Purpose
Alignment Model
A model that is used to assess ideas in the context of
customer and value.
Real Options
An approach to help people know when to make decisions
rather than how.
Relative
Estimation
Team estimation techniques using either story points,
which represent the relative complexity of a user story to
develop, or ideal days, which represent the amount of
total effort a story would take to develop.
Retrospectives
A similar term for the Lesson Learned technique.
Retrospectives focus on continuous improvement of the
teamwork process and are held after every iteration on
agile projects.



The Agile Perspective
Perspectives
376
11.1.4
Underlying Competencies
Agile is a mindset. Agile business analysts embody the values and principles of the
Agile Manifesto which are based on a humanistic view of product development
as a process founded in communication and collaboration. Refer to the Agile
Extension to the BABOK® Guide for a description of the principles for business
analysts. In adopting the agile mindset and philosophy, the business analyst
develops competencies in:
• Communication and collaboration: the ability to communicate the
sponsor’s vision and needs; assist in influencing others to support the vision;
participate and possibly facilitate negotiation of priorities; and facilitate
collaborative agreement on solution outcomes.
• Patience and tolerance: the ability to maintain self-control under pressure
and keep an open mind when interacting with others.
• Flexibility and adaptability: cross-functional skill sets that allow the
business analyst to step outside their specialization in order to support
other team members.
• Ability to handle change: the ability to quickly assess the impact of
change and determine what provides business value amongst frequently
changing requirements, and assisting with, or maintaining, the re-
prioritization of the to-do work list.
• Ability to recognize business value: the ability to understand how
changes and new features can achieve business value and support the
vision.
• Continuous improvement: periodically review with the agile team how to
become more effective.
Story
Decomposition
Ensures that the requirements for a product are
represented at the appropriate level of detail and are
derived from a valuable business objective.
Story Mapping
Provides a visual and physical view of the sequence of
activities to be supported by a solution.
Storyboarding
Detail visually and textually the sequence of activities that
represent user interactions with a system or business.
Value Stream
Mapping
Provides a complete, fact-based, time-series representation
of the stream of activities required to deliver a product or
service to the customer.
Table 11.1.2: Techniques used within Agile Approaches (Continued)
Technique
Brief Description



Perspectives
The Agile Perspective
377
11.1.5
Impact on Knowledge Areas
This section explains how specific business analysis practices within agile are
mapped to business analysis tasks and practices as defined by the BABOK®
Guide. It also describes how each knowledge area is applied or modified with the
agile discipline.
Each knowledge area lists techniques relevant to an agile perspective. BABOK®
Guide techniques are found in the Techniques chapter of the BABOK® Guide.
Agile Extension techniques are discussed in detail in the Agile Extension to the
BABOK® Guide. This is not intended to be an exhaustive list of techniques but
rather to highlight the types of techniques used by business analysts while
performing the tasks within the knowledge area.
.1 Business Analysis Planning and Monitoring
In agile approaches, detailed business analysis planning can be deferred until
work on an activity is ready to begin rather than done upfront as in predictive
projects.
An initial plan for business analysis activities is developed at the beginning of the
project. The plan then gets updated prior to the start of each cycle to account for
change and to ensure that the plan is always up to date. Stakeholder involvement
and engagement is key to the success of agile projects. Business analysts
proactively plan to involve, engage, and collaborate with stakeholders.
Communication is commonly much less formal and business analysis deliverables
are often interactions and collaboration with less emphasis on the written
documents.
BABOK® Guide Techniques
• Backlog Management (p. 220)
• Collaborative Games (p. 243)
• Estimation (p. 271)
• Metrics and Key Performance
Indicators (KPIs) (p. 297)
• Mind Mapping (p. 299)
• Prioritization (p. 311)
• Scope Modelling (p. 338)
• Stakeholder List, Map, or Personas
(p. 344)
• User Stories (p. 359)
• Workshops (p. 363)
Agile Extension Techniques
• Lightweight Documentation
• MoSCoW Prioritization
• Personas
• Relative Estimation
• Retrospective
.2 Elicitation and Collaboration
Progressive elicitation and elaboration occur throughout an agile initiative. The
most common pattern is an initial elicitation activity that establishes the high-level
vision and scope of the solution, and an initial milestone-based plan for the
delivery of the product. In every cycle there is more detailed elicitation for the



The Agile Perspective
Perspectives
378
backlog items that will be developed in that cycle. The intent of elicitation
activities is to generate just enough detail to ensure that the work at hand is
performed correctly while aiming towards the goals. Agile approaches aim to
minimize the time between the elaboration of needs and their implementation in
the solution. There is a strong focus on collaborative elicitation approaches such
as workshops with stakeholders.
BABOK® Guide Techniques
• Acceptance and Evaluation Criteria
(p. 217)
• Backlog Management (p. 220)
• Brainstorming (p. 227)
• Collaborative Games (p. 243)
• Concept Modelling (p. 245)
• Interface Analysis (p. 287)
• Mind Mapping (p. 299)
• Non-Functional Requirements
Analysis (p. 302)
• Process Modelling (p. 318)
• Prototyping (p. 323)
• Reviews (p. 326)
• Scope Modelling (p. 338)
• Stakeholder List, Map, or Personas
(p. 344)
• Use Cases and Scenarios (p. 356)
• User Stories (p. 359)
• Workshops (p. 363)
Agile Extension Techniques
• Behaviour Driven Development
• Lightweight Documentation
• Personas
• Storyboarding
• Story Mapping
.3 Requirements Life Cycle Management
As agile initiatives unfold, the scope is defined with increasing specificity. The
expectation is that the needs will change and that the design will evolve over the
course of the project. Prioritization of features based on value and development
priority drives the work done in each cycle. Validation of the evolving solution
with the stakeholders occurs at the end of every iteration in place of a formal
requirements approval process.
BABOK® Guide Techniques
• Acceptance and Evaluation Criteria
(p. 217)
• Backlog Management (p. 220)
• Collaborative Games (p. 243)
• Prioritization (p. 311)
• Reviews (p. 326)
• Workshops (p. 363)
Agile Extension Techniques
• Kano Analysis
• MoSCoW Prioritization
• Story Decomposition
• Story Mapping



Perspectives
The Agile Perspective
379
.4 Strategy Analysis
Agile approaches are often used when there is uncertainty about the needs, the
solution, or the scope of change. Strategy analysis is a constant part of an agile
initiative to ensure that the solution delivered continues to provide value to
stakeholders. Agile team members use strategy analysis to help understand and
define product vision, and develop and adjust the development roadmap, in
addition to conducting ongoing assessments of related risks. For every iteration,
the proposed solution is reassessed against the current business context to ensure
that it will effectively meet the business goals. The adaptive nature of agile
projects means that adapting the project to changes in the organization's goals is
not disruptive; rather, it is an expected part of the process.
BABOK® Guide Techniques
• Backlog Management (p. 220)
• Brainstorming (p. 227)
• Business Capability Analysis (p. 230)
• Collaborative Games (p. 243)
• Concept Modelling (p. 245)
• Metrics and Key Performance
Indicators (KPIs) (p. 297)
• Scope Modelling (p. 338)
• Workshops (p. 363)
Agile Extension Techniques
• Kano Analysis
• Personas
• Purpose Alignment Model
• Real Options
• Value Stream Analysis
.5 Requirements Analysis and Design Definition
Needs are progressively elaborated during an agile project. Analysis and design
are performed on a just-in-time basis, either just before or during the iteration in
which the solution component will be developed.
Analysis performed just before the iteration is to provide the team with enough
information to estimate the planned work. Analysis performed during the
iteration is to provide the team with enough information to construct or deliver
the planned work.
Models and other analysis and design techniques are typically used informally,
and may not be maintained once they have served their purposes. The analysis
and design approach used should support progressive elaboration, be adaptable
to change based on learning, and not cause the team to select solutions
prematurely. Agile teams tend to use user stories at the lowest level of
decomposition, usually supported by acceptance criteria which capture the
analysis and design details regarding how the stories should behave when
implemented. Validation of the evolving solution is performed with stakeholders
at the end of every iteration.
BABOK® Guide Techniques
• Acceptance and Evaluation Criteria
(p. 217)
• Business Capability Analysis (p. 230)
• Business Rules Analysis (p. 240)



The Agile Perspective
Perspectives
380
• Collaborative Games (p. 243)
• Concept Modelling (p. 245)
• Interface Analysis (p. 287)
• Non-Functional Requirements
Analysis (p. 302)
• Prioritization (p. 311)
• Process Analysis (p. 314)
• Process Modelling (p. 318)
• Scope Modelling (p. 338)
• Use Cases and Scenarios (p. 356)
• User Stories (p. 359)
• Workshops (p. 363)
Agile Extension Techniques
• Behaviour Driven Development
• Kano Analysis
• Lightweight Documentation
• MoSCoW Prioritization
• Purpose Alignment Model
• Real Options
• Story Decomposition
• Story Elaboration
• Story Mapping
• Storyboarding
• Value Stream Analysis
.6 Solution Evaluation
Throughout an agile project, the stakeholders and agile team continually assess
and evaluate the development solution as it is incrementally built and refined.
Evaluation of the evolving solution with the stakeholders occurs at the end of
every development cycle to ensure the deliverable meets their needs and satisfies
their expectations. The business analyst ensures that the product meets
expectations before a product is released, and identifies new opportunities that
will add value to the business.
BABOK® Guide Techniques
• Acceptance and Evaluation Criteria
(p. 217)
• Business Capability Analysis (p. 230)
• Metrics and Key Performance
Indicators (KPIs) (p. 297)
• Non-Functional Requirements
Analysis (p. 302)
• Process Analysis (p. 314)
• Prototyping (p. 323)
• Reviews (p. 326)
• Stakeholder List, Map, or Personas
(p. 344)
• Use Cases and Scenarios (p. 356)
• User Stories (p. 359)
• Workshops (p. 363)
Agile Extension Techniques
• Personas
• Value Stream Analysis



Perspectives
The Business Intelligence Perspective
381
11.2
The Business Intelligence Perspective
The Business Intelligence Perspective highlights the unique characteristics of
business analysis when practiced in the context of transforming, integrating, and
enhancing data.
The focus of business intelligence is the transformation of data into value-added
information: where to source it, how to integrate it, and how to enhance and
deliver it as analytic insight to support business decision making.
Business intelligence initiatives apply data-centric system architectures as well as
technologies and tools to deliver reliable, consistent, high-quality information
that enables stakeholders to better manage strategic, tactical, and operational
performance.
11.2.1
Change Scope
.1 Breadth of Change
A key objective of a business intelligence system is the consistent definition and
usage of information throughout an organization by establishing a 'single point
of truth' for diverse business data. A solution architecture that can integrate
multiple data sources from within (and potentially from outside) the organization
provides the foundation of a business intelligence solution.
Figure 11.2.1: Business Intelligence Solution - Conceptual Framework
Data
Sources
Data
Integration
Enterprise
Data View
Decision
Support
Decision
Points
Data
Transformation
Data Quality
Management
Data
Analytics
Information
Delivery
Data
Warehouse
Cyclical Reports
Ad-hoc Queries
Interactive
Dashboards
Conditional Alerts
Automated
Decision Data
EXTERNAL
SYSTEMS
Partner
Industry
Public
INTERNAL
SYSTEMS
Corporate
Business Area
Ad-hoc, isolated
Unstructured
Data
Analytical
Sandboxes
Operational
Data Stores
Data Marts
Machine data
Web data
Audio Visual
data
Documents &
text
OTHER
SOURCES



The Business Intelligence Perspective
Perspectives
382
The business intelligence promotes an enterprise-wide view of information
management. To support that conceptual framework, a business intelligence
initiative may also involve the development of infrastructure services in the
organization, such as data governance and metadata management.
.2 Depth of Change
Business intelligence initiatives focus on the information needed to support
decision making at, or across, different levels within the organization:
• executive level: supports strategic decisions,
• management level: supports tactical decisions, or
• process level: supports operational decisions.
Where information needs are initially expressed or identified at a particular level,
the business analyst investigates the business implications at other levels to assess
the overall impact of the change on the organization.
At each level, the business needs may involve any or all of the following:
• communication requirements for the development of new reporting or the
replacement of existing reporting,
• information requirements for the addition or extension of analytic
functionality, and/or
• data integration requirements for the construction or modification of the
enterprise data view with regard to data sources, definitions,
transformation rules and quality issues.
.3 Value and Solutions Delivered
The value of a business intelligence initiative is in its ability to provide timely,
accurate, high value, and actionable information to those people and systems
who can use it effectively in making business decisions.
Better informed decision making at all levels can lead to improved business
performance in:
• strategic processes such as market analysis, customer engagement, and
product development,
• tactical processes such as stock control and financial planning, and
• operational processes such as credit assessment, fault detection, and
accounts payable monitoring.
These improvements in an organization’s current and future performance may be
realized as increased revenues and reduced costs.
.4 Delivery Approach
A business intelligence solution presents a range of delivery options to meet the
emerging information needs of stakeholders and the priorities of the
organization.



Perspectives
The Business Intelligence Perspective
383
The extensibility and scalability of the solution architecture provide for the
support of business decision making to be progressively introduced or enhanced:
• at different levels in the organization, from strategic (senior executive),
through tactical (management), to operational (staff and systems), and
• in target functional areas in the organization, from a specific area through
to an enterprise-wide implementation.
The infrastructure services that provide data management, analytics, and
presentation capabilities, facilitate a phased or incremental development strategy
in respect of:
• the inclusion, coordination and control of different data sources, and
• the analysis and development of business information and insights.
Infrastructure components of a business intelligence solution are often provided
by a commercial off-the-shelf package configured to the specific business
environment and needs.
.5 Major Assumptions
The following is a list of major assumptions of a business intelligence initiative:
• existing business processes and transactional systems can provide source
data that is definable and predictable,
• the cross-functional data infrastructure that is needed to support a business
intelligence solution has not been precluded by the organization on
technical, financial, political/cultural, or other grounds, and
• the organization recognizes that process re-engineering and change
management might be needed in order to effectively realize the value from
a business intelligence solution.
11.2.2
Business Analysis Scope
.1 Change Sponsor
The change sponsor of a business intelligence initiative is ideally the highest level
role from the organizational unit affected by the change. This provides for a
consistent, cohesive approach to the shared usage of data assets within the cross-
functional architecture of a business intelligence solution.
.2 Change Targets
The targets of a business intelligence initiative are the business decisions made by
people or processes at multiple levels in the organization that can be improved by
better reporting, monitoring, or predictive modelling of performance-related data.
.3 Business Analyst Position
As in other initiatives, the business analyst acts as the primary liaison between
business intelligence stakeholders and solution providers in the elicitation,



The Business Intelligence Perspective
Perspectives
384
analysis, and specification of business needs.
In addition to that role, the business analyst may also participate in technical
activities that are specific to business intelligence, including:
• enterprise data modelling,
• decision modelling,
• specialized presentation design (for example, dashboards), and
• ad hoc query design.
A business analyst working on a business intelligence initiative serves in one or in
a combination of the following roles:
• business analyst who is competent in the definition of business
requirements and the assessment of potential solutions,
• business intelligence functional analyst who has an understanding of data
mining and predictive analytic techniques, as well as skills in developing
visualizations,
• data analyst who is experienced at defining source systems data to be used
for the required analytical purposes, or
• data modeller/architect who is skilled in defining the source and target data
structures in logical data models.
.4 Business Analysis Outcomes
In the business intelligence discipline, business analysis is focused on the major
components of the solution architecture:
• the specification of business decisions to be influenced or changed,
• the collection of data from source systems,
• the integration of divergent sources into a convergent enterprise
framework, and
• the provision of targeted information and analytic insight to business
stakeholders.
The business analyst is responsible for the analysis and specification of the
business requirements for all of these components and collaborates with
technical specialists to assess solution artifacts.
The major outcomes of business analysis are:
• Business process coverage: defines the scope of the change with a high-
level overview of the business decisions within the enterprise that are to be
supported by the solution. It identifies how the information output will be
used and what value it will provide.
• Decision models: identify the information requirements of each business
decision to be supported and specify the business rules logic of how the
individual information components contribute to the decision outcome.
• Source logical data model and data dictionary: the source logical data
model provides a standard definition of the required data as held in each



Perspectives
The Business Intelligence Perspective
385
source system. The source data dictionary provides a definition of each
element and the business rules applied to it: business description, type,
format and length, legal values, and any inter-dependencies.
• Source data quality assessment: evaluates the completeness, validity,
and reliability of the data from source systems. It identifies where further
verification and enhancement of source data is required to ensure
consistent business definitions and rules apply across the enterprise-wide
data asset.
• Target logical data model and data dictionary: the target logical data
model presents an integrated, normalized view of the data structures
required to support the business domain. The target data dictionary
provides the standardized enterprise-wide definition of data elements and
integrity rules.
• Transformation rules: map source and target data elements to specify
requirements for the decoding/encoding of values and for data correction
(error values) and enrichment (missing values) in the transformation
process.
• Business analytics requirements: define the information and
communication requirements for decision support outputs. These include:
• predefined reports,
• dashboards,
• balanced scorecards,
• ad hoc reports,
• online analytical processing (OLAP) queries,
• data mining,
• prescriptive analytics,
• conditional alerts,
• complex event processing, and
• predictive modelling.
• Specifications for each output can include: (1) data selections/dimensions,
level of granularity, filtering criterion applied, possibilities for drill down,
slice and dice, and user access and permissions; and (2) presentation rules
to define data element format, translation (labels, look-ups), calculations,
and data aggregations.
• Solution architecture: provides a high-level design view of how the
decision support requirements of each functional area will map to the
business intelligence framework. It is typically presented in the form of a
process (or data flow) model that defines:
• where the source data is held,
• how (pull/push) and when (frequency, latency) the data will be
extracted,



The Business Intelligence Perspective
Perspectives
386
• where the transformations will take place (cleansing, encoding,
enhancement),
• where the data will be physically stored (data warehouse, data marts),
and
• how the data will flow to presentation outputs (reporting facilities,
query tools).
11.2.3
Methodologies and Approaches
.1 Methodologies
There are no formalized business intelligence methodologies that impact the
responsibilities and activities of the business analyst. However, a business
intelligence initiative can operate within or alongside methodologies applicable to
other disciplines or perspectives which themselves might impact the business
analysis role.
.2 Approaches
Within the business intelligence framework there are a number of less formal and
potentially overlapping approaches that map to particular business and technical
contexts.
Types of Analytics
There are three types of data analytics that represent incremental solutions, with
increasing levels of systems complexity, cost, and value:
• Descriptive analytics: uses historical data to understand and analyze past
business performance. Business information can be categorized and
consolidated to best suit the stakeholder’s view including executive
management dashboards, middle level management key performance
indicator (KPI) scorecards, and operational level management charts. No
assumptions are made as to which situations are of interest to the
stakeholders, what decisions need to be made, or what actions might be
carried out. The business analysis focus is on the information and
communication requirements for standard reporting and dashboards, ad
hoc reporting, and query functionality.
• Predictive analytics: applies statistical analysis methods to historical data
to identify patterns, and then uses that understanding of relationships and
trends to make predictions about future events. The particular situations
that are of interest to the stakeholders are specified, and their business
rules are defined. The business analysis focus is on the information
requirements for pattern recognition through data mining, predictive
modelling, forecasting, and condition-driven alerts.
• Prescriptive analytics: expands on predictive analytics to identify decisions
to be made and to initiate appropriate action to improve business
performance. Statistical optimization and simulation techniques can be



Perspectives
The Business Intelligence Perspective
387
used to determine the best solution or outcome among various choices. For
situations of interest to stakeholders, full specification of the associated
decisions and potential actions are required. The business analysis focus is
on the business objectives, constraints criteria, and the business rules that
underpin the decision-making process.
Supply and Demand Driven
The objectives and priorities of a business intelligence initiative can be based on
the technical goals of improving existing information delivery systems (supply-
driven) or on the business goals of providing the appropriate information to
improve decision-making processes (demand-driven):
• Supply-driven: assumes the view of "for a given cost, what value can we
deliver?". This approach maps existing systems data to define what data is
available. A common implementation strategy would be to:

## phase the inclusion of existing databases into the business intelligence


solution architecture,

## explore new insights that might be gained from the consolidated


data.
• Demand-driven: assumes the view of "for a given value, what cost do we
incur?". This approach starts with identifying the information output
needed to support business decisions, and then tracing that information
back to the underlying data sources to determine feasibility and cost. It
provides for incremental implementation strategies that are not determined
by existing database structures, and allows for early exploratory usage of
business intelligence beyond existing reporting requirements.
Structured and Unstructured Data
There are two types of data that business intelligence approaches consider:
• Structured data: traditional data warehouse solutions have been based on
consolidating the structured data (numerical and categorical) recorded in
operational systems where business information sets are identified by
predefined structures (referred to as 'schema on write') and where a rules-
driven template ensures data integrity. The business analysis focus is on data
models, data dictionaries, and business rules to define information
requirements and capabilities.
• Unstructured data: business intelligence solutions can include semi-
structured or unstructured data which includes text, images, audio, and
video. This data frequently comes from external sources. For this type of
data, the structure and relationships are not predefined and no specific
organization rules have been applied to ensure data integrity. Information
sets are derived from the raw data (referred to as 'schema on read'). The
business analysis focus is on metadata definitions and data matching
algorithms to define information requirements and capabilities.



The Business Intelligence Perspective
Perspectives
388
11.2.4
Underlying Competencies
As in any business analysis discipline, the business analyst requires the
fundamental communication and analytical competencies to be effective in
liaising with both business stakeholders and technical solution providers.
In the business intelligence discipline, this coordination of business information
requirements with business intelligence systems outcomes can be further
enhanced by the business analyst’s specific competencies in:
• business data and functional usage, including terminology and rules,
• the analysis of complex data structures and their translation into
standardized format,
• business processes affected including KPIs and metrics,
• decision modelling,
• data analysis techniques including basic statistics, data profiling,and
pivoting,
• data warehouse and business intelligence concepts and architecture,
• logical and physical data models,
• ETL (Extract, Transform, Load) best practices including historical data track
and reference data management, and
• business intelligence reporting tools.
11.2.5
Impact on Knowledge Areas
This section explains how specific business analysis practices within business
intelligence are mapped to business analysis tasks and practices as defined by the
BABOK® Guide. This section describes how each knowledge area is applied or
modified with the business intelligence discipline.
Each knowledge area lists techniques relevant to a business intelligence
perspective. Techniques used in the discipline of business intelligence do not
deviate, to any great extent, from the BABOK® Guide techniques. BABOK® Guide
techniques are found in the Techniques chapter of the BABOK® Guide. This is not
intended to be an exhaustive list of techniques but rather to highlight the types of
techniques used by business analysts while performing the tasks within the
knowledge area.
.1 Business Analysis Planning and Monitoring
A business intelligence initiative may require establishing an underlying data
infrastructure to support the solution, or it might be an enhancement based on
the infrastructure of an existing solution. Scope Modelling is frequently used to
differentiate between these alternatives and plan the relevant business analysis
activities accordingly.
The business intelligence paradigm of information delivery might be a new,



Perspectives
The Business Intelligence Perspective
389
unfamiliar approach for business stakeholders and for the business analysts
themselves. In planning the initiative, the business analyst considers:
• how experienced the stakeholders are in expressing their information and
communication requirements in the business intelligence context, and
• how skilled the business analysts are in interpreting those requirements into
detailed specifications for business intelligence technical specialists.
Business intelligence solutions typically provide frameworks, tools, and
techniques that can assist in requirements definition and solution modelling. The
level of stakeholders’ and business analysts’ expertise in these can have an impact
on the planned approach.
When assessing stakeholder attitudes towards the business intelligence initiative,
the business analyst should be aware that an enterprise-wide business
intelligence solution might not provide direct value to some operational
stakeholders, but will deliver it elsewhere in the organization, and the flexibility
and extensibility provided by the business intelligence infrastructure delivers
longer-term strategic value that goes beyond short-term operational benefits.
A business intelligence solution that integrates multiple data sources typically
engages many stakeholders with overlapping information requirements. Business
analysts prepare for the analysis and synthesis of individual requirements into a
set that is complete and cohesive without conflicts and redundancies.
BABOK® Guide Techniques
• Acceptance and Evaluation Criteria
(p. 217)
• Balanced Scorecard (p. 223)
• Brainstorming (p. 227)
• Decision Analysis (p. 261)
• Estimation (p. 271)
• Functional Decomposition (p. 283)
• Interviews (p. 290)
• Item Tracking (p. 294)
• Metrics and Key Performance
Indicators (KPIs) (p. 297)
• Non-Functional Requirements
Analysis (p. 302)
• Organizational Modelling (p. 308)
• Prioritization (p. 311)
• Process Modelling (p. 318)
• Reviews (p. 326)
• Risk Analysis and Management
(p. 329)
• Roles and Permissions Matrix
(p. 333)
• Root Cause Analysis (p. 335)
• Scope Modelling (p. 338)
• Stakeholder List, Map, or Personas
(p. 344)
• Survey or Questionnaire (p. 350)
• Use Cases and Scenarios (p. 356)
• User Stories (p. 359)
• Workshops (p. 363)



The Business Intelligence Perspective
Perspectives
390
.2 Elicitation and Collaboration
The cross-functional nature of business intelligence typically requires business
analysts to employ specialized documentation tools and techniques to elicit
particular types of requirements from stakeholders, both business and technical.
Individual stakeholders may only possess partial knowledge and expertise
regarding:
• the business decisions that need support,
• the data elements that support those business decisions,
• the data sourcing, transformation, and integration rules, and
• the presentation of the required information.
Interviews with individual stakeholders identify the information and analytic
insight required to support their decision making. Workshops with stakeholders
from across different functional areas of the business can help detect common,
overlapping information requirements that would be better met with an
integrated solution.
Data models and data dictionaries provide definitions of the structure and
business rules of existing systems data. The business analyst assesses available
documentation to identify incompleteness of a model or inconsistencies between
models.
Process models that are extended to include data artifacts can help identify the
data sources required at decision points. Decision models specify the data analytic
requirements and business rules for decisions.
Commercial off-the-shelf packages of business intelligence functionality can
provide the business analyst with a set of highly effective prototyping tools to
elicit and clarify stakeholder information and communication requirements.
BABOK® Guide Techniques
• Brainstorming (p. 227)
• Document Analysis (p. 269)
• Focus Groups (p. 279)
• Functional Decomposition (p. 283)
• Glossary (p. 286)
• Interface Analysis (p. 287)
• Interviews (p. 290)
• Item Tracking (p. 294)
• Observation (p. 305)
• Prototyping (p. 323)
• Workshops (p. 363)
• Stakeholder List, Map, or Personas
(p. 344)
• Survey or Questionnaire (p. 350)
.3 Requirements Life Cycle Management
The architectural nature of the business intelligence discipline requires
establishing the infrastructure capabilities in the solution. This can introduce
structural dependencies within the solution, particularly where delivery is phased,



Perspectives
The Business Intelligence Perspective
391
that affect the prioritization of individual business needs. It is often possible to
achieve efficiencies by implementing related requirements at the same time.
BABOK® Guide Techniques
• Item Tracking (p. 294)
• Organizational Modelling (p. 308)
• Prioritization (p. 311)
• Reviews (p. 326)
• Roles and Permissions Matrix
(p. 333)
• Stakeholder List, Map, or Personas
(p. 344)
• Workshops (p. 363)
.4 Strategy Analysis
Business analysts can use high-level conceptual data models to map the current
state of corporate information, to identify information silos, and to assess their
related problems and opportunities. Organization Modelling can be used to
evaluate any current data management infrastructure, such as metadata
management and data governance.
In defining the future state strategy, business analysts can use high-level models
to map the architecture for data storage and for data conveyance and
transformation:
• Logical data models: provide a static view of the solution architecture,
representing the information portal that connects the sourcing of
operational data inputs with the delivery of the business information
outputs.
• Data flow diagrams: are commonly used to map the dynamic aspects of
the solution (data-in-motion) and to identify other architectural constructs
such as latency and accessibility.
• Decision models: are useful for defining how relevant business decisions
are made and where and how data analytics can be effectively used to meet
these needs.
• Physical data models: show the implementation environment including
the data warehouse and data marts.
The extensible architecture provided by business intelligence solutions can
support incremental implementation across different functional areas of the
business. Business analysts can define change strategy options based on business
needs and priorities, impact on the business operations, and the usability of
existing infrastructure components.
BABOK® Guide Techniques
• Backlog Management (p. 220)
• Benchmarking and Market Analysis
(p. 226)
• Brainstorming (p. 227)
• Business Rules Analysis (p. 240)
• Data Flow Diagrams (p. 250)
• Data Modelling (p. 256)
• Decision Analysis (p. 261)



The Business Intelligence Perspective
Perspectives
392
• Decision Modelling (p. 265)
• Document Analysis (p. 269)
• Estimation (p. 271)
• Focus Groups (p. 279)
• Functional Decomposition (p. 283)
• Glossary (p. 286)
• Organizational Modelling (p. 308)
• Risk Analysis and Management
(p. 329)
• Root Cause Analysis (p. 335)
• Stakeholder List, Map, or Personas
(p. 344)
• SWOT Analysis (p. 353)
.5 Requirements Analysis and Design Definition
When modelling and specifying back office data capture and storage
requirements, business analysts use specific data-oriented modelling techniques
such as Data Modelling, Data Dictionary, Decision Modelling, and Business Rules
Analysis.
Models of an existing system's data help to define data availability and identify
redundancies, inconsistencies, and data quality issues. Where existing systems
documentation is non-existent or out of date, reverse-engineered modelling can
be a substantial component of work, and frequently requires collaboration with
technical experts such as database administrators and application programmers.
A future state data model demonstrates how the source information is generically
structured in the proposed solution. The overall transformation process is
commonly modelled using Data Flow Diagrams to illustrate the management of
latency and accessibility requirements in the solution. Business analysts define
specific business rules for data integrity checking and for data transformation.
For modelling and specifying front office information outputs, business analysts:
• analyze existing reports to determine if they are candidates to be replaced
or repaired with business intelligence outputs, and
• use business intelligence capabilities such as ad hoc queries, data mining,
and complex event processing to identify and specify the content and
format of new business intelligence outputs.
Business analysts are involved in assessing the capability of a proposed solution
(typically a commercial off-the-shelf software package) in respect of the specified
requirements. In the business intelligence context, these include functional
requirements such as self-serve facilities, data analytics tools, data presentation
tools, drill down capabilities, and non-functional requirements related to issues
such as data quality, data latency, and query performance.
.6 BABOK® Guide Techniques
• Acceptance and Evaluation Criteria
(p. 217)
• Balanced Scorecard (p. 223)
• Business Rules Analysis (p. 240)
• Data Dictionary (p. 247)
• Data Flow Diagrams (p. 250)
• Data Modelling (p. 256)
• Decision Modelling (p. 265)



Perspectives
The Business Intelligence Perspective
393
• Document Analysis (p. 269)
• Functional Decomposition (p. 283)
• Glossary (p. 286)
• Interface Analysis (p. 287)
• Interviews (p. 290)
• Metrics and Key Performance
Indicators (KPIs) (p. 297)
• Non-Functional Requirements
Analysis (p. 302)
• Observation (p. 305)
• Organizational Modelling (p. 308)
• Prioritization (p. 311)
• Process Modelling (p. 318)
• Prototyping (p. 323)
• Reviews (p. 326)
• Scope Modelling (p. 338)
• Sequence Diagrams (p. 341)
• Stakeholder List, Map, or Personas
(p. 344)
• State Modelling (p. 348)
• Use Cases and Scenarios (p. 356)
• Vendor Assessment (p. 361)
.7 Solution Evaluation
A common enterprise limitation with the introduction of a business intelligence
solution is the under-utilization of the information resource and analytic
functionality that the solution provides. Stakeholders who are not familiar with
the capabilities of business intelligence might focus on simply replacing or
repairing existing information outputs. Business analysts explore and evaluate
opportunities for additional value that are enabled by a business intelligence
solution.
.8 BABOK® Guide Techniques
• Acceptance and Evaluation Criteria
(p. 217)
• Balanced Scorecard (p. 223)
• Business Rules Analysis (p. 240)
• Data Flow Diagrams (p. 250)
• Data Modelling (p. 256)
• Decision Analysis (p. 261)
• Decision Modelling (p. 265)
• Estimation (p. 271)
• Focus Groups (p. 279)
• Functional Decomposition (p. 283)
• Glossary (p. 286)
• Interviews (p. 290)
• Item Tracking (p. 294)
• Metrics and Key Performance
Indicators (KPIs) (p. 297)
• Observation (p. 305)
• Organizational Modelling (p. 308)
• Prioritization (p. 311)
• Process Modelling (p. 318)
• Risk Analysis and Management
(p. 329)
• Stakeholder List, Map, or Personas
(p. 344)
• Survey or Questionnaire (p. 350)
• SWOT Analysis (p. 353)
• Use Cases and Scenarios (p. 356)
• User Stories (p. 359)
• Vendor Assessment (p. 361)



The Information Technology Perspective
Perspectives
394
11.3
The Information Technology Perspective
The Information Technology Perspective highlights the characteristics of business
analysis when undertaken from the point of view of the impact of the change on
information technology systems.
This perspective
focuses on non-
agile approaches
to IT initiatives.
When working in the information technology (IT) discipline, business analysts deal
with a wide range of complexity and scope of activities. Initiatives may be as small
as minor bug fixes and enhancements, or as large as re-engineering the entire
information technology infrastructure for an extended enterprise. Business
analysts are called upon to work with this diverse level of knowledge and skills
among stakeholders to deliver valuable solutions to their IT needs.
For information
regarding agile
approaches within
information
technology
initiatives, see The
Agile Perspective
(p. 368).
Being able to effectively articulate the business' vision and needs to technical
stakeholders is central to the success of a business analyst in the information
technology discipline. Business analysts proactively collaborate with both the
business stakeholders and development teams to ensure that needs are
understood and aligned with organizational strategy. A business analyst
frequently plays the role of the translator who helps business and technology
stakeholders understand each other's needs, constraints, and context. The
concept of solution design is appropriate in a technology context, and from the IT
business analyst’s point of view. However, the term 'design', when discussed
within an IT setting, is generally assumed to mean 'technical design' or the
utilization of technologies to solve business problems. Business analysts within an
IT context define and elaborate solution requirements or participate in solution
design with business stakeholders while maintaining a separation with technical
design.
Important
In IT contexts, the term 'design' has traditionally been reserved for solution or
technical design performed by developers, IT architects, or solution architects. All
work done by IT business analysts is covered by the term 'requirements', including
concepts such as the definition and design of business processes, user interfaces,
reports or other elements of the solution relevant to stakeholders outside of the
implementation team. Business analysts working in this context may prefer the
term 'solution requirements' instead of 'design' in order to maintain a clear
separation of responsibility.
Business analysts working in an information technology environment consider
their tasks in light of three key factors:
• Solution impact: the value and risk of the solution to the business.
• Organizational maturity: the formality and flexibility of the
organizational change processes.
• Change scope: the breadth, depth, complexity, and context for the
proposed change.
11.3.1
Change Scope
Changes to IT systems are initiated for several reasons.
Each of the following triggers can lead to an IT change:



Perspectives
The Information Technology Perspective
395
• Create a new organizational capability: can be executed to transform
the organization. These types of IT initiatives may drive the creation of
larger programs to address non-IT changes, but are centered on a
technology that alters the business environment.
• Achieve an organizational objective by enhancing an existing
capability: is part of a change that meets a defined need. This may include
changes to meet regulatory requirements or to enable business specific
goals. These types of initiatives often modify an existing system but may
also require implementation and integration of new systems.
• Facilitate an operational improvement: is undertaken to improve
organizational efficiency or reduce organizational risk. The change scope,
organizational maturity, and solution impact dictate whether these changes
will be managed as a project, part of a continuous improvement effort, or
as an enhancement.
• Maintain an existing information technology system: is undertaken to
ensure smooth operation of an existing IT system. Depending on the scope
of the change, maintenance may be managed as a project or a regularly
scheduled activity. This may include technology driven changes such as a
vendor discontinuing support of a technology, scheduled releases or
upgrades to a purchased software package, or technical modifications
required to support architecture strategy.
• Repair a broken information technology system: is undertaken when
an IT system that is not performing as expected is changed to correct the
dysfunction. The urgency of the repair is generally based on the level of
disruption caused. In some cases the scope of the repair effort is very large,
so the repair is managed as a project.
.1 Breadth of Change
Information technology initiatives may focus on a single system or on multiple
systems which interact with each other. Some systems are developed and
maintained in-house while others are commercial off-the-shelf (COTS) systems
developed by an organization that is external to the group implementing the
system. It is also possible that an external organization completes custom
development, such as when development tasks are outsourced or contracted.
The scope of an IT initiative is often narrowly focused on software and hardware
and a minimal set of systems, applications, or stakeholders. Larger initiatives may
impact multiple user groups or systems, and often require collaboration with the
extended enterprise. The implementation of COTS information technology
systems may begin with a small or limited scope when the change is initiated, but
after analysis is complete the scope is broader than originally anticipated. The
business analysis approach for a COTS selection and implementation is
approached differently than in-house development. These IT systems almost
always require customization, integration, administration, and training. In some
cases, the initiatives are limited to initial installation and implementation, or
enhancements to an existing application. IT initiatives may also focus on a very
specific technology solution such as what data is needed, how data is gathered,



The Information Technology Perspective
Perspectives
396
how it is stored and accessed in order to support business transaction methods,
or how information is reported and available to the business groups.
Business analysts working in IT carefully consider the context for any information
technology change. They consider whether the change is managed as a project, a
continuous improvement, or a maintenance activity. Business analysts also
consider organizational change management and all impacts including training,
communications, and adoption of the change.
The nature of business analysis activities in an IT environment depend on a variety
of solution impact factors:
• What happens to the business if this system shuts down?
• What happens if the system performance degrades?
• What business capabilities and processes depend on the IT system?
• Who contributes to those capabilities and processes?
• Who uses those capabilities and processes?
When considering these solution impact factors, not only do business analysts
match the formality of analysis activities to the business analysis processes
defined by the organization, but also consider the importance of the IT system.
The importance of the system under analysis may indicate that more analysis is
needed to support and define the requirements for the change.
.2 Depth of Change
Changes in an IT environment frequently require the business analyst to define
explicit details, including technical details such as the definition of individual data
elements being manipulated or impacted by the change. Integration efforts can
require analysis and definition at a great level of detail while identifying and
defining the interfaces between IT systems. Due to the level of detail required in
these types of initiatives, business analysts elicit and analyze how the organization
works as a whole and how the IT system will support those operations. This
provides the necessary context for the business analyst to understand whether
the details being discovered and documented are relevant to delivering value. This
can be particularly challenging when an IT system change is initiated for
technology driven reasons but without sufficient clarity or alignment to business
purpose.
.3 Value and Solutions Delivered
Information technology systems are implemented to increase organizational
value, which includes any support capabilities and processes that use the system.
Business analysts seek to align IT functionality to these processes and capabilities,
and to measure the effect that the system has on them.
Changes to IT systems can increase value many ways, including:
• reducing operating costs,
• decreasing wasted effort,



Perspectives
The Information Technology Perspective
397
• increasing strategic alignment,
• increasing reliability and stability,
• automating error-prone or manual processes,
• repairing problems,
• making it possible to scale up, enhance, or make more readily available a
business capability, and
• implementing new functionality and new capabilities.
.4 Delivery Approach
The delivery of business analysis activities within an IT organization varies greatly.
Initiatives may range from small enhancement efforts which are completed with a
single, short time frame release schedule to multi-release, phased
implementations.
Short time frame initiatives may involve a single business analyst for a short period
of time. Larger efforts frequently involve several business analysts who may
coordinate analysis activities in several ways. Business analysts may divide work
based on business group involved or by specific activity.
.5 Major Assumptions
The following is a list of major assumptions of the IT discipline:
• business capabilities and processes that use an IT system are delivering value
to the organization,
• business analysts working from other perspectives can integrate their work
with the work of the IT business analysts, and
• IT systems changes are usually driven by a business need, although some
initiatives may originate from within technology developments.
11.3.2
Business Analysis Scope
.1 Change Sponsor
Information technology changes may be requested or sponsored by business
sponsors, IT departments, or as a collaboration between the two. These changes
should align to organizational strategy and business goals. It is possible for an IT
department to initiate change to align with technical strategy or reach technical
goals, but an overall organizational strategy alignment is still crucial for change
success.
The following list represents possible change sponsors:
• technical team,
• technical executive,
• application owner,



The Information Technology Perspective
Perspectives
398
• process owner,
• business owner,
• internal product manager, and
• regulatory representative (such as a corporate legal department).
Enterprises may use many methods to initiate changes related to information
technology. Frequently, large enterprises define a program or project
management office within the IT department, which intakes requests and
prioritizes efforts on behalf of the department.
.2 Change Targets
Business analysts identify all possible departments, processes, applications, and
functions which can be impacted by the proposed change. A business analyst not
only focuses on details of the initiative, but also keeps an eye on the larger picture
and the potential impact (both business and technical) of the change. This
involves a level of process and functional analysis with specific focus on both
technical interfaces as well as process hand-offs.
.3 Business Analyst Position
Within an IT initiative, the business analysis activities may be filled by personnel
with one of several types of backgrounds or job titles within the organization.
This assignment may be dependent upon the type of change, the level of
experience, knowledge needed, or simply the personnel available to staff the
effort. The personnel may be assigned to the business analysis tasks due to the
experience described below, and may complete some or all of the business
analysis responsibilities for a given change.
It is possible that all business analysis tasks for an IT project may be completed by
a person with only one of these backgrounds:
• a business analyst who works specifically with the business users of an IT
system,
• an IT business analyst who is the designated liaison between the technical
team and the business group which uses the application,
• a subject matter expert (SME) experienced with the current software
implementation,
• a software user experienced with the daily activity of how the software is
used and can focus on usability,
• a systems analyst who has experience within the business domain, but does
not have experience with the specific application,
• a business process owner who has a depth of experience with the business
capabilities or processes, but may not have any technical or IT experience,
• a technical person with a depth of technical experience, or



Perspectives
The Information Technology Perspective
399
• a COTS representative who will allow for customized implementations of a
packaged solution, and leverage the knowledge of the vendor's package
and past implementation experience.
.4 Business Analysis Outcomes
Within an IT initiative, a business analyst may consider business processes
impacted by the change, as well as the data and business intelligence information
collected by the system. Business analysts working in the initiative thoroughly
plan the business analysis effort and the deliverables that support the change
effort.
The change approach being utilized has a direct impact on business analysis
deliverables or outcomes. Many organizations have a defined system or solution
development methodology which, to some extent, dictates the deliverables which
are required at each project milestone. Even within the context of this structure
the business analyst may seek to complete additional deliverables beyond those
required by the change approach or organization specific process, and employ
techniques which support the comprehensive understanding of the change effort
needed.
Business analysts working in the IT discipline are responsible for delivering any of
the following:
• defined, complete, testable, prioritized, and verified requirements,
• analysis of alternatives,
• business rules,
• gap analysis,
• functional decomposition,
• use cases and scenarios, and/or user stories as appropriate,
• interface analysis,
• prototypes,
• process analysis,
• process models,
• state models,
• decision models,
• context models or scope models, and
• data models.
Additional deliverables not included in the above list but relating to any of the
outputs of business analysis techniques used may also be considered deliverables
of the business analyst.



The Information Technology Perspective
Perspectives
400
11.3.3
Methodologies
The methodologies followed by information technology organizations vary
widely.
In general, solution development methodologies fall into two generic
approaches:
• Predictive: structured processes which emphasize planning and formal
documentation of the processes used to complete the change. Each phase
of the process or sequence is completed before advancing to the next
phase.
• Adaptive: processes which allow for reworking within one or more of the
overall structured process cycles. Most adaptive models are both iterative
and incremental, focusing on growing the product in both breadth and
depth.
A hybrid methodology may also be utilized. A hybrid may include an overall vision
for the whole initiative (as in predictive), as well as a definition of details within
individual cycles or iterations (as in adaptive).
The following table identifies several established methodologies or approaches
that a business analyst practicing in an information technology environment may
encounter.
11.3.4
Underlying Competencies
A business analyst working within IT may possess skills related to IT development
such as programming, creating a database, creating a system or solution
Table 11.3.1: Information Technology Methodologies
Methodology
Brief Description
Homegrown or
Organization Specific
A methodology which is derived from components of
other established methodologies or approaches may
be created by an information technology organization
to govern information technology based initiatives.
Requirements
Engineering (RE)
Establishes a structured approach for requirements
development and management and is used in
predictive, adaptive, and agile environments.
Structured Systems
Analysis and Design
Method (SSADM)
A predictive development methodology that focuses
on established logical modelling and the separation of
requirements from solutions as central to systems
analysis and specification.
Unified Process (UP)
An adaptive development approach. The inception and
elaboration phases are of particular interest to business
analysts. UP is not considered agile but is an adaptive
methodology.



Perspectives
The Information Technology Perspective
401
architecture, software testing experience, or other technical skills. However,
development-related skills or technical skills are not necessary for a business
analyst to be successful within an IT environment. It is important for the business
analyst to have a strong understanding of the detail required within a
requirements package to support technical solutions, as well as an understanding
of what is technically feasible within the constraints of an organization’s technical
architecture. These skills will enable a business analyst to work with all
stakeholders to design a business solution framework which will also allow the
technical team the flexibility to design a technical solution.
Business analysts use influencing and facilitation skills when working with
stakeholders. Negotiation skills are frequently used when working with business
and technical staff to come to agreements and decisions if the costs of a solution
(either in budget, time, or architectural impact) conflict with the desired business
outcome.
Systems thinking is a crucial competency for business analysts practicing in an IT
environment. Systems thinking supports the ability of the business analyst to see
the larger picture including any other applications or technical aspects which may
be impacted, the details of the specific need, and possible technical solutions.
Systems thinking also supports the ability to identify impacts to people, processes,
and software which are not necessarily directly changed as part of an IT
development effort, and to analyze the risks and possible outcomes of those
impacts.
11.3.5
Impact on Knowledge Areas
This section explains how specific business analysis practices within information
technology are mapped to business analysis tasks and practices as defined by the
BABOK® Guide. It also describes how each knowledge area is applied or modified
within the IT discipline.
Each knowledge area lists techniques relevant to an IT perspective. Techniques
used in the discipline of information technology do not deviate, to any great
extent, from the BABOK® Guide techniques. BABOK® Guide techniques are
found in the Techniques chapter of the BABOK® Guide. This is not intended to be
an exhaustive list of techniques but rather to highlight the types of techniques
used by business analysts while performing the tasks within the knowledge area.
.1 Business Analysis Planning and Monitoring
A business analysis approach is a fundamental communication tool which can be
used to identify resources required for business analysis work and ensure
adequate time for the analysis effort. A well-defined business analysis plan
integrates into the overall project plan and provides business analysts with the
opportunity to define and schedule the business analysis activities for the project.
Many organizations have some standards and processes in place, which may
identify certain analysis tasks and deliverables. If these are not in place, the
business analyst identifies these tasks and deliverables based on the needs of the
specific initiative.



The Information Technology Perspective
Perspectives
402
It is important that the context of the analysis work is understood. This includes
understanding the inter-operation of software systems, business processes, and
the data that is passed from one system to the next. Changes to any single system
or process may have a ripple effect that brings additional systems, processes, or
stakeholder groups into the scope of the initiative.
The IT business analyst may be embedded within a software team. This approach
allows the business analyst to become quite knowledgeable about specific
software or processes supported by the software. Stakeholder attitudes and
needs may change or shift in regards to each particular change. Roles,
collaboration, and communication plans are planned for every change effort.
COTS solutions can involve major systems integration efforts, customizations, and
many unexpected tasks due to the introduction of external software. When
planning for unknown impacts and unknown customization needs, business
analysts engage both internal stakeholders who understand the needs of the
change, and external stakeholders who have expertise with the COTS solution
being implemented.
BABOK® Guide Techniques
• Backlog Management (p. 220)
• Document Analysis (p. 269)
• Estimation (p. 271)
• Functional Decomposition (p. 283)
• Item Tracking (p. 294)
• Metrics and Key Performance
Indicators (KPIs) (p. 297)
• Organizational Modelling (p. 308)
• Roles and Permissions Matrix
(p. 333)
• Scope Modelling (p. 338)
• Stakeholder List, Map, or Personas
(p. 344)
.2 Elicitation and Collaboration
Information technology changes frequently affect many stakeholders with
distinct relationships to the solution or change. When a change involves an IT
application or system, the technical staff may have expertise, perspectives, or
experience that can identify additional impacts to systems or processes as
requirements and solutions are defined. For this reason, it is beneficial to have at
least one elicitation session with IT technical personnel, such as development or
technical design staff, and business SMEs in the same room at the same time. This
type of elicitation approach provides a platform for collaboration between
technical and business teams, where the IT business analyst serves as a facilitator
and liaison for the process.
Business analysts practicing in an IT environment may utilize any of the
techniques identified in the Elicitation and Collaboration knowledge area.
Additionally, the following methods can be of great benefit in the information
technology discipline:
• Investigation: using organizational process assets, market research,
competitive analysis, functional specifications, and observation,



Perspectives
The Information Technology Perspective
403
• Simulations: using statistical modelling and mock-ups, and
• Experimentation: using proofs of concept, prototypes, alpha- and beta-
releases, and A/B testing.
Information technology changes can be seen as a distraction or cost by business
stakeholders if the change is not perceived as mission critical or if the stakeholder
is experiencing negative value from the change. This can make engagement for
elicitation challenging. Elicitation across organizational boundaries may be
impeded, causing collaboration breakdowns and rework. IT business analysts can
decrease the risk of rework by engaging information technology and business
resources in collaboration activities.
BABOK® Guide Techniques
• Brainstorming (p. 227)
• Collaborative Games (p. 243)
• Document Analysis (p. 269)
• Focus Groups (p. 279)
• Interface Analysis (p. 287)
• Interviews (p. 290)
• Observation (p. 305)
• Process Modelling (p. 318)
• Prototyping (p. 323)
• Scope Modelling (p. 338)
• Sequence Diagrams (p. 341)
• Stakeholder List, Map, or Personas
(p. 344)
• State Modelling (p. 348)
• Survey or Questionnaire (p. 350)
• Use Cases and Scenarios (p. 356)
• Workshops (p. 363)
.3 Requirements Life Cycle Management
IT initiatives frequently experience major discoveries while creating the change. It
is through exploration that the business analysts discover the implications of the
new functionality provided by the solution. This sense of discovery in IT
environments has led to the adaptation of short cycle times (agile and continuous
improvement), rigorous change control (Capability Maturity Model Integration
(CMMI) and predictive), and externalized information technology (Software as a
Service (SaaS) and cloud services).
Business analysts working in IT pay particular attention to alignment, approval,
change control, traceability, and requirements life cycle management tools. It is
the role of the business analyst to work with stakeholders to develop a consistent
method for reviewing evolving requirements to ensure alignment with the
business objectives for the initiative.
In many cases, changes to approved requirements are driven by changes to
higher-level requirements such as business objectives. Business analysts
collaborate with stakeholders to ensure these requirements are stable before
proceeding to solution or technical requirements. When changes to requirements
are presented, the business analyst analyzes the impact and plans how to manage
proposed changes.
As the complexity of an information technology environment grows, it becomes
increasingly important to track each change to each requirement or between



The Information Technology Perspective
Perspectives
404
requirements and other information. Traceability that includes dependencies and
relationships among requirements makes it easier for stakeholders to understand
what is changing about the IT system and predict impacts of additional changes.
As technical systems are changed over time, it is helpful when each version of
each requirement is stored in some way and accounted for. Traceability makes it
possible to find the source and owner of each requested function and feature, as
well as why, when, and how it changed over time. This history is important for
ensuring that the requirements are complete and that the approval of
requirements is a sensible decision. When the change–work and the IT system are
audited, regulators and other interested parties can understand what happened,
when, and why. This can be especially important for audit purposes, when an
application manages data or processes systematically without human intervention
for each transaction or instance of the process occurring. This tracing also helps
the organization understand why some functionality is not delivered or
implemented in the IT system, and why it was dropped from the scope of this
implementation.
BABOK® Guide Techniques
• Acceptance and Evaluation Criteria
(p. 217)
• Decision Analysis (p. 261)
• Item Tracking (p. 294)
• Metrics and Key Performance
Indicators (KPIs) (p. 297)
• Prioritization (p. 311)
.4 Strategy Analysis
Within an IT organization, strategy analysis focuses on the technologies and
systems, business units, business processes, and business strategies impacted by a
proposed change. It is possible that the impacts of a change cause a ripple effect
through other systems in the organization. In order to analyze needs and
proposed changes, business analysts seek to understand all the various aspects
that may be impacted by the change.
Current state analysis within IT initiatives includes analysis of manual processes,
understanding what the system or technology currently does, the data needed to
complete tasks, and the other systems and processes that interact with the
system. Business analysts plan for a thorough understanding of the current state
and a large context of the enterprise at first, with the understanding that the
scope will narrow as the future state is identified.
Once the current state is understood, the desired future state is described. This
may be process or capability related and usually includes how current system
functionality is required to change in order to support the future vision and meet
the objectives of both individual stakeholders and the enterprise. In
understanding both the current and future states, the gap between the two is
identified, and that is where the direction of the change effort can be set. It is at
this point of analysis that solution options are explored.
Once the aspects of the change scope and desired future state are understood,
business analysts assess uncertainty and risk. Uncertainty is clarified by:



Perspectives
The Information Technology Perspective
405
• identifying and defining risks,
• identifying and defining potential benefits,
• establishing parameters for variance in known processes and operations,
and
• exploring the unknown.
Business analysts also explore other potential risks including:
• vendor risks, such as their business and product stability,
• impacts to the system’s technical environment,
• scalability of the solution should volumes of transactions or users increase
over time, and
• additional process or system changes required based on the change
initiated.
BABOK® Guide Techniques
• Business Capability Analysis (p. 230)
• Focus Groups (p. 279)
• Functional Decomposition (p. 283)
• Interviews (p. 290)
• Item Tracking (p. 294)
• Observation (p. 305)
• Process Analysis (p. 314)
• Process Modelling (p. 318)
• Scope Modelling (p. 338)
• Survey or Questionnaire (p. 350)
• SWOT Analysis (p. 353)
• Vendor Assessment (p. 361)
• Workshops (p. 363)
.5 Requirements Analysis and Design Definition
It is important for business analysts working in IT to understand and clarify the
term 'design'. Many IT organizations think of design only as it applies to the
design or blueprint of a software or technical change. Within the Requirements
Analysis and Design Definition knowledge area, the term design is viewed more
broadly and from the business analyst’s point of view. Designs are usable
representations that focus on the solution and understanding how value might be
realized by a solution if it is built. For example, a model of a potential process
improvement (whether it impacts or utilizes an IT system or not), as well as user
interface layouts or report definitions, can all be considered designs.
Business analysts elaborate business and technical requirements, break down and
define stakeholder needs, and identify the value to be realized by stakeholders
once a technical solution or change is implemented. They elicit, define, and
analyze business and stakeholder requirements, and also define, analyze, and
model solution designs. They define requirements to a level of technical detail
that will be used as part of solution design and input into technical designs. This
elaboration will include both functional requirements and non-functional



The Information Technology Perspective
Perspectives
406
requirements. For some change initiatives, the definition of non-functional
requirements could define all business goals for the change effort.
Business analysts often rely on other change agents to produce technical designs
for software solutions. A systems architect, programmer, database manager, or
other technical expert is often needed to determine how to use technology to
satisfy a set of requirements. IT business analysts define process steps, business
rules, screen flows, and report layouts. Defining requirements to include detailed
functionality of a system, the business, and system processes is a crucial part of
solution design and does not separate analysis and design.
As part of requirements analysis, an IT business analyst may partner with another
business analyst with a different focus, such as an enterprise business analyst or
business architect, to ensure that the IT requirements align to business or
organizational strategy.
Requirements analysis and design definition frequently involves documenting
requirements using words and pictures. In some cases, requirements may be
represented in other ways such as a proof of concept, working software
prototypes, or simulations. In all cases, the business analyst works to produce
documentation with sufficient and appropriate details for:
• the business to verify and validate the requirements,
• the developers to design from, and
• the testers to measure the solution against before it is implemented into a
production environment.
BABOK® Guide Techniques
• Business Rules Analysis (p. 240)
• Data Dictionary (p. 247)
• Data Flow Diagrams (p. 250)
• Data Modelling (p. 256)
• Decision Analysis (p. 261)
• Decision Modelling (p. 265)
• Document Analysis (p. 269)
• Estimation (p. 271)
• Functional Decomposition (p. 283)
• Glossary (p. 286)
• Interface Analysis (p. 287)
• Non-Functional Requirements
Analysis (p. 302)
• Organizational Modelling (p. 308)
• Process Modelling (p. 318)
• Prototyping (p. 323)
• Reviews (p. 326)
• Roles and Permissions Matrix
(p. 333)
• Scope Modelling (p. 338)
• Sequence Diagrams (p. 341)
• State Modelling (p. 348)
• Use Cases and Scenarios (p. 356)
• User Stories (p. 359)
.6 Solution Evaluation
Solution evaluation focuses on solution components and the value they provide.
Within an IT context, this includes a focus on the interactions between multiple



Perspectives
The Information Technology Perspective
407
systems within the change and the surrounding environment. It is important for a
business analyst working in the IT discipline to understand the context of the
solution and how changes within one system or process can impact other systems
within the environment. These impacts can add negative or positive value to the
other systems, therefore impacting the overall realization of value for the change.
One aspect of solution evaluation within an IT context is software testing or
solution testing. Testing or quality assurance ensures that the solution performs as
anticipated or designed, and that it meets the needs of the business or
stakeholders who requested the change effort. The business analyst works with
quality assurance (testers) to ensure that technical solutions will meet the
business needs as defined by the requirements and other business analysis
deliverables. Testers utilize testing methodologies to plan, develop, and execute
tests. This aspect of solution testing generally focuses on complete process
testing, including across systems to ensure end-to-end solution quality and
accuracy. Business analysts work with stakeholders to plan, develop, and execute
user acceptance tests to ensure that the solution meets their needs.
Business analysts make themselves aware of the rationale for implementing an IT
solution and how that rationale works to create solution value. This value
realization is commonly associated with better support for business processes and
procedures.
Business and technical objectives are associated with benefits and value
realization which are measured against defined metrics used to evaluate success.
Requirements should trace back to the objectives, and this traceability provides a
foundation for solution evaluation. The analysis of solution performance focuses
on technical systems and how they provide potential and actual value to
stakeholders.
Where a large organizational change contains an IT element, an IT solution
evaluation can contribute to a broader benefits realization activity associated with
the whole change program.
As part of solution evaluation activities, a business analyst may work with a team
to complete tasks, such as assessing solution limitations and assessing the
impacts of such limitations. The business analyst may support and assess technical
testing efforts for all, or a portion of, the developed solution.
BABOK® Guide Techniques
• Acceptance and Evaluation Criteria
(p. 217)
• Decision Analysis (p. 261)
• Estimation (p. 271)
• Item Tracking (p. 294)
• Metrics and Key Performance
Indicators (KPIs) (p. 297)
• Organizational Modelling (p. 308)
• Risk Analysis and Management
(p. 329)
• Process Modelling (p. 318)
• SWOT Analysis (p. 353)
• Vendor Assessment (p. 361)



The Business Architecture Perspective
Perspectives
408
11.4
The Business Architecture Perspective
The Business Architecture Perspective highlights the unique characteristics of
business analysis when practiced in the context of business architecture.
Business architecture models the enterprise in order to show how strategic
concerns of key stakeholders are met and to support ongoing business
transformation efforts.
Business architecture provides architectural descriptions and views, referred to as
blueprints, to provide a common understanding of the organization for the
purpose of aligning strategic objectives with tactical demands. The discipline of
business architecture applies analytical thinking and architectural principles to the
enterprise level. The solutions may include changes in the business model,
operating model, organizational structure, or drive other initiatives.
Business architecture follows certain fundamental architectural principles:
• Scope: the scope of business architecture is the entire enterprise. It is not a
single project, initiative, process, or piece of information. It puts projects,
processes, and information into the larger business context to provide an
understanding of interactions, integration opportunities, redundancies, and
inconsistencies.
• Separation of concerns: business architecture separates concerns within
its context. It specifically separates what the business does from:
• the information the business uses,
• how the business is performed,
• who does it and where in the enterprise it is done,
• when it is done,
• why it is done, and
• how well it is done.
Once the independent concerns are identified, they can be grouped in
specific combinations or mappings, which can be used to analyze targeted
business issues.
• Scenario driven: there are many different questions that a business tries to
answer to provide the blueprint for alignment. Each of these different
questions or business scenarios requires a different set of blueprints
containing a different set of information and relationships, with different
types of outcomes and measures to determine success.
• Knowledge based: while the primary goal of business architecture is to
answer these business questions, a secondary but important goal is to
collect and catalogue the different architectural components (what, how,
who, why, etc.) and their relationships in a knowledge base so they can
quickly and easily be used to help answer the next business question that
comes up. The knowledge base is often managed in a formal architectural
repository.



Perspectives
The Business Architecture Perspective
409
11.4.1
Change Scope
.1 Breadth of Change
Business architecture may be performed:
• across the enterprise as a whole,
• across a single line of business within the enterprise (defining the
architecture of one of the enterprise's business models), or
• across a single functional division.
Business architecture activities are generally performed with a view of the entire
enterprise in mind, but may also be performed for an autonomous business unit
within the enterprise. A broad scope is required to manage consistency and
integration at the enterprise level. For example, business architecture can clarify a
situation where the same business capability is implemented by multiple different
processes and multiple different organizations using different information
models. Given the clarity that comes from an enterprise scope, the business can
then determine if this structure is the best way to align with strategic objectives.
.2 Depth of Change
A business architecture effort may focus on the executive level of the enterprise to
support strategic decision making, or on the management level to support the
execution of initiatives.
While business architecture provides important context, it does not usually
operate at the operational decision or process level; instead, it assesses processes
at the level of the value stream.
.3 Value and Solutions Delivered
Business architecture, using the principle of separation of concerns, develops
models that decompose the business system, solution, or organization into
individual elements with specific functions and shows the interactions between
them.
The elements of business architecture models include:
• capabilities,
• value,
• processes,
• information and data,
• organization,
• reporting and management,
• stakeholders,
• security strategies, and
• outcomes.



The Business Architecture Perspective
Perspectives
410
Architecture models enable organizations to see the big picture of the domain
that is under analysis. They provide insights into the important elements of the
organization or software system and how they fit together, and highlight the
critical components or capabilities.
The insights provided by business architecture help keep systems and operations
functioning in a coherent and useful manner, and add clarity to business
decisions. When change is being considered, the architecture provides details on
the elements that are most relevant for the purposes of the change, allowing for
prioritization and resource allocation. Because an architectural model also shows
how the parts are related, it can be used to provide impact analysis to tell what
other elements of the system or the business might be affected by the change.
The architecture itself can be used as a tool to help identify needed changes. The
performance metrics for each element of the architecture can be monitored and
assessed to identify when an element is under-performing. The importance of
each element can be compared with the performance of the organization or
system as a whole. This assists decision makers when considering where
investment is needed and how to prioritize those decisions.
The function of business architecture is to facilitate coordinated and synchronized
action across the organization by aligning action with the organization's vision,
goals, and strategy. The architectural models created in this process are the tools
used to clarify, unify, and provide understanding of the intent of the vision, goals,
and strategy, and to ensure that resources are focused and applied to the
elements of the organization that align with and support this direction.
Business architecture provides a blueprint that management can use to plan and
execute strategies from both information technology (IT) and non-IT perspectives.
Business architecture is used by organizations to guide:
• strategic planning,
• business remodelling,
• organization redesign,
• performance measurement and other transformation initiatives to improve
customer retention,
• streamlining business operations,
• cost reduction,
• the formalization of institutional knowledge, and
• the creation of a vehicle for businesses to communicate and deploy their
business vision.
.4 Delivery Approach
Business architecture creates a planning framework that provides clarity and
insight into the organization and assists decision makers in identifying required
changes. The architectural blueprints provided by business architecture provide an
insight and understanding of how well the organization aligns to its strategy. This
insight is the trigger for change or other planning activities.



Perspectives
The Business Architecture Perspective
411
For each blueprint provided, business architecture may define:
• current state,
• future state, and
• one or more transition states that are used to transition to the future state.
Business architects require a view of the entire organization. In general, they may
report directly to a member of senior leadership. Business architects require a
broad understanding of the organization, including its:
• environment and industry trends,
• structure and reporting relationships,
• value streams,
• capabilities,
• processes,
• information and data stores, and
• how all these elements align to support the strategy of the organization.
Business architects play an important role in communicating and innovating for
the strategy of the organization. They utilize blueprints, models, and insights
provided by business architecture to continually advocate for the strategy of the
organization and address individual stakeholder needs within the scope of the
organization's goals.
There are several factors central to a successful business architecture:
• support of the executive business leadership team,
• integration with clear and effective governance processes, including
organizational decision-making authorities (for example, for investments,
initiatives, and infrastructure decisions),
• integration with ongoing initiatives, (this might include participation in
steering committees or other similar advisory groups), and
• access to senior leadership, departmental managers, product owners,
solution architects, project business analysts, and project managers.
.5 Major Assumptions
To make business architecture useful to the organization, business analysts
require:
• a view of the entire organization that is under analysis,
• full support from the senior leadership,
• participation of business owners and subject matter experts (SMEs),
• an organizational strategy to be in place, and
• a business imperative to be addressed.



The Business Architecture Perspective
Perspectives
412
11.4.2
Business Analysis Scope
.1 Change Sponsor
Ideally, the sponsor of a business architecture initiative is a senior executive or
business owner within the organization. However, the sponsor may also be a line-
of-business owner.
.2 Change Targets
The following list identifies the possible primary change targets resulting from a
business architecture analysis:
• business capabilities,
• business value streams,
• initiative plans,
• investment decisions, and
• portfolio decisions.
The following groups of people use business architecture to guide change within
the organization:
• management at all levels of the organization,
• product or service owners,
• operational units,
• solution architects,
• project managers, and
• business analysts working in other contexts (for example, at the project
level).
.3 Business Analyst Position
The goal of a business analyst working within the discipline of business
architecture is to:
• understand the entire enterprise context and provide balanced insight into
all the elements and their relationship across the enterprise, and
• provide a holistic, understandable view of all the specialties within the
organization.
Business architecture provides a variety of models of the organization. These
models, or blueprints, provide holistic insight into the organization that becomes
the basis for strategic decisions by the leaders of the organization. To develop a
business architecture, the business analyst must understand, assimilate, and align



Perspectives
The Business Architecture Perspective
413
a wide variety of specialties that are of strategic concern to the organization. To
do this they require insight, skills, and knowledge from:
• business strategy and goals,
• conceptual business information,
• enterprise IT architecture,
• process architecture, and
• business performance and intelligence architecture.
Business architecture supports the strategic advisory and planning groups that
guide and make decisions regarding change within the organization. It provides
guidance and insights into how decisions align to the strategic goals of the
organization, and ensures this alignment throughout the various transition states
as the change moves towards its future state.
.4 Business Analysis Outcomes
Business architecture provides a broad scope and a holistic view for business
analysis.
The general outcomes of business architecture include:
• the alignment of the organization to its strategy,
• the planning of change in the execution of strategy, and
• ensuring that as change is implemented, it continues to align to the
strategy.
These business architecture outcomes provide context for requirements analysis,
planning and prioritization, estimation, and high-level system design. This
provides insight and alignment with strategy, stakeholder needs, and business
capabilities. Architectural views and blueprints provide information that may have
otherwise been based on assumptions, and minimize the risk of duplication of
efforts in creating capabilities, systems, or information that already exist
elsewhere in the enterprise.
The various models and blueprints provided by business architecture are its key
deliverables. These include, but are not limited to:
• business capability maps,
• value stream maps,
• organization maps,
• business information concepts,
• high-level process architecture, and
• business motivation models.



The Business Architecture Perspective
Perspectives
414
11.4.3
Reference Models and Techniques
.1 Reference Models
Reference models are predefined architectural templates that provide one or
more viewpoints for a particular industry or function that is commonly found
across multiple sectors (for example, IT or finance).
Reference models are frequently considered the default architecture ontology for
the industry or function. They provide a baseline architecture starting point that
business architects can adapt to meet the needs of their organization.
The follow table lists some of the common reference models.
.2 Techniques
The following table lists techniques that are commonly used within the discipline
of business architecture, and are not included in the Techniques section of the
BABOK® Guide.
Table 11.4.1: Business Architecture Reference Models
Reference Model
Domain
Association for Cooperative
Operations Research and
Development (ACORD)
Insurance and Financial industries
Business Motivation Model
(BMM)
Generic
Control Objectives for IT (COBIT)
IT governance and management
eTOM and FRAMEWORX
Communications sector
Federal Enterprise Architecture
Service Reference Model (FEA
SRM)
Government (developed for the U.S. Federal
Government)
Information Technology
Infrastructure Library (ITIL®)
IT service management
Process Classification Framework
(PCF)
Multiple sectors including aerospace,
defence, automotive, education, electric
utilities, petroleum, pharmaceutical, and
telecommunications
Supply Chain Operations
Reference (SCOR)
Supply chain management
Value Reference Model (VRM)
Value change and network management



Perspectives
The Business Architecture Perspective
415
Table 11.4.2: Business Architecture Techniques
Technique
Description
Archimate®
An open standard modelling language.
Business
Motivation Model
(BMM)
A formalization of the business motivation in terms of
mission, vision, strategies, tactics, goals, objectives,
policies, rules, and influencers.
Business Process
Architecture
The modelling of the processes, including interface points,
as a means of providing a holistic view of the processes
that exist within an organization.
Capability Map
A hierarchical catalogue of business capabilities, or what
the business does. Capabilities are categorized according
to strategic, core, and supporting.
Customer Journey
Map
A model that depicts the journey of a customer through
various touch points and the various stakeholders within
the service or organization. Customer journey maps are
frequently used to analyze or design the user experience
from multiple perspectives.
Enterprise Core
Diagram
Models the integration and standardizations of the
organization.
Information Map
A catalogue of the important business concepts
(fundamental business entities) associated with the
business capabilities and value delivery. This is typically
developed in conjunction with the capability model and
represents the common business vocabulary for the
enterprise. It is not a data model but rather a taxonomy of
the business.
Organizational
Map
A model that shows the relationship of business units to
each other, to external partners, and to capabilities and
information. Unlike a typical organizational chart the map
is focused on the interaction between units, not the
structural hierarchy.
Project Portfolio
Analysis
Used to model programs, projects, and portfolios to
provide a holistic view of the initiatives of the organization.
Roadmap
Models the actions, dependencies, and responsibilities
required for the organization to move from current state,
through the transition states, to the future state.
Service-Oriented
Analysis
Used to model analysis, design, and architecture of
systems and software to provide a holistic view of the IT
infrastructure of the organization.



The Business Architecture Perspective
Perspectives
416
11.4.4
Underlying Competencies
In addition to the underlying competencies, business analysts working in the
discipline of business architecture require:
• a high tolerance for ambiguity and uncertainty,
• the ability to put things into a broader context,
• the ability to transform requirements and context into a concept or design
of a solution.
• the ability to suppress unnecessary detail to provide higher level views,
• the ability to think in long time frames over multiple years,
• the ability to deliver tactical outcomes (short term), which simultaneously
provide immediate value and contribute to achieving the business strategy
(long term),
• the ability to interact with people at the executive level,
• the ability to consider multiple scenarios or outcomes,
• the ability to lead and direct change in organizations, and
• a great deal of political acumen.
The Open Group
Architecture
Framework
(TOGAF®)
Provides a method for developing enterprise architecture.
Phase B of the TOGAF Architecture Development Method
(ADM) is focused on the development of business
architecture. Organizations following TOGAF may choose
to tailor Phase B to adopt the business architecture
blueprints, techniques, and references described in the
BABOK® Guide.
Value Mapping
Value mapping provides a holistic representation of the
stream of activities required to deliver value. It is used to
identify areas of potential improvement in an end–to–end
process. Although there are several different types of value
mapping, a value stream is often used in business
architecture.
Zachman
Framework
Provides an ontology of enterprise primitive concepts
based on a matrix of six interrogatives (what, how, where,
who, when, why) and six levels of abstraction (executive,
business management, architect, engineer, technician,
enterprise). Business architects may find that exploring the
executive or business management perspectives across the
different interrogatives provides clarity and insight.
Table 11.4.2: Business Architecture Techniques (Continued)
Technique
Description



Perspectives
The Business Architecture Perspective
417
11.4.5
Impact on Knowledge Areas
This section explains how specific business analysis practices within business
architecture are mapped to business analysis tasks and practices as defined by the
BABOK® Guide. This section describes how each knowledge area is applied or
modified within the business architecture discipline.
Each knowledge area lists techniques relevant to a business architecture
perspective. BABOK® Guide techniques are found in the Techniques chapter of
the BABOK® Guide. Other business analysis techniques are not found in the
Techniques chapter of the BABOK® Guide but are considered to be particularly
useful to business analysts working in the discipline of business architecture. This
is not intended to be an exhaustive list of techniques but rather to highlight the
types of techniques used by business analysts while performing the tasks within
the knowledge area.
.1 Business Analysis Planning and Monitoring
During Business Analysis Planning and Monitoring, the discipline of business
architecture requires business analysts to understand the organization's:
• strategy and direction,
• operating model and value proposition,
• current business and operational capabilities,
• stakeholders and their points of engagement,
• plans for growth, governance, and planning processes,
• culture and environment, and
• capacity for change.
Once these elements are understood the business analyst can then develop an
understanding of which architectural viewpoints are relevant to the analysis.
Governance planning and monitoring activities primarily focus on:
• selecting which projects or initiatives will provide the most benefit in
achieving the business strategies and outcomes, and
• determining which frameworks or models exist or are utilized within the
organization.
BABOK® Guide Techniques
• Acceptance and Evaluation Criteria
(p. 217)
• Brainstorming (p. 227)
• Business Capability Analysis (p. 230)
• Decision Analysis (p. 261)
• Estimation (p. 271)
• Functional Decomposition (p. 283)
• Interviews (p. 290)
• Item Tracking (p. 294)
• Metrics and Key Performance
Indicators (KPIs) (p. 297)



The Business Architecture Perspective
Perspectives
418
• Non-Functional Requirements
Analysis (p. 302)
• Organizational Modelling (p. 308)
• Process Modelling (p. 318)
• Reviews (p. 326)
• Risk Analysis and Management
(p. 329)
• Roles and Permissions Matrix
(p. 333)
• Root Cause Analysis (p. 335)
• Scope Modelling (p. 338)
• Stakeholder List, Map, or Personas
(p. 344)
• Survey or Questionnaire (p. 350)
• Use Cases and Scenarios (p. 356)
• User Stories (p. 359)
Other Business Analysis Techniques
• Business Process Architecture
• Capability Map
• Project Portfolio Analysis
• Service-oriented Analysis
.2 Elicitation and Collaboration
Business analysts working in the discipline of business architecture typically deal
with a great deal of ambiguity and uncertainty. When undertaking Elicitation and
Collaboration tasks, business analysts consider changes in organizational
direction based on external and internal forces and changes in marketplace
environment. The types of changes can frequently be predicted, but external
market pressures frequently make the pace of the change unpredictable.
As business architecture requires many inputs from across the organization,
access to (and the availability of) stakeholders is critical to success. Business
analysts elicit inputs such as strategy, value, existing architectures, and
performance metrics.
Advocacy for the organization's strategy is central to the communication strategy
of business architects. As members of various steering committees and advisory
groups, business architects utilize formal communication channels within
projects, initiatives, and operational groups to communicate the organization's
strategy, explain the organizational context, and advocate alignment with the
strategy.
Ensuring stakeholders understand and support the organization's strategy is an
essential function within the discipline of business architecture. Business
architects may impose scope and constraints on a project or initiative as a means
to ensure the activity aligns to the organization's strategy, which may be viewed
unfavourably. It is the role of the business architect to bridge the needs and
desires of individual stakeholders, projects, and operational groups with the
context and understanding of the organizational goals and strategy. The business
architect's goal is to optimize the enterprise's goals and strategy, and discourage
activities that achieve a narrow goal at the cost of sub-optimizing the entire
objective. This is an exercise in both elicitation and in collaboration.
The business architect acquires a deep understanding of the strategy, drivers,
motivations, and aspirations of the organization and those of the stakeholders.
Once this level of understanding is achieved, the business architect collaborates



Perspectives
The Business Architecture Perspective
419
with all levels of the organization including senior leadership, managers, the
project management office (PMO), product owners, project managers, various
business analysts, solution architects, and IT personnel to bridge gaps in
understanding and communicating the importance of alignment with
organizational strategy. Facilitating effective collaboration requires that the
business architect is able to understand the wide variety of perspectives and
contexts from which each stakeholder operates. The business architect must also
be able to communicate with each of these stakeholders in a language that is
mutually understood and supported.
BABOK® Guide Techniques
• Brainstorming (p. 227)
• Document Analysis (p. 269)
• Focus Groups (p. 279)
• Functional Decomposition (p. 283)
• Glossary (p. 286)
• Interface Analysis (p. 287)
• Interviews (p. 290)
• Item Tracking (p. 294)
• Observation (p. 305)
• Prototyping (p. 323)
• Stakeholder List, Map, or Personas
(p. 344)
• Survey or Questionnaire (p. 350)
• Workshops (p. 363)
Other Business Analysis Techniques
• none
.3 Requirements Life Cycle Management
It is essential that business analysts working in the discipline of business
architecture have executive support and agreement of the work to be
undertaken. An architecture review board comprised of senior executives with
decision-making powers can review and assess changes to the business
architecture. This group will often also engage in portfolio management by
making decisions regarding the investment in and prioritization of change based
on their impact to business outcomes and strategy.
Business analysts working in the discipline of business architecture understand
how projects impact the business architecture on an ongoing basis and work to
continually expand, correct, or improve the business architecture. They also
identify possible emerging changes in both internal and external situations
(including market conditions), and decide on how to incorporate these changes
into the business architecture of the organization.
BABOK® Guide Techniques
• Balanced Scorecard (p. 223)
• Benchmarking and Market Analysis
(p. 226)
• Business Capability Analysis (p. 230)
• Collaborative Games (p. 243)
• Data Modelling (p. 256)
• Decision Analysis (p. 261)
• Estimation (p. 271)



The Business Architecture Perspective
Perspectives
420
• Interface Analysis (p. 287)
• Item Tracking (p. 294)
• Lessons Learned (p. 296)
• Metrics and Key Performance
Indicators (KPIs) (p. 297)
• Organizational Modelling (p. 308)
• Process Analysis (p. 314)
• Process Modelling (p. 318)
• Reviews (p. 326)
• Risk Analysis and Management
(p. 329)
• Roles and Permissions Matrix
(p. 333)
• Root Cause Analysis (p. 335)
• Stakeholder List, Map, or Personas
(p. 344)
• SWOT Analysis (p. 353)
Other Business Analysis Techniques
• Archimate®
• Business Process Architecture
• Business Value Modelling
• Capability Map
• Enterprise Core Diagram
• Project Portfolio Analysis
• Roadmap
• Service-oriented Analysis
• Value Mapping
.4 Strategy Analysis
Business architecture can play a significant role in strategy analysis. It provides
architectural views into the current state of the organization and helps to define
both the future state and the transition states required to achieve the future state.
Business architects develop roadmaps based on the organization's change
strategy. Clearly defined transition states help ensure that the organization
continues to deliver value and remain competitive throughout all the phases of
the change. To keep competitive, the business must analyze such factors as:
• market conditions,
• which markets to move into,
• how the organization will compete in the transition state, and
• how to best position the organization's brand proposition.
Business architecture provides the enterprise context and architectural views that
allow an understanding of the enterprise so these questions can be analyzed in
the context of cost, opportunity, and effort.
BABOK® Guide Techniques
• Balanced Scorecard (p. 223)
• Benchmarking and Market Analysis
(p. 226)
• Brainstorming (p. 227)
• Business Capability Analysis (p. 230)
• Business Model Canvas (p. 236)
• Business Rules Analysis (p. 240)
• Collaborative Games (p. 243)
• Data Modelling (p. 256)
• Document Analysis (p. 269)
• Estimation (p. 271)
• Focus Groups (p. 279)



Perspectives
The Business Architecture Perspective
421
• Glossary (p. 286)
• Metrics and Key Performance
Indicators (KPIs) (p. 297)
• Organizational Modelling (p. 308)
• Reviews (p. 326)
• Risk Analysis and Management
(p. 329)
• Stakeholder List, Map, or Personas
(p. 344)
• Survey or Questionnaire (p. 350)
• SWOT Analysis (p. 353)
• Workshops (p. 363)
Other Business Analysis Techniques
• Archimate®
• Business Process Architecture
• Capability Map
• Customer Journey Map
• Enterprise Core Diagram
• Project Portfolio Analysis
• Roadmap
• Service-oriented Analysis
• Strategy Map
• Value Mapping
.5 Requirements Analysis and Design Definition
Business architecture provides individual architectural views into the organization
through a variety of models that are selected for the stakeholders utilizing the
view. These architectural views can be provided by capability and value maps,
organizational maps, and information and business process models. Business
analysts working in the discipline of business architecture employ expertise,
judgment, and experience when deciding what is (and what is not) important to
model. Models are intended to provide context and information that result in
better requirements analysis and design.
The architectural context and the ability to reference readily available architectural
views provides information that would have otherwise been based on
assumptions that the analyst must make because no other information was
available. By providing this information, business architecture minimizes the risk
of duplication of efforts in creating capabilities, systems, or information that
already exist elsewhere in the enterprise.
Design is done in conjunction with understanding needs and requirements.
Business architecture provides the context to analyze the strategic alignment of
proposed changes and the effects those changes have upon each other. Business
architects synthesize knowledge and insights from multiple architectural views to
determine if proposed changes work towards or conflict with the organization's
goals.
Business architecture attempts to ensure that the enterprise as a whole continues
to deliver value to stakeholders both during normal operations and during
change. Business analysts working in the discipline of business architecture focus
on the value provided by the organization from a holistic view. They attempt to
avoid local optimization where effort and resources are put into a single process
or system improvement which does not align with the strategy and garners no
meaningful impact to the enterprise as a whole—or worse, sub-optimizes the
whole.



The Business Architecture Perspective
Perspectives
422
BABOK® Guide Techniques
• Acceptance and Evaluation Criteria
(p. 217)
• Backlog Management (p. 220)
• Balanced Scorecard (p. 223)
• Benchmarking and Market Analysis
(p. 226)
• Brainstorming (p. 227)
• Business Capability Analysis (p. 230)
• Business Model Canvas (p. 236)
• Business Rules Analysis (p. 240)
• Collaborative Games (p. 243)
• Data Dictionary (p. 247)
• Data Flow Diagrams (p. 250)
• Data Modelling (p. 256)
• Decision Analysis (p. 261)
• Document Analysis (p. 269)
• Estimation (p. 271)
• Focus Groups (p. 279)
• Functional Decomposition (p. 283)
• Glossary (p. 286)
• Interface Analysis (p. 287)
• Item Tracking (p. 294)
• Lessons Learned (p. 296)
• Metrics and Key Performance
Indicators (KPIs) (p. 297)
• Non-Functional Requirements
Analysis (p. 302)
• Observation (p. 305)
• Organizational Modelling (p. 308)
• Process Analysis (p. 314)
• Process Modelling (p. 318)
• Prototyping (p. 323)
• Reviews (p. 326)
• Risk Analysis and Management
(p. 329)
• Roles and Permissions Matrix
(p. 333)
• Root Cause Analysis (p. 335)
• Scope Modelling (p. 338)
• Sequence Diagrams (p. 341)
• Stakeholder List, Map, or Personas
(p. 344)
• State Modelling (p. 348)
• Survey or Questionnaire (p. 350)
• SWOT Analysis (p. 353)
• Use Cases and Scenarios (p. 356)
• User Stories (p. 359)
• Vendor Assessment (p. 361)
• Workshops (p. 363)
Other Business Analysis Techniques
• Archimate®
• Business Process Architecture
• Capability Map
• Customer Journey Map
• Enterprise Core Diagram
• Project Portfolio Analysis
• Roadmap
• Service-oriented Analysis
• Value Mapping
.6 Solution Evaluation
Business architecture asks fundamental questions about the business, including



Perspectives
The Business Architecture Perspective
423
the important question of how well the business is performing.
To answer this question, several other questions must be answered:
• What outcomes are the business, a particular initiative, or component
expecting to achieve?
• How can those outcomes be measured in terms of SMART (Specific,
Measurable, Achievable, Relevant, Time-bounded) objectives?
• What information is needed to measure those objectives?
• How do processes, services, initiatives, etc. need to be instrumented to
collect that information?
• How is the performance information best presented in terms of reports, ad
hoc queries, dashboards, etc.?
• How do we use this information to make investment decisions in the
future?
For example, at a more detailed level, an important part of capability definition
and process architecture is to identify the specific performance characteristics and
outcome that those capabilities or processes are expected to achieve. The actual
measurement is rarely conducted by business analysts. It is usually done by
business owners, operational, or information technology managers.
Business analysts working in the discipline of business architecture analyze the
results of measurements and factor these results into subsequent planning.
BABOK® Guide Techniques
• Balanced Scorecard (p. 223)
• Benchmarking and Market Analysis
(p. 226)
• Brainstorming (p. 227)
• Business Capability Analysis (p. 230)
• Collaborative Games (p. 243)
• Focus Groups (p. 279)
• Item Tracking (p. 294)
• Lessons Learned (p. 296)
• Metrics and Key Performance
Indicators (KPIs) (p. 297)
• Observation (p. 305)
• Organizational Modelling (p. 308)
• Process Analysis (p. 314)
• Process Modelling (p. 318)
• Risk Analysis and Management
(p. 329)
• Roles and Permissions Matrix
(p. 333)
• Root Cause Analysis (p. 335)
• Stakeholder List, Map, or Personas
(p. 344)
• Survey or Questionnaire (p. 350)
• SWOT Analysis (p. 353)
Other Business Analysis Techniques
• Business Motivation Modelling
• Business Process Architecture
• Capability Map
• Customer Journey Map
• Service-oriented Analysis
• Value Mapping



The Business Process Management Perspective
Perspectives
424
11.5
The Business Process Management Perspective
The Business Process Management Perspective highlights the unique
characteristics of business analysis when practiced in the context of developing or
improving business processes.
Business Process Management (BPM) is a management discipline and a set of
enabling technologies that:
• focuses on how the organization performs work to deliver value across
multiple functional areas to customers and stakeholders,
• aims for a view of value delivery that spans the entire organization, and
• views the organization through a process-centric lens.
A BPM initiative delivers value by implementing improvements to the way work is
performed in an organization.
BPM determines how manual and automated processes are created, modified,
cancelled, and governed. Organizations that hold a process-centric view treat
BPM as an ongoing effort and an integral part of the ongoing management and
operation of the organization.
11.5.1
Change Scope
Business analysts working within the BPM discipline may address a single process
with limited scope or they may address all of the processes in the organization.
Business analysts frequently focus on how the processes of an organization can
be changed in order to improve and meet the objectives of the organization.
BPM life cycles generally include the following activities:
• Designing: the identification of processes and definition of their current
state (as-is) and determining how we get to the future state (to-be). The
gap between these states may be used to specify stakeholders’ expectations
of how the business should be run.
• Modelling: the graphical representation of the process that documents the
process as well as comparing current state (as-is) and future state (to-be).
This phase of the BPM life cycle provides input to requirements and solution
design specification, as well as analyzing their potential value. Simulation
may use quantitative data so that the potential value of variations on the
process can be analyzed and compared.
• Execution and Monitoring: provides the same type of input as modelling
but in terms of the actual execution of processes. The data collected as a
result of the actual business process flow is very reliable and objective which
makes it a very strong asset in analyzing value and recommending
alternatives for design improvement.
• Optimizing: the act of ongoing repetition or iteration of the previous
phases. The results of business process execution and monitoring are
utilized to modify models and designs so that all inefficiencies are removed



Perspectives
The Business Process Management Perspective
425
and more value is added. Optimization may be a source of requirements
and solution design definitions that comes directly from stakeholders and
the user community. Optimization of processes is also a good way to
demonstrate the value of a suggested solution modification, and justify
process and product improvement initiatives.
.1 Breadth of Change
The goal of BPM is to ensure that value delivery is optimized across end-to-end
processes. A comprehensive BPM initiative can span the entire enterprise. A single
BPM initiative can make an organization become more process-centric by
providing insights into its processes. An organization's processes define what the
organization does and how it does it. Possessing a thorough understanding of its
processes allows stakeholders to adjust these processes to meet the evolving
needs of both the organization and its customers.
Individual initiatives may improve specific processes and sub-processes. Breaking
down larger, more complex processes into smaller chunks (sub-processes) allows
business analysts to better understand what each process is doing and how to
optimize them.
.2 Depth of Change
Business analysts use BPM frameworks to facilitate the analysis and deep
understanding of the organization's processes. BPM frameworks are sets or
descriptions of processes for a generic organization, specific industry, professional
area, or type of value stream. BPM frameworks define particular levels of
processes throughout the organization's process architecture.
As an example, business analysts perform supply chain analysis as a means of
evaluating specific processes in an organization. Analysis of the supply chain is
frequently conducted by decomposing group-level processes into individual sub-
components and then decomposing these down to individuals performing
specific tasks.
Business analysts involved with business process management are frequently
engaged in continuous improvement activities as they are often the ones most
familiar with BPM.
.3 Value and Solutions Delivered
The goal of BPM is to improve operational performance (effectiveness, efficiency,
adaptability, and quality) and to reduce costs and risks. Business analysts
frequently consider transparency into processes and operations as a common core
value of BPM initiatives. Transparency into processes and operations provides
decision makers a clear view of the operational consequences of previous process
related decisions. Business analysis efforts frequently begin with the identification
of the business need of the customers. Needs are generally referred to as BPM
drivers. BPM drivers include:
• cost reduction initiatives,
• increase in quality,



The Business Process Management Perspective
Perspectives
426
• increase in productivity,
• emerging competition,
• risk management,
• compliance initiatives,
• next generation process automation,
• core system implementation,
• innovation and growth,
• post merger and acquisition rationalization,
• standardization initiatives,
• major transformation programs,
• establishment of a BPM Centre of Excellence,
• increased agility, and
• speed or faster processes.
.4 Delivery Approach
The delivery approach for BPM initiatives across organizations ranges from a set
of tactical methods focused on improving individual processes to a management
discipline that touches all the processes in an organization. The main purpose of
process transformation is to help organizations identify, prioritize, and optimize
their business processes to deliver value to stakeholders.
Organizations conduct periodic assessments of key processes and engage in
ongoing continuous improvement to achieve and sustain process excellence. The
success of BPM can be measured by how well the BPM initiative aligns to the
objectives set for BPM in the organization.
There are several mechanisms that can be used to implement BPM:
• Business process re-engineering: methods that aim for major process
redesign across the enterprise.
• Evolutionary forms of change: methods that have overall objectives set
for the process and then individual changes aimed at bringing sub-
processes in line with those goals are implemented.
• Substantial discovery: methods are used when organizational processes
are undefined or if the documented version of the process is substantially
different from the actual process in use. Substantial discovery is about
revealing actual processes and is a method for organizational analysis.
• Process benchmarking: compares an organization's business processes
and performance metrics to industry best practices. Dimensions typically
measured are quality, time, and cost.
• Specialized BPMS applications: are designed to support BPM initiatives
and execute the process models directly. These applications are tools that



Perspectives
The Business Process Management Perspective
427
automate BPM activities. Often the organization's processes are required to
be changed to match the automated approach.
Process improvement approaches can be categorized in terms of their point of
origin and whether their solutions are primarily organizational (people-based) or
technological (IT-based). Organizations can better understand the process
improvement methodology, as mentioned in the previous paragraph, to apply
based on the following organizing principles:
• Top-down: initiatives are typically orchestrated from a central point of
control by senior management and have organization spanning
implications, targeted at end-to-end processes or major parts of the
business.
• Bottom-up: initiatives are typically tactical approaches to improving
individual processes and departmental workflows, or sub-processes in
smaller parts of the organization.
• People-centric: initiatives where the principal change is to the activities
and workflows in an organization.
• IT-centric: initiatives frequently focused on process automation.
.5 Major Assumptions
The following is a list of major assumptions from the BPM discipline:
• Processes are generally supported by information technology systems, but
the development of those systems is not covered by most BPM methods.
Business analysts may suggest additional business requirements based on
existing IT systems.
• BPM initiatives have senior management support. The business analyst may
be involved in suggesting additional business requirements based on
organizational strategies.
• BPM systems require a tight integration with organizational strategy but
most methods do not tackle the development of strategy which is outside
the scope of this perspective.
• BPM initiatives are cross-functional and end-to-end in the organization.
11.5.2
Business Analysis Scope
.1 Change Sponsor
Enterprise-wide BPM initiatives are typically started by executives focusing on
value and outcomes and then linking these strategic objectives to the
corresponding business processes which most closely support the objectives.
BPM initiatives are frequently triggered by an external situation which generates a
business need. Enterprise business analysis practices are applied to develop a
business case for a BPM initiative.



The Business Process Management Perspective
Perspectives
428
Process improvements are typically initiated or at least managed by a process
manager at any level of the organization. The scope of the process or sub-process
usually determines the authority of the process manager.
.2 Change Targets
The possible primary change targets for a BPM initiative include:
• Customer: the key stakeholder in any BPM initiative. The principal focus is
on the external customer but internal customers are also considered. Since
BPM is customer-centric by nature, the customer is part of BPM initiatives in
order to validate the effectiveness of the process change. Involving the
customer early in the initiative minimizes the risk of failure by ensuring the
goals of process delivery are aligned to the customer’s expectations.
• Regulator: a stakeholder in any BPM initiative due to evolving
requirements towards compliance and risk management by some
organizations. Regulators may trigger a BPM initiative due to changes in
regulations on such concerns as public safety, transparency, equal
opportunity, and non-discrimination.
• Process Owner: the key stakeholder in any BPM initiative and has the
responsibility and authority to make the final decision regarding any
changes to the affected processes. The process owner is also responsible for
measuring the process performance.
• Process Participants: stakeholders who directly or indirectly participate in
the process being evaluated. These participants define the activities of the
process. In order to ensure that the interests of process participants are met,
the process owner engages them during design of the process.
• Project Manager: manages the BPM initiative and is accountable for its
delivery and driving decisions. The project manager works with a team
including process analysts, process owners, and process designers. The
project manager is responsible for planning, scheduling, communication
management, change management, and risk management.
• Implementation Team: converts the plans of the BPM initiative into
functioning business processes. The success of a BPM initiative is the ability
to integrate all the functions that meet the needs of the customer.
.3 Business Analysis Position
Business analysts working within the discipline of business process management
may assume a variety of roles:
• Process Architect: responsible for modelling, analyzing, deploying,
monitoring, and continuously improving business processes. A process
architect knows how to design business processes and how to enhance
those processes either manually or for automated business process
execution on a BPM platform. Process architects address and guide the
decisions around what process knowledge, methodology, and technology is
required to meet the objectives of the organization with respect to a



Perspectives
The Business Process Management Perspective
429
particular BPM initiative. Process architects enhance and transform business
processes into technically enhanced and executable process templates.
Depending on the BPM initiative, process architects may be focused on
managing business performance or on mapping technology to business
operations. Process architects are responsible for developing and
maintaining standards and the repository of reference models for products
and services, business processes, key performance indicators (KPIs), and
critical success factors (CSF). They are engaged in process analysis and
transformation initiatives.
• Process Analyst/Designer: has detailed process knowledge, skills, and
interest. They are experts in documenting and understanding process
design along with performance trends. Process analysts/designers have an
interest in business process optimization to increase overall business
performance. This goal requires an understanding of the detailed process
and includes performing the necessary analysis for process optimization.
They perform analysis and assessment of as-is processes, evaluate alternate
process design options, and make recommendations for change based on
various frameworks.
• Process Modeller: captures and documents business (both the as-is and
to-be) processes. The process modeller is frequently a process analyst
working to document a process for implementation or support by an
information technology system.
The process analyst/designer and the process modeller functions frequently reside
within a single position.
Figure 11.5.1: Business Analyst Roles in a BPM Initiative
Process Change Initiative
Ongoing
Implementation
Project
Manager
Process
Owner
Functional
Manager
Staff
Process Manager
Process
Participants
Process Project
Manager
Key Stakeholder
Business Analyst
Process
Modeller
Process Architect
Process
Analyst
& Designer



The Business Process Management Perspective
Perspectives
430
.4 Business Analysis Outcomes
Outcomes for business analysts working within the discipline of business process
management include:
• business process models,
• business rules,
• process performance measures,
• business decisions, and
• process performance assessment.
Business Process Models
Business process models start at the highest level as an end-to-end model of the
whole process and can become as specific as modelling specific work flow.
Business process models serve as both an output and a starting point for the
analysis of the process. They are divided into current state (as-is) and future state
(to-be) models. Current state models portray the process as it currently functions,
without any improvements. The future state model envisions what the process
would look like if all improvement options are incorporated. The benefit of
developing the current state model is to justify the investment in the process by
enabling the business analyst to measure the effect of the process improvements
and prioritize changes to the process. Transition models describe the interim
states required to move from the current state process to the future state process.
Business Rules
Business rules guide business processes and are intended to assert business
structure or control the behaviour of business. Business rules are identified during
requirements elicitation and process analysis and often focus on business
calculations, access control issues, and policies of an organization. Classifying
business rules can help decide how they will be best implemented. Business rules
analysis provides insight into how the business functions and how the processes
contribute to meeting the business' goals and objectives. Business analysts
analyze the reasons for the existence of a business rule and study its impact on
the business process before improving or redesigning it. Business rules may,
where appropriate, be mapped to individual processes through the decisions they
influence unless they are related strictly to the performance of the process.
Process Performance Measures
Process performance measures are parameters that are used to identify process
improvement opportunities. Process performance measures are defined and
deployed to ensure that processes are aligned to the business needs and strategic
objectives of the organization. Process performance measures can address many
aspects of a process including quality, time, cost, agility, efficiency, effectiveness,
responsiveness, adaptability, flexibility, customer satisfaction, velocity, variability,
visibility, variety, rework, and volume. Many of the process performance measures
seek to measure the effectiveness and efficiency of the process as well as the
degree to which the process goals are achieved. When deployed across the



Perspectives
The Business Process Management Perspective
431
business, process performance measures can indicate the maturity level of process
culture in an organization and generate a shared understanding of process
performance across an organization. Performance measures are keys to defining
service level agreements where an organization provides service to their customers.
Business Decisions
Business decisions are a specific kind of task or activity in a business process that
determine which of a set of options will be acted upon by the process. Decisions
must be made (using a task or activity) and then acted upon (often with a
gateway or branch in the process). Decisions may be manual or automated, are
modelled independently, and are best described using business rules. Decision
rules, often implemented through a business rules engine, allow these business
decisions to be automated.
Process Performance Assessment
The success of any BPM initiative rests on the intention and capability to
continuously measure and monitor the performance of targeted business
processes. The assessment can be static and be documented with assessment
reports and scorecards, or dynamic and be delivered through dashboards. It
provides necessary information to decision makers in an organization to redeploy
and adjust resources in order to meet process performance goals.
11.5.3
Frameworks, Methodologies, and Techniques
.1 Frameworks
The following table lists frameworks that are commonly used within the discipline
of business process management.
BPM Frameworks
Framework
Brief description
ACCORD
A methodological framework that maps current
state models, as well as unstructured data, to
conceptual models.
Enhanced
Telecommunications
Operations Map (eTOM)
A hierarchical framework developed for the
telecommunications industry that has been
adopted by other service-oriented industries.
Governments Strategic
Reference Model (GSRM)
A life cycle framework that provides generic
government processes and patterns for each stage
of organizational maturity.
Model based and
Integrated Process
Improvement (MIPI)
A cyclical framework whose steps include assess
readiness, outline process under review, detail data
collection, form model of current process, assess
and redesign process, implement improved
process, and review process.



The Business Process Management Perspective
Perspectives
432
.2 Methodologies
The following table lists methodologies that are commonly used within the
discipline of business process management.
Process Classification
Framework(PCF)
A classification framework that details processes
and is used for benchmarking and performance
measurement.
Table 11.5.1: BPM Methodologies
Methodology
Brief description
Adaptive Case
Management (ACM)
A method used when processes are not fixed or
static in nature, and have a lot of human
interaction. An ACM process may be different each
time it is performed.
Business Process Re-
engineering (BPR)
The fundamental rethinking and redesigning of
business processes to generate improvements in
critical performance measures, such as cost, quality,
service, and speed.
Continuous Improvement
(CI)
The ongoing monitoring and adjustment of existing
processes to bring them closer to goals or
performance targets. This represents a permanent
commitment of the organization to change and
must be an important part of its culture.
Lean
A continuous improvement methodology that
focuses on the elimination of waste in a process,
defined as work for which the customer of the
process will not pay.
Six Sigma
A continuous improvement methodology that
focuses on the elimination of variations in the
outcome of a process. It is statistically oriented and
performance data centric.
Theory Of Constraints
(TOC)
A methodology that holds the performance of an
organization can be optimized by managing three
variables: the throughput of a process, operational
expense to produce that throughput, and the
inventory of products. The performance of a
process is dominated by one key constraint at any
given time, and the process can only be optimized
by improving the performance of that constraint.
BPM Frameworks (Continued)
Framework
Brief description



Perspectives
The Business Process Management Perspective
433
.3 Techniques
The following table lists techniques, not included in the Techniques chapter of the
BABOK® Guide and are commonly used within the discipline of BPM.
Total Quality
Management (TQM)
A management philosophy that holds to the
underlying principle that the processes of the
organization should provide the customer and
stakeholders, both internal and external, with the
highest quality products and services, and that
these products or services meet or exceed the
customers' and stakeholders' expectations.
Table 11.5.2: BPM Techniques
Technique
Brief Description
Cost Analysis
A list of the cost per activity totaled to show the detailed
cost of the process and is used frequently by businesses
to gain an understanding and appreciation of the cost
associated with a product or service. Cost analysis is also
known as activity based costing.
Critical to Quality
(CTQ)
A set of diagrams, in the form of trees, that assist in
aligning process improvement efforts to customer
requirements. CTQ is a technique used in Six Sigma, but
is not exclusive to Six Sigma.
Cycle-time Analysis
An analysis of the time each activity takes within the
process. Cycle-time analysis is also known as a duration
analysis.
Define Measure
Analyze Design
Verify (DMADV )
A data-driven structured roadmap used to develop new
or improve existing processes. DMADV is a technique
used in Six Sigma, but is not exclusive to Six Sigma.
Define Measure
Analyze Improve
Control (DMAIC)
A data-driven structured roadmap used to improve
processes. DMAIC is a technique used in Six Sigma, but is
not exclusive to Six Sigma.
Drum-Buffer-Rope
(DBR)
A method used to ensure that the system constraint
always functions at the maximum possible output, by
ensuring that there is a sufficient buffer of materials just
prior to the constraint to keep it continuously busy. It can
be used in BPM to ensure process efficiency.
Failure Mode and
Effect Analysis
(FMEA)
A systematic method of investigating process failures
and defects, and identifying potential causes. FMEA is a
technique that assists in locating problems in the as-is
process and correcting them when developing the to-be
processes.
Table 11.5.1: BPM Methodologies (Continued)
Methodology
Brief description



The Business Process Management Perspective
Perspectives
434
House of Quality/
Voice of Customer
A matrix relating customer desires and product
characteristics to the capabilities of an organization. It is
a technique that could be used in developing the to-be
processes.
Inputs, Guide,
Outputs, Enablers
(IGOE)
A diagram that describes the context of a process, by
listing the inputs and outputs of the process, the guides
that are used to inform the execution of the process, and
the supporting tools and information required for the
process.
Kaizen Event
A focused, rapid effort to improve value delivery in one
specific activity or sub-process.
Process Simulation
A model of the process and a set of randomized variables
to allow for multiple variations of a process to be
assessed and develop an estimate of their performance
under actual conditions.
Suppliers Inputs
Process Outputs
Customers (SIPOC)
A table that summarizes inputs and outputs from
multiple processes. Also known as COPIS, which is simply
SIPOC spelled backwards.
Theory of
Constraints (TOC)
Thinking Processes
A set of logical cause-and-effect models used to
diagnose conflicts, identify the root causes of problems,
and define future states of a system that successfully
resolve those root causes. TOC thinking processes is a
technique that assists in locating problems in the as-is
process and correcting them when developing the to-be
processes.
Value Added
Analysis
Looks at the benefit to the customer added at each step
of a process to identify opportunities for improvement.
Value Stream
Analysis
Used to assess the value added by each functional area
of a business to the customer, as part of an end-to-end
process.
Who What When
Where Why (5Ws)
A set of questions that form the foundation for basic
information gathering. The 5Ws may also include How
added to become the 5Ws and a H.
Table 11.5.2: BPM Techniques (Continued)
Technique
Brief Description



Perspectives
The Business Process Management Perspective
435
11.5.4
Underlying Competencies
Business analysts working within the discipline of business process management
are required to challenge the status quo, dig to understand the root causes of a
problem, assess why things are being done in a particular way, and encourage
subject matter experts (SMEs) to consider new ideas and approaches to make
their processes more efficient and effective. They are also required to understand,
articulate, and move back and forth between internal and external views of the
processes under analysis.
Due to the effects that changes to processes have on the working habits of
individuals, interaction skills are valuable in a BPM initiative. Business analysts
frequently negotiate and arbitrate between individuals with different opinions,
and expose and resolve conflicts between different groups within the
organization. The business analyst is a neutral and independent facilitator of the
change.
BPM initiatives are likely to involve all levels of the organization and the business
analyst is required to communicate across organizational boundaries as well as
outside the organization.
11.5.5
Impact on Knowledge Areas
This section explains how specific business analysis practices within business
process management are mapped to business analysis tasks and practices as
defined by the BABOK® Guide. This section also describes how each knowledge
area is applied or modified within the business process management discipline.
Each knowledge area lists techniques relevant to a business process management
perspective. BABOK® Guide techniques are found in the Techniques chapter of
the BABOK® Guide. Other business analysis techniques are not found in the
chapter, but are considered to be particularly useful to business analysts working
in the discipline of business process management. This is not intended to be an
exhaustive list of techniques but rather to highlight the types of techniques used
by business analysts while performing the tasks within the knowledge area.
.1 Business Analysis Planning and Monitoring
Progressive elaboration is common in the planning of BPM initiatives due to the
fact that the amount of information available for full planning may be limited in
the initial stages. BPM initiatives involve continuous improvement activities, and a
common cause of failure of BPM initiatives is the failure to plan for ongoing
monitoring of the effect of changes to the process. In BPM initiatives, the initial
focus of business analysis work is on analyzing and improving the business
process before looking at the technology used to support the process, and any
changes that might be required to software applications or work procedures.



The Business Process Management Perspective
Perspectives
436
BABOK® Guide Techniques
• Estimation (p. 271)
• Item Tracking (p. 294)
• Process Modelling (p. 318)
• Reviews (p. 326)
• Stakeholder List, Map, or Personas
(p. 344)
• Workshops (p. 363)
Other Business Analysis Techniques
• Inputs, Guide, Outputs, Enablers (IGOE)
.2 Elicitation and Collaboration
For the BPM initiative to be successful, the scope of the initiative and the scope of
the affected process must be defined and understood.
Process modelling and stakeholder analysis are generally utilized during the
elicitation phase of a BPM initiative. During elicitation, the business analyst
focuses on cause and effect of both changing existing processes and keeping the
processes as they are through the elicitation and collaboration effort. As an
existing process is changed, the effect of any process improvements identified on
the organization, people, and technology are considered. Process maps are an
important tool to drive elicitation in BPM initiatives and stakeholders are
frequently consulted during their development. Effective elicitation and
collaboration is critical in process modelling analysis and design work.
Process changes can have significant impacts across the organization, so
managing stakeholders and their expectations is particularly critical. Without
effective stakeholder management, process changes may not be successfully
implemented or the changes may not meet the organization's goals and
objectives.
BABOK® Guide Techniques
• Brainstorming (p. 227)
• Document Analysis (p. 269)
• Focus Groups (p. 279)
• Interface Analysis (p. 287)
• Interviews (p. 290)
• Metrics and Key Performance
Indicators (KPIs) (p. 297)
• Observation (p. 305)
• Process Modelling (p. 318)
• Prototyping (p. 323)
• Reviews (p. 326)
• Root Cause Analysis (p. 335)
• Scope Modelling (p. 338)
• Stakeholder List, Map, or Personas
(p. 344)
• Survey or Questionnaire (p. 350)
• Use Cases and Scenarios (p. 356)
• User Stories (p. 359)
• Workshops (p. 363)
Other Business Analysis Techniques
• House of Quality/Voice of Customer



Perspectives
The Business Process Management Perspective
437
.3 Requirements Life Cycle Management
BPM is a set of approaches that focus on ways to deliver value across multiple
functional areas through a process-centric lens. Delivering additional value is
often related to deliberately undertaking change but could also result from an ad
hoc request or review of processes. The impact of BPM activities on requirements
life cycle management is significant as it can drive out business requirements
resulting in new design, coding, implementation, and post-implementation
changes. It is the responsibility of the business analyst to maintain this connection
and ensure that communication is effectively conducted with stakeholders and
process owners who are the ultimate decision makers when it is about processes,
change, and supporting solutions.
The documentation of business processes is available to all stakeholders as it is to
be used in the daily operation of the business. If the process is automated
through a BPMS, the representation of the process may be directly executable.
BABOK® Guide Techniques
• Acceptance and Evaluation Criteria
(p. 217)
• Backlog Management (p. 220)
• Brainstorming (p. 227)
• Business Rules Analysis (p. 240)
• Non-Functional Requirements
Analysis (p. 302)
• Prioritization (p. 311)
• Process Analysis (p. 314)
• Process Modelling (p. 318)
• Prototyping (p. 323)
• Scope Modelling (p. 338)
• Workshops (p. 363)
Other Business Analysis Techniques
• none
.4 Strategy Analysis
In a BPM context, strategy analysis involves understanding the role the process
plays in an enterprise value chain. At a minimum, any process that interacts with
the processes affected by the initiative must be considered.
The current state is likely to be described by the as-is value chain and the current
performance measures for the business process. The future state will be described
by the to-be value chain and target performance measures. Continuous
improvement methods may simply focus on the performance measures to
determine the strategy. The change strategy will involve the identification of
possible process changes.
BABOK® Guide Techniques
• Document Analysis (p. 269)
• Functional Decomposition (p. 283)
• Interviews (p. 290)
• Lessons Learned (p. 296)
• Process Analysis (p. 314)
• Process Modelling (p. 318)



The Business Process Management Perspective
Perspectives
438
Other Business Analysis Techniques
• Drum-Buffer-Rope
• House of Quality/Voice of Customer
• Inputs, Guide, Outputs, Enablers
(IGOE)
• TOC Thinking Processes
.5 Requirements Analysis and Design Definition
Requirements analysis and design definition will focus on defining the to-be
process model. The requirements architecture is likely to include the process
model, associated business rules and decisions, information requirements, and
the organizational structure. Solution options typically include changes to IT
needed to support the process, outsourcing of aspects of the process, and similar
changes.
BABOK® Guide Techniques
• Benchmarking and Market Analysis
(p. 226)
• Business Rules Analysis (p. 240)
• Decision Modelling (p. 265)
• Estimation (p. 271)
• Functional Decomposition (p. 283)
• Metrics and Key Performance
Indicators (KPIs) (p. 297)
• Prioritization (p. 311)
• Prototyping (p. 323)
• Scope Modelling (p. 338)
• Stakeholder List, Map, or Personas
(p. 344)
• Workshops (p. 363)
Other Business Analysis Techniques
• Kaizen Event
• Process Simulation
.6 Solution Evaluation
Solution evaluation typically occurs repeatedly during BPM initiatives in order to
assess the performance of the business process. As processes are evaluated for
different scenarios, they can be refined and the results are monitored. Solution
evaluation tasks provide insight into the understanding of the impact of process
improvements and the value delivered by business process change. The solution
may also involve process mining which uses such techniques as audit trails or
transaction logs to obtain process details.
The analyze solution performance task is performed to understand the
differences between potential value and actual value. This analysis is performed
to discover why there is a variance between potential and actual value, to
determine if a solution can perform better or realize more value. The evaluation
examines opportunities or constraints of the implemented solution, how it
satisfies needs, or how it could be improved. This may trigger further optimization
of the process and a repeat of the BPM life cycle.



Perspectives
The Business Process Management Perspective
439
BABOK® Guide Techniques
• Acceptance and Evaluation Criteria
(p. 217)
• Balanced Scorecard (p. 223)
• Benchmarking and Market Analysis
(p. 226)
• Brainstorming (p. 227)
• Business Capability Analysis (p. 230)
• Business Rules Analysis (p. 240)
• Decision Analysis (p. 261)
• Document Analysis (p. 269)
• Estimation (p. 271)
• Interviews (p. 290)
• Metrics and Key Performance
Indicators (KPIs) (p. 297)
• Observation (p. 305)
• Organizational Modelling (p. 308)
• Process Modelling (p. 318)
• Reviews (p. 326)
• Risk Analysis and Management
(p. 329)
• Root Cause Analysis (p. 335)
• Stakeholder List, Map, or Personas
(p. 344)
• Survey or Questionnaire (p. 350)
• SWOT Analysis (p. 353)
Other Business Analysis Techniques
• Kaizen Event
• Failure Mode and Effect Analysis (FMEA)
• Process Simulation
• Value Stream Analysis



The Business Process Management Perspective
Perspectives
440



Glossary
441
Appendix A: Glossary
a
acceptance criteria: Criteria associated with requirements, products, or the
delivery cycle that must be met in order to achieve stakeholder acceptance.
actor (business analysis): A human, device, or system that plays some specified
role in interacting with a solution.
adaptive approach: An approach where the solution evolves based on a cycle of
learning and discovery, with feedback loops which encourage making
decisions as late as possible.
Agile Extension to the BABOK® Guide: A standard on the practice of business
analysis in an agile context. The Agile Extension to the BABOK® Guide
version 1 was published in 2013 by IIBA®, in partnership with the Agile
Alliance.
allocation: See requirements allocation.
architecture: The design, structure, and behaviour of the current and future states
of a structure in terms of its components, and the interaction between
those components. See also business architecture, enterprise architecture,
and requirements architecture.
artifact (business analysis): Any solution-relevant object that is created as part of
business analysis efforts.
assumption: An influencing factor that is believed to be true but has not been
confirmed to be accurate, or that could be true now but may not be in the
future.
b
behavioural business rule: A business rule that places an obligation (or
prohibition) on conduct, action, practice, or procedure; a business rule
whose purpose is to shape (govern) day-to-day business activity. Also
known as operative rule.
benchmarking: A comparison of a decision, process, service, or system's cost,
time, quality, or other metrics to those of leading peers to identify
opportunities for improvement.
body of knowledge: The aggregated knowledge and generally accepted practices
on a topic.
BPM: See business process management.
brainstorming: A team activity that seeks to produce a broad or diverse set of
options through the rapid and uncritical generation of ideas.
business (business analysis): See enterprise.
business (business world): An economic system where any commercial, industrial,
or professional activity is performed for profit.



Glossary
442
business analysis: The practice of enabling change in the context of an enterprise
by defining needs and recommending solutions that deliver value to
stakeholders.
business analysis information: Any kind of information at any level of detail that is
used as an input to business analysis work, or as an output of business
analysis work.
business analysis package: A document, presentation, or other collection of text,
matrices, diagrams and models, representing business analysis information.
business analyst: Any person who performs business analysis, no matter their job
title or organizational role. For more information, see Who is a Business
Analyst? (p. 2).
business analysis approach: The set of processes, rules, guidelines, heuristics, and
activities that are used to perform business analysis in a specific context.
business analysis communication plan: A description of the types of
communication the business analyst will perform during business analysis,
the recipients of those communications, and the form and frequency of
those communications.
business analysis effort: The scope of activities a business analyst is engaged in
during the life cycle of an initiative.
business analysis plan: A description of the planned activities the business analyst
will execute in order to perform the business analysis work involved in a
specific initiative. See also requirements management plan.
business architecture: The design, structure, and behaviour of the current and
future states of an enterprise to provide a common understanding of the
organization. It is used to align the enterprise’s strategic objectives and
tactical demands.
business case: A justification for a course of action based on the benefits to be
realized by using the proposed solution, as compared to the cost, effort, and
other considerations to acquire and live with that solution.
business decision: A decision that can be made based on strategy, executive
judgment, consensus, and business rules, and that is generally made in
response to events or at defined points in a business process.
business domain: See domain.
business goal: A state or condition that an organization is seeking to establish
and maintain, usually expressed qualitatively rather than quantitatively.
business need: A problem or opportunity of strategic or tactical importance to be
addressed.
business objective: An objective, measurable result to indicate that a business
goal has been achieved.
business policy: A non-practicable directive that controls and influences the
actions of an enterprise.



Glossary
443
business problem: An issue of strategic or tactical importance preventing an
enterprise or organization from achieving its goals.
business process: An end-to-end set of activities which collectively responds to an
event, and transforms information, materials, and other resources into
outputs that deliver value directly to the customers of the process. It may be
internal to an organization, or it may span several organizations.
business process management (BPM): A management discipline that determines
how manual and automated processes are created, modified, cancelled,
and governed.
business process re-engineering: Rethinking and redesigning business processes
to generate improvements in performance measures.
business requirement: A representation of goals, objectives and outcomes that
describe why a change has been initiated and how success will be assessed.
business rule: A specific, practicable, testable directive that is under the control of
the business and that serves as a criterion for guiding behaviour, shaping
judgments, or making decisions.
c
capability: The set of activities the enterprise performs, the knowledge it has, the
products and services it provides, the functions it supports, and the methods
it uses to make decisions.
cause-and-effect diagram: See fishbone diagram.
change: The act of transformation in response to a need.
change agent: One who is a catalyst for change.
change control: Controlling changes to requirements and designs so that the
impact of requested changes is understood and agreed-to before the
changes are made.
change management: Planned activities, tools, and techniques to address the
human side of change during a change initiative, primarily addressing the
needs of the people who will be most affected by the change.
change strategy: A plan to move from the current state to the future state to
achieve the desired business objectives.
change team: A cross-functional group of individuals who are mandated to
implement a change. This group may be comprised of product owners,
business analysts, developers, project managers, implementation subject
matter experts (SMEs), or any other individual with the relevant set of skills
and competencies required to implement the change.
checklist (business analysis): A standard set of quality elements that reviewers use
for requirements verification.
collaboration: The act of two or more people working together towards a
common goal.



Glossary
444
commercial off-the-shelf (COTS): A prepackaged solution available in the
marketplace which address all or most of the common needs of a large
group of buyers of those solutions. A commercial off-the-shelf solution may
require some configuration to meet the specific needs of the enterprise.
competitive analysis: A structured assessment which captures the key
characteristics of an industry to predict the long-term profitability prospects
and to determine the practices of the most significant competitors.
component: A uniquely identifiable element of a larger whole that fulfills a clear
function.
concept model: An analysis model that develops the meaning of core concepts
for a problem domain, defines their collective structure, and specifies the
appropriate vocabulary needed to communicate about it consistently.
constraint (business analysis): An influencing factor that cannot be changed, and
that places a limit or restriction on a possible solution or solution option.
context: The circumstances that influence, are influenced by, and provide
understanding of the change.
core concept (business analysis): One of six ideas that are fundamental to the
practice of business analysis: Change, Need, Solution, Context, Stakeholder,
and Value.
cost-benefit analysis: An analysis which compares and quantifies the financial and
non-financial costs of making a change or implementing a solution
compared to the benefits gained.
COTS: See commercial off-the-shelf.
create, read, update, and delete matrix (CRUD matrix): A two-dimensional matrix
showing which user roles have permission to access specific information
entities, and to create new records in those entities, view the data in existing
records, update or modify the data in existing records, or delete existing
records. The same type of matrix can be used to show which processes,
instead of users, have the create, read, update and delete rights.
CRUD matrix: See create, read, update, and delete matrix.
customer: A stakeholder who uses or may use products or services produced by
the enterprise and may have contractual or moral rights that the enterprise
is obliged to meet.
d
decision analysis: An approach to decision making that examines and models the
possible consequences of different decisions, and assists in making an
optimal decision under conditions of uncertainty.
decomposition: A technique that subdivides a problem into its component parts
in order to facilitate analysis and understanding of those components.
defect: A deficiency in a product or service that reduces its quality or varies from
a desired attribute, state, or functionality.



Glossary
445
definitional business rule: A rule that indicates something is necessarily true (or
untrue); a rule that is intended as a definitional criterion for concepts,
knowledge, or information. Also known as a structural rule.
deliverable: Any unique and verifiable work product or service that a party has
agreed to deliver.
design: A usable representation of a solution. For more information see Key Terms
(p. 14) and Requirements and Designs (p. 19).
document analysis (business analysis): An examination of the documentation of
an existing system in order to elicit requirements.
domain: The sphere of knowledge that defines a set of common requirements,
terminology, and functionality for any program or initiative solving a
problem.
domain subject matter expert: A stakeholder with in-depth knowledge of a topic
relevant to the business need or solution scope.
DSDM: See dynamic systems development method.
dynamic systems development method (DSDM): A project delivery framework
which focuses on fixing cost, quality, and time at the beginning while
contingency is managed by varying the features to be delivered.
e
elicitation: Iterative derivation and extraction of information from stakeholders or
other sources.
end user: A stakeholder who directly interacts with the solution.
enterprise: A system of one or more organizations and the solutions they use to
pursue a shared set of common goals.
enterprise architecture: A description of the business processes, information
technology, people, operations, information, and projects of an enterprise
and the relationships between them.
enterprise readiness assessment: An assessment that describes the enterprise is
prepared to accept the change associated with a solution and is able to use
it effectively.
entity-relationship diagram: A graphical representation of the entities relevant to
a chosen problem domain and the relationships between them.
estimate: A quantitative assessment of a planned outcome, resource
requirements, and schedule where uncertainties and unknowns are
systematically factored into the assessment.
evaluation: The systematic and objective assessment of a solution to determine its
status and efficacy in meeting objectives over time, and to identify ways to
improve the solution to better meet objectives. See also indicator; metric,
monitoring.



Glossary
446
event (business analysis): An occurrence or incident to which an organizational
unit, system, or process must respond.
evolutionary prototype: A prototype that is continuously modified and updated in
response to feedback from stakeholders.
experiment: Elicitation performed in a controlled manner to make a discovery, test
a hypothesis, or demonstrate a known fact.
external interface: An interaction that is outside the proposed solution. It can be
another hardware system, software system, or a human interaction with
which the proposed solution will interact.
f
facilitation: The art of leading and encouraging people through systematic efforts
toward agreed-upon objectives in a manner that enhances involvement,
collaboration, productivity, and synergy.
feasibility study: An evaluation of proposed alternatives to determine if they are
technically, organizationally, and economically possible within the
constraints of the enterprise, and whether they will deliver the desired
benefits to the enterprise.
feature: A distinguishing characteristic of a solution that implements a cohesive
set of requirements and which delivers value for a set of stakeholders.
fishbone diagram: A diagramming technique used in root cause analysis to
identify underlying causes of an observed problem, and the relationships
that exist between those causes. Also known as an Ishikawa or cause-and-
effect diagram.
focus group: A group formed to to elicit ideas and attitudes about a specific
product, service, or opportunity in an interactive group environment. The
participants share their impressions, preferences, and needs, guided by a
moderator.
force field analysis: A graphical method for depicting the forces that support and
oppose a change. Involves identifying the forces, depicting them on
opposite sides of a line (supporting and opposing forces) and then
estimating the strength of each set of forces.
functional requirement: A capability that a solution must have in terms of the
behaviour and information the solution will manage.
g
gap analysis: A comparison of the current state and desired future state of an
enterprise in order to identify differences that need to be addressed.
goal: See business goal.
governance process (change): A process by which appropriate decision makers
use relevant information to make decisions regarding a change or solution,
including the means for obtaining approvals and priorities.



Glossary
447
guideline (business analysis): An instruction or description on why or how to
undertake a task.
h
horizontal prototype: A prototype that is used to explore requirements and
designs at one level of a proposed solution, such as the customer-facing
view or the interface to another organization.
i
impact analysis: An assessment of the effects a proposed change will have on a
stakeholder or stakeholder group, project, or system.
implementation subject matter expert: A stakeholder who has specialized
knowledge regarding the implementation of one or more solution
components.
indicator: A specific numerical measurement that indicates progress toward
achieving an impact, output, activity, or input. See also metric.
initiative: A specific project, program, or action taken to solve some business
problem(s) or achieve some specific change objective(s).
input (business analysis): Information consumed or transformed to produce an
output. An input is the information necessary for a task to begin.
inspection: A formal review of a work product by qualified individuals that follows
a predefined process, and uses predefined criteria, for defect identification
and removal.
interface: A shared boundary between any two persons and/or systems through
which information is communicated.
interoperability: Ability of systems to communicate by exchanging data or
services.
interview: Eliciting information from a person or group of people in an informal
or formal setting by asking relevant questions and recording the responses.
Ishikawa diagram: See fishbone diagram.
iteration (business analysis): A single instance of progressive cycles of analysis,
development, testing, or execution.
k
knowledge area (business analysis): An area of expertise that includes several
specific business analysis tasks.
l
lessons learned process: A process improvement technique used to learn about
and improve on a process or project. A lessons learned session involves a
special meeting in which the team explores what worked, what didn't work,
what could be learned from the just-completed iteration, and how to adapt
processes and techniques before continuing or starting anew.



Glossary
448
life cycle: A series of changes an item or object undergoes from inception to
retirement
m
matrix: A textual form of modelling used to represent information that can be
categorized, cross-referenced, and represented in a table format.
metadata: A description of data to help understand how to use that data, either
in terms of the structure and specification of the data, or the description of
a specific instance of an object.
methodology: A body of methods, techniques, procedures, working concepts,
and rules used to solve a problem
metric: A quantifiable level of an indicator measured at a specified point in time.
mission statement: A formal declaration of values and goals that expresses the
core purpose of the enterprise.
model: A representation and simplification of reality developed to convey
information to a specific audience to support analysis, communication, and
understanding.
monitoring: Collecting data on a continuous basis from a solution in order to
determine how well a solution is implemented compared to expected
results. See also metric; indicator.
n
need: A problem or opportunity to be addressed.
non-functional requirement: A type of requirement that describes the
performance or quality attributes a solution must meet. Non-functional
requirements are usually measurable and act as constraints on the design of
a solution as a whole.
o
objective: See business objective.
observation (business analysis): Studying and analyzing one or more stakeholders
in their work environment in order to elicit requirements.
OLAP: See online analytical processing.
online analytical processing (OLAP): A business intelligence approach that allows
users to analyze large amounts of data from different points of view.
operational support: A stakeholder who is responsible for the day-to-day
management and maintenance of a system or product.
operative rule: See behavioural business rule.
organization: An autonomous group of people under the management of a
single individual or board, that works towards common goals and
objectives.



Glossary
449
organizational capability: A function inside the enterprise, made up of
components such as processes, technologies, and information and used by
organizations to achieve their goals.
organizational change management: See change management.
organization modelling: The analysis technique used to describe roles,
responsibilities and reporting structures that exist within an enterprise.
organizational unit: Any recognized association of people within an organization
or enterprise.
p
peer review: A formal or informal review of a work product to identify errors or
opportunities for improvement. See also inspection.
plan: A detailed scheme for doing or achieving something usually comprising a
set of events, dependencies, expected sequence, schedule, results or
outcomes, materials and resources needed, and how stakeholders need to
be involved.
policy: See business policy.
predictive approach: An approach where planning and baselines are established
early in the life cycle of the initiative in order to maximize control and
minimize risk.
prioritization: Determining the relative importance of a set of items in order to
determine the order in which they will be addressed.
process: A set of activities designed to accomplish a specific objective by taking
one or more defined inputs and turning them into defined outputs.
process model: A set of diagrams and supporting information about a process
and factors that could influence the process. Some process models are used
to simulate the performance of the process.
product (business analysis): A solution or component of a solution that is the
result of an initiative.
product backlog: A set of user stories, requirements, or features that have been
identified as candidates for potential implementation, prioritized, and
estimated.
product scope: See solution scope.
product vision statement: A brief statement or paragraph that describes the goals
of the solution and how it supports the strategy of the organization or
enterprise.
project: A temporary endeavour undertaken to create a unique product, service,
or result.
project manager: A stakeholder who is responsible for managing the work
required to deliver a solution that meets a business need, and for ensuring



Glossary
450
that the project's objectives are met while balancing the project constraints,
including scope, budget, schedule, resources, quality, and risk.
project scope: The work that must be performed to deliver a product, service, or
result with the specified features and functions.
proof of concept: A model created to validate the design of a solution without
modelling the appearance, materials used in the creation of work, or
processes and workflows ultimately used by the stakeholders.
prototype: A partial or simulated approximation of the solution for the purpose of
eliciting or verifying requirements with stakeholders.
q
quality: The degree to which a set of inherent characteristics fulfills needs.
quality assurance: A set of activities performed to ensure that a process will
deliver products that meet an appropriate level of quality.
quality attributes: A set of measures used to judge the overall quality of a system.
See also non-functional requirements.
questionnaire: A set of defined questions, with a choice of answers, used to
collect information from respondents.
r
RACI matrix: See responsible, accountable, consulted, and informed matrix.
regulator: A stakeholder from outside the organization who is responsible for the
definition and enforcement of standards.
repository: A real or virtual facility where all information on a specific topic is
stored and is available for retrieval.
request for information (RFI): A formal elicitation method intended to collect
information regarding a vendor's capabilities or any other information
relevant to a potential upcoming procurement.
request for proposal (RFP): A requirements document issued when an
organization is seeking a formal proposal from vendors. An RFP typically
requires that the proposals be submitted following a specific process and
using sealed bids which will be evaluated against a formal evaluation
methodology.
request for quote (RFQ): A procurement method of soliciting price and solution
options from vendors.
request for tender (RFT): An open invitation to vendors to submit a proposal for
goods or services.
requirement: A usable representation of a need.
requirements attribute: A characteristic or property of a requirement used to
assist with requirements management.



Glossary
451
requirements allocation: The process of assigning requirements to be
implemented by specific solution components.
requirements architecture: The requirements of an initiative and the
interrelationships between these requirements.
requirements artifact: A business analysis artifact containing information about
requirements such as a diagram, matrix, document or model.
requirements defect: A problem or error in a requirement. Defects may occur
because a requirement is poor quality (see requirements verification) or
because it does not describe a need that, if met, would provide value to
stakeholders (see requirements validation).
requirements document: See requirements package.
requirements life cycle: The stages through which a requirement progresses from
inception to retirement.
requirements management: Planning, executing, monitoring, and controlling any
or all of the work associated with requirements elicitation and collaboration,
requirements analysis and design, and requirements life cycle management.
requirements management plan: A subset of the business analysis plan for a
specific change initiative, describing specific tools, activities, and roles and
responsibilities that will be used on the initiative to manage the
requirements. See business analysis plan.
requirements management tool: Special-purpose software that provides support
for any combination of the following capabilities: elicitation and
collaboration, requirements modelling and/or specification, requirements
traceability, versioning and baselining, attribute definition for tracking and
monitoring, document generation, and requirements change control.
requirements model: An abstract (usually graphical) representation of some
aspect of the current or future state.
requirements package: A specialized form of a business analysis package
primarily concerned with requirements. A requirements package may
represent a baseline of a collection of requirements.
requirements traceability: The ability for tracking the relationships between sets
of requirements and designs from the original stakeholder need to the
actual implemented solution. Traceability supports change control by
ensuring that the source of a requirement or design can be identified and
other related requirements and designs potentially affected by a change are
known.
requirements validation: Work done to evaluate requirements to ensure they
support the delivery of the expected benefits and are within the solution
scope.
requirements verification: Work done to evaluate requirements to ensure they are
defined correctly and are at an acceptable level of quality. It ensures the
requirements are sufficiently defined and structured so that the solution



Glossary
452
development team can use them in the design, development, and
implementation of the solution.
requirements workshop: A structured meeting in which a carefully selected group
of stakeholders collaborate to define and/or refine requirements under the
guidance of a skilled neutral facilitator.
residual risk: The risk remaining after action has been taken or plans have been
put in place to deal with the original risk.
retrospective: See lessons learned process.
return on investment (ROI) (business analysis): A measure of the profitability of a
project or investment.
responsible, accountable, consulted, and informed matrix (RACI matrix): A tool
used to identify the responsibilities of roles or team members and the
activities or deliverables in which they will participate, by being responsible
(doing the work), accountable (approving the results), consulted (providing
input) or informed of the completed item after it has been completed.
RFI: See request for information.
RFP: See request for proposal.
RFQ: See request for quote.
RFT: See request for tender.
risk (business analysis): The effect of uncertainty on the value of a change, a
solution, or the enterprise. See also residual risk.
risk assessment: Identifying, analyzing and evaluating risks.
ROI: See return on investment.
root cause: The cause of a problem having no deeper cause, usually one of
several possible causes.
root cause analysis: A structured examination of an identified problem to
understand the underlying causes.
s
scope: The boundaries of control, change, a solution, or a need.
scope model: A model that defines the boundaries of a business domain or
solution.
secondary actor: An actor external to the system under design that supports the
execution of a use case.
sequence diagram: A type of diagram that shows objects participating in
interactions and the messages exchanged between them.
service (business analysis): The performance of any duties or work for a
stakeholder, from the perspective of the stakeholder.
SIPOC: See suppliers, inputs, process, outputs and customers.



Glossary
453
SME: See subject matter expert.
software engineer: See developer.
solution: A specific way of satisfying one or more needs in a context.
solution component: A sub-part of a solution that can be people, infrastructure,
hardware, software, equipment, facilities, and process assets or any
combination of these sub-parts.
solution option: One possible way to satisfy one or more needs in a context.
solution requirement: A capability or quality of a solution that meets the
stakeholder requirements. Solution requirements can be divided into two
sub-categories: functional requirements and non-functional requirements or
quality of service requirements.
solution life cycle: The stages through which a solution progresses from inception
to retirement.
solution scope: The set of capabilities a solution must deliver in order to meet the
business need.
SOW: See statement of work.
sponsor: A stakeholder who is responsible for initiating the effort to define a
business need and develop a solution that meets that need. They authorize
the work to be performed and control the budget and scope for the
initiative.
stakeholder: A group or individual with a relationship to the change, the need, or
the solution.
stakeholder analysis: Identifying and analyzing the stakeholders who may be
impacted by the change and assess their impact, participation, and needs
throughout the business analysis activities.
stakeholder list: A catalogue of the stakeholders affected by a change, business
need, or proposed solution, and a description of their attributes and
characteristics related to their involvement in the initiative.
stakeholder proxy (business analyst): The role a business analyst takes when
representing the needs of a stakeholder or stakeholder group.
stakeholder requirement: A description of the needs of a particular stakeholder or
class of stakeholders that must be met in order to achieve the business
requirements. They may serve as a bridge between business requirements
and the various categories of solution requirements.
state diagram: An analysis model showing the life cycle of a data entity or class.
stated requirement: A requirement articulated by a stakeholder that has not been
analyzed, verified, or validated. Stated requirements frequently reflect the
desires of a stakeholder rather than the actual need.
statement of work (SOW): A written description of the services or tasks that are
required to be performed.



Glossary
454
strategy: A description of the chosen approach to apply the capabilities of an
enterprise in order to reach a desired set of goals or objectives.
strengths, weaknesses, opportunities, and threats analysis (SWOT): An analysis
model used to understand influencing factors and how they may affect an
initiative. Also known as SWOT analysis.
structural rule: See definitional business rule.
subject matter expert (SME): See domain subject matter expert; implementation
subject matter expert.
supplier: A stakeholder outside the boundary of a given organization or
organizational unit who provides products or services to the organization
and may have contractual or moral rights and obligations that must be
considered.
suppliers, inputs, process, outputs, and customers (SIPOC): A tool used to
describe relevant high-level elements of a process. May be used in
conjunction with process mapping and ‘in/out of scope’ tools, to provide
additional detail.
survey: Collecting and measuring the opinions or experiences of a group of
people through a series of questions.
swimlane: A horizontal or vertical section of a process diagram that shows which
activities are performed by a particular actor or role.
SWOT analysis: See strengths, weaknesses, opportunities and threats analysis.
system: A set of interdependent components that interact in various ways to
produce a set of desired outcomes.
t
task (business analysis): A discrete piece of work that may be performed formally
or informally as part of business analysis.
technique: A manner, method, or style for conducting a business analysis task or
for shaping its output.
temporal event: An event based on time that can trigger the initiation of a
process, evaluation of business rules, or some other response.
tester: An individual responsible for determining how to verify that the solution
meets the requirements defined by the business analyst, and conducting the
verification process.
throw-away prototype: A prototype used to quickly uncover and clarify
requirements or designs using simple tools, sometimes just paper and
pencil. It is intended to be discarded when the final system has been
developed.
time-box: An agreed-upon period of time in which an activity is conducted or a
defined deliverable is intended to be produced.
traceability: See requirements traceability.



Glossary
455
transition requirement: A requirement that describes the capabilities the solution
must have and the conditions the solution must meet to facilitate transition
from the current state to the future state, but which are not needed once
the change is complete. They are differentiated from other requirements
types because they are of a temporary nature.
u
UAT: See user acceptance test.
UML®: See unified modelling language.
unified modelling language™ A notation specified by the Object Management
Group for describing software application structure, behaviour, and
architecture. It can also be used for describing business processes and data
structures. The most common UML® diagrams used by business analysts are
use case diagrams, activity diagrams, state machine diagrams (also known
as state diagrams), and class diagrams.
use case: A description of the observable interaction between an actor (or actors)
and a solution that occurs when the actor uses the system to accomplish a
specific goal.
use case diagram: A type of diagram defined by UML® that captures all actors
and use cases involved with a system or product.
user: See end user.
user acceptance test (UAT): Assessing whether the delivered solution meets the
needs of the stakeholder group that will be using the solution. The
assessment is validated against identified acceptance criteria.
user requirement: See stakeholder requirement.
user story: A small, concise statement of functionality or quality needed to deliver
value to a specific stakeholder.
v
validation (business analysis): The process of checking that a deliverable is
suitable for its intended use. See also requirements validation.
validated requirement: A requirement that has been reviewed and is determined
to support the delivery of the expected benefits, and is within the solution
scope.
value (business analysis): The worth, importance, or usefulness of something to a
stakeholder in a context.
value stream mapping: A complete, fact-based, time-series representation of the
stream of activities required to deliver a product or service.
verification (business analysis): The process of determining that a deliverable or
artifact meets an acceptable standard of quality. See also requirements
verification.



Glossary
456
verified requirement: A requirement that has been reviewed and is determined to
be defined correctly, adheres to standards or guidelines, and is at an
acceptable level of detail.
vertical prototype: A prototype that is used to drill down into a proposed solution
to uncover requirement and design considerations through multiple layers
of a solution that are not easily understood or that are not discernible on
the surface. It may include interaction between several solution
components.
viewpoint: A set of conventions that define how requirements will be
represented, how these representations will be organized, and how they
will be related.
VSM: See value stream mapping.
w
walkthrough: A review in which participants step through an artifact or set of
artifacts with the intention of validating the requirements or designs, and to
identify requirements or design errors, inconsistencies, omissions,
inaccuracies, or conflicts.
WBS: See work breakdown structure.
work breakdown structure (WBS): A deliverable-oriented hierarchical
decomposition of the work to be executed to accomplish objectives and
create the required deliverables. It organizes and defines the total scope of
the project.
work product (business analysis): A document or collection of notes or diagrams
used by the business analyst during the requirements development process.
Workshop: A facilitated and focused event attended by key stakeholders for the
purpose of achieving a defined goal.



Techniques to Task Mapping
457
Appendix B: Techniques to Task Mapping
The following table shows each BABOK® Guide task in which the technique is
included in the Techniques section.
This mapping is provided for reference purposes and does not preclude the
creative use of any technique during the application of any other task in which it
is not specifically listed.



Techniques to Task Mapping
458

## Business Analysis


Planning
and Monitoring

Planning
and Monitoring

Planning
and Monitoring

Planning
and Monitoring

Planning
and Monitoring

Planning
and Monitoring

Planning
and Monitoring

Planning
and Monitoring

Planning
and Monitoring

Planning
and Monitoring

Planning
and Monitoring

Planning
and Monitoring

Planning
and Monitoring

Planning
and Monitoring

Planning
and Monitoring

## Elicitation and


Collaboration

Collaboration

Collaboration

Collaboration

Collaboration

Collaboration

Collaboration

Collaboration

Collaboration

Collaboration

Collaboration

Collaboration

Collaboration

Collaboration

Collaboration

## Requirements


Life Cycle
Management

Life Cycle
Management

Life Cycle
Management

Life Cycle
Management

Life Cycle
Management

Life Cycle
Management

Life Cycle
Management

Life Cycle
Management

Life Cycle
Management

Life Cycle
Management

Life Cycle
Management

Life Cycle
Management

Life Cycle
Management

Life Cycle
Management

Life Cycle
Management

## Strategy Analysis 7. Requirements


Analysis and Design
Definition

Analysis and Design
Definition

Analysis and Design
Definition

Analysis and Design
Definition

Analysis and Design
Definition

Analysis and Design
Definition

Analysis and Design
Definition

Analysis and Design
Definition

Analysis and Design
Definition

Analysis and Design
Definition

Analysis and Design
Definition

Analysis and Design
Definition

Analysis and Design
Definition

Analysis and Design
Definition

Analysis and Design
Definition

## Solution


Evaluation

Evaluation



Techniques to Task Mapping
460

Evaluation



Techniques to Task Mapping
461
10.10.
Collaborative
Games

Evaluation



Techniques to Task Mapping
462

Evaluation



Techniques to Task Mapping
463

Evaluation



Techniques to Task Mapping
464

Evaluation



Techniques to Task Mapping
465

Evaluation



Techniques to Task Mapping
466

Evaluation



Techniques to Task Mapping
467

Evaluation



Techniques to Task Mapping
468
10.33.
Prioritization

Evaluation



Techniques to Task Mapping
469

Evaluation



Techniques to Task Mapping
470

Evaluation



Techniques to Task Mapping
471

Evaluation



Techniques to Task Mapping
472

Evaluation



Contributors
473
Appendix C: Contributors
Body of Knowledge Committee
Content for this release was primarily developed by the Body of Knowledge
Committee:
• Angela M. Wick, CBAP, PMP, PBA
• Emily Iem, CBAP, PMP: Chairperson
• John M. A. Burns, MSc, BSc, CEng
• Joy Beatty, CBAP, PMI-PBA
• Masahiko Soh
• Matthew W. Leach, CBAP
• Peter Lefterov, CBAP
• Phil Vincent, CBAP, M. Comp. Sci., PMP
• Shane Hastie, CBAP, MIM, ICE-VM
• Julian Sammy
• Laura Paton, CBAP, MBA, PMP: Past Chairperson
• Tom Burke, CBAP, MS, CSPO
Body of Knowledge Operations Team
The following individuals partnered with and supported all stakeholders to
provide the framework for content development and delivery:
• Kevin Brennan, CBAP, OCEB, PMP, Executive Vice President,
Product Management and Development, IIBA: Sponsor
• Paul Stapleton, Standards and Publications Manager, IIBA: Editor
• Sandi Campbell, Project Manager, IIBA: Project Manager
Content Contributors
The following individuals contributed additional content used in this revision:
• Alberto Vasquez
• Ales Stempihar
• Ali Mazer, CBAP, MBA
• Andrew Guitarte, CBAP, DBA,
PMP
• Angie Perris, CBAP, MBA, PMP
• Anne Fomim, CBAP
• Beth Faris, CBAP
• Brian T. Hunt, CBAP, I.Eng.,
FInstLM



Contributors
474
• Cari J. Faanes-Blakey, CBAP, PMI-
PBA
• Charles Bozonier, CBAP
• Christina D. Harris, ITIL, BA
• Colleen S. Berish, AIT
• Dean J. Larson, CBAP
• Dena Loadwick, CBAP
• Edwina Simons, CBAP, MBA,
SSGB
• Ellan Kay Young
• Gagan Saxena
• Georgy Saveliev, CBAP
• Greg Geracie
• Heather Mylan-Mains, CBAP
• Inger Dickson, CBAP
• James (Jim) Baird, CMC
• James Taylor
• Janet Wood, CBAP
• Jason Andrew Oliver, CBAP,
MBA, CISSP
• Jason Frink, CBAP
• Jason Questor
• Jennifer Battan, CBAP
• Jennifer Swearingen
• Josh Jones, CBAP
• Dr. Joyce Statz
• Judith A. Haughton, CBAP, MBA
• Jules Prevost, CBAP
• Kelly Morrison Smith, MBA, MS
• Manish S. Nachnani, CBAP, PMP,
CSM
• Marcelo Neves, CBAP
• Maria Amuchastegui, CBAP,
CTFL, CSM
• Marsha B. Hughes, CBAP, PMP,
CSM
• Martin Schedlbauer, CBAP, PhD
• Maureen McVey, CBAP
• McNaughton Lebohang, CBAP,
BSc (Hons) CS, PMP
• Mike Crawford
• Mike Rosen
• Milena Komitska, PhD
• Muhammad Saad Rahman,
CBAP, M.Sc., PMP
• Neale Croutear-Foy, BA (Hons.),
FBCS, FInstLM
• Norman A. Thuswaldner, CBAP
• Paul Mulvey, CBAP
• Poonam Dhanwani
• Ricardo Pereira, CBAP
• Richard Larson, CBAP, PMP, PMI-
PBA
• Ronald G. Ross
• Sean P. Boylan, CBAP, MAppLing
• Sergio Conte
• Sherri L. Nowak, CBAP, MSM
• Silke Goodwin, CBAP
• Steven Blais, PMP, PBA
• Suneet K. Garg, CBAP, TOGAF 9,
CBPP
• Suzanne R. Burgess, CBAP
• Tharshan Sreetharan, CBAP, PMP,
MBA
• Thea Rasins
• Thomas (Tom) Barker, CBAP, PhD,
PMP
• Tina M. Underhill
• Victoria Cupet, CBAP, PMP, PMI-
PBA



Contributors
475
Expert Advisory and Review Group
The following industry experts generously provided IIBA® with advice and
guidance on the scope and content of version 3.0 of the BABOK® Guide during
its planning and development, and helped to shape the content and direction of
this release.
• Barbara A. Carkenord, CBAP,
PMI-PBA, PMP
• Bill Bigler, PhD
• Brian Cameron
• Chuck Walrad
• Elizabeth Larson, CBAP, PMP,
CSM
• Ellen Gottesdiener, SM, CPS
• Gladys S. W. Lam
• Greg Geracie
• James Robertson
• James Taylor
• Jason Questor
• Jeff Scott
• Kent J. McDonald
• Kitty Hass
• Linda R. Finley
• Mary Gorman, CBAP, CSM, PMI-
PBA
• Mike Rosen
• Peter H.M. Brooks, B.Sc., FSM
• Roger T. Burlton, P. Eng, CMC
• Ronald G. Ross
• Suzanne Robertson
• Whynde Kuehn
Practitioner Reviewers
The following individuals participated in the practitioner review of version 3.0,
and provided feedback used to help to shape the content and direction of the
Public Review Draft.
• Aljaž Prusnik, CBAP
• Angela Musa, CBAP
• Annette Brice, CBAP
• Ashok Kaushal
• Barbara J Monaco, CBAP
• Beth Gomolka, CBAP, PMP, CSP
• Carol R. Drew, CBAP
• Cei Sanderson, CSPO
• Charles Raj, CBAP, B. Com., FCA
• Chen-Kuang Yu
• Cherie Wagner
• Devendra Shrikant Upadhye,
CBAP
• Diana Cagle, CBAP, MBA
• Fabrício Laguna, CBAP, PMP,
MBA
• Geoffrey Griffin, CBAP
• Iavi Rotberg
• Jayesh Jain, CBAP, B.Sc., CSPO
• Joe Goss
• Joseph F. Ruffolo
• Karen Gras, CBAP
• Kathleen C. McGoey



Contributors
476
• laith Obeidat, CBAP
• Laura R. Walker, LSS
• Lenche Pandovska, CBAP
• Lily V. Dang, CBAP
• Lynn Parkin, CCBA
• Michael D. Western, CBAP
• Nicolae Crudu, CCBA
• Partha Pratim Das, PMP, CSM
• Richard Freeley, CBAP
• Robert Dyason
• Steven J. Gara, CBAP, MS
• Teri A. McIntyre, CBAP, CAPM,
MA
• Theodora Tonkovska
• Tolani J Hassan, ISEB
• Tricia K. Dreixler, CBAP
• Wayne Li
• Yoshinori Tanaka, CBAP
• Zoya Roytblat, CBAP
The following individuals also served as review team leads:
• Billie Johnson, CBAP, PBA, CSM
• Camille L. Spruill, CBAP, PMP, CSM
• Chaithanya Atthanti, CBAP
• Jeanette Moore-Loggins, CBAP, BA, MBA,
• Kimberley Byron, CBAP
• Peter Johnson, CBAP
• Tom Karasmanis
Agile Extension
Content for this version includes content from the Agile Extension to the BABOK®
Guide. IIBA® would like to thank the following contributors to the Agile Extension
to the BABOK® Guide.
• Ali Mazer
• Brian Hemker
• Carol Scalice
• Chris Matts
• David C. Cook
• David Morris
• Dennis Stevens
• Ellen Gottesdiener
• Kevin Brennan
• Luiz Claudio Parzianello
• Marsha Hughes
• Pascal Van Cauwenberghe
• Paul Stapleton, Editor
• Peter Gordon
• Shane Hastie
• Steve Erlank
• Susan Block



Contributors
477
Enterprise Business Analysis Extension Draft
Content for this version includes content from the Enterprise Business Analysis
Extension to the BABOK® Guide Draft. IIBA® would like to thank the following
contributors to the Enterprise Business Analysis Extension to the BABOK® Guide
Draft.
• Charlie Huai-Ling Ch'ng
• Dean Larson
• Jason Questor
• Joanne Dong
• Kevin Brennan
• Matt Northrup
• Neil Burton
• Nitza Dovenspike
• Phillip Quinn
• Ron Babin
Version 3.0 also includes content developed for previous versions of the BABOK®
Guide.
Other Significant Contributors
• Aminah Nailor, CBAP
• Annie Thomas, CPAP
• Rose Ha, CBAP
• Bernard Aschwanden, Publishing Smarter: Layout and Design
• Irena Duniskvaric, Publishing Smarter: Illustrations
• Lynda Sydney, Ignite Writing Services: Copy Editing
• SOS Design Inc.: Cover
• Vic Bhai, Technical Writer/Editor, IIBA: Technical Writing
Additional Thanks
IIBA® and the Body of Knowledge Committee would like to thank all those
practitioners of business analysis who have provided us with comments and
feedback over the years, as well as those who have provided us with feedback on
the Public Review Draft.
Version 2.0
Body of Knowledge Committee
Content for this release was primarily developed by the Body of Knowledge
Committee:
• Kevin Brennan, CBAP, OCEB, PMP, Vice President, Professional Development



Contributors
478
• Barbara A. Carkenord, MBA, CBAP
• Mary Gorman, CBAP
• Kathleen B. Hass, PMP
• Brenda Kerton, MA
• Elizabeth Larson, CBAP, PMP
• Richard Larson, CBAP, PMP
• Jason Questor
• Laura Paton, MBA, CBAP, PMP (Project Manager)
Content Contributors
The following individuals contributed additional content used in this revision:
• Tony Alderson
• James Baird
• Jake Calabrese, CBAP
• Bruce C. Chadbourne, PgMP,
PMP
• Karen Chandler
• Carrolynn Chang
• Richard Fox, CBAP
• Rosemary Hossenlopp
• Peter Gordon, CBAP
• Ellen Gottesdiener
• Monica Jain
• Cherifa Mansoura Liamani, PhD
• Karen Little
• Laura Markey
• Richard Martin
• Gillian McCleary
• William B. Murray
• Angie Perris, CBAP
• David Wright
The Graphics Team developed graphics and graphics standards:
• Carl Gosselin
• Perry McLeod, CBAP, PMP
• Alexandre Romanov
• Patricia Sandino
• Maggie Yang
Version 2.0 also includes content developed for previous versions of the BABOK®
Guide.
Expert Advisory and Review Group
The following industry experts generously provided IIBA® with advice and
guidance on the scope and content of version 2.0 of the BABOK® Guide during
its planning and development, and helped to shape the content and direction of
this release.
• Scott Ambler
• James Baird
• Kurt Bittner
• Rafael Dorantes



Contributors
479
• Robin F. Goldsmith, JD
• Ellen Gottesdiener
• Paul Harmon
• Dean Leffingwell
• Gladys S.W. Lam
• Kent J. McDonald
• Mark McGregor
• Meilir Page-Jones
• James Robertson
• Suzanne Robertson
• Ronald G. Ross
• David Ruble
• Steve Tockey
Practitioner Reviewers
The following individuals participated in the practitioner review of version 2.0,
and provided feedback used in the revision of the Public Review Draft:
• Sharon M. Aker
• Betty H. Baker, CBAP
• B. D. Barnes PhD, PE, PMP,
CSSBB
• Jennifer S. Battan, CBAP
• Subrahmanya Gupta Boda
• Craig W. Brown, MPM, CSM
• Cathy Brunsting
• Peter Burg, PMP
• Greg Busby, CBAP
• Diana Cagle, MBA, CBAP
• Duncan Cairns
• Bruce Chadbourne, PgMP, PMP
• Carrollynn Chang
• Patricia Chappell, CBAP, MBA
• Mark Cheek, PMP
• Huai-Ling Ch'ng, CBAP
• Desirée Purvis (née Chu), CBAP
• Pauline Chung
• Joseph Da Silva
• Nitza Dovenspike
• James Downey, PhD, PMP
• Tamer El-Tonsy, CISA, PRINCE2,
ITIL
• Steve Erlank, BSc, BCom (Hons)
• Margaret Gaino Ewing, MBA,
CBAP
• Stephanie Garwood, CBAP
• Joe Goss
• Karen Gras, CBAP
• Kwabby Gyasi
• Bob Hillier, PMP
• Billie Johnson, CBAP
• Peter Johnson, CBAP
• Hans Jonasson, CBAP, PMP
• Barbara Koenig
• Steven R. Koss, MBA
• Douglas Kowalczyk
• Robert Lam, MBA, ISP
• Richard Larson, CBAP, PMP
• Karen Little, CBAP
• Joy Matthews
• Perry McLeod, CBAP, PMP
• Holly M. Meyer
• Michael Mohammed



Contributors
480
• Brian Monson, PMP
• Nancy A. Murphy, PMP, CBAP
• Richard L. Neighbarger, CSQA,
CSQE
• Tony Newport, CBAP
• Samia Osman
• Cecilia Rathwell
• Suzanna Etheridge Rawlins, PMP
• Helen Ronnenbergh
• Zoya Roytblat
• Christopher Ryba
• Julian Sammy
• Keith Sarre, CBAP
• Laura Schleicher
• Fred Seip
• Thomas Slahetka, CBAP
• Warren Steger
• Leah Sturm, CBAP
• James M. Szuch
• Robin Tucker
• Krishna Vishwanath
• A. S. Umashankar
The following individuals also served as review team leads:
• Cathy Brunsting
• Patricia Chappell, CBAP, MBA
• Stephanie Garwood, CBAP
• Robert Lam, MBA, ISP
Version 1.6
Body of Knowledge Committee
• Kathleen Barret (President)
• Kevin Brennan, CBAP, PMP (Vice-President)
• Barbara Carkenord, MBA, CBAP
• Mary Gorman, CBAP
• Kathleen B. Hass, PMP
• Brenda Kerton
• Elizabeth Larson, CBAP, PMP
• Richard Larson, CBAP, PMP
• Dulce Oliveira
• Cleve Pillifant



Contributors
481
Contributors to Version 1.6
• Tony Alderson
• Finny Barker
• Neil Burton
• Karen Chandler
• Richard Fox, CBAP
• Rosemary Hossenlopp
• Peter Gordon, CBAP
• Monica Jain
• Peter Kovaks
• Chris Matts
• Laura Markey
• Patricia Martin
• Richard Martin
• Rosina Mete
• William Murray
• Harish Pathria
• Kathleen Person
• Tony Rice
• John Slater
• Mark Tracy
• Jacqueline Young
Reviewers of Version 1.6
• Sharon Aker
• Betty H. Baker, CBAP
• Jo Bennett
• Cathy Brunsting
• Carrollynn Chang, CBAP
• Patricia Chappell, CBAP, MBA
• Pauline Chung
• Joseph R. Czarnecki
• Stephanie Garwood, CBAP
• May Jim, CBAP
• Day Knez
• Barb Koenig
• Robert Lam
• Cherifa Mansoura Liamani, PhD
• Gillian McCleary
• Kelly Piechota
• Howard Podeswa
• Leslie Ponder
• Cecilia Rathwell
• Jennifer Rojek
• Keith Sarre, CBAP
• Jessica Gonzalez Solis
• Jim Subach
• Diane Talbot
• Krishna Vishwanath
• Marilyn Vogt
• Scott Witt



Contributors
482



Summary of Changes from BABOK® Guide v 2.0
483
Appendix D: Summary of Changes from BABOK®
Guide v 2.0
Overview
Version 3 of the BABOK® Guide has extensively revised, restructured, and
rewritten BABOK® Guide version 2.0. This summary of changes provides an
overview of where topics covered in version 2.0 may be found in version 3. This
summary is not a complete description of the changes, and in some cases the
scope of a task or technique has changed significantly at a lower level.
Introduction
Business Analysis
The definition of this primary concept has been updated to align with other
changes in the BABOK® Guide, specifically the Business Analysis Core Concept
Model™ (BACCM™).
Business Analysis Key Concepts
Business Analysis Core Concept Model™ ( BACCM™ ) (NEW)
A model comprised of six terms that have a common meaning to all business
analysis practitioners and helps them discuss business analysis and its
relationships in common terminology.
Requirements and Design (NEW)
This section describes the distinction between and overlap of two key business
analysis concepts: requirements and design.



Summary of Changes from BABOK® Guide v 2.0
484
Knowledge Areas
Business Analysis Planning and Monitoring
The focus and name of this knowledge area remains the same for version 3.
Some tasks were renamed, one new task was added and some elements were
moved around. Version 3 continues to address the business analyst's role in
defining the business analysis work and defining the approach for the initiative.
Elicitation (Version 2.0 name) is now
Elicitation and Collaboration (Version 3 name)
The focus of this knowledge area remains similar but has expanded to include
communication topics from version 2.0 and the new topic of collaboration.
In addition, the simpler content from version 2.0 was expanded to provide more
guidance for practitioners. Also, an explicit reference to unplanned elicitation is
made to acknowledge the informal elicitation that can occur during conversation.
Business analysis information is also referenced throughout rather than just
requirements as the object of elicitation.
2.0 Task: Business Analysis Planning
and Monitoring
3.0 Task: Business Analysis Planning
and Monitoring
2.1 Plan Business Analysis Approach
Prioritization and Change
Management content shifted to 3.3
Plan Business Analysis Governance
3.1 Plan Business Analysis Approach
2.2 Conduct Stakeholder Analysis
3.2 Plan Stakeholder Engagement
2.3 Plan Business Analysis Activities
3.1 Plan Business Analysis Approach
2.4 Plan Business Analysis
Communication
3.2 Plan Stakeholder Engagement
2.5 Plan Requirements Management
Process
Prioritization and Change
Management content shifted to 3.3
Plan Business Analysis Governance
3.4 Plan Business Analysis Information
Management
2.6 Manage Business Analysis
Performance
3.5 Identify Business Analysis
Performance Improvements
2.0 Task: Elicitation
3.0 Task: Elicitation and Collaboration
3.1 Prepare for Elicitation
4.1 Prepare for Elicitation
3.2 Conduct Elicitation Activity
4.2 Conduct Elicitation



Summary of Changes from BABOK® Guide v 2.0
485
Requirements Management and Communication (Version 2.0 name)
is now Requirements Life Cycle Management (Version 3 name)
Requirements Life Cycle Management was determined to be a more appropriate
name for this knowledge area in order to emphasize that requirements have their
own life cycle and that requirements management is an ongoing activity.
Communication activities were shifted from this knowledge area to the Elicitation
and Collaboration knowledge area.
3.4 Confirm Elicitation Results
4.3 Confirm Elicitation Results
3.3 Document Elicitation Results
4.4 Communicate Business Analysis
Information
n/a
4.5 Manage Stakeholder
Collaboration
2.0 Task: Requirements Management
and Communication
3.0 Task: Requirements Life Cycle
Management
4.1 Manage Solution Scope and
Requirements
Solution Scope Management is
addressed within 5.1 Trace
Requirements. Conflict and Issue
Management and Presenting
Requirements for Review are
addressed in 5.5 Approve
Requirements.
5.1 Trace Requirements
5.5 Approve Requirements
4.2 Manage Requirements Traceability
Relationships and Configuration
Management are addressed in 5.1
Trace Requirements. Impact Analysis is
addressed in 5.4 Assess Requirements
Changes.
5.1 Trace Requirements
5.4 Assess Requirements Changes
4.3 Maintain Requirements for Reuse
5.2 Maintain Requirements
4.4 Prepare Requirements Package
4.4 Communicate Business Analysis
Information
4.5 Communicate Requirements
4.4 Communicate Business Analysis
Information



Summary of Changes from BABOK® Guide v 2.0
486
Enterprise Analysis (Version 2.0 name) is now
Strategy Analysis (Version 3 name)
This knowledge area has taken on a new name and expanded purpose.
Enterprise Analysis focused on the upfront work the business analyst conducted
at the start of a project. Strategy Analysis is broader and includes the work the
business analyst conducts to understand the current state of the business, to
define the desired future state, to develop a change strategy to achieve the
desired business outcomes and to assess the risks inherent in the change strategy.
5.3 Prioritize Requirements
Moved from 6.1 Prioritize
Requirements (v2.0)
N/A
5.5 Approve Requirements
New task which includes the concepts
from the v2 Elements Conflict and
Issue Management , Presenting
Requirements for Review and
Approval from the v2 Task Manage
Solution Scope and Requirements.
2.0 Task: Enterprise Analysis
3.0 Task: Strategy Analysis
5.1 Define Business Need
Business Problem or Opportunity is
addressed in 6.1 Analyze Current
State. Business Goals and Objectives
and Desired Outcome are addressed in
6.2 Define Future State.
6.1 Analyze Current State, 6.2 Define
Future State
5.2 Assess Capability Gaps
Current Capability Analysis is
addressed in 6.1 Analyze Current
State. Assessment of New Capability
Requirements and Assumptions are
addressed in 6.2 Define Future State.
6.1 Analyze Current State, 6.2 Define
Future State, 6.4 Define Change
Strategy
Define Change Strategy includes a
Gap Analysis which was not explicitly
identified in 5.2 Assess Capability
Gaps but was the intent of the task.
5.3 Determine Solution Approach
Alternative Generation and
Assumptions and Constraints are
addressed in 6.2 Define Future State.
Ranking and Selection of Approaches
is addressed in 7.5 Define Design
Options and 7.6 Analyze Potential
Value and Recommend Solution.
6.2 Define Future State, 7.5 Define
Design Options (v3 Requirements
Analysis and Design Definition
knowledge area), 7.6 Analyze
Potential Value and Recommend
Solution (v3 Requirements Analysis
and Design Definition knowledge
area)



Summary of Changes from BABOK® Guide v 2.0
487
Requirements Analysis (Version 2.0 name) is now
Requirements Analysis and Design Definition (Version 3 name)
This knowledge area was renamed to accommodate expanded content.
Version 3 now addresses the topic of design and explains where business analysts
have involvement with design activities. Requirements Analysis and Design
Definition also incorporates some of the tasks from the version 2.0 Solution
Assessment and Validation. Activities involved with the proposed solution
assessment—before any construction of a solution; whether in part or in whole—
are now part of this Requirements Analysis and Design Definition.
5.4 Define Solution Scope
6.4 Define Change Strategy
5.5 Define Business Case
7.6 Analyze Potential Value and
Recommend Solution (Requirements
Analysis and Design Definition
knowledge area), 10.7 Business Cases
(Technique)
2.0 Task: Requirements Analysis
3.0 Task: Requirements Analysis and
Design Definition
6.1 Prioritize Requirements
5.3 Prioritize Requirements (v3
Requirements Life Cycle Management
knowledge area)
6.2 Organize Requirements
7.4 Define Requirements Architecture
6.3 Specify and Model Requirements
7.1 Specify and Model Requirements
6.4 Define Assumptions and
Constraints
Assumptions and Business Constraints
are addressed in 6.2 Define Future
State. Technical Constraints are
addressed in 7.6 Analyze Potential
Value and Recommend Solution
6.2 Define Future State (v3 Strategy
Analysis knowledge area) and 7.6
Analyze Potential Value and
Recommend Solution
6.5 Verify Requirements
7.2 Verify Requirements
6.6 Validate Requirements
7.3 Validate Requirements



Summary of Changes from BABOK® Guide v 2.0
488
Solution Assessment and Validation (Version 2.0 name) is now
Solution Evaluation (Version 3 name)
The version 3 knowledge area provides less focus on implementing a solution and
more focus on evaluating solutions.
The knowledge area includes content on evaluating whether value is being
delivered by a solution and discusses the business analyst's role in assessing what
is hindering an organization from receiving full value from a solution.
N/A
7.5 Define Design Options
New task in Requirements Analysis
and Design Definition which
incorporates 5.3 Determine Solution
Approach (v2.0 Enterprise Analysis
knowledge area), 7.1 Assess Proposed
Solution (v2.0 Solution Assessment
and Validation knowledge area), and
7.2 Allocate Requirements (v2.0
Solution Assessment and Validation
knowledge area)
N/A
7.6 Analyze Potential Value and
Recommend Solution
New task in Requirements Analysis
and Design Definition which
incorporates 5.5 Define Business Case
(v2.0 Enterprise Analysis knowledge
area) and 7.1 Assess Proposed
Solution (v2.0 Solution Assessment
and Validation knowledge area)
2.0 Task: Solution Assessment and
Validation
3.0 Task: Solution Evaluation
7.1 Assess Proposed Solution
7.5 Define Design Options and 7.6
Analyze Potential Value and
Recommend Solution (v3
Requirements Analysis and Design
Definition knowledge area)
7.2 Allocate Requirements
7.5 Define Design Options (v3
Requirements Analysis and Design
Definition knowledge area)
7.3 Assess Organizational Readiness
6.4 Define Change Strategy (v3
Strategy Analysis knowledge area)



Summary of Changes from BABOK® Guide v 2.0
489
Underlying Competencies
Analytical Thinking and Problem Solving
• NEW—Conceptual Thinking
• NEW—Visual Thinking
Behavioural Characteristics
• Ethics—removed
• Personal Organization—renamed and expanded Organization and Time
Management
• NEW—Personal Accountability
• NEW—Adaptability
Business Knowledge
• Business Principles and Practices—renamed Business Acumen
• NEW—Methodology Knowledge
7.4 Define Transition Requirements
6.4 Define Change Strategy (v3
Strategy Analysis knowledge area),
2.3 Requirements Classification
Schema
7.5 Validate Solution
8.3 Assess Solution Limitations
7.6 Evaluate Solution Performance
8.5 Recommend Actions to Increase
Solution Value
N/A
8.1 Measure Solution Performance
New task that incorporates defining
solution performance measures and
measuring the actual performance
N/A
8.2 Analyze Performance Measures
New task that focuses on comparing
the actual value (solution
performance) against the expected
value
N/A
8.4 Assess Enterprise Limitations
New task that identifies what, external
to the solution, may be preventing it
from delivering its expected value



Summary of Changes from BABOK® Guide v 2.0
490
Communication Skills
• Oral Communications—renamed Verbal Communication
• Teaching—moved to Interaction Skills
• NEW—Non-verbal Communication
• NEW—Listening
Interaction Skills
• Facilitation and Negotiation—split competencies and renamed Facilitation
• NEW—Negotiation and Conflict Resolution
Software Applications (Version 2.0 name) is now
Tools and Technology (Version 3 name)
• General-Purpose Applications—renamed Office Productivity Tools and
Technology
• Specialized Applications—renamed Business Analysis Tools and Technology
• NEW—Communication Tools and Technology
Techniques
Name or Focus Change
• Benchmarking and Market Analysis (v2.0 Benchmarking)
• Data Dictionary (v2.0 Data Dictionary and Glossary)
• Glossary (v2.0 Data Dictionary and Glossary)
• Reviews (v2.0 Structured Walkthrough)
• Risk Analysis and Management (v2.0 Risk Analysis)
• Use Cases and Scenarios (v2.0 Scenarios and Use Cases)
• User Stories
• Workshops (v2.0 Requirements Workshop)
New Techniques
• Backlog Management
• Balanced Scorecard
• Business Capability Analysis



Summary of Changes from BABOK® Guide v 2.0
491
• Business Case
• Business Model Canvas
• Collaborative Games
• Concept Modelling
• Data Mining
• Decision Modelling
• Financial Analysis
• Mind Mapping
• Prioritization
• Process Analysis
• Roles and Permissions Matrix
• Stakeholder List, Map, or Personas
Perspectives (NEW)
Perspectives are used within business analysis work to provide focus to tasks and
techniques specific to the context of the initiative.
Most initiatives are likely to engage one or more perspectives. The perspectives
included in the BABOK® Guide are:
• Agile,
• Business Intelligence,
• Information Technology,
• Business Architecture, and
• Business Process Management.
These perspectives do not presume to represent all the possible perspectives from
which business analysis is practiced. The perspectives discussed in the BABOK®
Guide represent some of the more common views of business analysis at the time
of writing.
Perspectives are not mutually exclusive, in that a given initiative might employ
more than one perspective.



Summary of Changes from BABOK® Guide v 2.0
492



493
Index
A
Acceptance and Evaluation Criteria 217
Access to Information, Improve 154
Adaptability 197
Adaptability and flexibility 376
Adaptive 400
Agile Extension to the BABOK 368, 370,
372, 375, 376, 377
Agile Perspective 368
Agile Team Leader 372
Alternatives, Define 262
Analytical Thinking and Problem Solving 188
Analytics, Prescriptive 386
Analyze
Current State 100, 103
Performance Measures 164, 170
Potential Value and Recommend
Solution 134, 157
Approve Requirements 76, 95
Architecture
Business 408
Requirements 134, 148
Solution 385
Assess
Enterprise Limitations 164, 177
Requirements Changes 76, 91
Risks 100, 120
Solution Limitations 164, 173
Assumptions, Risks, and Constraints 235
Avoid Waste 184
B
Backlog Management 220
Balanced Scorecard 223
Behavioural Characteristics 194
Benchmarking and Market Analysis 226
Brainstorming 227
Business Acumen 199
Business Analysis Core Concept Model™ 11,
12, 22, 54, 76, 101, 134, 164
Business Analysis Information,
Communicate 54, 67



Index
494
Business Analysis Key Concepts 3, 11
Business Analysis Performance
Assessment 29
Business Analysis Performance
Improvements, Identify 22, 47
Business Analysis Planning and Monitoring 4
Business Analysis Planning
and Monitoring 21
Business Analysis Tools and Technology 213
Business Analytics Requirements 385
Business Architecture Perspective 408
Business Capability Analysis 230
Business Cases 29, 234
Business Intelligence Perspective 381
Business Knowledge 199
Business Knowledge Models 267
Business Model Canvas 236
Business Outcomes 284
Business Policies 29
Business Process 284
Business Process Coverage 384
Business Process Management
Perspective 424
Business Process Model and Notation
(BPMN) 319
Business Process Re-engineering 426
Business Requirements 16
Business Rules Analysis 240
Business Unit 284
C
Capabilities, Identify 154, 184
Capability 138
Cause-Effect diagrams 285
Change 22, 55, 77, 101, 135, 165
Change Strategy, Define 100, 124
Collaboration
Communication 376
Games 243
Group 70
Knowledge Management Tools 212
Manage Stakeholders 54, 71
Collaboration and Knowledge Management
Tools 212
Collaborative Games 243
Collection, Data 335
Communicate Business Analysis
Information 54, 67
Communication
Skills 203
Tools 212
Tools and Technology 215
Verbal 204
Written 205
Communication and Collaboration 376
Communication, Non-Verbal 205
Component diagram 285
Component, Solution 284
Concept Modelling 245
Conceptual Data Model 256
Conceptual Thinking 192
Conduct Elicitation 54, 61
Confirm Elicitation Results 54, 65
Conflict Resolution 210
Constraints 235
Constraints on the Solution 160
Context 22, 55, 77, 101, 135, 165
Continuous improvement 376
Cost and time estimates 39
Creative Thinking 188
Credible 298
Current State, Analyze 100, 103



Index
495
D
Data
Collection 335
Conceptual Model 256
Dictionary 247
Flow Diagrams 250, 319, 391
Mining 253
Modelling 256
Structured 387
Unstructured 387
Data Dictionary 385
Data Model
Logical 257
Physical 257
Data Models
Logical 391
Physical 391
Decision
Analysis 261
Criteria 262
Model and Notation 285
Modelling 265
Models 384, 391
Decision Making 189
Decision Nodes 263
Decision Point 319
Decision Trees 285
Decisions 267, 285
Decomposition, Functional 283
Define
Alternatives 262
Change Strategy 100, 124
Design Options 152
Future State 100, 110
Problem Statement 262
Requirements Architecture 134, 148
Solution Options 134
Demand-driven 387
Dependencies 88
Dependencies between Requirements 160
Descriptive Analytics 386
Designing 284, 424
Diagrams
Data Flow 250, 319, 391
Use Case 285
Dictionary, Data 247, 385
Discovery, Substantial 426
Document Analysis 30, 269
Documentation, Informal 69
Domain Subject Matter Expert 17
E
Efficiencies, Increase 154
Elements 158
Elicitation and Collaboration 4, 53
Elicitation, Prepare for 54, 56
Eliminate Redundancy 184
End User 17
Escalation Matrix 295
Estimating and Forecasting 284
Estimation 271
Ethics 194
Evaluate Alternatives 262
Evaluation, Solution 5, 163
Execution and Monitoring 424
Expected Benefits 276
Experimentation 403
Experiments 61
Expert Judgment 29, 273
External Stakeholders 372
F
Facilitation 207
Facilitator 364
Feasibility 235
Feasible 143
Financial 238
Financial Analysis 274
Financial Analysis and Value Assessment 235
Flexibility and adaptability 376
Flow diagrams 285
Flowcharts 319



Index
496
Focus Groups 279
Forecasting and Estimating 284
Form Study Prototype 324
Formal Documentation 69
Formal Walkthrough 327
Frequency 168
Functional
Decomposition 283
Prototype 325
Requirements 16
Future State, Define 100, 110
G
Glossary 286
Group Collaboration 70
Guide 416
I
IDEF 319
Identify Additional Capabilities 154, 184
Identify Business Analysis Performance
Improvements 22, 47
IGOE 319
Impact, Solution 394
Implementation Subject Matter Expert 17
Implementation Team 428
Improve Access to Information 154
Increase Efficiencies 154
Industry Knowledge 200
Industry Structure 107
Influencing and Leadership 208
Informal Documentation 69
Informal Walkthrough 327
Information Technology Perspective 394
Information, Improve Access to 154
Input, Guide, Output, Enabler (IGOE)
Diagrams 319
Inputs 142, 157
Integrated DEFinition (IDEF) notation 319
Interaction Skills 207
Interface Analysis 287
Interview 290
Interview, Unstructured 290
Interviews 290
Investigation 402
Item Tracking 294
K
Key Concepts 4
Key Performance Indicators 297
Key Terms 11, 14
Kinesthetic 190
Knowledge, Industry 200
KPIs 297
L
Leadership and Influencing 208
Learning 190
Lessons Learned 296
Listening 206
Localization 303
Logical Data Model 257, 385
Logical Data Models 391
M
Maintain Requirements 76, 83
Maintainability 303
Manage Stakeholder Collaboration 54, 71
Management, Risk Analysis 329
Market-oriented 309
Matrices 138
Matrix Model 310
Measure Solution Performance 164, 166



Index
497
Measures
Qualitative 168
Quantitative 168
Measuring and Managing 284
Methodology Knowledge 202
Metrics and Key Performance Indicators
(KPIs) 297
Mind Mapping 299
Mind Maps 285
Mining, Data 253
Model
Conceptual 256
Logical Data 385
Modelling 348
Conceptual 245
Data 256
Decision 265
Process 318
Scope 338
Workflow 325
Models, Decision 384, 391
Monitoring and Execution 424
N
Need 22, 55, 77, 101, 135, 165
Negotiation and Conflict Resolution 210
Net Benefits 276
Non-Functional Requirements 16
Non-Functional Requirements Analysis 302
Non-Verbal Communication 205
O
Observation 305
Office Productivity Tools and
Technology 212
Onion Diagram 345
Operational improvement, Facilitate 395
Operational Releases 163
Operational Support 18
Opportunity Cost 185
Optimization 284
Optimizing 424
Options, Define 152
Organization
History 273
Knowledge 201
Organization and Time Management 196
Organizational
Change 184
Maturity 394
Modelling 308
Support 49
Unit 310
P
Paper Prototyping 325
Parametric Estimation 272
Performance Assessment, Business
Analysis 29
Performance Efficiency 303
Performance Improvement, Business
Analysis 22, 47
Performance Measures, Analyze 164, 170
Personal Accountability 195
Perspectives 367
PERT 272
Physical Data Model 257
Physical Data Models 391
Pilot or Beta releases 163
Plan Business Analysis
Approach 21, 24
Governance 21, 37
Information Management 21, 42
Plan Stakeholder Engagement 21, 31
Policy Compliance 89
Political and Regulatory Environment 107
Potential Value and Recommend Solution,
Analyze 134, 157
Predictive 254, 400



Index
498
Predictive Analytics 386
Prepare for Elicitation 54, 56
Prescriptive Analytics 386
Presentation Programs 212
Presentation Software 212
Presentations 69
Prioritization 311
Prioritize Requirements 76, 86
Prioritized 143
Priority 39, 45, 294
Proactive Analysis 335
Problem Solving 191
Problem Statement Definition 335
Problem Statement, Define 262
Process Analysis 314
Process Analyst/Designer 429
Process Architect 428
Process Benchmarking 426
Process Modeller 429
Process Modelling 318
Process Owner 428
Process Participants 428
Productivity Tools and Technology 212
Project Manager 18, 428
Proof of Concept 324
Proof of Principle 324
Proofs of Concept 163
Prototype
Functional 324, 325
Usability 325
Visual 325
Prototypes 163
Evolutionary 324
Throw-away 324
Prototyping 323, 325
Prototyping, Paper 325
Q
Qualitative Measures 168
Quality of service requirements 16
Quantifiable 298
Quantitative Measures 168
Questionnaire 350
R
Reactive Analysis 335
Recommend Actions to Increase Solution
Value 164, 182
Regulator 18, 428
Regulatory and Political Environment 107
Regulatory Compliance 89
Requirements Analysis and Design
Definition 5, 133
Requirements and Designs 11, 19
Requirements Architecture, Define 134, 148
Requirements Classification Schema 11, 16
Requirements Life Cycle Management 4, 75
Requirements, Functional 16
Review
Single Issue 327
Technical 327
Reviews 326
Risk 88
Risk Analysis and Management 329
Risk-aversion 122
Risks 39, 46, 235
Risk-seeking 122
Roles and Permissions Matrix 333
ROM 272
Root Cause Analysis 335
Rough Order of Magnitude (ROM) 272
S
Scalability 303
Scenario driven 408
Scenarios 356
Scope Modelling 338



Index
499
Scope of Change 338
Scope of Control 338
Scope of Need 338
Scope of Solution 338
Separation of Concerns 408
Sequence Diagrams 341
Service Level Agreements 303
Simulation 325
Simulations 403
Single Issue Review 327
SIPOC 319
Solution 22, 55, 77, 101, 135, 165
Solution Architecture 385
Solution Component 284
Solution Evaluation 5, 163
Solution Impact 394
Solution Knowledge 202
Solution Options, Define 134
Solution Requirements 16
Solution Value, Recommend Actions to
Increase 164, 182
Specify and Model Requirements 134, 136
Sponsor 18, 364
Stakeholder 22, 55, 77, 101, 135, 165
Stakeholder Engagement Approach 29
Stakeholder Engagement Plan 21, 31
Stakeholder List 344
Stakeholder List, Map, or Personas 344
Stakeholder Map 344
Stakeholder Matrix 345
Stakeholder Personas 344
Stakeholder Requirements 16
Stakeholders, External 372
State 348
State Modelling 348
State Transition Diagrams 285
Storyboarding 325
Strategy Analysis 4, 99
Structured 290
Structured Data 387
Structured Interview 290
Subject Matter Expert
Domain 17
Implementation 17
Substantial Discovery 426
Sunk Cost 185
Supplier 18
Supplier-Consumer 340
Suppliers 107
Supply-driven 387
Survey 350
Survey or Questionnaire 350
SWOT Analysis 353
Systems Thinking 191
T
Teaching 210
Team Implementation 428
Team Review 327
Teamwork 209
Technical Review 327
Testable 143
Tester 19
Thinking, Visual 193
Time Management and Organization 196
Time Sensitivity 88
Timelines 281
Timeliness 49
Timing 168
Tools and Technology 211
Tools and Technology, Productivity 212
Total Annual benefits 276
Total Costs 276
Trace Requirements 76, 79
Transformation Rules 385
Transition Requirements 16
Tree Diagrams 285
Trustworthiness 195



Index
500
Trustworthy 298
Trustworthy and Credible 298
U
Unstructured Data 387
Unstructured Interview 290
Usability 303
Usability Prototype 325
Use Case Diagrams 285
Use Cases 356
Use Cases and Scenarios 356
User Stories 359
V
Validate Requirements 134, 144
Value 22, 55, 77, 101, 135, 165
Value Assessment and Financial Analysis 235
Value Stream Analysis 319
Value Stream Mapping 319
Vendor Assessment 361
Verbal Communication 204
Verify Requirements 134, 141
Visual 190
Visual Prototype 325
Visual Thinking 193
VSM 319
W
Walkthrough, Informal 327
Word Processing Programs 212
Workflow Modelling 325
Workshops 363
Written Communication 205






502
About IIBA®
International Institute of Business Analysis™ (IIBA®) is the
independent non-profit professional association formed in 2003
to serve the growing field of business analysis.
As the voice of the business analysis community, IIBA supports
the recognition of the profession, and works to maintain
standards for the practice and certification. Through a global
network, IIBA connects Members, Chapters, Corporations and
Partners around the world to advance the business analysis
profession by uniting a community of professionals to create
better business outcomes.
For individuals working in a broad range of roles – business
analysis, systems analysis, requirements analysis, project
management, consulting, process improvement and more –
IIBA provides the resources to help you enhance your career and
advance your career path.
As an IIBA Member, business analysis professionals gain
extensive access to insight, knowledge and support. IIBA can
help you create a professional career path through the ability to
grow a variety of skills. Member benefits include:
• Access to essential tools and knowledge, including
webinars, quick tips, best practices, online library and
newsletters.
• Connections to a global network of learning and
collaboration.
• Opportunity to engage a community of professionals
and grow at a local level through your IIBA Chapter.
• Support in achieving success, recognition and
opportunity in your career.
• Free access to PDF and eBook editions of the BABOK®
Guide.
• Discounted fee for IIBA certification exam.
You can gain even greater value through participation in your
local IIBA Chapter. By joining a Chapter, you can also access
additional tools and resources and you will have the opportunity
to participate in events, study groups and general interest
groups.
To become an IIBA member, visit iiba.org/Membership. To find
your local Chapter, visit iiba.org/Chapter.
IIBA Certifications
IIBA certifications are the globally recognized standard for
business analysis.
Many certifications in the business analysis space cover the core
skills of requirements engineering and management, but IIBA
certifications go beyond those basics to deliver unique value.
IIBA programs address the need for business analysis
professionals to link strategy to execution, ensure long-term
benefits are realized from a change, and integrate innovation
and process improvement with technology change. This means
that professionals certified by IIBA are able to contribute to the
success of the entire business, not just help a project deliver on
time, on scope, and on budget.
IIBA certification offers many benefits, including:
• Establishment and implementation of best practices in
business analysis by individuals acknowledged as
knowledgeable and skilled.
• More reliable, higher quality results produced with
increased efficiency and consistency.
• Recognition as a business analysis professional to
colleagues, clients and business stakeholders.
• Professional development and recognition for
experienced business analysis professionals.
• Demonstrated commitment to the field of business
analysis, which is increasingly recognized as vital to all
areas of business.






STRATEGY
REQUIREMENTS
SOLUTIONS
A Guide to the Business Analysis Body of Knowledge®
(BABOK® Guide) is the only globally recognized
standard of practice for business analysis. Developed
through a rigorous consensus-driven standards
process, the BABOK® Guide incorporates the collective
wisdom and experience of experts in the fi eld from
around the world.
Previous editions have guided hundreds of thousands
of professionals in their work, and it has been adopted
by hundreds of enterprises as the basis of their
business analysis practice.
This latest version of the guide extends its scope
beyond business analysis in projects to address agile
development, business process management, business
intelligence, and business architecture.
This thoroughly revised and updated version includes:
• A concept model that unifi es ideas and terminology
across business analysis disciplines.
• Restructured knowledge areas to support business
analysis at every level from small tactical initiatives to
major business transformations.
• Five perspectives covering the most prominent
business analysis disciplines and demonstrating how
to apply the knowledge areas in different situations.
• Coverage of new business analysis techniques that
have gained wide acceptance in the community.
• Updated and revised content in every knowledge
area and more!
Whether you are considering starting a career
in business analysis, or you are an experienced
professional in the fi eld, the BABOK® Guide is your key
resource to help you and your stakeholders discover
opportunities for business success, deliver successful
organizational change, and create business value.

## Solution
### Acceptance

and Evaluation
Criteria

## Solution
### Approve

Requirements

Requirements

Requirements

Requirements

Requirements

## Solution
### Define Future

State

State

State

State

State

State

State

State

State

State

State

State

State

State

State

State

State

State

State

State

State

State

State

## Solution
### Specify and

Model
Requirements

Model
Requirements

Model
Requirements

Model
Requirements

Model
Requirements

Model
Requirements

Model
Requirements

Model
Requirements

Model
Requirements

Model
Requirements

Model
Requirements

Model
Requirements

Model
Requirements

Model
Requirements

Model
Requirements

Model
Requirements

Model
Requirements

Model
Requirements

Model
Requirements
10.43.
Stakeholder List,
Map, or Personas

Model
Requirements

Model
Requirements

Model
Requirements

Model
Requirements

## Solution
### Verify

Requirements

Requirements

Requirements

Requirements

## Solution
### Validate

Requirements

Requirements

Requirements

Requirements

Requirements

Requirements

Requirements

## Solution
### Analyze

Potential Value and
Recommend
Solution

Performance
Measures

Potential Value and
Recommend
Solution

Current State

Performance
Measures

Potential Value and
Recommend
Solution

Current State

Current State

Potential Value and
Recommend
Solution

Current State

Potential Value and
Recommend
Solution

Current State

Current State

Performance
Measures

Potential Value and
Recommend
Solution

Current State

Potential Value and
Recommend
Solution

Current State

Potential Value and
Recommend
Solution

Current State

Potential Value and
Recommend
Solution

Current State

Current State

Potential Value and
Recommend
Solution

Performance
Measures

Current State

Current State

Current State

Potential Value and
Recommend
Solution

Performance
Measures

Current State

Current State

Performance
Measures

Current State

Current State

Current State

Potential Value and
Recommend
Solution

Performance
Measures

Current State

Performance
Measures

Current State

Current State

Potential Value and
Recommend
Solution

Performance
Measures

Current State

Potential Value and
Recommend
Solution

Current State

Current State

Potential Value and
Recommend
Solution

## Solution
### Measure

Solution
Performance

Solution
Performance

Solution
Performance

Solution
Performance

Solution
Performance

Solution
Performance

Solution
Performance

Solution
Performance
10.31.
Observation

Solution
Performance

Solution
Performance

Solution
Performance

Solution
Performance

Solution
Performance
10.50.
Workshops

## Solution
### Assess Solution

Limitations

Limitations

Limitations

Limitations

Limitations

Limitations

Limitations

Limitations

Limitations

Limitations

Limitations

## Solution
### Backlog

Management

## Solution
### Prioritize

Requirements

Requirements

Requirements

Requirements

Requirements

Requirements

Requirements

Requirements

Requirements

Requirements

## Solution
### Balanced

Scorecard

## Solution
### Define Change

Strategy



Techniques to Task Mapping
459
10.4.
Benchmarking
and Market
Analysis

Strategy

Strategy

Strategy

Strategy

Strategy

Strategy

Strategy

Strategy

Strategy

Strategy

Strategy

Strategy

Strategy

Strategy

Strategy

Strategy

Strategy

Strategy

Strategy

## Solution
### Conduct

Elicitation

Elicitation

Elicitation

Elicitation

Elicitation

Elicitation

Elicitation

Elicitation

Elicitation

Elicitation

Elicitation

Elicitation

Elicitation

Elicitation

Elicitation

Elicitation

Elicitation

Elicitation

## Solution
### Define Design

Options

Options

Options

Options

Options

Options

Options

Options

Options

Options

## Solution
### Assess

Enterprise
Limitations
10.5.
Brainstorming

Enterprise
Limitations

Requirements
Changes

Requirements
Changes

Enterprise
Limitations

Requirements
Changes

Enterprise
Limitations

Requirements
Changes

Enterprise
Limitations

Requirements
Changes

Requirements
Changes

Requirements
Changes

Requirements
Changes

Enterprise
Limitations

Requirements
Changes

Enterprise
Limitations

Enterprise
Limitations

Enterprise
Limitations
10.32.
Organizational
Modelling

Enterprise
Limitations

Enterprise
Limitations

Enterprise
Limitations
10.36.
Prototyping

Requirements
Changes

Enterprise
Limitations

Enterprise
Limitations

Enterprise
Limitations

Enterprise
Limitations

Enterprise
Limitations

Requirements
Changes

Enterprise
Limitations

## Solution
### Plan Business

Analysis Approach

Analysis
Governance

Analysis
Information
Management

Analysis Approach

Analysis Approach

Analysis
Governance

Analysis Approach

Analysis Approach

Analysis Approach

Analysis
Governance

Analysis
Information
Management

Analysis Approach

Analysis
Governance

Analysis
Information
Management

Analysis Approach

Analysis
Governance

Analysis
Information
Management

Analysis
Information
Management

Analysis
Governance

Analysis Approach

Analysis
Governance

Analysis
Information
Management

Analysis
Governance

Analysis
Governance

Analysis
Information
Management

Analysis Approach

Analysis
Governance

Analysis
Information
Management

## Solution
### Plan

Stakeholder
Engagement

Stakeholder
Engagement

Stakeholder
Engagement

Stakeholder
Engagement

Stakeholder
Engagement

Stakeholder
Engagement

Stakeholder
Engagement

Stakeholder
Engagement

Stakeholder
Engagement

Stakeholder
Engagement

Stakeholder
Engagement

Stakeholder
Engagement

Stakeholder
Engagement

## Solution
### Identify

Business Analysis
Performance
Improvements

Business Analysis
Performance
Improvements

Business Analysis
Performance
Improvements

Business Analysis
Performance
Improvements

Business Analysis
Performance
Improvements

Business Analysis
Performance
Improvements

Business Analysis
Performance
Improvements

Business Analysis
Performance
Improvements

Business Analysis
Performance
Improvements

Business Analysis
Performance
Improvements

Business Analysis
Performance
Improvements

Business Analysis
Performance
Improvements

Business Analysis
Performance
Improvements

## Solution
### Prepare for

Elicitation

Elicitation

Elicitation

Elicitation

Elicitation

Elicitation

Elicitation

Elicitation

## Solution
### Business

Capability
Analysis

Cases

Model Canvas

Rules Analysis

## Solution
### Maintain

Requirements

Requirements

Requirements

Requirements

Requirements

Requirements

Requirements

Requirements

## Solution
### Manage

Stakeholder
Collaboration

Stakeholder
Collaboration

Stakeholder
Collaboration

Stakeholder
Collaboration

## Solution
### Concept

Modelling

## Solution
### Data

Dictionary

Mining

Modelling

## Solution
### Data Flow

Diagrams

## Solution
### Recommend

Actions to Increase
Solution Value

Actions to Increase
Solution Value

Actions to Increase
Solution Value

Actions to Increase
Solution Value

Actions to Increase
Solution Value

Actions to Increase
Solution Value

Actions to Increase
Solution Value

Actions to Increase
Solution Value

Actions to Increase
Solution Value

## Solution
### Define

Requirements
Architecture

Requirements
Architecture

Requirements
Architecture

Requirements
Architecture

Requirements
Architecture

Requirements
Architecture

## Solution
### Decision

Analysis

Modelling

## Solution
### Document

Analysis

## Solution
### Confirm

Elicitation Results

Elicitation Results

Elicitation Results

Elicitation Results

## Solution
### Estimation 3.1. Plan Business

Analysis Approach

## Solution
### Financial

Analysis

## Solution
### Focus

Groups

## Solution
### Functional

Decomposition

## Solution
### Trace

Requirements

## Solution
### Interface

Analysis

## Solution
### Communicate

Business Analysis
Information

Business Analysis
Information

Business Analysis
Information

## Solution
### Item

Tracking

## Solution
### Lessons

Learned

## Solution
### Metrics

and Key
Performance
Indicators (KPIs)

## Solution
### Mind

Mapping

## Solution
### Non-

Functional
Requirements
Analysis

## Solution
### Process

Analysis

Modelling

## Solution
### Risk

Analysis and
Management

## Solution
### Roles and

Permissions
Matrix

## Solution
### Root

Cause Analysis

## Solution
### Scope

Modelling

## Solution
### Sequence

Diagrams

## Solution
### State

Modelling

## Solution
### Survey or

Questionnaire

## Solution
### SWOT

Analysis

## Solution
### Use Cases

and Scenarios

## Solution
### User

Stories

## Solution
### Vendor

Assessment

