from langchain_classic.retrievers import EnsembleRetriever

def hybrid_retrieval(dense_retriever, sparse_retriever):

    hybrid_retriever = EnsembleRetriever(
        retrievers=[
            dense_retriever,
            sparse_retriever
        ],
        weights=[0.5, 0.5]
    )

    return hybrid_retriever