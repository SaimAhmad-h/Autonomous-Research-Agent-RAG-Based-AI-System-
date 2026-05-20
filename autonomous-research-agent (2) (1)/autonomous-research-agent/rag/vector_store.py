from langchain_community.vectorstores import FAISS

class VectorStore:
    def __init__(self, embeddings):
        self.embeddings = embeddings
        self.db = None

    def build(self, chunks):
        self.db = FAISS.from_documents(chunks, self.embeddings)

    def search(self, query):
        docs = self.db.similarity_search(query, k=3)
        return [d.page_content for d in docs]