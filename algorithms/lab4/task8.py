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
        output.append(int(b_tree.has(test)))

    return output


def run_tests():
    test_cases = [
        {
            "standards": [
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
            "tests": [[9, 7, 2], [1, 6, 5], [3, 7, 7], [4, 4, 6], [3, 9, 7]],
            "expected": [1, 1, 0, 0, 1],
        },
    ]

    all_tests_passed = True

    for i, test_case in enumerate(test_cases, start=1):
        input_data = (test_case["standards"], test_case["tests"])
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
