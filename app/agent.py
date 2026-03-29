from app.llm import query_llm

def analyze_with_agent(log: str):
    # Step 1: Classify issue
    classification_prompt = f"""
    Classify this issue:
    {log}

    Categories:
    - database
    - kubernetes
    - network
    - unknown
    """

    category = query_llm(classification_prompt)

    # Step 2: Analyze based on category
    analysis_prompt = f"""
    You are a senior SRE.

    Issue category: {category}

    Log:
    {log}

    Give:
    1. Root cause
    2. Fix
    """

    result = query_llm(analysis_prompt)

    return {
        "category": category,
        "analysis": result
    }