import unittest
from lab1.task2 import solve


class TestTask2(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
