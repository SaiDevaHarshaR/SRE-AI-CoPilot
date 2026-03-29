import requests

HF_API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

def query_llm(prompt: str):
    response = requests.post(
        HF_API_URL,
        json={"inputs": prompt}
    )

    data = response.json()

    # HuggingFace returns list
    return data[0]["generated_text"]