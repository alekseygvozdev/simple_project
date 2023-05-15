
import unittest

class TestSimple(unittest.TestCase):
    def test_simple(self):
        x = 5
        y = 10
        name = "John"
        expected_sum = 15
        expected_str = "Hello John, the sum of 5 and 10 is 15"
        actual_sum, actual_str = simple(x, y, name)
        self.assertEqual(expected_sum, actual_sum)
        self.assertEqual(expected_str, actual_str)

if __name__ == '__main__':
    unittest.main()
