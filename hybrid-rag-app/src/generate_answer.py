def generate_answer(query, llm, documents):

    context = "\n\n".join(doc.page_content for doc in documents)

    prompt = f"""
You are a helpful PDF assistant.

Answer ONLY from the provided context.

Keep Answer natural and conversational.

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content