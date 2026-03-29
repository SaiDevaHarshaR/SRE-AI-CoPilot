#pip install faiss-cpu sentence-transformers

#Convert text → numbers (embedding)
#Compare similarity
#Pick closest match

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

# store embeddings + logs
embeddings = []
logs = []
responses = []

# FAISS index
index = faiss.IndexFlatL2(384)


def add_to_memory(log, response):
    vector = model.encode([log])[0]

    embeddings.append(vector)
    logs.append(log)
    responses.append(response)

    index.add(np.array([vector]))


def search_similar(log):
    if len(logs) == 0:
        return None

    query_vector = model.encode([log])[0]

    D, I = index.search(np.array([query_vector]), k=1)

    if D[0][0] < 0.5:  # threshold
        return responses[I[0][0]]

    return None