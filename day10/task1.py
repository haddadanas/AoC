def find_the_start(data:list[str]):
    for index, line in enumerate(data):
        if line.find("S") != -1:
            return index, line.find("S")

class Pipe():

    pipes = {}
    order = -1

    @classmethod
    def get_pipe(cls, x, y):
        return cls.pipes[hash((x, y))]

    @classmethod
    def pipe_exists(cls, x, y):
        return hash((x, y)) in cls.pipes

    @classmethod
    def create_pipe(cls, x, y, character):
        key = hash((x, y))
        if key not in cls.pipes:
            cls.pipes[key] = cls(x, y, character)
            cls.order += 1
        return cls.pipes[key]

    def __init__(self, x, y, character):
        self.x = x
        self.y = y
        self.is_start = character == "S"
        self.connection = []

    def connect(self, pipe):
        if len(self.connection) == 2:
            return False
        if pipe in self.connection:
            return False
        self.connection.append(pipe)
        pipe.connection.append(self)
        return True
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def __eq__(self, o: object) -> bool:
        return hash(self) == hash(o)
    
    def __bool__(self) -> bool:
        return True



def walk_through_pipes(data, pipe, x, y, start_pipe):
    while True:
        if x < len(data) - 1 and data[x][y] in ["S", "7", r"|", "F"] and data[x + 1][y] in ["|", "L", "J"]:
            x_new = x + 1
            new_pipe = Pipe.create_pipe(x_new, y, data[x_new][y])
            if pipe.connect(new_pipe):
                pipe = new_pipe
                x = x_new
                continue
        if x > 0 and data[x][y] in ["S", "L", r"|", "J"] and data[x - 1][y] in ["|", "7", "F"]:
            x_new = x - 1
            new_pipe = Pipe.create_pipe(x_new, y, data[x_new][y])
            if pipe.connect(new_pipe):
                pipe = new_pipe
                x = x_new
                continue
        if y < len(data[x]) - 1 and data[x][y] in ["S", "F", "-", "L"] and data[x][y + 1] in ["-", "J", "7"]:
            y_new = y + 1
            new_pipe = Pipe.create_pipe(x, y_new, data[x][y_new])
            if pipe.connect(new_pipe):
                pipe = new_pipe
                y = y_new
                continue
        if y > 0 and data[x][y] in ["S", "7", "-", "J"] and data[x][y - 1] in ["-", "L", "F"]:
            y_new = y - 1
            new_pipe = Pipe.create_pipe(x, y_new, data[x][y_new])
            if pipe.connect(new_pipe):
                pipe = new_pipe
                y = y_new
                continue
        pipe.connect(start_pipe)
        break

if __name__ == "__main__":
    with open("/home/haddadan/AoC/day6/data.txt") as f:
        data = f.read().splitlines()


    # | is a vertical pipe connecting north and south.
    # - is a horizontal pipe connecting east and west.
    # L is a 90-degree bend connecting north and east.
    # J is a 90-degree bend connecting north and west.
    # 7 is a 90-degree bend connecting south and west.
    # F is a 90-degree bend connecting south and east.

    start_x, start_y = find_the_start(data)

    pipe = Pipe.create_pipe(start_x, start_y, "S")
    walk_through_pipes(data, pipe, start_x, start_y, pipe)
    print(round(Pipe.order/2))

    enclosed_tiles = 0
    for x, line in enumerate(data[1:-1], 1):
        for y in range(1, len(line) - 1):
            if Pipe.pipe_exists(x, y):
                continue
            pathes = 0
            direction = ""
            for y_char in range(0, y):
                if Pipe.pipe_exists(x, y_char):
                    if line[y_char - 1] in ["L", "-", "F"]:
                        if line[y_char] == "7" and direction == "du":
                            pathes += 1
                        if line[y_char] == "J" and direction == "ud":
                            pathes += 1
                        continue
                    direction = "ud" if Pipe.pipe_exists(x - 1, y_char) else "du"
                    pathes += 1

            if pathes % 2 == 1:
                enclosed_tiles += 1
    print(enclosed_tiles)
