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
        {"n": 4, "x": 1, "y": 1, "expected": 3},
        {"n": 5, "x": 1, "y": 2, "expected": 4},
        {"n": 78, "x": 9, "y": 13, "expected": 423},
        {"n": 8, "x": 8, "y": 3, "expected": 19},
        {"n": 7, "x": 7, "y": 7, "expected": 28},
        {"n": 15, "x": 1, "y": 5, "expected": 13},
    ]

    all_tests_passed = True

    for i, test_case in enumerate(test_cases, start=1):
        input_data = (test_case["n"], test_case["x"], test_case["y"])
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
