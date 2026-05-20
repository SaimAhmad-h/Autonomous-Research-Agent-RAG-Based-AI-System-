from langchain.tools import tool

@tool
def check_logs(query: str):
    """Returns failure logs"""
    with open("data/failure_logs.txt") as f:
        return f.read()