import unittest
from lab2.task4 import solve, Record


class TestTask4(unittest.TestCase):
    cases = [
        {
            "priorities": [2, 1, 3],
            "data": [
                {
                    "key": "A",
                    "columns": [1, 2, 3]
                },
                {
                    "key": "B",
                    "columns": [3, 2, 1]
                },
                {
                    "key": "C",
                    "columns": [3, 1, 2]
                }
            ],
            "expected": ["B", "A", "C"]
        },
        {
            "priorities": [3, 1, 2],
            "data": [
                {
                    "key": "A",
                    "columns": [5, 10, 3]
                },
                {
                    "key": "B",
                    "columns": [7, 8, 2]
                },
                {
                    "key": "C",
                    "columns": [5, 10, 4]
                }
            ],
            "expected": ["C", "A", "B"]
        },
        {
            "priorities": [2, 4, 1, 3],
            "data": [
                {
                    "key": "D",
                    "columns": [10, 5, 12, 8]
                },
                {
                    "key": "E",
                    "columns": [9, 5, 11, 9]
                },
                {
                    "key": "F",
                    "columns": [10, 6, 12, 7]
                }
            ],
            "expected": ["F", "E", "D"]
        },
        {
            "priorities": [1, 3, 2],
            "data": [
                {
                    "key": "X",
                    "columns": [2, 7, 5]
                },
                {
                    "key": "Y",
                    "columns": [3, 6, 4]
                },
                {
                    "key": "Z",
                    "columns": [2, 8, 6]
                }
            ],
            "expected": ["Y", "Z", "X"]
        },
        {
            "priorities": [4, 2, 3, 1],
            "data": [
                {
                    "key": "M",
                    "columns": [5, 3, 7, 10]
                },
                {
                    "key": "N",
                    "columns": [4, 3, 6, 11]
                },
                {
                    "key": "O",
                    "columns": [5, 2, 7, 9]
                }
            ],
            "expected": ["N", "M", "O"]
        },
        {
            "priorities": [5, 3, 1, 2, 4],
            "data": [
                {
                    "key": "P",
                    "columns": [8, 4, 6, 2, 12]
                },
                {
                    "key": "Q",
                    "columns": [7, 5, 5, 3, 11]
                },
                {
                    "key": "R",
                    "columns": [8, 4, 6, 2, 13]
                }
            ],
            "expected": ["R", "P", "Q"]
        },
        {
            "priorities": [3, 1, 4, 2],
            "data": [
                {
                    "key": "A",
                    "columns": [5, 8, 12, 3]
                },
                {
                    "key": "B",
                    "columns": [7, 6, 10, 4]
                },
                {
                    "key": "C",
                    "columns": [5, 7, 11, 5]
                },
                {
                    "key": "D",
                    "columns": [6, 9, 13, 2]
                },
                {
                    "key": "E",
                    "columns": [8, 5, 9, 6]
                },
                {
                    "key": "F",
                    "columns": [7, 8, 10, 4]
                },
                {
                    "key": "G",
                    "columns": [6, 6, 12, 3]
                }
            ],
            "expected": ["D", "G", "A", "C", "F", "B", "E"]
        }
    ]

    def test_1(self):
        input = (
            [2, 1, 3],
            [
                Record("A", (1, 2, 3)),
                Record("B", (3, 2, 1)),
                Record("C", (3, 1, 2))
            ]
        )

        expected = ["B", "A", "C"]

        self.assertEqual(solve(*input), expected)

    def test_cases(self):
        for case in self.cases:
            with self.subTest():
                records = [Record(x["key"], tuple(x["columns"]))
                           for x in case["data"]]

                self.assertEqual(
                    solve(case["priorities"], records), case["expected"])


if __name__ == '__main__':
    unittest.main()
