import unittest
from lab1.task5 import solve


class TestTask5(unittest.TestCase):
    cases = [
        {
            "operand1": "20",
            "operation": "+",
            "operand2": "40",
            "expected": "60"
        },
        {
            "operand1": "20",
            "operation": "+",
            "operand2": "-40",
            "expected": "-20"
        },
        {
            "operand1": "20",
            "operation": "-",
            "operand2": "40",
            "expected": "-20"
        },
        {
            "operand1": "20",
            "operation": "-",
            "operand2": "-40",
            "expected": "60"
        },
        {
            "operand1": "-20",
            "operation": "+",
            "operand2": "40",
            "expected": "20"
        },
        {
            "operand1": "-20",
            "operation": "-",
            "operand2": "40",
            "expected": "-60"
        },
        {
            "operand1": "-20",
            "operation": "+",
            "operand2": "-40",
            "expected": "-60"
        },
        {
            "operand1": "-20",
            "operation": "-",
            "operand2": "-40",
            "expected": "20"
        },

        {
            "operand1": "200",
            "operation": "+",
            "operand2": "40",
            "expected": "240"
        },
        {
            "operand1": "20",
            "operation": "+",
            "operand2": "-400",
            "expected": "-380"
        },
        {
            "operand1": "2000",
            "operation": "-",
            "operand2": "40",
            "expected": "1960"
        },
        {
            "operand1": "200000",
            "operation": "-",
            "operand2": "-4000",
            "expected": "204000"
        },
        {
            "operand1": "-2000",
            "operation": "+",
            "operand2": "40000000",
            "expected": "39998000"
        },
        {
            "operand1": "-20000",
            "operation": "-",
            "operand2": "40",
            "expected": "-20040"
        },
        {
            "operand1": "-2000",
            "operation": "+",
            "operand2": "-40",
            "expected": "-2040"
        },
        {
            "operand1": "-20",
            "operation": "-",
            "operand2": "-4000",
            "expected": "3980"
        },
        {
            "operand1": "12345678901234567890",
            "operation": "+",
            "operand2": "98765432109876543210",
            "expected": "111111111011111111100"
        },
        {
            "operand1": "-12345678901234567890",
            "operation": "+",
            "operand2": "-98765432109876543210",
            "expected": "-111111111011111111100"
        },
        {
            "operand1": "12345678901234567890",
            "operation": "-",
            "operand2": "98765432109876543210",
            "expected": "-86419753208641975320"
        },
        {
            "operand1": "-12345678901234567890",
            "operation": "-",
            "operand2": "98765432109876543210",
            "expected": "-111111111011111111100"
        },
        {
            "operand1": "0",
            "operation": "+",
            "operand2": "40",
            "expected": "40"
        },
        {
            "operand1": "0",
            "operation": "-",
            "operand2": "40",
            "expected": "-40"
        },
        {
            "operand1": "40",
            "operation": "+",
            "operand2": "0",
            "expected": "40"
        },
        {
            "operand1": "40",
            "operation": "-",
            "operand2": "0",
            "expected": "40"
        },
        {
            "operand1": "0",
            "operation": "+",
            "operand2": "0",
            "expected": "0"
        },
        {
            "operand1": "0",
            "operation": "-",
            "operand2": "0",
            "expected": "0"
        },
        {
            "operand1": "123",
            "operation": "+",
            "operand2": "-456",
            "expected": "-333"
        },
        {
            "operand1": "-123",
            "operation": "+",
            "operand2": "456",
            "expected": "333"
        },
        {
            "operand1": "123",
            "operation": "-",
            "operand2": "-456",
            "expected": "579"
        },
        {
            "operand1": "-123",
            "operation": "-",
            "operand2": "-456",
            "expected": "333"
        },
        {
            "operand1": "99999999999999999999",
            "operation": "+",
            "operand2": "1",
            "expected": "100000000000000000000"
        },
        {
            "operand1": "-99999999999999999999",
            "operation": "+",
            "operand2": "-1",
            "expected": "-100000000000000000000"
        },
        {
            "operand1": "99999999999999999999",
            "operation": "-",
            "operand2": "1",
            "expected": "99999999999999999998"
        },
        {
            "operand1": "-99999999999999999999",
            "operation": "-",
            "operand2": "-1",
            "expected": "-99999999999999999998"
        },
        {
            "operand1": "12345678901234567890",
            "operation": "+",
            "operand2": "98765432109876543210",
            "expected": "111111111011111111100"
        },
        {
            "operand1": "12345678901234567890",
            "operation": "-",
            "operand2": "98765432109876543210",
            "expected": "-86419753208641975320"
        },
        {
            "operand1": "12345678901234567890",
            "operation": "+",
            "operand2": "0",
            "expected": "12345678901234567890"
        },
        {
            "operand1": "12345678901234567890",
            "operation": "-",
            "operand2": "0",
            "expected": "12345678901234567890"
        },
        {
            "operand1": "0",
            "operation": "+",
            "operand2": "12345678901234567890",
            "expected": "12345678901234567890"
        },
        {
            "operand1": "0",
            "operation": "-",
            "operand2": "12345678901234567890",
            "expected": "-12345678901234567890"
        },
        {
            "operand1": "12345678901234567890",
            "operation": "+",
            "operand2": "-12345678901234567890",
            "expected": "0"
        },
        {
            "operand1": "12345678901234567890",
            "operation": "-",
            "operand2": "12345678901234567890",
            "expected": "0"
        },
        {
            "operand1": "-12345678901234567890",
            "operation": "+",
            "operand2": "12345678901234567890",
            "expected": "0"
        },
        {
            "operand1": "-12345678901234567890",
            "operation": "-",
            "operand2": "-12345678901234567890",
            "expected": "0"
        },
        {
            "operand1": "123",
            "operation": "+",
            "operand2": "4567",
            "expected": "4690"
        },
        {
            "operand1": "123",
            "operation": "-",
            "operand2": "4567",
            "expected": "-4444"
        },
        {
            "operand1": "4567",
            "operation": "+",
            "operand2": "123",
            "expected": "4690"
        },
        {
            "operand1": "4567",
            "operation": "-",
            "operand2": "123",
            "expected": "4444"
        },
        {
            "operand1": "-123",
            "operation": "+",
            "operand2": "-4567",
            "expected": "-4690"
        },
        {
            "operand1": "-123",
            "operation": "-",
            "operand2": "-4567",
            "expected": "4444"
        }
    ]

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

    def test_cases(self):
        for case in self.cases:
            with self.subTest():
                self.assertEqual(
                    solve(case["operand1"], case["operation"], case["operand2"]), case["expected"])


if __name__ == '__main__':
    unittest.main()
