from functools import reduce


def sum(arr: list[int]):
    return reduce(lambda acc, val: acc + val, arr, 0)


def max(a: int, b: int) -> int:
    if (a > b):
        return a
    else:
        return b


def calc(stones: list[int], i: int, sum: int, half_sum: float) -> int:
    if (i >= len(stones)):
        return sum

    result_with = 0

    if (sum + stones[i] < half_sum):
        result_with = calc(stones, i+1, sum + stones[i], half_sum)

    result_without = calc(stones, i+1, sum, half_sum)

    return max(result_with, result_without)


def solve(stones: list[int]) -> int:
    stones_sum = sum(stones)
    half_sum = stones_sum / 2

    result = stones_sum - (calc(stones, 0, 0, half_sum) * 2)

    return result
