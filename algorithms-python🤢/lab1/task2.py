def solve(hand_count: int, keyboard: list[int]) -> int:
    num_dict = dict[int, int]()
    result = 0

    for i in keyboard:
        if (i not in num_dict):
            num_dict[i] = 1
        else:
            num_dict[i] += 1

    for i in set(keyboard):
        if (hand_count * 2 >= num_dict[i]):
            result += 1

    return result
