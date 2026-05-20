from langchain.tools import tool

def create_rag_tool(vector_store):

    @tool
    def rag_search(query: str):
        """Search internal knowledge (logs + rules)"""
        results = vector_store.search(query)
        return "\n".join(results)

    return rag_search