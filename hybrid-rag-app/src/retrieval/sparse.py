from langchain_community.retrievers import BM25Retriever

def sparse_retrieval(chunks : list):

    print("Initializing Sparse Retriever")
    
    bm25 = BM25Retriever.from_documents(chunks)
    bm25.k = 5

    print("Sparse Retriever Initialized Successfully")

    return bm25