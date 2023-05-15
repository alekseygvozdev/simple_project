import io
import unittest
from unittest.mock import patch
from example import hello_world

class TestHelloWorld(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_hello_world(self, mock_stdout):
        hello_world()
        self.assertEqual(mock_stdout.getvalue(), "Hello, World!\n")

if __name__ == '__main__':
    unittest.main()
