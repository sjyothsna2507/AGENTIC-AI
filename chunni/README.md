
# CrewAI Job Application Automation System

Welcome to CrewAI, a cutting-edge system designed to automate the job application process. With AI-powered agents tailored for sourcing, fitting, and applying to jobs, this project provides a seamless experience for job seekers.

## Project Overview

This project contains three primary AI agents focused on job sourcing, career fit analysis, and automated application submission:

1. **Job Sourcing Agent** - Collects and normalizes job listings based on given parameters like job title, location, skills, and experience level.
2. **Fit and Advice Agent** - Matches job listings to user profiles and provides tailored career advice.
3. **Application Concierge Agent** - Automates resume tailoring, application submissions, and tracks the application process.

## Installation Guide

### Python Version Requirements

CrewAI requires Python >= 3.10 and < 3.13. Here’s how to check your version:

```bash
python3 --version
```

If you need to update Python, visit [python.org/downloads](https://python.org/downloads).

### Install UV

CrewAI uses UV as its dependency management and package handling tool. To install UV, follow these steps:

#### On macOS/Linux:
Use `curl` to download the script and execute it with `sh`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

If your system doesn’t have `curl`, you can use `wget`:

```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```

#### On Windows:
Use `irm` to download the script and `iex` to execute it:

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

For further installation details, refer to the [UV Installation Guide](https://astral.sh/uv/install).

### Install CrewAI

Once UV is installed, run the following command to install the CrewAI CLI:

```bash
uv tool install crewai
```

To verify that CrewAI is installed, run:

```bash
uv tool list
```

You should see something like:

```bash
crewai v0.102.0
```

If you need to update CrewAI, run:

```bash
uv tool install crewai --upgrade
```

### Verifying Installation

Once installation is successful, you’re ready to create your first crew!

```bash
crewai create crew <your_project_name>
```

This will generate the following project structure:

```plaintext
my_project/
├── .gitignore
├── knowledge/
├── pyproject.toml
├── README.md
├── .env
└── src/
    └── my_project/
        ├── __init__.py
        ├── main.py
        ├── crew.py
        ├── tools/
        │   ├── custom_tool.py
        │   └── __init__.py
        └── config/
            ├── agents.yaml
            └── tasks.yaml
```

### Customizing Your Project

- **agents.yaml**: Define your AI agents and their roles.
- **tasks.yaml**: Set up agent tasks and workflows.
- **.env**: Store API keys and environment variables securely.
- **main.py**: The project entry point and execution flow.
- **crew.py**: Orchestrates the coordination of the crew.
- **tools/**: Custom agent tools.
- **knowledge/**: Directory for your knowledge base.

Start by editing `agents.yaml` and `tasks.yaml` to define your crew’s behavior. Be sure to keep sensitive information, like API keys, in the `.env` file.

### Running Your Crew

Before running your crew, make sure to install the necessary dependencies:

```bash
crewai install
```

To add additional packages, use:

```bash
uv add <package-name>
```

Finally, run your crew with:

```bash
crewai run
```

## Tasks Overview

1. **Job Sourcing**: Collect job listings based on criteria like job title, location, skills, experience level, and job type from multiple platforms (LinkedIn, Indeed, Naukri, corporate pages).
   
2. **Career Fit Analysis**: Match job listings to user profiles using cosine similarity, providing tailored career advice.

3. **Application Concierge**: Automate resume tailoring, application submission, and track the status of applications.

## Contributions

We appreciate any contributions to this project! Feel free to fork and submit pull requests for improvements.

## Special Thanks

A special thanks to [Vicky Bytes](https://vickybytes.com/) for providing the inspiration and guidance for the AI Agents Unleashed: Hiring Challenge, along with the associated prizes and payouts. Their contribution to AI innovation is invaluable.

---

CrewAI is ready to help you streamline your job application process, leveraging the power of AI to make the experience efficient, automated, and personalized.

Enjoy your job hunt with CrewAI 🚀!
