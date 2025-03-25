"""
Лабораторная работа № 4
Задача № 5 Ксерокопии
Порядковый номер 3
"""

import math


def solve(N, x, y):
    k1 = (y * N) / (x + y)
    k2 = (x * N) / (x + y)

    t1 = math.floor(k1) * x
    t2 = math.floor(k2) * y

    T = max(t1, t2) + min(x, y)

    return T


def run_tests():
    test_cases = [
        {"N": 4, "x": 1, "y": 1, "expected": 3},
        {"N": 5, "x": 1, "y": 2, "expected": 4},
        {"N": 78, "x": 9, "y": 13, "expected": 423},
        {"N": 200000000, "x": 1, "y": 1, "expected": 100000001},
        {"N": 6, "x": 2, "y": 2, "expected": 8},
    ]

    all_tests_passed = True

    for i, test_case in enumerate(test_cases, start=1):
        input_data = (test_case["N"], test_case["x"], test_case["y"])
        expected_output = test_case["expected"]

        actual_output = solve(*input_data)

        if actual_output == expected_output:
            print(f"Test case {i}: PASSED ✅")
        else:
            all_tests_passed = False
            print(f"Test case {i}: FAILED ❌")
            print(f"  Input: {input_data}")
            print(f"  Expected output: {expected_output}")
            print(f"  Actual output: {actual_output}")

    if all_tests_passed:
        print("Все тесты пройдены, поставьте 5 😅!")
    else:
        print("Что-то пошло не так, только не бейте 🥺")


if __name__ == "__main__":
    run_tests()
