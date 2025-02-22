def min(a: int, b: int) -> int:
    if (a < b):
        return a
    else:
        return b


def solve(arr1: list[int], arr2: list[int]) -> int:
    i = 0
    j = 0
    result = 0

    while (i < len(arr1) and j < len(arr2)):
        if (arr1[i] == arr2[j]):
            result += 1
            i += 1
            j += 1
        elif (arr1[i] < arr2[j]):
            i += 1
        else:
            j += 1

    return result
