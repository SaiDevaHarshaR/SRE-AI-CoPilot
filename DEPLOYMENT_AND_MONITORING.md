# 🚀 Deployment & Monitoring Guide

**Project: AI-Powered SRE Incident Analyzer**

---

# 📌 Overview

This document explains how the system is deployed and monitored in a production-like environment using:

* Docker (Containerization)
* GitHub Actions (CI/CD)
* AWS ECS (Deployment)
* Prometheus (Metrics Collection)
* Grafana (Visualization & Monitoring)

---

# 🐳 1. Containerization using Docker

## Step 1: Create Dockerfile

```dockerfile
FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi uvicorn requests redis faiss-cpu sentence-transformers prometheus-client

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Step 2: Build Docker Image

```bash
docker build -t sre-ai .
```

## Step 3: Run Container

```bash
docker run -p 8000:8000 sre-ai
```

---

# 🔁 2. CI/CD using GitHub Actions

## File: `.github/workflows/deploy.yml`

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Code
      uses: actions/checkout@v3

    - name: Build Docker Image
      run: docker build -t sre-ai .

    - name: Run Container Test
      run: docker run -d -p 8000:8000 sre-ai
```

## What this does:

* Automatically triggers on push to `main`
* Builds Docker image
* Runs container to validate deployment

---

# 📊 3. Monitoring using Prometheus

## Step 1: Add Metrics in FastAPI

Install:

```bash
pip install prometheus-client
```

## Add in `main.py`

```python
from prometheus_client import Counter, Histogram, start_http_server
import time

REQUEST_COUNT = Counter("request_count", "Total API Requests")
REQUEST_LATENCY = Histogram("request_latency_seconds", "API Latency")

@app.middleware("http")
async def monitor_requests(request, call_next):
    start_time = time.time()
    
    response = await call_next(request)
    
    latency = time.time() - start_time
    REQUEST_COUNT.inc()
    REQUEST_LATENCY.observe(latency)

    return response
```

## Step 2: Run Prometheus

Create `prometheus.yml`

```yaml
global:
  scrape_interval: 5s

scrape_configs:
  - job_name: "fastapi-app"
    static_configs:
      - targets: ["localhost:8000"]
```

Run Prometheus:

```bash
docker run -p 9090:9090 \
-v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
prom/prometheus
```

---

# 📈 4. Visualization using Grafana

## Step 1: Run Grafana

```bash
docker run -d -p 3000:3000 grafana/grafana
```

## Step 2: Access Dashboard

* URL: http://localhost:3000
* Username: admin
* Password: admin

## Step 3: Add Data Source

* Select: Prometheus
* URL: http://localhost:9090

## Step 4: Create Dashboard

Track:

* API request count
* API latency
* Error rates

---

# ☁️ 5. AWS Deployment (ECS - Fargate)

## Step 1: Push Image to ECR

```bash
aws ecr create-repository --repository-name sre-ai

docker tag sre-ai:latest <account-id>.dkr.ecr.region.amazonaws.com/sre-ai

docker push <account-id>.dkr.ecr.region.amazonaws.com/sre-ai
```

---

## Step 2: Create ECS Cluster

* Go to AWS ECS
* Select **Fargate (serverless containers)**
* Create Cluster

---

## Step 3: Create Task Definition

* Launch Type: Fargate
* Container Image: ECR Image
* Port Mapping: 8000

---

## Step 4: Create Service

* Attach Load Balancer (ALB)
* Enable Auto Scaling
* Set desired count (e.g., 2 tasks)

---

## Step 5: Access Application

* Use Load Balancer DNS
* API accessible via:
  `http://<alb-dns>:8000`

---

# 📡 Architecture Flow

```
User → Load Balancer → ECS (FastAPI Containers)
                         ↓
                  Prometheus (metrics)
                         ↓
                      Grafana
```

---

# 🧠 Key Design Decisions

* **Async FastAPI** for high concurrency
* **Docker** for portability
* **ECS Fargate** for serverless scaling
* **Prometheus + Grafana** for observability
* **CI/CD** for automation

---

# 🎤 Interview Explanation (Short Version)

> “I containerized the FastAPI application using Docker, set up CI/CD with GitHub Actions, deployed it on AWS ECS Fargate behind a load balancer, and implemented monitoring using Prometheus and Grafana to track system performance and latency.”

---

# 🚀 Production Enhancements (Future Work)

* Add distributed tracing (OpenTelemetry)
* Use managed Prometheus (AWS AMP)
* Add autoscaling policies based on CPU/latency
* Secure APIs with API Gateway + Auth

---

# ✅ Outcome

* Fully production-ready GenAI system
* Scalable, observable, and deployable
* Resume-ready for 5+ year GenAI roles

---
