import unittest
from lab2.task1 import solve


class TestTask1(unittest.TestCase):
    cases = [
        {
            "arr": [19, 21, 100, 101, 1, 4, 5, 7, 12],
            "val": 5,
            "expected": 6
        },
        {
            "arr": [19, 21, 100, 101, 1, 4, 5, 7, 12],
            "val": 100,
            "expected": 2
        },
        {
            "arr": [19, 21, 100, 101, 1, 4, 5, 7, 12],
            "val": 7,
            "expected": 7
        },
        {
            "arr": [19, 21, 100, 101, 1, 4, 5, 7, 12],
            "val": 21,
            "expected": 1
        },
        {
            "arr": [-5, -4, -1, 0, 2, 5, 8, 12, 17, 21],
            "val": 5,
            "expected": 5
        },
        {
            "arr": [-5, -4, -1, 0, 2, 5, 8, 12, 17, 21],
            "val": 3,
            "expected": -1
        },
        {
            "arr": [-5, -4, -1, 0, 2, 5, 8, 12, 17, 21],
            "val": -8,
            "expected": -1
        }
    ]

    def test_1(self):
        input = ([19, 21, 100, 101, 1, 4, 5, 7, 12], 5)
        expected = 6

        self.assertEqual(solve(*input), expected)

    def test_2(self):
        input = ([5, 1, 2, 3, 4], 10)
        expected = -1

        self.assertEqual(solve(*input), expected)

    def test_cases(self):
        for case in self.cases:
            with self.subTest():
                self.assertEqual(
                    solve(case["arr"], case["val"]), case["expected"])


if __name__ == '__main__':
    unittest.main()
