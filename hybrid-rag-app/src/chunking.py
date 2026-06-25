from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(loaded_documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 600,
        chunk_overlap = 100,
        separators=["\n\n", "\n", " " , ""],
        length_function= len,
    )

    chunks = text_splitter.split_documents(loaded_documents)
    print(f"Splitted {len(loaded_documents)} documents into {len(chunks)} chunks")
    return chunks