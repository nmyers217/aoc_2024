from collections import defaultdict

input = open("input.txt", "r").read().strip()
lines = input.split("\n")
w = len(lines[0])
h = len(lines)
grid = defaultdict(lambda: ".")
seen = set()
islands = []

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        grid[x, y] = c


def search_island(x, y, c):
    result = set()

    def dfs(x, y, c):
        if (x, y) not in seen and grid[x, y] == c:
            seen.add((x, y))
            result.add((x, y))
            dfs(x - 1, y, c)
            dfs(x + 1, y, c)
            dfs(x, y - 1, c)
            dfs(x, y + 1, c)

    dfs(x, y, c)
    return result


def find_perimeter(island):
    result = 0
    c = grid[list(island)[0]]
    for x, y in island:
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if grid[x + dx, y + dy] != c:
                result += 1
    return result


def find_sides(island):
    fences = set()
    c = grid[list(island)[0]]
    for x, y in island:
        px, py = x * 3, y * 3
        if grid[x - 1, y] != c:
            fences.add((px - 1, py))
        if grid[x + 1, y] != c:
            fences.add((px + 1, py))
        if grid[x, y - 1] != c:
            fences.add((px, py - 1))
        if grid[x, y + 1] != c:
            fences.add((px, py + 1))
    p = 0
    for px, py in list(fences):
        if (px - 3, py) not in fences and (px, py - 3) not in fences:
            p += 1
    return p


for y in range(h):
    for x in range(w):
        if (x, y) not in seen:
            islands.append(search_island(x, y, grid[x, y]))
print(sum(find_perimeter(r) * len(r) for r in islands))
print(sum(find_sides(r) * len(r) for r in islands))
