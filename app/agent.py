from app.llm import query_llm
from app.tools import search_logs, get_k8s_fix
from app.memory import get_from_memory, save_to_memory

def analyze_with_agent(log: str):
    # Step 0: Check memory
    cached = get_from_memory(log)
    if cached:
        return {"source": "memory", "data": cached}

    # Step 1: classify
    category = query_llm(f"Classify this log: {log}")

    # Step 2: tool usage
    log_insight = search_logs(log)
    fix = get_k8s_fix(log)

    # Step 3: final reasoning
    final_prompt = f"""
    You are a senior SRE.

    Log: {log}
    Category: {category}
    Insights: {log_insight}
    Suggested Fix: {fix}

    Give final root cause and refined fix.
    """

    result = query_llm(final_prompt)

    # Step 4: save memory
    save_to_memory(log, result)

    return {
        "source": "llm",
        "category": category,
        "insight": log_insight,
        "fix": fix,
        "final_analysis": result
    }