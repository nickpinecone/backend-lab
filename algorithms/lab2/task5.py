"""
Лабораторная работа № 2
Задача 5 Оболочка
4
"""

import math


def rotate(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]):
    return (b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0])


def graham_scan(a: list[tuple[int, int]]):
    n = len(a)  # число точек
    p = [x for x in range(n)]  # список номеров точек

    for i in range(1, n):
        if a[p[i]][0] < a[p[0]][0]:  # если P[i]-ая точка лежит левее P[0]-ой точки
            p[i], p[0] = p[0], p[i]  # меняем местами номера этих точек

    for i in range(2, n):  # сортировка вставкой
        j = i
        while j > 1 and (rotate(a[p[0]], a[p[j-1]], a[p[j]]) < 0):
            p[j], p[j-1] = p[j-1], p[j]
            j -= 1

    S = [p[0], p[1]]  # создаем стек

    for i in range(2, n):
        while rotate(a[S[-2]], a[S[-1]], a[p[i]]) < 0:
            del S[-1]  # pop(S)

        S.append(p[i])  # push(S,P[i])

    return S


def distance(a: tuple[int, int], b: tuple[int, int]):
    return math.sqrt((b[0]-a[0])*(b[0]-a[0]) + (b[1]-a[1])*(b[1]-a[1]))


def solve(points: list[tuple[int, int]]) -> float:
    sorted = graham_scan(points)

    sum = 0
    for i in range(len(sorted) - 1):
        ind_1 = sorted[i]
        a = points[ind_1]

        ind_2 = sorted[i+1]
        b = points[ind_2]

        sum += distance(a, b)

    ind_1 = sorted[0]
    a = points[ind_1]

    ind_2 = sorted[len(sorted)-1]
    b = points[ind_2]
    sum += distance(a, b)

    return round(sum, 2)
