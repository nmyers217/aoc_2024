from collections import deque

input = open("input.txt", "r").read().strip()
grid = {
    complex(x, y): int(n)
    for y, row in enumerate(input.split("\n"))
    for x, n in enumerate(row)
}
dirs = [complex(x, y) for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]]


def dfs(n):
    total = 0
    stack = [n]
    seen = set()

    while stack:
        pos = stack.pop()

        if grid[pos] == 9:
            total += 1
            continue

        for d in dirs:
            new_pos = pos + d

            if (
                new_pos in grid
                and new_pos not in seen
                and grid[new_pos] == grid[pos] + 1
            ):
                stack.append(new_pos)
                seen.add(new_pos)

    return total


def bfs(n):
    total = 0
    queue = deque([n])

    while queue:
        pos = queue.pop()

        if grid[pos] == 9:
            total += 1
            continue
        for d in dirs:
            new_pos = pos + d
            if new_pos in grid and grid[new_pos] == grid[pos] + 1:
                queue.appendleft(new_pos)

    return total


print(sum(dfs(k) for k, v in grid.items() if v == 0))
print(sum(bfs(k) for k, v in grid.items() if v == 0))
