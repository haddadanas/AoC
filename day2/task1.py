import re

class game():
    def __init__(self, red:int=0, green:int=0, blue:int=0):
        self.red = red
        self.green = green
        self.blue = blue

    def is_valid(self):
        return self.red < 13 and self.green < 14 and self.blue < 15


def convert_to_dict(data:list):
    data_dict = {}
    for line in data:
        id, rest = re.match(r"Game (\d+): (.*)", line).groups()
        id = int(id)
        rest = rest.split("; ")
        data_dict[id] = []
        for combi in rest:
            colors = combi.split(", ")
            args = {}
            for color in colors:
                num, color = re.match(r"(\d+) (.*)", color).groups()
                args[color] = int(num)
            data_dict[id].append(game(**args))
    return data_dict

if __name__ == "__main__":
    with open("./data.txt") as f:
        data = f.read().splitlines()

    data = convert_to_dict(data)
    result = 0
    for id, games in data.items():
        if all([g.is_valid() for g in games]):
            result += id
    print(result)