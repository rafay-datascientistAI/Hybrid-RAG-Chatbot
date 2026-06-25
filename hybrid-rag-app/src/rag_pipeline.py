from loader import loader
from chunking import split_text
from vectorDB import vector_store
from retrieval.dense import dense_retrieval
from retrieval.sparse import sparse_retrieval
from retrieval.hybrid import hybrid_retrieval
from retrieval.reranker import rerank_documents
from llm import llm
from generate_answer import generate_answer
from retrieval.history_aware import contextualize_q_prompt
from langchain_classic.chains import create_history_aware_retriever

class RagPipeline:

    def __init__(self, uploaded_files):

        print("Initializing RAG Pipeline")

        self.loaded_files = loader(uploaded_files)

        self.chunks = split_text(self.loaded_files)

        self.vector_store = vector_store(self.chunks)

        self.llm = llm()

        self.dense_retreiver = dense_retrieval(self.vector_store)

        self.sparse_retreiver = sparse_retrieval(self.chunks)

        self.hybrid_retriever = hybrid_retrieval(self.dense_retreiver, self.sparse_retreiver)

        self.history_aware_retriever = create_history_aware_retriever(
            llm=self.llm,
            retriever=self.hybrid_retriever,
            prompt=contextualize_q_prompt
        )

    
    def execute_pipeline(self, query, chat_history=""):

        print("Executing Hybrid RAG Pipeline")

        retrieved_docs = self.history_aware_retriever.invoke({"input" : query, "chat_history" : chat_history})

        reranked_docs = rerank_documents(query, retrieved_docs)

        final_answer = generate_answer(query, self.llm, reranked_docs)

        return final_answer      