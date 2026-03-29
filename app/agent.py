from app.llm import query_llm
from app.tools import search_logs, get_k8s_fix

def analyze_with_agent(log: str):
    # Step 1: classify
    category = query_llm(f"Classify this log: {log}")

    # Step 2: use tool
    log_insight = search_logs(log)

    # Step 3: generate fix using tool
    fix = get_k8s_fix(log)

    # Step 4: combine everything
    final_prompt = f"""
    You are a senior SRE.

    Log: {log}
    Category: {category}
    Insights: {log_insight}
    Suggested Fix: {fix}

    Give final root cause and refined fix.
    """

    result = query_llm(final_prompt)

    return {
        "category": category,
        "insight": log_insight,
        "fix": fix,
        "final_analysis": result
    }