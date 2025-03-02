"""
Лабораторная работа № 1
Задача 5 Длинное сложение и вычитание
4
"""

from shared.mymath import max


def normalize(a: str, b: str) -> tuple[str, str]:
    length = max(len(a), len(b))

    a = ("0" * (length - len(a))) + a
    b = ("0" * (length - len(b))) + b

    return (a, b)


def denormalize(a: str) -> str:
    result = a

    for i in range(len(a)):
        if (a[i] != '0' and a[i] != '-'):
            break

        if (a[i] == '0'):
            result = result.replace('0', '', 1)

    return result


def sum(a: str, b: str) -> str:
    result: list[str] = []
    digit = 0

    for i in range(len(a)-1, -1, -1):
        num1 = int(a[i])
        num2 = int(b[i])

        sum = num1 + num2 + digit

        result.append(str(sum % 10))

        digit = 0
        if (sum >= 10):
            digit = 1

    if (digit > 0):
        result.append(str(digit))

    return "".join(result[::-1])


def compare(a: str, b: str) -> int:
    for i in range(len(a)):
        if (a[i] > b[i]):
            return 1
        elif (a[i] < b[i]):
            return -1

    return 0


def sub(a: str, b: str, neg_compare=-1) -> str:
    result: list[str] = []
    digit = 0

    compare_result = compare(a, b)

    if (compare_result == -1):
        a, b = b, a

    for i in range(len(a) - 1, -1, -1):
        num1 = int(a[i])
        num2 = int(b[i])

        diff = num1 - num2 - digit

        result.append(str(diff % 10))

        digit = 0
        if (diff < 0):
            digit = 1

    if (compare_result == neg_compare):
        result.append("-")

    return "".join(result[::-1])


def solve(a: str, operand: str, b: str) -> str:
    a_sign = '-' if a.startswith('-') else '+'
    b_sign = '-' if b.startswith('-') else '+'

    a = a.replace('-', '')
    b = b.replace('-', '')

    a, b = normalize(a, b)

    result = ""

    match (a_sign, operand, b_sign):
        case ["+", "+", "+"]:
            result = sum(a, b)

        case ["+", "-", "-"]:
            result = sum(a, b)

        case ["-", "+", "-"]:
            result = "-" + sum(a, b)

        case ["-", "-", "+"]:
            result = "-" + sum(a, b)

        case ["+", "-", "+"]:
            result = sub(a, b, -1)

        case ["-", "-", "-"]:
            result = sub(a, b, 1)

        case ["-", "+", "+"]:
            result = sub(a, b, 1)

        case ["+", "+", "-"]:
            result = sub(a, b, -1)

    return denormalize(result)
