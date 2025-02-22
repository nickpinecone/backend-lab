import unittest
from task4 import solve


class TestTask4(unittest.TestCase):
    def test_1(self):
        input = (list[int]([1, 1, 2, 2, 3]), list[int]([0, 1, 3, 3, 4]))
        expected = 2

        self.assertEqual(solve(*input), expected)


if __name__ == '__main__':
    unittest.main()
