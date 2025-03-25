"""
Лабораторная работа № 4
Задача № 2 Брокеры
Порядковый номер 1
"""


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

        if self.values[index] < self.values[parent]:
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

        min_index = index

        if left < length and self.values[left] < self.values[min_index]:
            min_index = left

        if right < length and self.values[right] < self.values[min_index]:
            min_index = right

        if index != min_index:
            self.values[index], self.values[min_index] = (
                self.values[min_index],
                self.values[index],
            )

            self.sift_down(min_index)


def solve(capitals):
    pay = 0
    heap = Heap()

    for capital in capitals:
        heap.append(capital)

    while len(heap.values) > 1:
        first = heap.pop()
        second = heap.pop()
        result = first + second

        pay += result
        heap.append(result)

    return round(pay * 0.01, 2)


def run_tests():
    test_cases = [
        {"input": [1, 2, 3, 4, 5], "expected": "0.33"},
        {"input": [2, 10, 100, 30, 7, 4, 15, 2, 15, 80], "expected": "6.52"},
    ]

    all_tests_passed = True

    for i, test_case in enumerate(test_cases, start=1):
        input_data = test_case["input"]
        expected_output = test_case["expected"]

        actual_output = str(solve(input_data))

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
