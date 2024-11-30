import re


class Card():
    def __init__(self, id, winning: list, numbers: list):
        self.id = int(id)
        self.n_winning = self.number_winings(winning, numbers)
        self.points = 2 ** (self.n_winning - 1) if self.n_winning > 0 else 0

    def number_winings(self, win, num):
        points = 0
        for number in num:
            if number in win:
                points += 1
        return points

def format_input(line: str):
    id, win, nums = re.match(r"Card\s+(\d+): (.*) \| (.*)", line).groups()
    win = list(map(int, re.findall(r"\d+", win)))
    nums = list(map(int, re.findall(r"\d+", nums)))
    return Card(id, win, nums)

if __name__ == "__main__":
    with open("/home/haddadan/AoC/day4/data.txt") as f:
        data = f.read().splitlines()
    cards = [format_input(line) for line in data]
    points = [card.points for card in cards]

    print(f"Sum of points: {sum(points)}")