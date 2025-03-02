import unittest
from lab2.task5 import solve


class TestTask5(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
