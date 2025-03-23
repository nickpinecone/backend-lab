"""
Лабораторная работа № 3
Задача № 3 Пирамидальная сортировка
Порядковый номер 2
"""


class Player:
    def __init__(self, name, task_count, penalty):
        self.name = name
        self.task_count = task_count
        self.penalty = penalty

    def __gt__(self, other):
        if self.task_count > other.task_count:
            return True
        elif self.task_count == other.task_count and self.penalty < other.penalty:
            return True
        elif (
            self.task_count == other.task_count
            and self.penalty == other.penalty
            and self.name.lower() < other.name.lower()
        ):
            return True

        return False

    def __lt__(self, other):
        if self.task_count < other.task_count:
            return True
        elif self.task_count == other.task_count and self.penalty > other.penalty:
            return True
        elif (
            self.task_count == other.task_count
            and self.penalty == other.penalty
            and self.name.lower() > other.name.lower()
        ):
            return True

        return False


class Heap:
    def __init__(self):
        self.values = []

    def append(self, value):
        self.values.append(value)
        self.sift_up(len(self.values) - 1)

    def sift_up(self, index):
        if index <= 0:
            return

        parent = (index - 1) // 2

        if self.values[index] > self.values[parent]:
            self.values[index], self.values[parent] = (
                self.values[parent],
                self.values[index],
            )

            self.sift_up(parent)

    def pop(self):
        if len(self.values) <= 1:
            return self.values.pop()

        value = self.values[0]
        self.values[0] = self.values.pop()

        self.sift_down(0)

        return value

    def sift_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        length = len(self.values)

        max_index = index

        if left < length and self.values[left] > self.values[max_index]:
            max_index = left

        if right < length and self.values[right] > self.values[max_index]:
            max_index = right

        if index != max_index:
            self.values[index], self.values[max_index] = (
                self.values[max_index],
                self.values[index],
            )

            self.sift_down(max_index)


def solve(players):
    heap = Heap()

    for player in players:
        split = player.split(" ")

        name = split[0]
        task_count = split[1]
        penalty = split[2]

        actual = Player(name, int(task_count), int(penalty))

        heap.append(actual)

    arr = []
    for _ in range(len(players)):
        arr.append(heap.pop())

    return [x.name.lower() for x in arr]


def run_tests():
    test_cases = [
        {
            "input": [
                "alla 4 100",
                "gena 6 1000",
                "gosha 2 90",
                "rita 2 90",
                "Timofey 4 80",
            ],
            "expected": ["gena", "timofey", "alla", "gosha", "rita"],
        },
        {
            "input": [
                "alla 0 0",
                "gena 0 0",
                "gosha 0 0",
                "rita 0 0",
                "Timofey 0 0",
            ],
            "expected": ["alla", "gena", "gosha", "rita", "timofey"],
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
