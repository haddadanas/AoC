def get_calibration_value(code: str):
    calibration_value = ''
    for char in code:
        if char.isdigit():
            calibration_value += char
            break
    for char in code[::-1]:
        if char.isdigit():
            calibration_value += char
            return int(calibration_value)
    return 0


if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        # Read all the lines
        lines = file.readlines()

    result = 0
    for line in lines:
        result += get_calibration_value(line)
    print(result)
