"""
Лабораторная работа № 3
Задача № 4 Очередь с минимумом
Порядковый номер 3
"""

import math


class Node:
    def __init__(self, value, current_min):
        self.value = value
        self.current_min = current_min
        self.next: Node | None = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        if self.top is None:
            self.top = Node(value, value)
        else:
            current_min = min(value, self.top.current_min)
            node = Node(value, current_min)
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return "error"

        value = self.top.value
        self.top = self.top.next
        return value

    def is_empty(self):
        return self.top is None

    def fetch_min(self):
        if self.top is None:
            return math.inf

        return self.top.current_min


class MinQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, elem):
        self.s1.push(elem)

    def pop(self):
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
        return self.s2.pop()

    def fetch_min(self):
        return min(self.s1.fetch_min(), self.s2.fetch_min())


def solve(commands: list[str]):
    queue = MinQueue()
    output = []

    for command in commands:
        if command.startswith("+"):
            split = command.split(" ")
            value = int(split[1])
            queue.push(value)
        elif command.startswith("-"):
            output.append(str(queue.pop()))
        elif command.startswith("?"):
            output.append(str(queue.fetch_min()))

    return output


def run_tests():
    test_cases = [
        {"command": ["+ 5", "?", "-"], "expected": ["5", "5"]},
        {
            "command": ["+ 3", "+ 7", "?", "-", "?", "-"],
            "expected": ["3", "3", "7", "7"],
        },
        {
            "command": ["+ 10", "+ 5", "+ 8", "?", "-", "?", "-", "?", "-"],
            "expected": ["5", "10", "5", "5", "8", "8"],
        },
        {
            "command": ["+ 1", "+ 2", "+ 3", "?", "-", "?", "-", "?", "-"],
            "expected": ["1", "1", "2", "2", "3", "3"],
        },
        {
            "command": ["+ 4", "+ 4", "+ 4", "?", "-", "?", "-", "?", "-"],
            "expected": ["4", "4", "4", "4", "4", "4"],
        },
        {
            "command": ["+ 10", "+ 1", "?", "-", "?", "-"],
            "expected": ["1", "10", "1", "1"],
        },
        {
            "command": [
                "+ 5",
                "+ 3",
                "+ 7",
                "+ 2",
                "?",
                "-",
                "?",
                "-",
                "?",
                "-",
                "?",
                "-",
            ],
            "expected": ["2", "5", "2", "3", "2", "7", "2", "2"],
        },
        {
            "command": ["+ 100", "+ 200", "+ 50", "?", "-", "?", "-", "?", "-"],
            "expected": ["50", "100", "50", "200", "50", "50"],
        },
        {
            "command": ["+ 1", "?", "-", "+ 2", "?", "-", "+ 3", "?", "-"],
            "expected": ["1", "1", "2", "2", "3", "3"],
        },
        {
            "command": [
                "+ 10",
                "+ 20",
                "+ 5",
                "+ 1",
                "?",
                "-",
                "?",
                "-",
                "?",
                "-",
                "?",
                "-",
            ],
            "expected": ["1", "10", "1", "20", "1", "5", "1", "1"],
        },
        {
            "command": ["+ 5", "+ 5", "+ 5", "?", "-", "?", "-", "?", "-"],
            "expected": ["5", "5", "5", "5", "5", "5"],
        },
        {
            "command": [
                "+ 10",
                "+ 5",
                "+ 8",
                "+ 3",
                "?",
                "-",
                "?",
                "-",
                "?",
                "-",
                "?",
                "-",
            ],
            "expected": ["3", "10", "3", "5", "3", "8", "3", "3"],
        },
    ]

    all_tests_passed = True

    for i, test_case in enumerate(test_cases, start=1):
        input_data = test_case["command"]
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
