import os
import logging
from typing import List
from config import Config

def setup_logging():
    """Set up logging configuration"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('app.log'),
            logging.StreamHandler()
        ]
    )

def ensure_directory_exists(path: str) -> None:
    """Create directory if it doesn't exist"""
    os.makedirs(path, exist_ok=True)

def get_file_extension(filename: str) -> str:
    """Get file extension in lowercase"""
    return os.path.splitext(filename.lower())[1]

def is_supported_file(filename: str) -> bool:
    """Check if file format is supported"""
    return get_file_extension(filename) in Config.SUPPORTED_FORMATS

def validate_file_size(file_size: int) -> bool:
    """Validate file size against maximum allowed"""
    return file_size <= Config.MAX_FILE_SIZE