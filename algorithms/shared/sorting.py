def binary_search(arr: list, element) -> int:
    start = 0
    end = len(arr) - 1

    while (start <= end):
        middle = (start + end) // 2

        if (arr[middle] == element):
            return middle

        elif (arr[middle] < element):
            start = middle + 1

        else:
            end = middle - 1

    return -1


def quick_sort(arr: list, left: int, right: int, reverse: bool = False):
    if (left >= right):
        return

    pivot = (left + right) // 2
    l, r = left, right

    while (l <= r):
        if (reverse):
            while (arr[l] > arr[pivot]):
                l += 1
            while (arr[r] < arr[pivot]):
                r -= 1
        else:
            while (arr[l] < arr[pivot]):
                l += 1
            while (arr[r] > arr[pivot]):
                r -= 1

        if (l <= r):
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    quick_sort(arr, left, r, reverse)
    quick_sort(arr, l, right, reverse)
