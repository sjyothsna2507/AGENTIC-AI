from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from chunni.tools_used.custom_tool import InternetSearchTool
# from crewai_tools import SerperDevTool
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
from dotenv import load_dotenv
import os

load_dotenv()

# Ensure the Groq API key is set
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

gemini_llm = LLM(
    api_key=os.getenv("GEMINI_API_KEY"),
    model="gemini/gemini-2.0-flash"
)

embedder_config = {
    "provider": "google",
    "config": {
        "model": "models/text-embedding-004",
        "api_key": os.getenv("GEMINI_API_KEY")
    }
}

# Define the PDF knowledge source
pdf_source = PDFKnowledgeSource(
    file_paths=["Suggula_Jyothsna_07_04_v5.pdf"],    embedder=embedder_config

)

@CrewBase
class Chunni:
    """Chunni crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # --- Agents ---
    @agent
    def job_sourcing_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['job_sourcing_agent'],
            verbose=True,
            tools=[InternetSearchTool()],
             llm=self.agents_config['job_sourcing_agent']['llm']
        )

    @agent
    def fit_and_advice_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['fit_and_advice_agent'],
            verbose=True,
            knowledge_sources=[pdf_source],
             llm=self.agents_config['fit_and_advice_agent']['llm']
        )

    @agent
    def application_concierge_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['application_concierge_agent'],
            verbose=True,
            knowledge_sources=[pdf_source],
             llm=self.agents_config['application_concierge_agent']['llm']
        )

    # --- Tasks ---
    @task
    def job_sourcing_task(self) -> Task:
        return Task(
            config=self.tasks_config['job_sourcing_task'],
        )

    @task
    def fit_and_advice_task(self) -> Task:
        return Task(
            config=self.tasks_config['fit_and_advice_task'],
        )

    @task
    def application_concierge_task(self) -> Task:
        return Task(
            config=self.tasks_config['application_concierge_task'],
            output_file='applications_status.json'
        )

    # --- Crew ---
    @crew
    def crew(self) -> Crew:
        """Creates the Chunni crew"""
        return Crew(
             agents=[self.job_sourcing_agent(), self.fit_and_advice_agent(), self.application_concierge_agent()],
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            knowledge_sources=[pdf_source],
            embedder=embedder_config

        )

# from crewai import Agent, Crew, Process, Task ,LLM
# from crewai.project import CrewBase, agent, crew, task
# from crewai_tools import SerperDevTool
# from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
# from dotenv import load_dotenv
# knowledge_dir = 'knowledge'
# from chunni.tools_used.custom_tool import InternetSearchTool

# load_dotenv()
# import os
# os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
# pdf_files = [os.path.join(knowledge_dir, file) for file in os.listdir(knowledge_dir) if file.endswith('.pdf')]

# # Create a PDF knowledge source
# # pdf_source = PDFKnowledgeSource(file_paths=pdf_files)
# pdf_source = PDFKnowledgeSource(
#     file_paths=["John_Doe_Data_Scientist_Resume.pdf"]
# )

# @CrewBase
# class Chunni():
#     """Chunni crew"""

#     agents_config = 'config/agents.yaml'
#     tasks_config = 'config/tasks.yaml'

#     # --- Agents ---
#     @agent
#     def job_sourcing_agent(self) -> Agent:
#         return Agent(
#             config=self.agents_config['job_sourcing_agent'],
#             verbose=True,
#             tools=[InternetSearchTool()],
#             llm=LLM(model="gemini/gemini-1.5-flash", temperature=0.7)
#         )

#     @agent
#     def fit_and_advice_agent(self) -> Agent:
#         return Agent(
#             config=self.agents_config['fit_and_advice_agent'],
#             verbose=True,
#             knowledge_sources=[pdf_source],
#             llm=LLM(model="gemini/gemini-1.5-flash", temperature=0.7)
#         )

#     @agent
#     def application_concierge_agent(self) -> Agent:
#         return Agent(
#             config=self.agents_config['application_concierge_agent'],
#             verbose=True,
#             knowledge_sources=[pdf_source],
#             llm=LLM(model="gemini/gemini-1.5-flash", temperature=0.7)
#         )

#     # --- Tasks ---
#     @task
#     def job_sourcing_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['job_sourcing_task'],
#         )

#     @task
#     def fit_and_advice_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['fit_and_advice_task'],
#         )

#     @task
#     def application_concierge_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['application_concierge_task'],
#             output_file='applications_status.json'
#         )

#     # --- Crew ---
#     @crew
#     def crew(self) -> Crew:
#         """Creates the Chunni crew"""
#         return Crew(
#             agents=self.agents,
#             tasks=self.tasks,
#             process=Process.sequential,
#             verbose=True,
#             knowledge_sources=[pdf_source]
#         )
