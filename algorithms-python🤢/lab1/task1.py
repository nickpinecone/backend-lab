def min(a: int, b: int) -> int:
    if (a < b):
        return a
    else:
        return b


def solve(distances: list[int]) -> list[int]:
    to_zero = 0
    result = list[int]()

    for i in range(len(distances)):
        if (distances[i] == 0):
            to_zero = 0
            result.append(to_zero)
        else:
            to_zero += 1
            result.append(to_zero)

    for i in range(len(distances) - 1, -1, -1):
        if (distances[i] == 0):
            to_zero = 0
        else:
            to_zero += 1
            result[i] = min(result[i], to_zero)

    return result
