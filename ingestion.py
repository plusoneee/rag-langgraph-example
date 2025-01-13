"""
Run the script to load documents from the specified file,
split them into chunks, and store them in the Chroma vector store. This only needs to be done once.
"""

from typing import List
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

DATA_FILE_PATH = "state_of_the_union.txt"
EMBEDDING_MODEL = "sentence-transformers/all-mpnet-base-v2"
COLLECTION_NAME = "rag_demo"
PERSIST_DIRECTORY = "./.chroma"
CHUNK_SIZE = 256
CHUNK_OVERLAP = 20

embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)


# def load_documents(file_path: str = DATA_FILE_PATH) -> List[str]:
#     print(f"Loading documents from {file_path}")
#     loader = TextLoader(file_path)
#     documents = loader.load()
#     chunks = splitter.split_documents(documents)
#     Chroma.from_documents(
#         documents=chunks,
#         embedding=embeddings,
#         collection_name=COLLECTION_NAME,
#         persist_directory=PERSIST_DIRECTORY,
#     )

retriever = Chroma(
    embedding_function=embeddings,
    collection_name=COLLECTION_NAME,
    persist_directory=PERSIST_DIRECTORY,
).as_retriever()
