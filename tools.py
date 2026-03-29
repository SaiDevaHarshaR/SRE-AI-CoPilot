def search_logs(log: str):
    # Simulated log search
    if "OOM" in log:
        return "Memory usage exceeded"
    if "timeout" in log:
        return "Service not responding"
    return "No pattern found"


def get_k8s_fix(log: str):
    if "OOM" in log:
        return "kubectl set resources deployment xyz --limits=memory=512Mi"
    if "crashloop" in log:
        return "kubectl describe pod xyz"
    return "Check logs manually"

#👉 These are tools your AI can use
#Like:
#calculator
#search engine
#kubectl helper