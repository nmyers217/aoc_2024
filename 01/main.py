from collections import defaultdict

input = open("input.txt", "r").read().strip()

a, b = [], []

for line in input.split("\n"):
    left, right = line.split("   ")
    a.append(int(left))
    b.append(int(right))

a, b = sorted(a), sorted(b)

part_one = sum([abs(b[i] - a[i]) for i in range(len(a))])

right_counts = defaultdict(lambda: 0)

for right in b:
    right_counts[right] += 1

part_two = 0
for left in a:
    part_two += left * right_counts[left]

print(part_one)
print(part_two)
