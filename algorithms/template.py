"""
Лабораторная работа № Х
Задача № (подставить из файла) + название задачи
Порядковый номер (от 1 до 5)
"""


def solve(input_data):
    return input_data * 2


def run_tests():
    test_cases = [
        {"input": 10, "expected": 20},
        {"input": 5, "expected": 10},
        {"input": -3, "expected": -6},
        {"input": 0, "expected": 0},
    ]

    all_tests_passed = True

    for i, test_case in enumerate(test_cases, start=1):
        input_data = test_case["input"]
        expected_output = test_case["expected"]

        actual_output = solve(input_data)

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
