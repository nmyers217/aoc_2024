import re
import numpy as np

input = open("input.txt", "r").read().strip()
claws = input.split("\n\n")

part_one, part_two = 0, 0
for claw in claws:
    lines = claw.split("\n")
    ax, ay, bx, by, target_x, target_y = [int(x) for x in re.findall(r"\d+", claw)]
    A = [[ax, bx], [ay, by]]
    B = [target_x, target_y]
    a, b = np.linalg.solve(A, B)

    if a > 0 and b > 0 and abs(a - round(a)) < 0.0001 and abs(b - round(b)) < 0.0001:
        part_one += 3 * round(a) + round(b)

    big_num = 10000000000000
    B = [target_x + big_num, target_y + big_num]
    a, b = np.linalg.solve(A, B)
    if a > 0 and b > 0 and abs(a - round(a)) < 0.0001 and abs(b - round(b)) < 0.0001:
        part_two += 3 * round(a) + round(b)

print(part_one)
print(part_two)
