import unittest
from lab2.task3 import solve


class TestTask3(unittest.TestCase):
    cases = [
        {
            "arr": [-1, 2, 3, -4, -2, 5, -1, 5, -3, -2],
            "expected": 75
        },
        {
            "arr": [1, 2, 3, 4],
            "expected": 24
        },
        {
            "arr": [-10, -10, 5, 2],
            "expected": 500
        },
        {
            "arr": [1, 10, 2, 8, 3, 7, 4, 6, 5, 9],
            "expected": 720
        },
        {
            "arr": [-5, -6, -1, -2, -3, -4, 0, 1],
            "expected": 30
        }
    ]

    def test_1(self):
        input = [-1, 2, 3, -4, -2, 5, -1, 5, -3, -2]
        expected = 75

        self.assertEqual(solve(input), expected)

    def test_cases(self):
        for case in self.cases:
            with self.subTest():
                self.assertEqual(
                    solve(case["arr"]), case["expected"])


if __name__ == '__main__':
    unittest.main()
