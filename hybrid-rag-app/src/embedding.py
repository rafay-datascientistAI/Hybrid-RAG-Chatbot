from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()

def embedding_model():

    print("Loading Hugging Face Model")

    model = HuggingFaceEmbeddings(
        
        model_name = "BAAI/bge-small-en-v1.5",
        model_kwargs = {"token" : os.getenv("HF_TOKENS")},
        encode_kwargs = {"normalize_embeddings" : True}
    )

    print(f"Model Loaded Successfully")

    return model