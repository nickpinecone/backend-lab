import unittest
from lab2.task8 import solve


class TestTask8(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
