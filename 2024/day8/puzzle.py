import numpy as np


with open('input') as f:
    data = np.array([list(line.strip()) for line in f.readlines()])

antenne_symbols = np.unique(data)


def check_if_inside(antenne_mask, pos):
    return (0 <= pos[0] < antenne_mask.shape[0]) and (0 <= pos[1] < antenne_mask.shape[1])


def get_freq_positions(antenne_mask):
    freq_positions = []
    x_pos, y_pos = np.where(antenne_mask)
    for i in range(len(x_pos)):
        for j in range(i+1, len(x_pos)):
            antenne1 = np.array([x_pos[i], y_pos[i]])
            antenne2 = np.array([x_pos[j], y_pos[j]])
            distance = antenne2 - antenne1
            if check_if_inside(antenne_mask, antenne1 - distance):
                freq_positions.append(antenne1 - distance)
            if check_if_inside(antenne_mask, antenne2 + distance):
                freq_positions.append(antenne2 + distance)
    return freq_positions


freqs = set()
freq_map = data.copy()
for antenne_symbol in antenne_symbols:
    if antenne_symbol == '.':
        continue
    antenne_mask = data == antenne_symbol
    freq_positions = get_freq_positions(antenne_mask)
    for freq_pos in freq_positions:
        freqs.add(tuple(freq_pos))
        freq_map[tuple(freq_pos)] = '#'

print(len(freqs))

# Part 2
def get_antinode_positions(antenne_mask):
    antinode_positions = []
    x_pos, y_pos = np.where(antenne_mask)
    for i in range(len(x_pos)):
        for j in range(i+1, len(x_pos)):
            antenne1 = np.array([x_pos[i], y_pos[i]])
            antenne2 = np.array([x_pos[j], y_pos[j]])
            distance = antenne2 - antenne1
            pos1 = antenne1 - distance
            pos2 = antenne2 + distance
            while check_if_inside(antenne_mask, pos1):
                antinode_positions.append(tuple(pos1))
                pos1 -= distance
            while check_if_inside(antenne_mask, pos2):
                antinode_positions.append(tuple(pos2))
                pos2 += distance
            antinode_positions.append(tuple(antenne1))
            antinode_positions.append(tuple(antenne2))

    return antinode_positions


antinodes = set()
antinode_map = data.copy()
for antenne_symbol in antenne_symbols:
    if antenne_symbol == '.':
        continue
    antenne_mask = data == antenne_symbol
    antinode_positions = get_antinode_positions(antenne_mask)
    for antinode_pos in antinode_positions:
        antinodes.add(tuple(antinode_pos))
        antinode_map[tuple(antinode_pos)] = '#'

print(len(antinodes))