import re

input = open("input.txt", "r").read().strip()

# input = """##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########
#
# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
# """.strip()

map, moves = input.split("\n\n")
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


print_grid(grid)

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

    # print_grid(grid)

gps = sum([100 * y + x for x, y in grid.keys() if grid[(x, y)] == "O"])
print(gps)
