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
        actual = Player(player["login"], player["tasks"], player["fine"])

        heap.append(actual)

    arr = []
    for _ in range(len(players)):
        arr.append(heap.pop())

    return [x.name.lower() for x in arr]


def run_tests():
    test_cases = [
        {
            "data": [
                {"login": "anna", "tasks": 4, "fine": 100},
                {"login": "gena", "tasks": 6, "fine": 1000},
                {"login": "gosha", "tasks": 2, "fine": 90},
                {"login": "rita", "tasks": 2, "fine": 90},
                {"login": "timofey", "tasks": 4, "fine": 80},
            ],
            "expected": ["gena", "timofey", "anna", "gosha", "rita"],
        },
        {
            "data": [
                {"login": "alex123", "tasks": 7, "fine": 4500},
                {"login": "john_doe", "tasks": 12, "fine": 12300},
                {"login": "sarah99", "tasks": 3, "fine": 2100},
                {"login": "mike45", "tasks": 9, "fine": 8700},
                {"login": "lisa_lee", "tasks": 5, "fine": 6500},
                {"login": "david_88", "tasks": 15, "fine": 19800},
                {"login": "kate_w", "tasks": 6, "fine": 3200},
                {"login": "andy_x", "tasks": 10, "fine": 11000},
                {"login": "samanta_z", "tasks": 4, "fine": 1800},
                {"login": "tommy_y", "tasks": 8, "fine": 9600},
                {"login": "jessica_a", "tasks": 2, "fine": 1500},
                {"login": "harry_b", "tasks": 11, "fine": 13400},
            ],
            "expected": [
                "david_88",
                "john_doe",
                "harry_b",
                "andy_x",
                "mike45",
                "tommy_y",
                "alex123",
                "kate_w",
                "lisa_lee",
                "samanta_z",
                "sarah99",
                "jessica_a",
            ],
        },
        {
            "data": [
                {"login": "user_a1", "tasks": 5, "fine": 3200},
                {"login": "user_b2", "tasks": 8, "fine": 7600},
                {"login": "user_c3", "tasks": 5, "fine": 4500},
                {"login": "user_d4", "tasks": 12, "fine": 15000},
                {"login": "user_e5", "tasks": 3, "fine": 1200},
                {"login": "user_f6", "tasks": 8, "fine": 9000},
                {"login": "user_g7", "tasks": 10, "fine": 11000},
                {"login": "user_h8", "tasks": 7, "fine": 5600},
                {"login": "user_i9", "tasks": 7, "fine": 6700},
                {"login": "user_j10", "tasks": 12, "fine": 15000},
            ],
            "expected": [
                "user_d4",
                "user_j10",
                "user_g7",
                "user_b2",
                "user_f6",
                "user_h8",
                "user_i9",
                "user_a1",
                "user_c3",
                "user_e5",
            ],
        },
        {
            "data": [
                {"login": "alpha_1", "tasks": 6, "fine": 4200},
                {"login": "beta_2", "tasks": 10, "fine": 12000},
                {"login": "gamma_3", "tasks": 6, "fine": 4800},
                {"login": "delta_4", "tasks": 4, "fine": 2100},
                {"login": "epsilon_5", "tasks": 10, "fine": 13000},
                {"login": "zeta_6", "tasks": 10, "fine": 12000},
                {"login": "eta_7", "tasks": 2, "fine": 1500},
                {"login": "theta_8", "tasks": 9, "fine": 8900},
                {"login": "iota_9", "tasks": 9, "fine": 9200},
                {"login": "kappa_10", "tasks": 3, "fine": 1800},
            ],
            "expected": [
                "beta_2",
                "zeta_6",
                "epsilon_5",
                "theta_8",
                "iota_9",
                "alpha_1",
                "gamma_3",
                "delta_4",
                "kappa_10",
                "eta_7",
            ],
        },
        {
            "data": [
                {"login": "admin_x", "tasks": 11, "fine": 14000},
                {"login": "mod_y", "tasks": 7, "fine": 6000},
                {"login": "guest_z", "tasks": 7, "fine": 6500},
                {"login": "editor_a", "tasks": 5, "fine": 3000},
                {"login": "viewer_b", "tasks": 11, "fine": 14000},
                {"login": "helper_c", "tasks": 3, "fine": 1900},
                {"login": "tester_d", "tasks": 8, "fine": 8000},
                {"login": "support_e", "tasks": 8, "fine": 8500},
                {"login": "manager_f", "tasks": 15, "fine": 19000},
                {"login": "operator_g", "tasks": 15, "fine": 19000},
            ],
            "expected": [
                "manager_f",
                "operator_g",
                "admin_x",
                "viewer_b",
                "tester_d",
                "support_e",
                "mod_y",
                "guest_z",
                "editor_a",
                "helper_c",
            ],
        },
        {
            "data": [
                {"login": "student_01", "tasks": 4, "fine": 2200},
                {"login": "teacher_02", "tasks": 10, "fine": 11000},
                {"login": "professor_03", "tasks": 4, "fine": 2500},
                {"login": "assistant_04", "tasks": 13, "fine": 16000},
                {"login": "lecturer_05", "tasks": 10, "fine": 11500},
                {"login": "dean_06", "tasks": 10, "fine": 11000},
                {"login": "researcher_07", "tasks": 2, "fine": 1300},
                {"login": "scientist_08", "tasks": 9, "fine": 9000},
                {"login": "engineer_09", "tasks": 9, "fine": 9300},
                {"login": "developer_10", "tasks": 13, "fine": 16000},
            ],
            "expected": [
                "assistant_04",
                "developer_10",
                "dean_06",
                "teacher_02",
                "lecturer_05",
                "scientist_08",
                "engineer_09",
                "student_01",
                "professor_03",
                "researcher_07",
            ],
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
