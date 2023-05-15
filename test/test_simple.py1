# файл test/ test_*.py
# файл test/ *_test.py

from io import StringIO
from unittest.mock import patch
from src.simple import hello_world

def test_hello_world(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
