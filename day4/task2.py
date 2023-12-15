from task1 import Card, format_input

if __name__ == "__main__":
    with open("/home/haddadan/AoC/day4/data.txt") as f:
        data = f.read().splitlines()

    cards = [format_input(line) for line in data]

    factor = {card.id: 1 for card in cards}
    for card in cards:
        d = card.n_winning
        for i in range(card.n_winning):
            bonus_card = card.id + i + 1
            if bonus_card < len(cards) + 1:
                factor[bonus_card] += 1 * factor[card.id]

    print(f"Sum of points: {sum(factor.values())}")