from langchain_chroma import Chroma
from embedding import embedding_model

def vector_store (chunks : list):

    print("Initializing Vector Store")

    embeddings = embedding_model()
    vectorDB = Chroma.from_documents(
        documents= chunks,
        embedding=embeddings,
        persist_directory= "../chroma/vector_db",
        collection_name = "pdf_reader"
    )

    print("Vector Store Initialized Successfully")

    return vectorDB