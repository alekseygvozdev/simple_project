import unittest

def simple(x, y, name):
    sum = x + y
    result_str = f"Hello {name}, the sum of {x} and {y} is {sum}"
    return sum, result_str

class SimpleTest(unittest.TestCase):
    def test_simple(self):
        # Проверяем, что сумма вычисляется правильно
        x = 3
        y = 5
        name = "John"
        expected_sum = 8
        expected_result_str = f"Hello {name}, the sum of {x} and {y} is {expected_sum}"
        actual_sum, actual_result_str = simple(x, y, name)
        self.assertEqual(actual_sum, expected_sum)
        self.assertEqual(actual_result_str, expected_result_str)

if __name__ == '__main__':
    unittest.main()
