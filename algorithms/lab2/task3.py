"""
Лабораторная работа № 2
Задача 3 Максимальная тройка
3
"""

from shared.mymath import max


def solve(arr: list[int]) -> int:
    min1, min2 = arr[0], arr[0]
    max1, max2, max3 = arr[0], arr[0], arr[0]

    for i in arr:
        if (i > max1):
            max3 = max2
            max2 = max1
            max1 = i

        elif (i > max2):
            max3 = max2
            max2 = i

        elif (i > max3):
            max3 = i

        elif (i < min1):
            min2 = min1
            min1 = i

        elif (i < min2):
            min2 = i

    return max(max1 * max2 * max3, min1 * min2 * max1)
