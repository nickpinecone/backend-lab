import unittest
from lab2.task4 import solve, Record


class TestTask4(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
