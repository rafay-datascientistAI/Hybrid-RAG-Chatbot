# 🚀 Hybrid RAG Chatbot

A production-style **Hybrid Retrieval-Augmented Generation (RAG)** chatbot built using **LangChain**, **ChromaDB**, **BM25**, **Cross-Encoder Reranking**, **Hugging Face**, and **Streamlit**.

Unlike a basic Vector RAG, this project combines **Dense Retrieval** and **Sparse Retrieval** to improve document retrieval quality before generating responses with an LLM.

---

# ✨ Features

- 📄 Upload one or multiple PDF files
- ✂️ Recursive Character Text Chunking
- 🔎 Dense Retrieval using ChromaDB
- 📝 Sparse Retrieval using BM25
- ⚡ Hybrid Retrieval using EnsembleRetriever
- 🎯 Cross-Encoder Reranking
- 💬 Conversational Memory
- 🤖 LLM-based Answer Generation
- 🖥️ Streamlit Chat Interface

---

# 🏗️ Architecture

```
                User Query
                     │
                     ▼
      Conversational Memory
                     │
                     ▼
        History-Aware Retrieval
                     │
                     ▼
      Hybrid Retrieval
(Dense Retrieval + BM25)
                     │
                     ▼
     Cross-Encoder Reranker
                     │
                     ▼
         Relevant Documents
                     │
                     ▼
          LLM Answer Generation
                     │
                     ▼
          Streamlit Chat UI
```

---

# 🛠️ Tech Stack

- Python
- LangChain
- Hugging Face
- ChromaDB
- BM25
- Sentence Transformers
- Streamlit
  
---

# 📂 Project Structure

```
src/
│
├── retrieval/
│   ├── dense.py
│   ├── sparse.py
│   ├── hybrid.py
│   ├── reranker.py
│   └── history_aware.py
│
├── loader.py
├── chunking.py
├── embedding.py
├── vectorDB.py
├── llm.py
├── generate_answer.py
├── rag_pipeline.py
└── app.py
```

---

# ⚙️ Pipeline

1. Load PDF Documents
2. Split Documents into Chunks
3. Generate Embeddings
4. Store Embeddings in ChromaDB
5. Retrieve using:
   - Dense Retrieval
   - BM25
6. Combine Results with Hybrid Retrieval
7. Re-rank using Cross Encoder
8. Generate Final Answer using LLM

---

# 🚀 Installation

```bash
git clone https://github.com/yourusername/Hybrid-RAG-Chatbot.git

cd Hybrid-RAG-Chatbot

pip install -r requirements.txt
```

Create a `.env` file:

```env
HF_TOKEN=YOUR_TOKEN
GROQ_API_KEY=YOUR_API_KEY
```

Run:

```bash
streamlit run src/app.py
```

---

# 📸 Demo

```
https://www.linkedin.com/posts/muhammad-rafay-30267b3b7_ai-generativeai-rag-activity-7476049750690168832-1SmD?utm_source=share&utm_medium=member_android&rcm=ACoAAGW5evIBYys9sIO2f9zN54Qu_vVfutnw-A0
```

---

# 🔮 Future Improvements

- Source Citations
- Page Number References
- Better Streamlit UI
- Streaming Responses
- Multi-Query Retrieval
- Query Expansion
- RAG Evaluation (RAGAS)
- Multi-Document Collections
- Docker Deployment
- Cloud Deployment

---

# 🤝 Contributions

Contributions, suggestions, and feedback are always welcome.

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
