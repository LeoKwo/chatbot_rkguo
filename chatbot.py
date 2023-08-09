from llama_index import VectorStoreIndex, download_loader
import openai
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

openai.api_key = os.getenv('api_key')

PDFReader = download_loader("PDFReader")

loader = PDFReader()
documents = loader.load_data(file=Path('./resume.pdf'))

index = VectorStoreIndex.from_documents(documents)
# query_engine = index.as_query_engine()
chat_engine = index.as_chat_engine()

def chatbot(q):
    return chat_engine.chat(q)
    # return query_engine.query(q)