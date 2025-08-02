import logging
from typing import Dict, Any
from langchain.llms import OpenAI  # Use old import
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.vectorstores import Chroma

from config import Config
from src.utils import setup_logging

logger = logging.getLogger(__name__)

class QASystem:
    def __init__(self, vector_store: Chroma):
        setup_logging()
        self.vector_store = vector_store
        self.llm = OpenAI(
            temperature=0,
            openai_api_key=Config.OPENAI_API_KEY
        )
        
        # Custom prompt template
        self.prompt_template = PromptTemplate(
            template="""Use the following pieces of context to answer the question at the end. 
            If you don't know the answer based on the context provided, just say that you don't know, 
            don't try to make up an answer.
            
            Context: {context}
            
            Question: {question}
            
            Helpful Answer: """,
            input_variables=["context", "question"]
        )
        
        # Create QA chain
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever(
                search_kwargs={"k": 4}
            ),
            chain_type_kwargs={"prompt": self.prompt_template},
            return_source_documents=True
        )
        
        logger.info("QA System initialized successfully")
    
    def ask_question(self, question: str) -> Dict[str, Any]:
        """Ask a question and get answer with sources"""
        try:
            logger.info(f"Processing question: {question}")
            result = self.qa_chain({"query": question})
            
            response = {
                "answer": result["result"],
                "source_documents": result["source_documents"],
                "success": True
            }
            
            logger.info("Question processed successfully")
            return response
            
        except Exception as e:
            logger.error(f"Error processing question: {str(e)}")
            return {
                "answer": "Sorry, I encountered an error while processing your question.",
                "source_documents": [],
                "success": False,
                "error": str(e)
            }