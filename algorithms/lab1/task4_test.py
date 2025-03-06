import unittest
from lab1.task4 import solve


class TestTask4(unittest.TestCase):
    cases = [
        {
            "first_arr": [1, 1, 2, 2, 3],
            "second_arr": [0, 1, 3, 3, 4],
            "expected": 2
        },
        {
            "first_arr": [1, 1, 2, 2, 3, 4, 5, 7, 7],
            "second_arr": [0, 1, 3, 3, 4, 7, 8],
            "expected": 4
        },
        {
            "first_arr": [0, 1, 1, 2, 2, 3, 3, 4, 5, 9],
            "second_arr": [0, 1, 3, 3, 4, 7, 8, 9],
            "expected": 6
        }
    ]

    def test_1(self):
        input = ([1, 1, 2, 2, 3], [0, 1, 3, 3, 4])
        expected = 2

        self.assertEqual(solve(*input), expected)

    def test_cases(self):
        for case in self.cases:
            with self.subTest():
                self.assertEqual(
                    solve(case["first_arr"], case["second_arr"]), case["expected"])


if __name__ == '__main__':
    unittest.main()
