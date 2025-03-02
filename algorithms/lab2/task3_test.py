import unittest
from lab2.task3 import solve


class TestTask3(unittest.TestCase):
    def test_1(self):
        input = [-1, 2, 3, -4, -2, 5, -1, 5, -3, -2]
        expected = 75

        self.assertEqual(solve(input), expected)


if __name__ == '__main__':
    unittest.main()
