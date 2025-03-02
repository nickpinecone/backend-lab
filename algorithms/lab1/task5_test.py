import unittest
from lab1.task5 import solve


class TestTask5(unittest.TestCase):
    def test_1(self):
        input = ("1", "-", "10")
        expected = "-9"

        self.assertEqual(solve(*input), expected)

    def test_2(self):
        input = ("-1", "-", "10")
        expected = "-11"

        self.assertEqual(solve(*input), expected)

    def test_3(self):
        input = ("-1000", "-", "-100")
        expected = "-900"

        self.assertEqual(solve(*input), expected)


if __name__ == '__main__':
    unittest.main()
