import unittest
from lab2.task8 import solve


class TestTask8(unittest.TestCase):
    cases = [
        {
            "visits": [
                "09:00 10:07",
                "10:20 11:35",
                "12:00 17:00",
                "11:00 11:30",
                "11:20 12:30",
                "11:30 18:15"
            ],
            "expected": 4
        },
        {
            "visits": [
                "00:00 00:00",
                "00:00 00:00",
                "00:00 00:00"
            ],
            "expected": 3
        },
        {
            "visits": [
                "10:10 10:20",
                "10:21 10:30"
            ],
            "expected": 1
        },
        {
            "visits": [
                "00:01 23:59",
                "00:00 00:00"
            ],
            "expected": 1
        },
        {
            "visits": [
                "09:00 10:30",
                "09:15 11:00",
                "09:30 11:15",
                "10:00 11:30",
                "10:15 11:45",
                "10:30 12:00",
                "11:00 12:30",
                "11:15 12:45",
                "11:30 13:00",
                "12:00 13:30"
            ],
            "expected": 6
        }, {
            "visits": [
                "09:30 11:15",
                "13:15 15:00",
                "08:30 10:30",
                "15:45 16:30",
                "12:30 16:45",
                "15:15 16:15",
                "14:30 15:30",
                "10:15 14:30",
                "15:30 16:30",
                "11:30 12:15"
            ],
            "expected": 4
        }

    ]

    def test_1(self):
        input = [
            "09:00 10:07",
            "10:20 11:35",
            "12:00 17:00",
            "11:00 11:30",
            "11:20 12:30",
            "11:30 18:15",
        ]

        expected = 4

        self.assertEqual(solve(input), expected)

    def test_cases(self):
        for case in self.cases:
            with self.subTest():
                self.assertEqual(
                    solve(case["visits"]), case["expected"])


if __name__ == '__main__':
    unittest.main()
