logs_db = []

def store_log(log: str):
    logs_db.append({
        "log": log,
        "status": "pending",
        "analysis": None
    })

def get_pending_logs():
    return [l for l in logs_db if l["status"] == "pending"]

def update_log(log_item, analysis):
    log_item["status"] = "done"
    log_item["analysis"] = analysis