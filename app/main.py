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