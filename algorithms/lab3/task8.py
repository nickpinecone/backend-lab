"""
Лабораторная работа № 3
Задача № 8 Считаем комментарии
Порядковый номер 4
"""


def solve(text):
    star_comments = 0
    curly_comments = 0
    inline_comments = 0
    literal_strings = 0

    i = 0
    length = len(text)

    while i < length:
        if i + 1 < length and text[i] == "(" and text[i + 1] == "*":
            star_comments += 1
            i += 2
            while i + 1 < length and not (text[i] == "*" and text[i + 1] == ")"):
                i += 1
            i += 2

        elif text[i] == "{":
            curly_comments += 1
            i += 1
            while i < length and text[i] != "}":
                i += 1
            i += 1

        elif i + 1 < length and text[i] == "/" and text[i + 1] == "/":
            inline_comments += 1
            i += 2
            while i < length and text[i] != "\n":
                i += 1

        elif text[i] == "'":
            literal_strings += 1
            i += 1
            while i < length and text[i] != "'":
                i += 1
            i += 1

        else:
            i += 1

    return (star_comments, curly_comments, inline_comments, literal_strings)


def run_tests():
    test_cases = [
        {
            "input": """
program test;
(*just for testing *)
var
(* variables
note that
// here is not comment
and (* here is
not a begin of
another comment
*)
x: integer; (* *)
begin
write('(*is not comment//');
write(' and (*here*) '
,x // y);
End. // It is comment
""",
            "expected": (3, 0, 2, 2),
        },
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
