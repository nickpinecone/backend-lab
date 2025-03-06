import unittest
from lab1.task2 import solve


class TestTask2(unittest.TestCase):
    cases = [
        {
            "board": "1231\n2..2\n2..2\n2..2\n",
            "k": 3,
            "expected": 2
        },
        {
            "board": "1111\n9999\n1111\n9911",
            "k": 4,
            "expected": 1
        },
        {
            "board": "1111\n1111\n1111\n1111",
            "k": 4,
            "expected": 0
        },
        {
            "board": "1221\n1331\n1331\n1221",
            "k": 4,
            "expected": 3
        },
        {
            "board": "....\n....\n....\n1111",
            "k": 2,
            "expected": 1
        }
    ]

    def test_1(self):
        input = (3, [1, 2, 3, 1, 2, 2, 2, 2, 2, 2])
        expected = 2

        self.assertEqual(solve(*input), expected)

    def test_2(self):
        input = (4, [1, 1, 1, 1, 9, 9, 9, 9, 1, 1, 1, 1, 9, 9, 1, 1])
        expected = 1

        self.assertEqual(solve(*input), expected)

    def test_3(self):
        input = (4, [1 for x in range(16)])
        expected = 0

        self.assertEqual(solve(*input), expected)

    def test_cases(self):
        for case in self.cases:
            with self.subTest():
                arr = case["board"]
                arr = list(map(int, arr.replace(
                    ".", "").replace("\n", "")))

                self.assertEqual(
                    solve(case["k"], arr), case["expected"])


if __name__ == '__main__':
    unittest.main()
