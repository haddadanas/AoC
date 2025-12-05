import sys

sys.path.append("C:\\Users\\famil\\Documents\\Sonstiges\\AoC\\2025\\")

from aoc_utils import read_input, validate_test
import numpy as np


def mask_out_lower_indicies(np_array: np.ndarray, max_indicies: np.ndarray):
    index_array = np.array([np.arange(np_array.shape[1]) for _ in range(np_array.shape[0])])
    mask = index_array <= max_indicies[:, None]
    np_array[mask] = -1


def solution(data: list[str], digits: int) -> int:
    np_array = np.array([[int(char) for char in line] for line in data])
    max_values = np.ones((np_array.shape[0], digits), dtype=int) * -1

    for i in range(digits):
        upper_slice = -digits + i + 1 if -digits + i + 1 != 0 else None
        ith_max = np.argmax(np_array[:, :upper_slice], axis=1)
        max_values[:, i] = np.take_along_axis(np_array, ith_max[:, None], axis=1).flatten()
        mask_out_lower_indicies(np_array, ith_max) 
    if np.any(max_values == -1):
        raise ValueError("Not enough digits in some rows")

    sorted_maxima_str = max_values.astype("<U2")
    jolts_array = [sorted_maxima_str[:, i] for i in range(1, digits)]
    jolts = sum(jolts_array, start=sorted_maxima_str[:, 0])
    return int(jolts.astype("i8").sum())


if __name__ == "__main__":
    test_data = read_input("test.txt", "\n")
    input_data = read_input("input.txt", "\n")

    validate_test(solution(test_data, 2), 357)
    print("Part 1:", solution(input_data, 2))

    validate_test(solution(test_data, 12), 3121910778619)
    print("Part 2:", solution(input_data, 12))
