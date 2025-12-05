from typing import Callable
import sys

sys.path.append("C:\\Users\\famil\\Documents\\Sonstiges\\AoC\\2025\\")

from aoc_utils import read_input, validate_test
import numpy as np


def check_range(func: Callable, low: str, high: str) -> list[int]:
    range_array = np.arange(int(low), int(high) + 1)
    np_check = np.vectorize(func, otypes=[bool])
    invalid_numbers = np_check(range_array)
    return range_array[invalid_numbers].tolist()


def check_repetition_twice(num: int) -> bool:
    str_num = str(num)
    if len(str_num) % 2:
        return False
    mid_index = len(str_num) // 2
    return str_num[:mid_index] == str_num[mid_index:]


def part1(inputs) -> int:
    result = 0
    for low, high in inputs:
        if len(low) == len(high) and len(low) % 2:
            continue
        result += np.sum(check_range(check_repetition_twice, low, high))
    return result


def check_repetition(num: int) -> bool:
    str_num = str(num)
    length = len(str_num)
    for i in range(1, length // 2 + 1):
        if length % i:
            continue
        sub_str = [str_num[j:j+i] for j in range(0, length, i)]
        if all(s == sub_str[0] for s in sub_str):
            return True
    return False


def part2(inputs) -> int:
    result = 0
    for low, high in inputs:
        result += np.sum(check_range(check_repetition, low, high))
    return int(result)


if __name__ == "__main__":
    test_data = read_input("test.txt", ",", pattern=r"(\d+)-(\d+)")
    input_data = read_input("input.txt", ",", pattern=r"(\d+)-(\d+)")

    validate_test(part1(test_data), 1227775554)
    print("Part 1:", part1(input_data))

    # No part 2 for day 2
    validate_test(part2(test_data), 4174379265)
    print("Part 2:", part2(input_data))