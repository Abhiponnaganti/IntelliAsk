import os
import logging
from typing import List, Optional
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
from langchain.embeddings import OpenAIEmbeddings  # Use old import
from langchain.vectorstores import Chroma
from langchain.schema import Document

from config import Config
from src.utils import setup_logging, ensure_directory_exists

logger = logging.getLogger(__name__)

class DocumentProcessor:
    def __init__(self):
        setup_logging()
        self.embeddings = OpenAIEmbeddings(openai_api_key=Config.OPENAI_API_KEY)
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP,
            length_function=len,
        )
        ensure_directory_exists(Config.VECTOR_STORE_PATH)
        
    # ... rest of the class remains the same
        
    def load_document(self, file_path: str) -> List[Document]:
        """Load document based on file extension"""
        try:
            if file_path.endswith('.pdf'):
                loader = PyPDFLoader(file_path)
            elif file_path.endswith('.docx'):
                loader = Docx2txtLoader(file_path)
            elif file_path.endswith('.txt'):
                loader = TextLoader(file_path, encoding='utf-8')
            else:
                raise ValueError(f"Unsupported file type: {file_path}")
            
            documents = loader.load()
            logger.info(f"Successfully loaded {len(documents)} pages from {file_path}")
            return documents
            
        except Exception as e:
            logger.error(f"Error loading document {file_path}: {str(e)}")
            raise
    
    def process_documents(self, file_paths: List[str]) -> Optional[Chroma]:
        """Process multiple documents and create vector store"""
        try:
            all_docs = []
            
            for file_path in file_paths:
                docs = self.load_document(file_path)
                # Add metadata
                for doc in docs:
                    doc.metadata.update({
                        'source_file': os.path.basename(file_path),
                        'file_path': file_path
                    })
                all_docs.extend(docs)
            
            if not all_docs:
                logger.warning("No documents loaded")
                return None
            
            # Split documents into chunks
            text_chunks = self.text_splitter.split_documents(all_docs)
            logger.info(f"Created {len(text_chunks)} text chunks")
            
            # Create vector store
            vector_store = Chroma.from_documents(
                documents=text_chunks,
                embedding=self.embeddings,
                persist_directory=Config.VECTOR_STORE_PATH
            )
            
            vector_store.persist()
            logger.info("Vector store created and persisted successfully")
            return vector_store
            
        except Exception as e:
            logger.error(f"Error processing documents: {str(e)}")
            raise
    
    def load_existing_vector_store(self) -> Optional[Chroma]:
        """Load existing vector store if it exists"""
        try:
            if os.path.exists(Config.VECTOR_STORE_PATH) and os.listdir(Config.VECTOR_STORE_PATH):
                vector_store = Chroma(
                    persist_directory=Config.VECTOR_STORE_PATH,
                    embedding_function=self.embeddings
                )
                logger.info("Loaded existing vector store")
                return vector_store
            return None
        except Exception as e:
            logger.error(f"Error loading existing vector store: {str(e)}")
            return None