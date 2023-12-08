from task1 import get_calibration_value
import regex as re

digits = {"one": "1", "two": "2", "three": "3", "four": "4",
            "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def rewrite_code(code: str):
    new_code = re.findall(rf"(\d|{'|'.join(digits.keys())})", code, overlapped=True)
    return ''.join([digits.get(digit, digit) for digit in new_code])


if __name__ == '__main__':
    with open('./data.txt', 'r') as file:
        # Read all the lines
        lines = file.read().splitlines()

    result = 0
    for line in lines:
        result += get_calibration_value(rewrite_code(line))
    print(result)
