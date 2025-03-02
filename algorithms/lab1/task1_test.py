import unittest
from lab1.task1 import solve


class TestTask1(unittest.TestCase):
    def test_1(self):
        input = [0, 1, 4, 9, 0]
        expected = [0, 1, 2, 1, 0]

        self.assertSequenceEqual(solve(input), expected)

    def test_2(self):
        input = [0, 7, 9, 4, 8, 20]
        expected = [0, 1, 2, 3, 4, 5]

        self.assertSequenceEqual(solve(input), expected)


if __name__ == '__main__':
    unittest.main()
