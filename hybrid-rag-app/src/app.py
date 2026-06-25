import streamlit as st
from rag_pipeline import RagPipeline
from langchain_community.chat_message_histories import StreamlitChatMessageHistory

history = StreamlitChatMessageHistory()

st.title("My RAG Chatbot")


if "pipeline" not in st.session_state:
    st.session_state.pipeline = None

uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if uploaded_files and st.session_state.pipeline is None:
    st.session_state.pipeline = RagPipeline(uploaded_files)


for message in history.messages:
    with st.chat_message(message.type):
        st.write(message.content)


query = st.chat_input("Ask Question")

if query and st.session_state.pipeline:


    history.add_user_message(query)

    with st.chat_message("User"):
        st.write(query)
    
    with st.spinner("Thinking...."):

        answer = st.session_state.pipeline.execute_pipeline(query, chat_history=history.messages)


    history.add_ai_message(answer)

    with st.chat_message("AI"):
        st.write(answer)
