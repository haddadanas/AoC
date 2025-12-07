import sys
from copy import deepcopy
import numpy as np

sys.path.append("C:\\Users\\famil\\Documents\\Sonstiges\\AoC\\2025\\")

from aoc_utils import read_input, validate_test


def shoot_beam(raw_data: list[list[str]]) -> list[list[str]]:
    data = deepcopy(raw_data)
    row_idx = 1
    col_idx = {data[0].index("S")}
    while row_idx < len(data):
        idxs = list(col_idx)
        for idx in idxs:
            if data[row_idx][idx] == ".":
                data[row_idx][idx] = "|"
            if data[row_idx][idx] == "^":
                col_idx.remove(idx)
                data[row_idx][idx + 1] = "|"
                data[row_idx][idx - 1] = "|"
                col_idx.add(idx - 1)
                col_idx.add(idx + 1)
        row_idx += 1
    return data


def shoot_quantum_beam(raw_data: list[list[str]]) -> list[list[str]]:
    data = np.array(raw_data)
    data = np.where(data == ".", "0", data).tolist()
    row_idx = 1
    start_idx = data[0].index("S")
    data[0][start_idx] = "1"
    col_idx = {start_idx}
    while row_idx < len(data):
        idxs = list(col_idx)
        for idx in idxs:
            prev_val = data[row_idx - 1][idx]
            if data[row_idx][idx] == "^":
                col_idx.remove(idx)
                data[row_idx][idx + 1] = str(int(data[row_idx][idx + 1]) + int(prev_val))
                data[row_idx][idx - 1] = str(int(data[row_idx][idx - 1]) + int(prev_val))
                col_idx.add(idx - 1)
                col_idx.add(idx + 1)
            else:
                data[row_idx][idx] = int(prev_val) + int(data[row_idx][idx])
        row_idx += 1
    return data


def solution(data: list[list[str]]) -> int:
    array = np.array(data)
    splitter_y, splitter_x = np.where(array == "^")
    splits = 0
    for x, y in zip(splitter_x, splitter_y):
        if array[y - 1, x] == "|":
            splits += 1
    return splits


def solution_quantum(data: list[list[str]]) -> int:
    array = np.array(data)
    return int(np.sum(array[-1].astype(int)))


if __name__ == "__main__":
    test_data = [list(line) for line in read_input("test.txt", "\n")]
    input_data = [list(line) for line in read_input("input.txt", "\n")]

    test_beam = shoot_beam(test_data)
    input_beam = shoot_beam(input_data)

    validate_test(solution(test_beam), 21)
    print("Part 1:", solution(input_beam))

    test_q_beam = shoot_quantum_beam(test_data)
    input_q_beam = shoot_quantum_beam(input_data)

    validate_test(solution_quantum(test_q_beam), 40)
    print("Part 2:", solution_quantum(input_q_beam))