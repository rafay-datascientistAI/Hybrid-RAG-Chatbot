def dense_retrieval(vector_store):

    print("Initializing Dense Retriever")

    dense_retriever = vector_store.as_retriever(
        search_type = "similarity",
        search_kwargs = {"k" : 5}
    )

    print("Dense Retriever Initialized Successfully")

    return dense_retriever

