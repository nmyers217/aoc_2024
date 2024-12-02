input = open("input.txt", "r").read().strip()

lines = [line.split() for line in input.splitlines()]


def is_safe(line):
    direction = 0
    line = [int(x) for x in line]

    for i in range(1, len(line)):
        diff = line[i] - line[i - 1]

        if abs(diff) < 1 or abs(diff) > 3:
            return False

        if direction == 0:
            direction = 1 if diff > 0 else -1
        elif direction == 1:
            if diff < 0:
                return False
        elif direction == -1:
            if diff > 0:
                return False

    return True


print(len([l for l in filter(is_safe, lines)]))

part_two = 0
for l in lines:
    if is_safe(l):
        part_two += 1
    else:
        for i in range(len(l)):
            cpy = l.copy()
            cpy = cpy[:i] + cpy[i + 1 :]
            if is_safe(cpy):
                part_two += 1
                break
print(part_two)
