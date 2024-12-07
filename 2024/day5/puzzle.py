from collections import defaultdict
import os 

current_dir = os.path.dirname(os.path.realpath(__file__))
with open(f"{current_dir}/rules", "r") as file:
    rules = file.read().splitlines()

with open(f"{current_dir}/update", "r") as file:
    data = [line.split(",") for line in file.read().splitlines()]


class Rule:
    def __init__(self):
        self.rules: dict[str: list] = defaultdict(list)

    def add_rule(self, pre, post):
        self.rules[str(pre)].append(str(post))

    def is_valid(self, num, post):
        if not isinstance(post, list):
            post = [post]
        for p in post:
            if str(num) in self.rules[str(p)]:
                return False
        return True

    def before(self, num1, num2):
        if str(num1) in self.rules[str(num2)]:
            return False
        return True

    def check_invalid(self, num, post):
        if not isinstance(post, list):
            post = [post]
        invalid = []
        for p in post:
            if str(num) in self.rules[str(p)]:
                invalid.append(str(p))
        return invalid

    def sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_sorted = self.sort(left_half)
        right_sorted = self.sort(right_half)

        return self.merge(left_sorted, right_sorted)

    def merge(self, left, right):
        result = []
        left_index = 0
        right_index = 0

        while left_index < len(left) and right_index < len(right):
            if self.before(left[left_index], right[right_index]):
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        result.extend(left[left_index:])
        result.extend(right[right_index:])

        return result


update_rules = Rule()
for rule in rules:
    pre, post = rule.strip().split("|")
    update_rules.add_rule(pre, post)

passing = set()
is_pass = True
for i, line in enumerate(data):
    is_pass = True
    for ind in range(len(line) - 1):
        if update_rules.is_valid(line[ind], line[ind + 1:]):
            pass
        else:
            is_pass = False
            break
    if is_pass:
        passing.add(i)

median_sum = 0
for i in passing:
    line = data[i]
    middleIndex = (len(line) - 1)/2
    median_sum += int(line[int(middleIndex)])

print(median_sum)


# part 2
sorted_median_sum = 0
for i, line in enumerate(data):
    if i in passing:
        continue
    sorted_line = update_rules.sort(line)
    middleIndex = (len(sorted_line) - 1)/2
    sorted_median_sum += int(sorted_line[int(middleIndex)])

print(sorted_median_sum)