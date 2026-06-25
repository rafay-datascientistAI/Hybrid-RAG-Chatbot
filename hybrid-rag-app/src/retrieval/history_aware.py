from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",

            """Given a chat history and the latest user question,
            rewrite the latest question into a standalone question
            that can be understood without the chat history.
            
            Do NOT answer the question.
            Only rewrite it if needed.
            Otherwise return it unchanged.
            """
        ),

        MessagesPlaceholder("chat_history"),

        ("human", "{input}")
    ]
)
