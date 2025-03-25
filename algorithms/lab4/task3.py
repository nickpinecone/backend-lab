"""
Лабораторная работа № 4
Задача № 3 Пересечение множеств
Порядковый номер 2
"""


class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.height = 1
        self.right: Node | None = None
        self.left: Node | None = None


class Tree:
    def __init__(self):
        self.top: Node | None = None

    def height(self, node: Node | None):
        return node.height if node else 0

    def bfactor(self, node: Node):
        return self.height(node.right) - self.height(node.left)

    def fix_height(self, node):
        left_h = self.height(node.left)
        right_h = self.height(node.right)

        node.height = (left_h if left_h > right_h else right_h) + 1

    def rotate_right(self, node):
        temp = node.left
        node.left = temp.right
        temp.right = node

        self.fix_height(node)
        self.fix_height(temp)

        return temp

    def rotate_left(self, node):
        temp = node.right
        node.right = temp.left
        temp.left = node

        self.fix_height(node)
        self.fix_height(temp)

        return temp

    def balance(self, node: Node) -> Node:
        self.fix_height(node)

        if self.bfactor(node) == 2:
            if self.bfactor(node.right) < 0:  # type: ignore
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)  # type: ignore

        if self.bfactor(node) == -2:
            if self.bfactor(node.left) > 0:  # type: ignore
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)  # type: ignore

        return node

    def insert(self, node: Node | None, value: int) -> Node:
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)

        return self.balance(node)

    def append(self, value: int):
        self.top = self.insert(self.top, value)

    def search(self, node, value):
        if node is None:
            return None

        if value < node.value:
            return self.search(node.left, value)
        if value > node.value:
            return self.search(node.right, value)

        return node.value

    def has(self, value):
        result = self.search(self.top, value)
        return result is not None


def solve(sets: list[list[int]]):
    trees: list[Tree] = []

    for val_set in sets:
        tree = Tree()
        for value in val_set:
            tree.append(value)
        trees.append(tree)

    max_intersect = 0

    for i in range(len(trees)):
        for k in range(i + 1, len(trees)):
            values = sets[i]
            second = trees[k]
            current_intersect = 0

            for m in values:
                if second.has(m):
                    current_intersect += 1

            max_intersect = max(current_intersect, max_intersect)

    return max_intersect


def run_tests():
    test_cases = [
        {"input": [[9, 7, 1, 8], [5, 7, 6, 3], [5, 9, 8, 6]], "expected": 2},
        {
            "input": [
                [-2, 6, 8, 4, -1],
                [5, 3, 10, -5, -1],
                [7, 8, -5, -1, -2],
                [-1, 8, 4, 9, 0],
            ],
            "expected": 3,
        },
    ]

    all_tests_passed = True

    for i, test_case in enumerate(test_cases, start=1):
        input_data = test_case["input"]
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
