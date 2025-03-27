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

    return {
        "first": star_comments,
        "second": curly_comments,
        "third": inline_comments,
        "fourth": literal_strings,
    }


def run_tests():
    test_cases = [
        {
            "code": "program test; (* just for testing *) begin end.",
            "expected": {"first": 1, "second": 0, "third": 0, "fourth": 0},
        },
        {
            "code": "program test; { just for testing } begin end.",
            "expected": {"first": 0, "second": 1, "third": 0, "fourth": 0},
        },
        {
            "code": "program test; // just for testing\nbegin end.",
            "expected": {"first": 0, "second": 0, "third": 1, "fourth": 0},
        },
        {
            "code": "program test; writeln('Hello, World!'); begin end.",
            "expected": {"first": 0, "second": 0, "third": 0, "fourth": 1},
        },
        {
            "code": "program test;\n(* comment 1 *)\n{ comment 2 }\n// comment 3\nwriteln('text'); begin end.",
            "expected": {"first": 1, "second": 1, "third": 1, "fourth": 1},
        },
        {
            "code": "program test;\n(* comment (* nested *) still comment *)\nbegin end.",
            "expected": {"first": 1, "second": 0, "third": 0, "fourth": 0},
        },
        {
            "code": "program test;\nwrite('(* is not comment // ');\nwrite(' and (*here*) ', x // y);\n) end. // It is comment",
            "expected": {"first": 0, "second": 0, "third": 2, "fourth": 2},
        },
        {
            "code": "program test;\n(* comment 1 *)\n(* comment 2 *)\nbegin end.",
            "expected": {"first": 2, "second": 0, "third": 0, "fourth": 0},
        },
        {
            "code": "program test;\n{ comment 1 }\n{ comment 2 }\nbegin end.",
            "expected": {"first": 0, "second": 2, "third": 0, "fourth": 0},
        },
        {
            "code": "program test;\n// comment 1\n// comment 2\nbegin end.",
            "expected": {"first": 0, "second": 0, "third": 2, "fourth": 0},
        },
        {
            "code": "program test;\nwriteln('text 1');\nwriteln('text 2');\nbegin end.",
            "expected": {"first": 0, "second": 0, "third": 0, "fourth": 2},
        },
        {
            "code": "program test;\n(* comment *)\n{ another comment }\n// yet another comment\nwriteln('comments are tricky');\nbegin end.",
            "expected": {"first": 1, "second": 1, "third": 1, "fourth": 1},
        },
        {
            "code": "program test;\n(* comment *)\nwrite('(* is not comment *)');\n// comment after string\nbegin end.",
            "expected": {"first": 1, "second": 0, "third": 1, "fourth": 1},
        },
        {
            "code": "program test;\n(* comment (* nested *) *)\nwrite('(* still not comment *)');\nbegin end.",
            "expected": {"first": 1, "second": 0, "third": 0, "fourth": 1},
        },
        {
            "code": "program test;\n{ comment { nested } }\nwrite('{ not a comment }');\nbegin end.",
            "expected": {"first": 0, "second": 1, "third": 0, "fourth": 1},
        },
    ]

    all_tests_passed = True

    for i, test_case in enumerate(test_cases, start=1):
        input_data = test_case["code"]
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
