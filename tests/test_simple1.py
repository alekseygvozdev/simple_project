
from io import StringIO
from unittest.mock import patch
import example

def test_hello_world(capsys):
    example.hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
