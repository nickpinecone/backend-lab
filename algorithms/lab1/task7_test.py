import unittest
from lab1.task7 import solve


class TestTask7(unittest.TestCase):
    def test_1(self):
        input = [8, 9, 6, 9, 8]
        expected = 4

        self.assertEqual(solve(input), expected)

    def test_2(self):
        input = [14, 2, 12, 9, 9, 8]
        expected = 2

        self.assertEqual(solve(input), expected)


if __name__ == '__main__':
    unittest.main()
