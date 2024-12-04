input = open("input.txt", "r").read().strip()
diags = [(-1, -1), (1, -1), (-1, 1), (1, 1)]
dirs = [*diags, (0, -1), (0, 1), (-1, 0), (1, 0)]
lines = input.split("\n")
W, H = len(lines[0]), len(lines)

part_one = 0
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        for dx, dy in dirs:
            word = [c]
            nx, ny = x + dx, y + dy

            while 0 <= nx < W and 0 <= ny < H and len(word) < 4:
                word.append(lines[ny][nx])
                nx += dx
                ny += dy

            if word == ["X", "M", "A", "S"]:
                part_one += 1

print(part_one)

part_two = 0
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c != "A":
            continue

        corners = []
        for dx, dy in diags:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= W or ny < 0 or ny >= H:
                break

            corners.append(lines[ny][nx])

        valid_sets = [
            ["M", "M", "S", "S"],
            ["S", "S", "M", "M"],
            ["M", "S", "M", "S"],
            ["S", "M", "S", "M"],
        ]

        if corners in valid_sets:
            part_two += 1

print(part_two)
