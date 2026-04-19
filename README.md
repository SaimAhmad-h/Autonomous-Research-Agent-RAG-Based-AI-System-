# 🤖 Autonomous Research Agent (RAG-Based AI System)

## 📌 Overview

This project is an **AI-powered Autonomous Research Agent** that analyzes system data (logs, rules, and sensor data) to **identify root causes of failures**.

It combines:

* 🔍 Retrieval-Augmented Generation (RAG)
* 🧠 Large Language Models (LLMs)
* 🛠️ Tool-based reasoning
* 💡 Hypothesis generation & verification

---

## 🚀 Features

* 📊 Reads **sensor data (CSV)**
* 📄 Analyzes **logs and rules**
* 🔎 Retrieves relevant information using **vector search (FAISS)**
* 🤖 Uses **LLM (Groq / LLaMA 3.1)** for reasoning
* 💡 Generates multiple **hypotheses**
* ✔ Verifies correct causes
* 🧠 Provides final **root-cause analysis**

---

## 🧠 How It Works

### 🔄 System Flow

User Query → Agent → Tools → RAG Retrieval → LLM → Hypothesis → Verification → Final Answer

---

### ⚙️ Step-by-Step

1. **User asks a question**

   ```
   why system fails?
   ```

2. **Agent decides actions**

   * Calls tools (logs, rules, CSV)

3. **Tools fetch real data**

   * Logs → overheating, vibration
   * Rules → failure conditions

4. **RAG retrieves relevant chunks**

   * Using embeddings + FAISS

5. **LLM analyzes data**

   * Finds patterns and relationships

6. **Hypothesis Engine**

   * Generates possible causes

7. **Verifier**

   * Filters only valid causes

8. **Final Output**

   * Clear explanation of failure

---

## 📂 Project Structure

```
autonomous-research-agent/
│
├── agent/
│   ├── agent.py          # Main agent logic
│   ├── hypothesis.py     # Hypothesis generation
│   └── verifier.py       # Hypothesis verification
│
├── rag/
│   ├── chunker.py        # Text splitting
│   ├── embedder.py       # Embeddings (HuggingFace)
│   └── vector_store.py   # FAISS database
│
├── tools/
│   ├── csv_tool.py       # Sensor data analysis
│   ├── logs_tool.py      # Logs reader
│   └── rules_tool.py     # Rules checker
│
├── data/
│   ├── sensor_data.csv
│   ├── logs.txt
│   └── rules.txt
│
├── main.py               # Entry point
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/autonomous-research-agent.git
cd autonomous-research-agent
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔑 Setup API (Groq)

1. Get API key from:
   👉 https://console.groq.com/

2. Add in `agent/agent.py`:

```python
groq_api_key="your_api_key_here"
```

---

## ▶️ Run the Project

```
python main.py
```

---

## 💬 Example

### Input:

```
why system fails?
```

### Output:

```
🧠 Answer:
The system fails due to overheating, vibration anomalies, and pressure instability.

💡 Hypotheses:
- Failure due to overheating
- Mechanical failure due to vibration
- Failure due to pressure instability

✔ Verified:
- Failure due to overheating
- Mechanical failure due to vibration
```

---

## 🧠 Core Concepts

### 🔹 RAG (Retrieval-Augmented Generation)

Combines:

* Data retrieval (FAISS)
* LLM reasoning

---

### 🔹 Tools

Custom Python functions used by agent:

* Access logs
* Read rules
* Analyze data

---

### 🔹 Hypothesis Engine

Generates possible explanations from context.

---

### 🔹 Verifier

Filters correct explanations based on evidence.

---

## 🛠️ Technologies Used

* Python 🐍
* LangChain
* Groq API (LLaMA 3.1)
* FAISS (Vector DB)
* HuggingFace Embeddings
* Pandas

---

## ⚠️ Known Issues

* Agent may loop without `max_iterations`
* Model updates may break API (Groq changes)
* Requires API key for LLM

---

## 🔥 Future Improvements

* ✅ Replace deprecated `initialize_agent`
* ✅ Add UI (Streamlit / Web App)
* ✅ Improve hypothesis using LLM
* ✅ Add real-time sensor monitoring
* ✅ Memory & chat history

---

## 🎯 Use Cases

* Industrial fault diagnosis
* Predictive maintenance
* Smart troubleshooting systems
* AI research assistants

---

## 📌 Author

**Saim**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
