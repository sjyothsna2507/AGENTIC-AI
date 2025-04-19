#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from chunni.crew import Chunni
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    # Define the job listing inputs for the crew task
    inputs = {
        'job_title': 'Data Scientist',           # Specify job title
        'location': 'Bangalore',                 # Specify job location
        'skills': [
    "Python",
    "PySpark",
    "SQL",
    "Machine Learning",
    "Generative AI",
    "Large Language Models (LLMs)",
    "Prompt Engineering",
    "Retrieval-Augmented Generation (RAG)",
    "Agentic AI",
    "Langchain",
    "Data Preprocessing",
    "Exploratory Data Analysis (EDA)",
    "Feature Engineering",
    "Natural Language Processing (NLP)",
    "Text Analytics",
    "Sentiment Analysis",
    "Power BI",
    "Microsoft Azure",
    "Google Cloud Platform (GCP)",
    "Azure OpenAI",
    "Git",
    "Jupyter Notebook",
    "Streamlit"
],
  # Specify required skills
        'experience_level': '1+ years',              # Specify experience level (e.g., Mid, Senior, Junior)
        'job_type': 'Full-time',                # Specify job type (e.g., Full-time, Part-time, Contract)
        'current_year': str(datetime.now().year)  # Current year
    }
    
    try:
        # Run the crew with provided inputs
        Chunni().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    # Define the job listing inputs for training
    inputs = {
        'job_title': 'Data Scientist',           # Specify job title
        'location': 'San Francisco',            # Specify job location
        'skills': ['Python', 'Deep Learning'],  # Specify required skills
        'experience_level': 'Senior',           # Specify experience level
        'job_type': 'Full-time',                # Specify job type
    }

    try:
        # Train the crew with the specified number of iterations
        Chunni().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        # Replay the crew execution from the specified task_id
        Chunni().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and return the results.
    """
    # Define the job listing inputs for testing
    inputs = {
        'job_title': 'Data Engineer',            # Specify job title
        'location': 'Los Angeles',              # Specify job location
        'skills': ['SQL', 'Cloud Computing'],   # Specify required skills
        'experience_level': 'Junior',           # Specify experience level
        'job_type': 'Contract',                 # Specify job type
        'current_year': str(datetime.now().year)  # Current year
    }

    try:
        # Test the crew execution with the specified number of iterations and OpenAI model
        Chunni().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
