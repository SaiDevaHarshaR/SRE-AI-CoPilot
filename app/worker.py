import time
from app.logs import get_pending_logs, update_log
from app.llm import query_llm

from app.agent import analyze_with_agent

def process_logs():
    while True:
        pending_logs = get_pending_logs()

        for log_item in pending_logs:
            prompt = f"""
            You are a senior DevOps engineer.

            Analyze this production log:
            {log_item['log']}

            Give root cause and fix.
            """

            #result = query_llm(prompt)
            #👉 ONE step 👉 ONE prompt 👉 ONE response --> gives generic/basic answers

            result = analyze_with_agent(log_item["log"])
            #👉 MULTIPLE steps 👉 Each step has a purpose 👉 More accurate + structured
            update_log(log_item, result)

        time.sleep(5)