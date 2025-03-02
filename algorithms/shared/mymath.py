from functools import reduce


def min(a, b):
    if (a < b):
        return a
    else:
        return b


def max(a, b):
    if (a > b):
        return a
    else:
        return b


def abs(a):
    if (a < 0):
        a *= -1

    return a


def sum(arr: list):
    return reduce(lambda acc, val: acc + val, arr, 0)
