"""
Лабораторная работа № 2
Задача 4 Сортировка по многим полям
2
"""

from shared.sorting import quick_sort


class Record:
    name = ""
    values: tuple[int, ...] = ()

    def __init__(self, name: str, values: tuple[int, ...]):
        self.name = name
        self.values = values

    def __gt__(self, other):
        return self.values > other.values

    def __lt__(self, other):
        return self.values < other.values


def solve(placements: list[int], records: list[Record]) -> list[str]:
    for record in records:
        temp: list[int] = []

        for placement in placements:
            temp.append(record.values[placement-1])

        record.values = tuple(temp)

    quick_sort(records, 0, len(records) - 1, reverse=True)

    return [x.name for x in records]
