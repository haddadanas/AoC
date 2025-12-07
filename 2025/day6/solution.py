from gettext import find
import sys
import re

from matplotlib.pylab import f
import numpy as np

sys.path.append("C:\\Users\\famil\\Documents\\Sonstiges\\AoC\\2025\\")

from aoc_utils import read_input, validate_test


def split_input(data: list[str]) -> tuple[np.ndarray, np.ndarray]:
    ops_pattern = re.compile(r"(\+|\*)")
    ops = np.array(ops_pattern.findall(data[-1]))

    numbers_pattern = re.compile(r"(\d+)")
    numbers = np.array([numbers_pattern.findall(num_str) for num_str in data[:-1]]).astype(int)
    return ops, numbers


def solution(ops, nums) -> int:
    nums_T = nums.T
    sel_res = 0
    for i in ["*", "+"]:
        op = np.sum if i == "+" else np.prod
        sel_nums = nums_T[ops == i]
        sel_res += np.sum(op(sel_nums, axis=1))
    return sel_res


def find_seperating_spaces(data: list[str]) -> set[int]:
    spaces = set(range(len(data[0])))
    pattern = re.compile(r"\s")
    for line in data:
        line_spaces = [m.start() for m in pattern.finditer(line)]
        spaces = spaces.intersection(set(line_spaces))
    return spaces


def split_by_spaces(data: list[str]) -> list[list[str]]:
    split_data = []
    spaces = sorted(find_seperating_spaces(data))
    ps = 0
    for s in spaces:
        split_data.append([line[ps: s] for line in data])
        ps = s + 1
    split_data.append([line[ps:] for line in data])
    return split_data


def restructure_number(nums: list[str]) -> np.ndarray:
    np_array = np.array([[ch for ch in num] for num in nums])
    return np.astype(sum(np_array[1:], start=np_array[0]), int)


def solution_2(ops: np.ndarray, raw_numbers: list[str]) -> int:
    split_data = split_by_spaces(raw_numbers)
    op_dict = {"+": np.sum, "*": np.prod}
    numbers = np.array([op_dict[op](restructure_number(num_block)) for op, num_block in zip(ops, split_data)])
    return np.sum(numbers)


if __name__ == "__main__":
    test_data = read_input("test.txt", "\n")
    input_data = read_input("input.txt", "\n")

    test_ops, test_nums = split_input(test_data)
    input_ops, input_nums = split_input(input_data)

    validate_test(solution(test_ops, test_nums), 4277556)
    print("Part 1:", solution(input_ops, input_nums))

    validate_test(solution_2(test_ops, test_data[:-1]), 3263827)
    print("Part 2:", solution_2(input_ops, input_data[:-1]))
