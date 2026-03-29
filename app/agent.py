from app.llm import query_llm
from app.tools import search_logs, get_k8s_fix
from app.memory import get_from_memory, save_to_memory
from app.vector_memory import search_similar, add_to_memory


def analyze_with_agent(log: str):

    # Step 0: semantic search
    similar = search_similar(log)
    if similar:
        return {"source": "semantic_memory", "data": similar}

    # existing logic...
    category = query_llm(f"Classify this log: {log}")
    log_insight = search_logs(log)
    fix = get_k8s_fix(log)

    final_prompt = f"""
    You are a senior SRE.

    Log: {log}
    Category: {category}
    Insights: {log_insight}
    Suggested Fix: {fix}

    Give final root cause and refined fix.
    """

    result = query_llm(final_prompt)

    # store in vector memory
    add_to_memory(log, result)

    return {
        "source": "llm",
        "analysis": result
    }