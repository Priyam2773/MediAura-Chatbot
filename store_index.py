import os
from dotenv import load_dotenv

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.embeddings import HuggingFaceEmbeddings

from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore

# -------------------------------
# Load Environment Variables
# -------------------------------

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY not found in .env")

# -------------------------------
# Load PDF Files
# -------------------------------

def load_pdf_files(data_path):
    loader = DirectoryLoader(
        data_path,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )

    return loader.load()


# -------------------------------
# Keep only required metadata
# -------------------------------

def filter_to_minimal_docs(docs):
    minimal_docs = []

    for doc in docs:
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={
                    "source": doc.metadata.get("source")
                }
            )
        )

    return minimal_docs


# -------------------------------
# Split Documents
# -------------------------------

def text_split(docs):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20
    )

    return splitter.split_documents(docs)


# -------------------------------
# Embeddings
# -------------------------------

def download_embeddings():

    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


embedding = download_embeddings()


# -------------------------------
# Load Data
# -------------------------------

print("Loading PDFs...")

documents = load_pdf_files("data")

print(f"Loaded {len(documents)} pages.")

minimal_docs = filter_to_minimal_docs(documents)

texts_chunk = text_split(minimal_docs)

print(f"Created {len(texts_chunk)} chunks.")


# -------------------------------
# Pinecone
# -------------------------------

pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "medical-chatbot"

if not pc.has_index(index_name):

    print("Creating Pinecone index...")

    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

else:
    print("Pinecone index already exists.")


# -------------------------------
# Upload Embeddings
# -------------------------------

print("Uploading embeddings to Pinecone...")

docsearch = PineconeVectorStore.from_documents(
    documents=texts_chunk,
    embedding=embedding,
    index_name=index_name
)

print("======================================")
print("✅ Pinecone index created successfully.")
print("======================================")