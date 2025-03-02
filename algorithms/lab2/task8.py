"""
Лабораторная работа № 2
Задача 8 Музей
5
"""

from shared.sorting import quick_sort
from shared.mymath import max


def to_minutes(time: str) -> int:
    split = time.split(":")
    hours = int(split[0])
    minutes = int(split[1])

    return hours * 60 + minutes


def solve(arrivals: list[str]) -> int:
    arr: list[tuple[int, int]] = []

    for arrival in arrivals:
        split = arrival.split(" ")

        arr.append((to_minutes(split[0]), -1))
        arr.append((to_minutes(split[1]), 1))

    quick_sort(arr, 0, len(arr)-1)

    max_guests = 0
    current = 0
    for i in arr:
        current -= i[1]
        max_guests = max(current, max_guests)

    return max_guests
