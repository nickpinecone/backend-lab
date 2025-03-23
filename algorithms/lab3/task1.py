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
                deque.push_front(value)
            elif name == "push_back":
                deque.push_back(value)

    return arr


def run_tests():
    test_cases = [
        {
            "deque_size": 4,
            "commands": ["push_front 861", "push_front -819", "pop_back", "pop_back"],
            "expected": ["861", "-819"],
        },
        {
            "deque_size": 10,
            "commands": [
                "push_front -855",
                "push_front 720",
                "pop_back",
                "pop_back",
                "push_back 844",
                "pop_back",
                "push_back 823",
            ],
            "expected": ["-855", "720", "844"],
        },
    ]

    all_tests_passed = True

    for i, test_case in enumerate(test_cases, start=1):
        deque_size = test_case["deque_size"]
        commands = test_case["commands"]
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
