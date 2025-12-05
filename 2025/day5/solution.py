import sys
import re

sys.path.append("C:\\Users\\famil\\Documents\\Sonstiges\\AoC\\2025\\")

from aoc_utils import read_input, validate_test


class Rule:
    idx = 0

    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper
        self.size = upper - lower + 1
        self.id = Rule.idx
        Rule.idx += 1

    def is_valid(self, food_id: int) -> bool:
        return self.lower <= food_id <= self.upper

    def merge(self, other_rule):
        if self.has_overlap(other_rule):
            return Rule(min(self.lower, other_rule.lower), max(self.upper, other_rule.upper))
        raise ValueError("Cannot merge non-overlapping rules")

    def has_overlap(self, other_rule) -> bool:
        return not (self.upper < other_rule.lower or self.lower > other_rule.upper)


class Id_Checker:
    def __init__(self):
        self.bounds = {}
        self.size = 0

    def add_bounds(self, bounds: str):
        pattern = re.compile(r"(\d+)-(\d+)")
        match = pattern.match(bounds)
        if not match:
            raise ValueError(f"Invalid bounds format: {bounds}")
        self.update_bounds(int(match.group(1)), int(match.group(2)))
        self.update_size()

    def update_size(self):
        self.size = sum(rule.size for rule in self.bounds.values())

    def update_bounds(self, lower: int, upper: int):
        new_rule = Rule(lower, upper)
        overlapping_rules = self.get_overlapping_rules(new_rule)
        if overlapping_rules:
            while self.get_overlapping_rules(new_rule):
                rule = self.bounds.pop(overlapping_rules.pop())
                new_rule = new_rule.merge(rule)
        self.bounds[new_rule.id] = new_rule

    def is_valid(self, food_id: int) -> bool:
        return any(rule.is_valid(food_id) for rule in self.bounds.values())

    def get_valid_rules(self, food_id: int) -> list[bool]:
        return [rule.id for rule in self.bounds.values() if rule.is_valid(food_id)]

    def get_overlapping_rules(self, other_rule) -> list[Rule]:
        return [rule.id for rule in self.bounds.values() if rule.has_overlap(other_rule)]


def split_input(checker: Id_Checker, data: list[str]) -> list[int]:
    split_index = data.index("")
    [checker.add_bounds(rule) for rule in data[:split_index]]
    foods = [int(food) for food in data[split_index + 1:]]
    return foods


def solution(checker: Id_Checker, foods: list[int]) -> int:
    good_food = 0
    for food in foods:
        if checker.is_valid(food):
            good_food += 1
    return good_food


if __name__ == "__main__":
    test_checker = Id_Checker()
    input_checker = Id_Checker()

    test_data = read_input("test.txt", "\n")
    input_data = read_input("input.txt", "\n")

    test_foods = split_input(test_checker, test_data)
    input_foods = split_input(input_checker, input_data)

    validate_test(solution(test_checker, test_foods), 3)
    print("Part 1:", solution(input_checker, input_foods))

    validate_test(test_checker.size, 14)
    print("Part 2:", input_checker.size)
