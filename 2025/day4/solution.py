import sys

sys.path.append("C:\\Users\\famil\\Documents\\Sonstiges\\AoC\\2025\\")

from aoc_utils import read_input, validate_test
import numpy as np


def convolute(array: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    if kernel.shape[0] != kernel.shape[1]:
        raise Exception("Kernel shape must be a square!")

    kernel_width = int((kernel.shape[0] - 1) / 2)
    padded_array = np.pad(array, pad_width=kernel_width, mode="constant", constant_values=0)
    result = np.zeros_like(padded_array)

    for i in range(kernel_width, padded_array.shape[0] - kernel_width):
        for j in range(kernel_width, padded_array.shape[1] - kernel_width):
            if padded_array[i, j] == 0:
                continue
            result[i, j] = np.sum(
                kernel * padded_array[
                    i - kernel_width: i + kernel_width + 1,
                    j - kernel_width: j + kernel_width + 1
                ]
            )
    return result[kernel_width: -kernel_width, kernel_width: -kernel_width]


def solution(input_data: list[str], iterations: int | float) -> int:
    np_array = np.array([[1 if char == "@" else 0 for char in line] for line in input_data])
    kernel = np.ones((3, 3), dtype=int)
    kernel[1, 1] = 0
    removed_rolls = 0

    while iterations > 0:
        iterations -= 1
        neighbours = convolute(np_array, kernel)
        removable_rolls = (neighbours < 4) & (np_array == 1)
        removed_rolls += np.sum(removable_rolls)
        np_array[removable_rolls] = 0
        if not np.any(removable_rolls):
            break
    return removed_rolls



if __name__ == "__main__":
    test_data = read_input("test.txt", "\n")
    input_data = read_input("input.txt", "\n")

    validate_test(solution(test_data, 1), 13)
    print("Part 1:", solution(input_data, 1))

    validate_test(solution(test_data, float("inf")), 43)
    print("Part 2:", solution(input_data, float("inf")))