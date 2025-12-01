import os
import re

dir_path = os.path.dirname(__file__)
pattern = re.compile(r"[LR](\d+)")

with open(f"{dir_path}/input.txt", "r") as file:
    rots = [(int((pat := pattern.match(line.strip())).group(1)), 1 if pat.group(0)[0] == "R" else -1) for line in file]

with open(f"{dir_path}/test.txt", "r") as file:
    test_rots = [(int((pat := pattern.match(line.strip())).group(1)), 1 if pat.group(0)[0] == "R" else -1) for line in file]

def rotation(start, rot, sign):
    return start + sign * rot

def main1(input_data):
    start = 50
    password = 0

    for rot, sign in input_data:
        start = rotation(start, rot, sign) % 100
        if start == 0:
            password += 1
    return password


def main2(input_data):
    start = 50
    password = 0
    for rot, sign in input_data:
        password += rot // 100
        rot %= 100
        tmp = rotation(start, rot, sign)
        if rot == 0:
            continue
        if tmp == 0:
            password += 1
        if (tmp % 100 != tmp) and (start != 0):
            password += 1
        start = tmp % 100
    return password


if __name__ == "__main__":
    assert main1(test_rots) == 3, "Test case failed"
    print("Final Password:", main1(rots))
    assert main2(test_rots) == 6, "Test case 2 failed"
    print("Final Password with Overflow:", main2(rots))
