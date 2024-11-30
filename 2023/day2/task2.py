from task1 import convert_to_dict, game

def game_power(red:int, green:int, blue:int):
    return red * green * blue

def get_power_per_game(games:list):
    reds = [g.red for g in games]
    greens = [g.green for g in games]
    blues = [g.blue for g in games]
    return game_power(max(reds), max(greens), max(blues))

if __name__ == "__main__":
    with open("./data.txt") as f:
        data = f.read().splitlines()

    data = convert_to_dict(data)
    result = 0
    for id, games in data.items():
        result += get_power_per_game(games)

    print(result)