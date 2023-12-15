import re

headers = ["seeds", "seed-to-soil map:", "soil-to-fertilizer map:",
            "fertilizer-to-water map:", "water-to-light map:",
            "light-to-temperature map:", "temperature-to-humidity map:",
            "humidity-to-location map:"]

def get_maps(key: str, values: list):
    if key == "seeds":
        return key, list(map(int, re.findall(r"\d+", values[0])))
    returns = {}
    title = "_".join(key[:-4].split("-to-"))
    for value in values:
        matches = re.match(r"(\d+)\s(\d+)\s(\d+)", value)
        for i in range(int(matches.group(3))):
            returns[int(matches.group(2)) + i] = int(matches.group(1)) + i
    return title, returns

if __name__ == "__main__":
    with open("/afs/desy.de/user/h/haddadan/private/AoC/day5/data.txt", "r") as f:
        data_iter = iter(f.read().splitlines())
    header = "seeds"
    data_seperated = {header: []}
    for line in data_iter:
        if not line:
            header = next(data_iter)[:-1]
            data_seperated[header] = []
            continue
        data_seperated[header].append(line)
    
    data_mapping = {}
    for key, values in data_seperated.items():
        new_key, new_values = get_maps(key, values)
        data_mapping[new_key] = new_values
    
    locations = {}
    seeds = data_mapping.pop("seeds")
    for seed in seeds:
        key_src, key_dst = "seed", "soil"
        distanation = seed
        while key_dst != "location":
            distanation = data_mapping[f"{key_src}_{key_dst}"].get(distanation, distanation)
            for key in data_mapping:
                new_key_src, new_key_dst = key.split("_")
                if key_dst == new_key_src:
                    key_src, key_dst = new_key_src, new_key_dst
                    break
        locations[seed] = data_mapping["humidity_location"].get(distanation, distanation)
    print(locations)
    print(min(locations.values()))

