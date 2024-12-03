import re

input = open("input.txt", "r").read().strip()

matches = re.findall(r"mul\((\d+),(\d+)\)", input)

print(sum(int(a) * int(b) for a, b in matches))

regex = r"mul\((\d+),(\d+)\)|(do)\(|(don't)\("
matches = re.findall(regex, input)

part_two = 0
on = True
for a, b, do, dont in matches:
    if do:
        on = True
    elif dont:
        on = False
    elif on:
        part_two += int(a) * int(b)

print(part_two)
