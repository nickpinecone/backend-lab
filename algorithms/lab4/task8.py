"""
Лабораторная работа № 4
Задача № 8 Поиск множеств
Порядковый номер 4
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


class BTree:
    def __init__(self):
        self.root = Node(None)

    def insert(self, node, arr: list[int]):
        if len(arr) <= 0:
            return

        first = arr[0]

        for child in node.children:
            if child.value == first:
                return self.insert(child, arr[1:])

        child = Node(first)
        node.children.append(child)
        self.insert(child, arr[1:])

    def append(self, arr: list[int]):
        arr.sort()
        self.insert(self.root, arr)

    def search(self, node, arr: list[int]):
        if len(arr) <= 0:
            return True

        first = arr[0]

        for child in node.children:
            if child.value == first:
                return self.search(child, arr[1:])

        return False

    def has(self, arr: list[int]):
        arr.sort()
        result = self.search(self.root, arr)
        return result


def solve(standards: list[list[int]], tests: list[list[int]]):
    b_tree = BTree()
    output = []

    for standard in standards:
        b_tree.append(standard)

    for test in tests:
        output.append(str(int(b_tree.has(test))))

    return output


def run_tests():
    test_cases = [
        {
            "data": [
                [6, 5, 1],
                [7, 9, 3],
                [2, 3, 2],
                [7, 2, 9],
                [9, 6, 2],
                [6, 6, 6],
                [9, 4, 1],
                [8, 4, 4],
                [8, 3, 2],
                [1, 2, 6],
            ],
            "queries": [[9, 7, 2], [1, 6, 5], [3, 7, 7], [4, 4, 6], [3, 9, 7]],
            "expected": ["1", "1", "0", "0", "1"],
        },
        {
            "data": [
                [8, 4, 0, 3, 6, 9, 2],
                [3, 5, 0, 4, 3, 1, 1],
                [7, 1, 0, 3, 1, 2, 4],
                [7, 1, 5, 1, 5, 5, 1],
                [3, 4, 0, 0, 3, 4, 0],
                [3, 3, 3, 6, 3, 9, 3],
                [3, 4, 1, 3, 1, 8, 1],
                [1, 1, 6, 8, 6, 8, 2],
                [5, 6, 8, 1, 3, 9, 3],
                [7, 5, 7, 1, 4, 0, 3],
            ],
            "queries": [
                [1, 1, 3, 3, 8, 4, 1],
                [2, 1, 1, 6, 6, 8, 8],
                [1, 1, 5, 7, 5, 1, 5],
                [3, 4, 1, 3, 1, 1, 8],
                [0, 0, 1, 2, 8, 2, 6],
            ],
            "expected": ["1", "1", "1", "1", "0"],
        },
        {
            "data": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "queries": [[3, 2, 1], [6, 5, 4], [10, 11, 12]],
            "expected": ["1", "1", "0"],
        },
        {
            "data": [[5, 5, 5], [5, 5, 5], [5, 5, 5]],
            "queries": [[5, 5, 5], [5, 5, 6]],
            "expected": ["1", "0"],
        },
        {
            "data": [[0, 0, 0], [0, 0, 1], [0, 1, 1], [1, 1, 1]],
            "queries": [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 1]],
            "expected": ["1", "1", "1", "1"],
        },
        {
            "data": [
                [10, 20, 30],
                [20, 30, 10],
                [30, 10, 20],
                [10, 10, 10],
                [20, 20, 20],
            ],
            "queries": [[10, 20, 30], [10, 10, 10], [20, 20, 20], [30, 20, 10]],
            "expected": ["1", "1", "1", "1"],
        },
    ]

    all_tests_passed = True

    for i, test_case in enumerate(test_cases, start=1):
        input_data = (test_case["data"], test_case["queries"])
        expected_output = test_case["expected"]

        actual_output = solve(*input_data)

        if actual_output == expected_output:
            print(f"Test case {i}: PASSED ✅")
        else:
            all_tests_passed = False
            print(f"Test case {i}: FAILED ❌")
            print(f"  Input: {input_data}")
            print(f"  Expected output: {expected_output}")
            print(f"  Actual output: {actual_output}")

    if all_tests_passed:
        print("Все тесты пройдены, поставьте 5 😅!")
    else:
        print("Что-то пошло не так, только не бейте 🥺")


if __name__ == "__main__":
    run_tests()
