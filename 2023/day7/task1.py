cards = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

class Card():

    def __init__(self, card: str):
        self.card = card
        self.value = [cards[char] for char in card]
        self.typ = self.determine_type()

    def determine_type(self):
        counts = {}
        for char in self.card:
            counts[char] = self.card.count(char)
        if 5 in counts.values():
            return 5 # "five of a kind"
        elif 4 in counts.values():
            return 4 # "four of a kind"
        elif 3 in counts.values():
            if 2 in counts.values():
                return 3 # "full house"
            else:
                return 2 # "three of a kind"
        elif 2 in counts.values():
            if len(counts.values()) == 3:
                return 1 # "two pairs"
            else:
                return 0 # "pair"
        else:
            return -1 # "high card"

    def __gt__(self, other):
        if self.typ == other.typ:
            for v1, v2 in zip(self.value, other.value):
                if v1 == v2:
                    continue
                return v1 > v2
        return self.typ > other.typ

    def __lt__(self, other):
        if self.typ == other.typ:
            for v1, v2 in zip(self.value, other.value):
                if v1 == v2:
                    continue
                return v1 < v2
        return self.typ < other.typ
    
    def __eq__(self, other):
        if self.typ == other.typ:
            for v1, v2 in zip(self.value, other.value):
                if v1 == v2:
                    continue
                return v1 == v2
        return self.typ == other.typ
    

if __name__ == "__main__":
    with open("/home/anas-haddad/Documents/AoC/day7/data.txt") as f:
        data = f.read().splitlines()
    data = [line.split() for line in data]
    data = [(line[:5], line[5:]) for line in data]
    data = [(list(map(Card, line[0])), list(map(Card, line[1]))) for line in data]
    results = 0
    for player1, player2 in data:
        results += sum([card1 > card2 for card1, card2 in zip(player1, player2)])
    print("task 1:", results)
    results = 0
    for player1, player2 in data:
        results += sum([card1 > card2 for card1, card2 in zip(player1, player2)])
    print("task 2:", results)