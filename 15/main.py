from collections import deque

inp = open("input.txt", "r").read().strip()
map, moves = inp.split("\n\n")
grid = {(x, y): c for y, line in enumerate(map.split("\n")) for x, c in enumerate(line)}
moves = [m for m in moves if m in "^v<>"]
x, y = next(k for k, v in grid.items() if v == "@")


def print_grid(grid):
    min_x, min_y = min(grid.keys())
    max_x, max_y = max(grid.keys())
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(grid.get((x, y), " "), end="")
        print()


for i, move in enumerate(moves):
    dx, dy = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}[move]
    nx, ny = x + dx, y + dy
    c = grid[(nx, ny)]

    if c == "#":
        continue
    elif c == ".":
        grid[(x, y)] = "."
        grid[(nx, ny)] = "@"
        x, y = nx, ny
    elif c == "O":
        can_move = False

        while grid[(nx, ny)] == "O":
            nx, ny = nx + dx, ny + dy
            c = grid[(nx, ny)]
            if c == "#":
                break
            elif c == ".":
                can_move = True
                break

        if can_move:
            cx, cy = nx, ny
            while grid[(cx, cy)] != "@":
                grid[(cx, cy)] = grid[(cx - dx, cy - dy)]
                cx, cy = cx - dx, cy - dy
            grid[(x, y)] = "."
            x, y = x + dx, y + dy

gps = sum([100 * y + x for x, y in grid.keys() if grid[(x, y)] == "O"])
print(gps)

map_lines = map.split("\n")
W, H = len(map_lines[0]), len(map_lines)

twice_map = []
for line in map_lines:
    row = []
    for c in line:
        if c == "#":
            row += ["#", "#"]
        elif c == "O":
            row += ["[", "]"]
        elif c == ".":
            row += [".", "."]
        elif c == "@":
            row += ["@", "."]
    twice_map += [row]

grid = {(x, y): c for y, line in enumerate(twice_map) for x, c in enumerate(line)}
x, y = next(k for k, v in grid.items() if v == "@")

for i, move in enumerate(moves):
    # print(i, move)
    dx, dy = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}[move]
    nx, ny = x + dx, y + dy
    c = grid[(nx, ny)]

    if c == "#":
        continue
    elif c == ".":
        grid[(x, y)] = "."
        grid[(nx, ny)] = "@"
        x, y = nx, ny
    elif c in "[]" and move in "<>":
        can_move = False
        while grid[(nx, ny)] in "[]":
            nx, ny = nx + dx, ny + dy
            c = grid[(nx, ny)]
            if c == "#":
                break
            elif c == ".":
                can_move = True
                break

        if can_move:
            cx, cy = nx, ny
            while grid[(cx, cy)] != "@":
                grid[(cx, cy)] = grid[(cx - dx, cy - dy)]
                cx, cy = cx - dx, cy - dy
            grid[(x, y)] = "."
            x, y = x + dx, y + dy
    elif c in "[]" and move in "^v":
        can_move = True
        side = c
        queue = deque([(nx, ny)])
        seen = set()
        empties = set()

        if side == "[":
            queue.append((nx + 1, ny))
        else:
            queue.append((nx - 1, ny))

        while queue:
            cx, cy = queue.popleft()
            seen.add((cx, cy))
            cx2, cy2 = cx + dx, cy + dy
            c2 = grid[(cx2, cy2)]

            if c2 == "#":
                can_move = False
                break
            elif c2 in "[]":
                queue.append((cx2, cy2))
                if c2 == "[":
                    queue.append((cx2 + 1, cy2))
                else:
                    queue.append((cx2 - 1, cy2))
            elif c2 == ".":
                empties.add((cx2, cy2))

        # print(can_move)
        # print(seen)
        # print(empties)

        if can_move:
            empties = deque(empties)
            while empties:
                ex, ey = empties.popleft()
                if (ex - dx, ey - dy) in seen:
                    grid[(ex, ey)] = grid[(ex - dx, ey - dy)]
                    grid[(ex - dx, ey - dy)] = "."
                    empties.append((ex - dx, ey - dy))

            grid[(x, y)] = "."
            grid[(x + dx, y + dy)] = "@"
            x, y = x + dx, y + dy

    # print_grid(grid)
    # input("press enter to continue")

gps = sum([100 * y + x for x, y in grid.keys() if grid[(x, y)] == "["])
print(gps)
