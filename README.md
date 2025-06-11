# Nexus Insight: Multi-Tool Research Agent


---

## 🚀 Project Overview

**Nexus Insight** is an advanced AI agent designed to autonomously explore, analyze, and synthesize information from academic research. Leveraging multi-tool reasoning and a sophisticated LangGraph architecture, it aims to automate the tedious process of scientific trend scouting and literature review, providing clear, actionable insights into emerging fields like Diffusion Models and Vision Language Models (VLMs).

### The Problem Nexus Insight Solves:

The rapid pace of scientific discovery makes it challenging for researchers, strategists, and innovators to keep up with emerging trends, influential papers, and key contributors. Manually sifting through thousands of publications is time-consuming and often leads to overlooked connections.

### Our Solution:

Nexus Insight streamlines this process by:
* **Intelligently Querying Diverse Data Sources:** Accessing academic databases (like Semantic Scholar, ArXiv) to retrieve relevant papers.
* **Performing Dynamic Data Analysis:** Utilizing Python code execution to conduct quantitative analysis on retrieved data (e.g., citation trends, publication frequency, author networks).
* **Generating Comprehensive Reports:** Synthesizing findings into structured, digestible reports, complete with data-driven visualizations.
* **Uncovering Hidden Insights:** Identifying subtle patterns and connections that might be missed by manual review, providing a deeper understanding of research landscapes.

## ✨ Features (Planned)

* **Academic Search Tools:**
    * **Semantic Scholar Integration:** Search for papers, authors, citations.
    * **ArXiv Integration:** Retrieve pre-prints and recent publications.
* **Code Execution Tool:**
    * Execute Python code dynamically for data analysis, visualization, and complex calculations (e.g., plotting trends, statistical analysis).
* **Reasoning and Planning:**
    * Utilize LangGraph to enable multi-step reasoning, tool orchestration, and adaptive problem-solving.
    * Support for long-running, stateful conversations/analysis tasks.
* **Structured Output & Reporting:**
    * Generate markdown-based reports summarizing findings.
    * Incorporate generated charts/graphs for visual understanding.
* **Observability:**
    * Full tracing and debugging capabilities via LangSmith.

## 🛠️ Getting Started (Docker Setup)

This project is designed to be run using Docker for easy setup and reproducibility.

### Prerequisites

* **Docker Desktop:** Installed and running on your system (with WSL 2 integration enabled if you're on Windows).
    * [Download Docker Desktop](https://www.docker.com/products/docker-desktop/)
* **Git:** Installed on your system.

### Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/MuhammadMaazA/nexus_insight.git](https://github.com/MuhammadMaazA/nexus_insight.git)
    cd nexus_insight
    ```

2.  **Configure Environment Variables:**
    Create a `.env` file in the root of your `nexus_insight` directory. This file will store your sensitive API keys.
    * Create the file:
        ```bash
        cp .env.example .env
        ```
    * Open `.env` (e.g., `nano .env` or with a text editor like VS Code) and replace the placeholder values with your actual API keys:
        ```dotenv
        OPENAI_API_KEY=sk-YOUR_ACTUAL_OPENAI_API_KEY
        LANGCHAIN_API_KEY=ls__YOUR_ACTUAL_LANGSMITH_API_KEY
        LANGCHAIN_TRACING_V2=true
        LANGCHAIN_PROJECT="Nexus Insight Agent Docker"
        # Add other API keys here as tools are implemented (e.g., SEMANTIC_SCHOLAR_API_KEY if needed)
        ```
    * **Security Note:** The `.env` file is already added to `.gitignore` to prevent it from being committed to your public repository.

3.  **Build the Docker Image:**
    This command will build the Docker image based on the `Dockerfile`, installing all necessary Python dependencies inside the container.
    ```bash
    docker compose build
    ```

4.  **Run the Agent (Test Script):**
    This will start a container from your built image and run the initial `src/main.py` test script.
    ```bash
    docker compose up
    ```
    You should see an LLM response in your terminal, and a new trace will appear in your LangSmith project (`Nexus Insight Agent Docker`).

---

## 📂 Project Structure

```
nexus_insight/
├── src/                    # Main source code for the agent
│   ├── agent/              # LangGraph agent definition, state, and nodes
│   ├── tools/              # External tools (Semantic Scholar, ArXiv, Code Executor)
│   │   ├── __init__.py
│   │   └── semantic_scholar_tool.py  # Initial Semantic Scholar Tool
│   ├── prompts/            # Custom prompts for the LLM
│   ├── utils/              # Utility functions (e.g., data processing, helpers)
│   └── main.py             # Entry point for testing and running the agent
├── notebooks/              # Jupyter notebooks for exploration, analysis, or prototyping
├── data/                   # Local data, outputs, or intermediate results
├── config/                 # Configuration files (e.g., model parameters)
├── .env                    # Local environment variables (ignored by Git)
├── .env.example            # Template for environment variables
├── Dockerfile              # Docker image build instructions
├── docker-compose.yml      # Docker Compose configuration
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore rules
└── README.md               # Project overview and documentation
```

---

## 🗺️ Roadmap & What's Next

Our development will proceed in phases, incrementally adding capabilities to Nexus Insight.

### Phase 1: Core Tools Implementation
* **Complete Semantic Scholar Tool:** Ensure robust error handling and expand capabilities if needed (e.g., fetching citations).
* **ArXiv Tool:** Develop a tool for searching and retrieving papers from ArXiv.
* **Python Code Execution Tool:** Implement a secure and isolated tool that allows the LLM to write and execute Python code for data analysis and visualization (e.g., using `pandas`, `matplotlib`).

### Phase 2: LangGraph Agent Development
* **Define Agent State:** Design the `State` for the LangGraph agent to hold conversation history, analysis context, and tool outputs.
* **Implement Nodes:** Create distinct nodes for different steps in the reasoning process (e.g., `plan_research`, `execute_tool`, `analyze_results`, `generate_report`).
* **Define Edges & Conditional Routing:** Configure the flow of execution between nodes based on the agent's reasoning and the outcomes of tool calls.
* **Integrate Tools:** Connect the developed tools to the LangGraph nodes, allowing the LLM to select and use them dynamically.

### Phase 3: Enhanced Output & Reporting
* **Report Generation:** Develop a dedicated module to compile findings into well-structured Markdown reports.
* **Visualization Integration:** Ensure the code execution tool can generate and save charts (e.g., PNG files) that can then be embedded into the final report.
* **Structured Output Parsers:** Fine-tune the agent's output to ensure consistent and parseable responses for report generation.

### Phase 4: Evaluation & Refinement
* **Define Evaluation Metrics:** Establish criteria for assessing the agent's performance (e.g., accuracy of trend identification, quality of reports).
* **Testing Framework:** Implement unit and integration tests for tools and agent logic.
* **Iterative Prompt Engineering:** Continuously refine prompts to improve reasoning capabilities and tool usage.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository, create a new branch, and submit a pull request. (More detailed guidelines will be added here later).

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

--- 