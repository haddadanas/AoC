import numpy as np

with open('input') as f:
    data = np.array([list(line.strip()) for line in f.readlines()])

assert data[0,0] == "8" 
assert data[0,-1] == "7"

def expand(line):
    files = line[::2]
    free_spaces = line[1::2]
    ids = np.astype(np.arange(len(files)), str)
    ids_expanded = np.strings.multiply(ids, np.astype(files, int))
    free_spaces_expanded = np.strings.multiply(".", np.astype(free_spaces, int))
    result = np.zeros_like(line, dtype=">U50")
    result[::2] = ids_expanded
    result[1::2] = free_spaces_expanded
    result = "".join(result)
    return np.array(list(result))


def compress(line):
    empty = np.where(line == ".")[0]
    filled = np.flip(np.where(line != ".")[0])
    i_empty = 0
    i_filled = 0
    while empty[i_empty] < filled[i_filled]:
        line[empty[i_empty]] = line[filled[i_filled]]
        line[filled[i_filled]] = "."
        i_empty += 1
        i_filled += 1
    return line
result = 0
for line in data:
    line = expand(line)
    line = compress(line)
    number_idx = np.where(line != ".")[0]
    number = np.astype(line[number_idx], int)
    position_id = np.arange(len(number))
    result += np.sum(position_id * number)
print(result)
