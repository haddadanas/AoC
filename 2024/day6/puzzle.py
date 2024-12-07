from collections import defaultdict
import numpy as np

with open("input", "r") as file:
    data = np.array([list(line) for line in file.read().splitlines()])


class Guard:
    def __init__(self, map):
        self.map = np.copy(map)
        self.x, self.y = self.get_start()
        self.symbol = "^"
        self.distinct_steps = 0
        self.left = False

    def get_start(self):
        [start_x], [start_y] = np.where(self.map == "^")
        self.map[start_x, start_y] = "."
        return start_x, start_y

    def get_direction(self):
        if self.symbol == "^":
            return (-1, 0)
        elif self.symbol == "v":
            return (1, 0)
        elif self.symbol == "<":
            return (0, -1)
        elif self.symbol == ">":
            return (0, 1)

    def turn(self):
        if self.symbol == "^":
            self.symbol = ">"
        elif self.symbol == ">":
            self.symbol = "v"
        elif self.symbol == "v":
            self.symbol = "<"
        elif self.symbol == "<":
            self.symbol = "^"

    def move(self):
        direction = self.get_direction()
        next_x, next_y = self.x + direction[0], self.y + direction[1]
        if next_x < 0 or next_x >= self.map.shape[0] or next_y < 0 or next_y >= self.map.shape[1]:
            self.left = True
            return
        if self.map[next_x, next_y] == "#":
            self.turn()
            return

        self.map[self.x, self.y] = "X"
        self.x, self.y = next_x, next_y
        if self.map[self.x, self.y] == ".":
            self.distinct_steps += 1

    def run(self):
        while not self.left:
            self.move()
        return self.distinct_steps + 1

    def print_map(self):
        map = np.copy(self.map)
        map[self.x, self.y] = self.symbol
        print(map)


guard = Guard(data)
print(guard.run())


# part 2
class StuckGuard(Guard):
    def __init__(self, map):
        super().__init__(map)
        self.stuck = False
        self.positions = set() 
        self.visited = defaultdict(list)
        self.start_x, self.start_y = self.x, self.y
        self.start_symbol = self.symbol
        self.start_map = np.copy(self.map)

    def hash_position(self, x=None, y=None):
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        return hash((x, y))

    def move(self):
        direction = self.get_direction()
        next_x, next_y = self.x + direction[0], self.y + direction[1]
        if next_x < 0 or next_x >= self.map.shape[0] or next_y < 0 or next_y >= self.map.shape[1]:
            self.left = True
            return
        if self.map[next_x, next_y] == "#":
            self.turn()
            return

        self.x, self.y = next_x, next_y
        self.positions.add((self.x, self.y))

        if self.symbol in self.visited[self.hash_position()]:
            self.stuck = True
            return
        else:
            self.visited[self.hash_position()].append(self.symbol)

    def run(self):
        while not self.left:
            self.move()
            if self.stuck:
                return True
        return False

    def run_with_obejct(self):
        n_stuck = 0
        self.run()
        for i, j in self.positions:
            self.visited = defaultdict(list)
            self.map = np.copy(self.start_map)
            self.map[i, j] = "#"
            self.positions = set()
            self.x, self.y = self.start_x, self.start_y
            self.symbol = self.start_symbol
            self.stuck = False
            self.left = False
            if self.run():
                n_stuck += 1
        return n_stuck

stuck_guard = StuckGuard(data)
print(stuck_guard.run_with_obejct())