import unittest
from lab2.task5 import solve


class TestTask5(unittest.TestCase):
    cases = [
        {
            "points": [
                [0, 1],
                [1, 0],
                [-1, 0],
                [0, -1],
                [0, 0]
            ],
            "expected": "5.66"
        },
        {
            "points": [[0, 0], [3, 0], [1, 2], [3, 2], [3, 1], [3, 2]],
            "expected": "9.24"
        },
        {
            "points": [[1, 1], [4, 0], [4, 3], [2, 3], [3, 2], [2, 1], [4, 1]],
            "expected": "10.4"
        },
        {
            "points":  [[0, 0], [2, 3], [3, 2], [3, -1], [1, -3], [0, 3], [2, -1], [1, 3]],
            "expected": "15.4"
        },
        {
            "points": [[1, 0], [2, 2], [0, 3], [-2, 1], [-2, 0], [-2, -2], [0, 1], [0, 2], [0, 2]],
            "expected": "14.67"
        },
        {
            "points":  [[1, 2], [3, 4], [6, 3], [4, 0], [1, -1], [2, 0], [5, 2], [3, 0]],
            "expected": "15.76"
        },
        {
            "points":  [[0, 0], [1, 4], [3, 0], [1, -4], [-1, -3], [-4, 0], [-2, 4], [1, -2], [1, -1], [-1, 1]],
            "expected": "22.9"
        },
        {
            "points":  [[0, 2], [1, 3], [1, 2], [3, 0], [1, -1], [0, -3], [0, -1], [0, -3], [-1, -1], [-3, 0], [-2, 2], [-1, 2], [0, 1], [0, 0], [0, 0]],
            "expected": "20.12"
        },
        {
            "points":  [[0, 0], [1, 1], [2, 3], [1, 5], [0, 3], [-1, 4], [-3, 2], [-1, 0], [-3, 0], [-2, -3], [0, -1], [1, -3], [2, -1], [0, 0], [0, 3], [0, 3]],
            "expected": "26.86"
        }
    ]

    def test_1(self):
        input = [
            (2, 1),
            (2, 2),
            (2, 3),
            (3, 2),
            (1, 2)
        ]

        expected = 5.66

        self.assertEqual(solve(input), expected)

    def test_cases(self):
        for case in self.cases:
            with self.subTest():
                self.assertEqual(
                    solve(case["points"]), float(case["expected"]))


if __name__ == '__main__':
    unittest.main()
