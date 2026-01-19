import unittest
from main import calculate_average

class TestCalculateAverage(unittest.TestCase):

    def test_normal_list(self):
        numbers = [2, 4, 6, 8]
        self.assertEqual(calculate_average(numbers), 5)

    def test_empty_list(self):
        numbers = []
        self.assertEqual(calculate_average(numbers), 0)

if __name__ == "__main__":
    unittest.main()
