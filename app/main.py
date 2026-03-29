from fastapi import FastAPI
from app.llm import query_llm

app = FastAPI()

@app.get("/")
def home():
    return {"message": "SRE AI Copilot running"}

@app.post("/analyze")
def analyze(log: str):
    prompt = f"""
    You are a senior DevOps engineer.

    Analyze this production issue log:
    {log}

    Give:
    1. Root cause
    2. Fix
    """

    result = query_llm(prompt)

    return {"analysis": result}

from fastapi import FastAPI
from app.logs import store_log, logs_db

app = FastAPI()

@app.get("/")
def home():
    return {"message": "SRE AI Copilot running"}

@app.post("/ingest")
def ingest(log: str):
    store_log(log)
    return {"message": "Log received"}

@app.get("/logs")
def get_logs():
    return logs_db    


    #to run server: uvicorn app.main:app --reload
    #to test it: http://127.0.0.1:8000/docs
    #in another terminal: python -c "from app.worker import process_logs; process_logs()"