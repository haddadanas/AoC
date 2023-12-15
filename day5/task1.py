import re

headers = ["seeds", "seed-to-soil map:", "soil-to-fertilizer map:",
            "fertilizer-to-water map:", "water-to-light map:",
            "light-to-temperature map:", "temperature-to-humidity map:",
            "humidity-to-location map:"]

def format_input(data: list):
    results = {}
    current_header = "seeds:"
    for line in data:
        if line in headers:
            current_header = line
            results[current_header] = []
            continue
        results[current_header].append(line)

if __name__ == "__main__":
    with open("data.txt", "r") as f:
        data = f.read().splitlines()
    print(format_input(data).keys())

