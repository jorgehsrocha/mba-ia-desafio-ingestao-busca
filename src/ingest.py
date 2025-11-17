import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyMuPDFLoader

from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector
from src.check_env import check_env

load_dotenv()
check_env()

PDF_PATH = os.path.join(os.path.dirname(__file__), "..","document.pdf")

def ingest_pdf():
    try:
        with open(PDF_PATH, 'rb'):
            loader = PyMuPDFLoader(PDF_PATH)
            documents = loader.load()
            
            embeddings = OpenAIEmbeddings(model=os.environ.get("OPENAI_EMBEDDING_MODEL"))
            vector_store = PGVector(
                embeddings=embeddings,
                collection_name=os.environ.get("PG_VECTOR_COLLECTION_NAME"),
                connection=os.environ.get("DATABASE_URL"),
                use_jsonb=True
            )
            vector_store.add_documents(
                documents,
                chunk_size=1000,
                chunk_overlap=150
            )
            print("PDF ingested and stored in PostgreSQL vector store successfully.")
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {PDF_PATH} was not found.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while loading the PDF: {e}")


if __name__ == "__main__":
    try:
        ingest_pdf()
    except Exception as e:
        print(f"Error during ingestion: {e}")
        exit(1)