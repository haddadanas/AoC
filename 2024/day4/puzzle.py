import numpy as np
import re

with open('input', "r") as f:
    data = np.array([list(line) for line in f.read().split('\n')])


# part 1 with re
pattern = re.compile(r'(?=XMAS)|(?=SAMX)')

def build_horizontal_string(array):
    result = []
    for i in range(array.shape[0]):
        result.append("".join(array[i]))
    return result

def build_vertical_string(array):
    result = []
    for i in range(array.shape[1]):
        result.append("".join(array[:, i]))
    return result

def build_diagonal_string(array):
    result = []
    for i in range(-array.shape[0] + 1, array.shape[1]):
        result.append("".join(np.diagonal(array, i)))
    return result

def build_other_diagonal_string(array):
    result = []
    array = np.fliplr(array)
    return build_diagonal_string(array)

possibilities = [build_horizontal_string, build_vertical_string, build_diagonal_string, build_other_diagonal_string]
def __main__():
    result = 0
    for func in possibilities:
        for string in func(data):
            result += len(pattern.findall(string))
    return result

print(__main__())

# part 2
pattern = re.compile(r'(?=MAS)|(?=SAM)')
def check_diagonals(array, pos_x, pos_y):
    array = array[pos_x - 1:pos_x + 2, pos_y - 1:pos_y + 2]
    diags = ["".join(np.diagonal(array)), "".join(np.fliplr(array).diagonal())]
    found = all([pattern.match(diag) for diag in diags])
    return int(found)

result = 0
for x, y in zip(*np.where(data == 'A')):
    if (x == 0 or x == data.shape[0] - 1) or (y == 0 or y == data.shape[1] - 1):
        continue
    result += check_diagonals(data, x, y)
print(result)