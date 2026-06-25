from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

def llm():

    llm = ChatGroq(
        model_name= "llama-3.1-8b-instant",
        temperature=0.3,
        max_tokens=1024,
        api_key=os.getenv("GROQ_API_KEY")
    )

    return llm
