#Log comes in
#   ↓
#Check memory (cache)
#   ↓
#If found → return instantly
#Else → run agent → store result


memory_store = {}

def get_from_memory(log: str):
    return memory_store.get(log)

def save_to_memory(log: str, result):
    memory_store[log] = result

import redis #pip install redis
import json

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def get_from_memory(log: str):
    data = r.get(log)
    if data:
        return json.loads(data)
    return None

def save_to_memory(log: str, result):
    r.set(log, json.dumps(result))