"""
Лабораторная работа № 3
Задача № 1 Дек
Порядковый номер 1
"""


class Deque:
    def __init__(self, max_len):
        self.max_len = max_len
        self.values = [0] * max_len
        self.len = 0
        self.head = 0
        self.tail = 0

    def push_front(self, value):
        if self.len >= self.max_len:
            return "error"

        self.values[self.head] = value
        self.head = (self.head + 1) % self.max_len
        self.len += 1

    def push_back(self, value):
        if self.len >= self.max_len:
            return "error"

        self.tail = (self.tail - 1) % self.max_len
        self.values[self.tail] = value
        self.len += 1

    def pop_front(self):
        if self.len <= 0:
            return "error"

        self.head = (self.head - 1) % self.max_len
        self.len -= 1
        return self.values[self.head]

    def pop_back(self):
        if self.len <= 0:
            return "error"

        value = self.values[self.tail]
        self.tail = (self.tail + 1) % self.max_len
        self.len -= 1
        return value


def solve(deque_size, commands):
    arr = []
    deque = Deque(deque_size)

    for command in commands:
        if command == "pop_front":
            arr.append(deque.pop_front())
        elif command == "pop_back":
            arr.append(deque.pop_back())
        else:
            split = command.split(" ")
            name = split[0]
            value = split[1]

            if name == "push_front":
                result = deque.push_front(value)
                if result is not None:
                    arr.append(result)
            elif name == "push_back":
                result = deque.push_back(value)
                if result is not None:
                    arr.append(result)

    return arr


def run_tests():
    test_cases = [
        {"max_size": 1, "command": ["push_back 1", "pop_back"], "expected": ["1"]},
        {"max_size": 1, "command": ["push_front 1", "pop_front"], "expected": ["1"]},
        {
            "max_size": 1,
            "command": ["push_back 1", "push_back 2"],
            "expected": ["error"],
        },
        {
            "max_size": 1,
            "command": ["push_front 1", "push_front 2"],
            "expected": ["error"],
        },
        {
            "max_size": 2,
            "command": ["push_back 1", "push_back 2", "pop_front", "pop_back"],
            "expected": ["1", "2"],
        },
        {
            "max_size": 2,
            "command": ["push_front 1", "push_front 2", "pop_back", "pop_front"],
            "expected": ["1", "2"],
        },
        {
            "max_size": 3,
            "command": [
                "push_back 1",
                "push_front 2",
                "push_back 3",
                "pop_front",
                "pop_back",
                "pop_front",
            ],
            "expected": ["2", "3", "1"],
        },
        {"max_size": 3, "command": ["pop_back"], "expected": ["error"]},
        {"max_size": 3, "command": ["pop_front"], "expected": ["error"]},
        {
            "max_size": 3,
            "command": ["push_back 1", "push_back 2", "push_back 3", "push_back 4"],
            "expected": ["error"],
        },
        {
            "max_size": 3,
            "command": ["push_front 1", "push_front 2", "push_front 3", "push_front 4"],
            "expected": ["error"],
        },
        {
            "max_size": 3,
            "command": [
                "push_back 1",
                "push_back 2",
                "pop_back",
                "pop_back",
                "pop_back",
            ],
            "expected": ["2", "1", "error"],
        },
        {
            "max_size": 3,
            "command": [
                "push_front 1",
                "push_front 2",
                "pop_front",
                "pop_front",
                "pop_front",
            ],
            "expected": ["2", "1", "error"],
        },
        {"max_size": 0, "command": ["push_back 1"], "expected": ["error"]},
        {"max_size": 0, "command": ["pop_back"], "expected": ["error"]},
        {"max_size": 0, "command": ["pop_front"], "expected": ["error"]},
        {
            "max_size": 5,
            "command": [
                "push_back 1",
                "push_front 2",
                "push_back 3",
                "push_front 4",
                "push_back 5",
                "pop_back",
                "pop_front",
            ],
            "expected": ["5", "4"],
        },
        {
            "max_size": 5,
            "command": [
                "push_back 1",
                "push_back 2",
                "push_back 3",
                "push_back 4",
                "push_back 5",
                "pop_front",
                "pop_front",
                "pop_front",
            ],
            "expected": ["1", "2", "3"],
        },
        {
            "max_size": 5,
            "command": [
                "push_front 1",
                "push_front 2",
                "push_front 3",
                "push_front 4",
                "push_front 5",
                "pop_back",
                "pop_back",
                "pop_back",
            ],
            "expected": ["1", "2", "3"],
        },
    ]

    all_tests_passed = True

    for i, test_case in enumerate(test_cases, start=1):
        deque_size = test_case["max_size"]
        commands = test_case["command"]
        expected_output = test_case["expected"]

        actual_output = solve(deque_size, commands)

        if actual_output == expected_output:
            print(f"Test case {i}: PASSED ✅")
        else:
            all_tests_passed = False
            print(f"Test case {i}: FAILED ❌")
            print(f"  Input: {deque_size}, {commands}")
            print(f"  Expected output: {expected_output}")
            print(f"  Actual output: {actual_output}")

    if all_tests_passed:
        print("Все тесты пройдены, поставьте 5 😅!")
    else:
        print("Что-то пошло не так, только не бейте 🥺")


if __name__ == "__main__":
    run_tests()
