import unittest
from lab1.task4 import solve


class TestTask4(unittest.TestCase):
    def test_1(self):
        input = ([1, 1, 2, 2, 3], [0, 1, 3, 3, 4])
        expected = 2

        self.assertEqual(solve(*input), expected)


if __name__ == '__main__':
    unittest.main()
