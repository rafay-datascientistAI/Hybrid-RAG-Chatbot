from sentence_transformers import CrossEncoder
from langchain_core.documents import Document
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["HF_TOKENS"] = os.getenv("HF_TOKENS")

def load_reranker():

    model = CrossEncoder(
        "BAAI/bge-reranker-base"
    )

    return model

reranker = load_reranker()

def rerank_documents(query : str, documents : list[Document], reranker=reranker, top_k : int = 3):

    pairs = [
        (query, doc.page_content) for doc in documents
    ]

    scores = reranker.predict(pairs)

    doc_score_pairs = list(zip(documents, scores))

    ranked_docs = sorted(
        doc_score_pairs,
        key = lambda x : x[1],
        reverse= True
    )

    return [doc for doc, score in ranked_docs[:top_k]]