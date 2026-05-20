from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embeddings():
    """
    Returns a local embedding model (no API required).
    Uses Sentence-Transformers model running locally.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings