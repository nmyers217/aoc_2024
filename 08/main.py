input = open("input.txt", "r").read().strip()
lines = input.split("\n")
W, H = len(lines[0]), len(lines)
frequencies = {}

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == ".":
            continue
        if c not in frequencies:
            frequencies[c] = []
        frequencies[c].append((x, y))


def analyze(harmonics=False):
    antinodes = set()

    for k, v in frequencies.items():
        for i in range(len(v)):
            for j in range(len(v)):
                if i == j:
                    continue

                x1, y1 = v[i]
                x2, y2 = v[j]
                dx, dy = x2 - x1, y2 - y1
                # Idk exaclty why i had to flip the signs on part 2 but i tried it and it works so idc
                if harmonics:
                    new_x, new_y = x1 + dx, y1 + dy
                else:
                    new_x, new_y = x1 - dx, y1 - dy

                if new_x < 0 or new_x >= W or new_y < 0 or new_y >= H:
                    continue
                antinodes.add((new_x, new_y))

                while harmonics:
                    new_x, new_y = new_x + dx, new_y + dy
                    if new_x < 0 or new_x >= W or new_y < 0 or new_y >= H:
                        break
                    antinodes.add((new_x, new_y))

    return len(antinodes)


print(analyze())
print(analyze(True))
