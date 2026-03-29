# 🚀 AI-Powered SRE Incident Analyzer (GenAI + DevOps)

---

# 📌 Overview

This project is a **production-grade GenAI system** that analyzes system logs, detects incidents, retrieves similar past issues, and generates intelligent root-cause analysis using an **agent-based architecture**.

It is designed to simulate a **real-world SRE (Site Reliability Engineering) assistant**, combining:

* LLM-powered reasoning
* Semantic memory (vector search)
* Tool-using agents
* Async processing
* Production-ready DevOps stack

---

# 🎯 Problem Statement

Modern systems generate massive logs, and debugging incidents manually is:

* Time-consuming
* Repetitive
* Error-prone

This system automates:

✅ Log ingestion
✅ Incident understanding
✅ Similar issue retrieval
✅ Root cause analysis

---

# 🧠 Key Features

## 🔹 1. Agent-Based Reasoning

Instead of directly calling an LLM, the system uses an **agent** that:

* Decides what to do
* Chooses tools dynamically
* Combines multiple sources of knowledge

---

## 🔹 2. Tool Integration

The agent can use:

* **Vector Memory Tool** → Retrieve similar past incidents
* **Cache Tool** → Reuse previous responses
* **LLM Tool** → Generate final reasoning

---

## 🔹 3. Semantic Memory (Vector Search)

* Uses embeddings to store incidents
* Retrieves **similar incidents (not exact matches)**
* Enables context-aware reasoning

---

## 🔹 4. Caching Layer

* Stores frequently asked queries
* Reduces LLM calls
* Improves latency and cost efficiency

---

## 🔹 5. Async Processing

* Background ingestion of logs
* Non-blocking API calls
* Scalable architecture

---

## 🔹 6. Production-Ready DevOps

* Dockerized application
* CI/CD pipeline (GitHub Actions)
* AWS ECS deployment
* Monitoring with Prometheus & Grafana

---

# 🏗️ System Architecture

```
                ┌──────────────┐
                │    User      │
                └──────┬───────┘
                       ↓
              ┌─────────────────┐
              │   FastAPI App   │
              └──────┬──────────┘
                     ↓
              ┌─────────────────┐
              │     Agent       │
              └──────┬──────────┘
                     ↓
     ┌───────────────┼───────────────┐
     ↓               ↓               ↓
Vector DB       Redis Cache       LLM
 (FAISS)                           ↓
     └───────────────┬─────────────┘
                     ↓
            Final Response
```

---

# ⚙️ Tech Stack

## 🧠 GenAI Layer

* LLM (API-based or local-compatible)
* Embeddings (sentence-transformers)
* FAISS (vector similarity search)

## ⚡ Backend

* FastAPI (async APIs)
* Python

## 🧩 Memory & Cache

* FAISS (semantic memory)
* Redis (caching layer)

## 🐳 DevOps

* Docker (containerization)
* GitHub Actions (CI/CD)
* AWS ECS (deployment)

## 📊 Monitoring

* Prometheus (metrics)
* Grafana (dashboards)

---

# 📁 Project Structure

```
sre-ai/
│
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── agent.py             # Agent logic
│   ├── tools.py             # Tools (vector, cache, LLM)
│   ├── vector_store.py      # FAISS implementation
│   ├── cache.py             # Redis integration
│   └── ingestion.py         # Async ingestion logic
│
├── .github/workflows/
│   └── deploy.yml           # CI/CD pipeline
│
├── Dockerfile
├── prometheus.yml
├── requirements.txt
└── README.md
```

---

# 🔄 How It Works (Step-by-Step)

## 1️⃣ Log Ingestion

* Logs are sent to `/ingest`
* Processed asynchronously
* Stored in vector database (FAISS)

👉 Why async?
So ingestion does not block user requests.

---

## 2️⃣ User Query

User sends:

```
"My API is timing out frequently"
```

---

## 3️⃣ Agent Decision

The agent:

* Checks cache → quick response if exists
* Searches vector DB → finds similar incidents
* Calls LLM → generates reasoning

---

## 4️⃣ Tool Execution Flow

```
User Query
   ↓
Check Cache
   ↓ (miss)
Vector Search
   ↓
LLM Reasoning
   ↓
Store in Cache
   ↓
Return Response
```

---

## 5️⃣ Final Output

User gets:

* Root cause analysis
* Suggested fixes
* Context from past incidents

---

# 🚀 Setup Instructions

## 1. Clone Repo

```bash
git clone <repo-url>
cd sre-ai
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Run Redis

```bash
docker run -d -p 6379:6379 redis
```

---

## 4. Start FastAPI

```bash
uvicorn app.main:app --reload
```

---

## 5. Test APIs

* Ingest logs → `/ingest`
* Query system → `/query`

---

# 🐳 Run with Docker

```bash
docker build -t sre-ai .
docker run -p 8000:8000 sre-ai
```

---

# 🔁 CI/CD Pipeline

* Triggered on push to `main`
* Builds Docker image
* Runs container tests

---

# ☁️ Deployment (AWS ECS)

* Push image to ECR
* Deploy using ECS Fargate
* Attach Load Balancer
* Enable auto-scaling

---

# 📊 Monitoring

* Prometheus collects metrics
* Grafana visualizes:

  * API latency
  * Request count
  * System health

---

# 🧠 Key Engineering Decisions

### ❓ Why Agent instead of direct LLM?

→ Enables tool usage, reasoning, and modular design

---

### ❓ Why FAISS?

→ Efficient semantic similarity search

---

### ❓ Why Redis?

→ Fast caching layer for repeated queries

---

### ❓ Why Async FastAPI?

→ Handles high concurrency efficiently

---

# 📈 Scalability Design

* Stateless FastAPI services
* Horizontal scaling via ECS
* Separate memory & cache layers
* Background workers for ingestion

---

# 🧪 Future Improvements

* Multi-agent collaboration
* Streaming responses
* Fine-tuned domain model
* Distributed vector DB (Pinecone/Weaviate)
* OpenTelemetry tracing

---

# 🎤 Interview Pitch (30 sec)

> “I built a production-grade AI SRE assistant using FastAPI with an agent-based architecture. It performs semantic incident retrieval using FAISS, uses Redis caching for optimization, processes logs asynchronously, and is deployed via Docker and AWS ECS with monitoring through Prometheus and Grafana.”

---

# 📄 Resume Bullet

> Built an AI-powered SRE incident analysis system using FastAPI with agent-based reasoning, semantic search (FAISS), and Redis caching; deployed via Docker, CI/CD, and AWS ECS with monitoring using Prometheus and Grafana.

---

# ⭐ Why This Project Stands Out

✅ Not a basic RAG project
✅ Uses agents + tools
✅ Includes memory + caching
✅ Has real system design
✅ Fully production-ready
✅ Covers GenAI + DevOps

---

# 👨‍💻 Author

Built as a **production-grade GenAI + DevOps portfolio project** to demonstrate real-world engineering capability.

---
