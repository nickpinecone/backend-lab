import unittest
from lab2.task1 import solve


class TestTask1(unittest.TestCase):
    def test_1(self):
        input = ([19, 21, 100, 101, 1, 4, 5, 7, 12], 5)
        expected = 6

        self.assertEqual(solve(*input), expected)

    def test_2(self):
        input = ([5, 1, 2, 3, 4], 10)
        expected = -1

        self.assertEqual(solve(*input), expected)


if __name__ == '__main__':
    unittest.main()
