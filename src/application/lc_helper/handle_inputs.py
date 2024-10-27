from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_transformers.openai_functions import create_metadata_tagger
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    return loader.load()

def create_chuncks(docs, chunk_size, chunk_overlap):
    """Create chuncks using spliter text"""
    splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '---', ' ', ''],
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(docs)

def get_embedding_function():
    """Get embedding function"""
    model = "sentence-transformers/all-mpnet-base-v2"
    return HuggingFaceEndpointEmbeddings(
        model=model,
        task="feature-extraction",
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    )

def get_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
    )

def create_metadata(schema, docs):
    llm = get_llm()
    tranformer = create_metadata_tagger(metadata_schema=schema, llm=llm)
    return tranformer.transform_documents(docs)

    