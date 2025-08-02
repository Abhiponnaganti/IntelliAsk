import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # Document Processing Settings
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 200))

    # File Storage Settings
    VECTOR_STORE_PATH = "./vector_store"
    UPLOAD_PATH = "./data/uploads"

    # File Upload Limits
    MAX_FILE_SIZE = (
        int(os.getenv("MAX_FILE_SIZE_MB", 10)) * 1024 * 1024
    )  # Convert MB to bytes
    SUPPORTED_FORMATS = [".pdf", ".docx", ".txt"]

    # Vector Store Settings
    SIMILARITY_SEARCH_K = 4  # Number of similar chunks to retrieve

    @classmethod
    def validate(cls):
        """Validate that required configuration is present"""
        if not cls.OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY is required. Please set it in your .env file."
            )
        return True
