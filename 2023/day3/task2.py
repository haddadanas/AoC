import re 

from task1 import get_neighbours, find_numbers_position


def find_gears(line: str):
    return {match.span(): match.group(1)
            for match in re.finditer(r"(\*+)", line)
    }

def get_all_numbers(file: list):
    d = {}
    for ind, line in enumerate(file):
        numbers = find_numbers_position(line)
        d.update({ind: [Number(int(num), pos) for pos, num in numbers.items()]})
    return d

class Number():
    def __init__(self, value: int, position: tuple):
        self.value = value
        self.start = position[0]
        self.end = position[1]

    def is_neighbour(self, position:tuple):
        if ((position[0] > self.start - 2 and position[0] < self.start + 2) or
            (position[1] > self.end - 2 and position[1] < self.end + 2)):
            return True
        return False


if __name__ == "__main__":
    with open("/home/haddadan/AoC/day3/data.txt") as f:
        data = f.read().splitlines()

    numbers = get_all_numbers(data)
    result = 0
    for index, line in enumerate(data):
        gears = find_gears(line)
        for pos, gear in gears.items():
            neightbours = []
            for i in range(index - 1, index + 2):
                if i < 0 or i >= len(data):
                    continue
                for num in numbers[i]:
                    if num.is_neighbour(pos):
                        neightbours.append(num.value)
            if len(neightbours) == 2:
                result += neightbours[0] * neightbours[1]

    print(result)