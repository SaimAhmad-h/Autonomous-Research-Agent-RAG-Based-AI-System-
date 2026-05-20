from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

def chunk_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=50
    )
    return splitter.split_documents([Document(page_content=text)])