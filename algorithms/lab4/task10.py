"""
Лабораторная работа № 4
Задача № 10 Анаграммы
Порядковый номер 5
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


class BTree:
    def __init__(self):
        self.root = Node(None)

    def insert(self, node, arr: list[str]):
        if len(arr) <= 0:
            return

        first = arr[0]

        for child in node.children:
            if child.value == first:
                return self.insert(child, arr[1:])

        child = Node(first)
        node.children.append(child)
        self.insert(child, arr[1:])

    def append(self, word: str):
        word_arr = sorted(word)
        self.insert(self.root, word_arr)

    def traverse(self, node):
        if len(node.children) <= 0:
            return 1

        sum = 0
        for child in node.children:
            sum += self.traverse(child)

        return sum

    def count(self):
        return self.traverse(self.root)


def solve(words):
    b_tree = BTree()

    for word in words:
        b_tree.append(word)

    return b_tree.count()


def run_tests():
    test_cases = [
        {
            "data": ["BCB", "ABA", "BCB", "BAA", "BBC", "CCB", "CBC", "CBC"],
            "expected": 3,
        },
        {"data": ["LOOP", "POOL", "POLO"], "expected": 1},
        {"data": ["ABC", "CAB", "BAC", "XYZ", "ZYX"], "expected": 2},
        {"data": ["AAAA", "AAAA", "AAAA"], "expected": 1},
        {"data": ["LOOP", "POOL", "POLO", "XYZZ", "ZZYX", "ABCD"], "expected": 3},
        {"data": ["CAT", "DOG", "ACT", "GOD", "TAC", "ODG"], "expected": 2},
        {"data": ["AAAAA", "BBBBB", "CCCCC"], "expected": 3},
        {"data": ["ABCDE", "EDCBA", "BCDEA", "FGHIJ", "JIHGF"], "expected": 2},
        {"data": ["A", "A", "A", "B", "B", "C"], "expected": 3},
        {"data": ["LOOP", "POOL", "POLO", "LOOP", "POOL", "POLO"], "expected": 1},
        {
            "data": [
                "LOOP",
                "POOL",
                "POLO",
                "XYZZ",
                "ZZYX",
                "ABCD",
                "DCBA",
                "AAAA",
                "AAAA",
            ],
            "expected": 4,
        },
    ]

    all_tests_passed = True

    for i, test_case in enumerate(test_cases, start=1):
        input_data = test_case["data"]
        expected_output = test_case["expected"]

        actual_output = solve(input_data)

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
