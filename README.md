
# 🧠 Multi-Agent AI System with LangGraph, MCP & Groq

This project demonstrates a modular, multi-agent system using:

- **LangGraph** for agent orchestration  
- **Groq LLMs** via `.env`-based configuration  
- **Model Context Protocol (MCP)** for shared agent memory  
- **Python** with LangChain & OpenAI SDK (Groq-compatible)

> 💡 Use this project as a starting point for building intelligent agent-based workflows or capacity planning tools.

---

## 🔁 Overview

This system simulates a real-world AI task resolution flow using multiple autonomous agents:

1. `InputAgent` – Captures and stores the user query
2. `PlannerAgent` – Classifies the task type (e.g., "lookup")
3. `KnowledgeAgent` – Uses an LLM (from Groq) to provide an answer
4. Context is shared via a local JSON-based **Model Context Protocol (MCP)**

Agents communicate through a LangGraph-powered directed graph, enabling **stateful, flexible routing**.

---

## 🧱 Tech Stack

| Component        | Tech/Tool                    |
|------------------|------------------------------|
| Agent Orchestration | `LangGraph`                  |
| LLM Provider     | `Groq` via OpenAI-compatible API |
| Context Storage  | JSON-based MCP (Model Context Protocol) |
| Agent Framework  | `LangChain`, `RunnableLambda` |
| Secrets Mgmt     | `.env` (via `python-dotenv`)  |

---

## 📁 Project Structure

```
multi_agent_langgraph/
├── agents/
│   ├── input_agent.py
│   ├── planner_agent.py
│   ├── knowledge_agent.py
├── mcp/
│   └── context_store.py
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/your-org/multi-agent-groq.git
cd multi-agent-groq
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Configure `.env` with Groq API**

```
OPENAI_API_KEY=your_groq_api_key
OPENAI_BASE_URL=https://api.groq.com/openai/v1
```

4. **Run the project**

```bash
python main.py
```

---

## 🧠 Example Usage

```
User: what is LLM?

[Final Output]
LLM is large language model...
```

---

## 💡 Key Concepts

### 🧬 LangGraph
A stateful, directed graph framework for chaining AI agents with memory, branching, and retries.

### 🧠 MCP (Model Context Protocol)
A lightweight context manager that allows all agents to read/write to shared memory (`context.json`), ensuring persistence and traceability.

### 🔗 Agent-to-Agent (A2A) Protocol
Agents are decoupled but connected through shared state. LangGraph handles the orchestration and routing.

---

## 🚀 Future Enhancements

- Add **LangGraph branching** for more task types
- Add **RAG (Retrieval-Augmented Generation)** with internal docs
- Integrate **LangSmith** for tracing and debugging
- Replace MCP JSON with Redis for scalable state sharing
- Add **Streamlit UI** for internal demos

---

## 📄 License

This project is licensed under the **Apache 2.0 License**.  
Built for educational and prototyping purposes.

---

## 🧑‍💻 Author


