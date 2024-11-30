import re

def find_numbers_position(line:str):
    return {match.span(): match.group(1)
        for match in re.finditer(r"([0-9]+)", line)
    }

def get_neighbours(file: list, line_number:int, position:tuple):
    neighbours = ''
    for i in range(line_number - 1, line_number + 2):
        if i < 0:
            continue
        for j in range(position[0] - 1, position[1] + 1):
            if j < 0:
                continue
            if i == line_number and j in range(position[0], position[1]):
                continue
            try:
                neighbours += file[i][j]
            except IndexError:
                pass
    return neighbours

if __name__ == "__main__":
    with open("/home/haddadan/AoC/day3/data.txt") as f:
        data = f.read().splitlines()

    result = 0
    for index, line in enumerate(data):
        numbers = find_numbers_position(line)
        for pos, num in numbers.items():
            neighbours = get_neighbours(data, index, pos)
            if neighbours.replace('.',''):
                result += int(num)
    print(result)
