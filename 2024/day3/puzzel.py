import re

with open('input') as f:
    data = f.readlines()

# part 1
pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
result = 0
for line in data:
    m = pattern.findall(line)
    for a, b in m:
        result += int(a) * int(b)

print(result)

# part 2
pattern = re.compile(r'(do\(\)|don\'t\(\))|mul\((\d{1,3}),(\d{1,3})\)')

result = 0
do = True
for line in data:
    m = pattern.findall(line)
    for match in m:
        if match[0] == 'do()':
            do = True
            continue
        elif match[0] == 'don\'t()':
            do = False
            continue
        if do:
            result += int(match[1]) * int(match[2])
        
print(result)