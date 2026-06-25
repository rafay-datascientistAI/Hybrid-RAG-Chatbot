from langchain_community.document_loaders import PyPDFLoader,PyMuPDFLoader
import tempfile

def loader(uploaded_files):
    
    all_docs = []

    print(f"Procesing {len(uploaded_files)} files.")

    for pdf_file in uploaded_files:
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                temp_file.write(pdf_file.read())
                temp_file_path = temp_file.name
            
            loader = PyPDFLoader(temp_file_path)
            documents = loader.load()

            for doc in documents:
                doc.metadata["source_file"] = pdf_file.name
                doc.metadata["file_type"] = ".pdf"

            all_docs.extend(documents)

            print(f"Loaded {len(documents)} pages")
        
        except Exception:
            pass
    
    print(f"Loaded {len(all_docs)} documents")

    return all_docs

