from langchain.tools import tool

@tool
def check_rules(query: str):
    """Returns rules"""
    with open("data/rules.txt") as f:
        return f.read()