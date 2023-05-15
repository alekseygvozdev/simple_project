
import unittest
from unittest.mock import patch
from src.simple import hello_world

class TestHelloWorld(unittest.TestCase):
    @patch('src.simple.print')
    def test_hello_world(self, mock_print):
        hello_world()
        mock_print.assert_called_once_with('Hello, World!')

if __name__ == '__main__':
    unittest.main()
