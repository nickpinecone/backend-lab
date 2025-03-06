import unittest
from lab1.task7 import solve


class TestTask7(unittest.TestCase):
    cases = [
        {
            "stones": [6, 7, 9, 13, 18, 24, 31, 50],
            "expected": 0
        },
        {
            "stones": [8, 9, 6, 9, 8],
            "expected": 4
        },
        {
            "stones": [14, 2, 12, 9, 9, 8],
            "expected": 2
        },
        {
            "stones": [15, 16, 30, 2],
            "expected": 1
        },
        {
            "stones": [5, 8, 13, 27, 14],
            "expected": 3
        },
        {
            "stones": [15, 7, 8, 24, 6, 4, 10, 4, 17],
            "expected": 1
        }
    ]

    def test_1(self):
        input = [8, 9, 6, 9, 8]
        expected = 4

        self.assertEqual(solve(input), expected)

    def test_2(self):
        input = [14, 2, 12, 9, 9, 8]
        expected = 2

        self.assertEqual(solve(input), expected)

    def test_cases(self):
        for case in self.cases:
            with self.subTest():
                self.assertEqual(
                    solve(case["stones"]), case["expected"])


if __name__ == '__main__':
    unittest.main()
