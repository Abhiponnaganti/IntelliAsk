import unittest
import tempfile
import os
from src.utils import is_supported_file, validate_file_size
from config import Config

class TestUtils(unittest.TestCase):
    def test_supported_file_formats(self):
        self.assertTrue(is_supported_file("test.pdf"))
        self.assertTrue(is_supported_file("test.docx"))
        self.assertTrue(is_supported_file("test.txt"))
        self.assertFalse(is_supported_file("test.jpg"))
        self.assertFalse(is_supported_file("test.xlsx"))
    
    def test_file_size_validation(self):
        self.assertTrue(validate_file_size(1024))  # 1KB
        self.assertTrue(validate_file_size(Config.MAX_FILE_SIZE - 1))
        self.assertFalse(validate_file_size(Config.MAX_FILE_SIZE + 1))

if __name__ == '__main__':
    unittest.main()