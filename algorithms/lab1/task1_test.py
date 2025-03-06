import unittest
from lab1.task1 import solve


class TestTask1(unittest.TestCase):
    cases = [
        {
            "arr": [0, 1, 4, 9, 0],
            "expected": [0, 1, 2, 1, 0]
        },
        {
            "arr": [0, 7, 9, 4, 8, 20],
            "expected": [0, 1, 2, 3, 4, 5]
        },
        {
            "arr": [0, 0, 5, 8, 0, 3, 2, 0],
            "expected": [0, 0, 1, 1, 0, 1, 1, 0]
        },
        {
            "arr": [0, 7, 9, 4, 0, 20],
            "expected": [0, 1, 2, 1, 0, 1]
        },
        {
            "arr": [0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 8, 0],
            "expected": [0, 0, 0, 0, 0, 1, 2, 3, 4, 3, 2, 1, 0]
        }
    ]

    def test_1(self):
        input = [0, 1, 4, 9, 0]
        expected = [0, 1, 2, 1, 0]

        self.assertSequenceEqual(solve(input), expected)

    def test_2(self):
        input = [0, 7, 9, 4, 8, 20]
        expected = [0, 1, 2, 3, 4, 5]

        self.assertSequenceEqual(solve(input), expected)

    def test_cases(self):
        for case in self.cases:
            with self.subTest():
                self.assertSequenceEqual(solve(case["arr"]), case["expected"])


if __name__ == '__main__':
    unittest.main()
