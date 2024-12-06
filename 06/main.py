input = open("input.txt", "r").read().strip()

start = None
sparse_grid = {}
for y, row in enumerate(input.split("\n")):
    for x, value in enumerate(row):
        sparse_grid[(x, y)] = value
        if value == "^":
            start = (x, y)


def walk():
    iterations = 0
    cur = start
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    cur_dir = 0
    visited = set()

    while cur and cur in sparse_grid:
        if iterations > len(sparse_grid) // 2:
            # Safe to say we're stuck
            return visited, True

        visited.add(cur)
        (dx, dy) = dirs[cur_dir]
        next = (cur[0] + dx, cur[1] + dy)

        while sparse_grid.get(next) == "#":
            cur_dir = (cur_dir + 1) % 4
            (dx, dy) = dirs[cur_dir]
            next = (cur[0] + dx, cur[1] + dy)

        iterations += 1
        cur = next

    return visited, False


part_two = 0
for k, v in sparse_grid.items():
    if v != ".":
        continue
    sparse_grid[k] = "#"
    visited, stuck = walk()
    if stuck:
        part_two += 1
    sparse_grid[k] = "."

print(len(walk()[0]))
print(part_two)
