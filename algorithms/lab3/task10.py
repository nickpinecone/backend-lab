"""
Лабораторная работа № 3
Задача № 10 Вложенные отрезки
Порядковый номер 5
"""

import math


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node | None = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        if self.top is None:
            self.top = Node(value)
        else:
            node = Node(value)
            node.next = self.top
            self.top = node

    def fetch(self):
        if self.top is None:
            return "error"

        return self.top.value

    def pop(self):
        if self.top is None:
            return "error"

        value = self.top.value
        self.top = self.top.next
        return value

    def is_empty(self):
        return self.top is None


class Segment:
    def __init__(self, start, end, index):
        self.start = start
        self.end = end
        self.index = index

    def is_inside(self, point):
        return self.start <= point <= self.end

    def length(self):
        return self.end - self.start


class Tree:
    def __init__(self, segment: Segment, parent):
        self.parent = parent
        self.segment = segment
        self.children: list[Tree] = []

    def add(self, tree):
        self.children.append(tree)


def solve(segments, points):
    segments = [Segment(int(x.split()[0]), int(x.split()[1]), i+1) for i, x in enumerate(segments)]

    stack = Stack()
    line = Tree(Segment(-math.inf, math.inf, -1), None)

    stack.push(line)

    for segment in segments:
        last = stack.fetch()

        if segment.end <= last.segment.end: # type: ignore
            tree = Tree(segment, last)
            last.add(tree) # type: ignore
            stack.push(tree)
        else:
            while segment.end > last.segment.end: # type: ignore
                stack.pop()
                last = stack.fetch()

            tree = Tree(segment, last)
            last.add(tree) # type: ignore
            stack.push(tree)

    output = []

    for point in points:
        current = line
        is_continue = True

        while is_continue:
            is_continue = False

            for child in current.children:
                if child.segment.is_inside(point):
                    current = child
                    is_continue = True

        output.append(current.segment.index)

    return output


def run_tests():
    test_cases = [
        {
            "segments": ["2 10", "2 3", "5 7"],
            "points": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            "expected": [
                -1,
                2,
                2,
                1,
                3,
                3,
                3,
                1,
                1,
                1,
                -1,
            ],
        },
    ]

    all_tests_passed = True

    for i, test_case in enumerate(test_cases, start=1):
        input_data = test_case["segments"]
        points = test_case["points"]
        expected_output = test_case["expected"]

        actual_output = solve(input_data, points)

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
