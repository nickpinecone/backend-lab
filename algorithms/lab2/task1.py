"""
Лабораторная работа № 2
Задача 1 Поиск в сломанном массиве
1
"""


def solve(arr: list, element) -> int:
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle = (start + end) // 2

        if arr[middle] == element:
            return middle

        if arr[start] <= arr[middle]:
            if arr[start] <= element < arr[middle]:
                end = middle - 1
            else:
                start = middle + 1
        else:
            if arr[middle] < element <= arr[end]:
                start = middle + 1
            else:
                end = middle - 1
    return -1
