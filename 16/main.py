import networkx as nx
import numpy as np

grid = np.array([[*line] for line in open("input.txt").read().splitlines()])
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
G = nx.DiGraph()

for pos, char in np.ndenumerate(grid):
    if char == "#":
        continue
    if char == "S":
        start = pos
    elif char == "E":
        end = pos
    for i, dir in enumerate(dirs):
        G.add_edge((pos, i), (pos, (i + 1) % 4), weight=1000)
        G.add_edge((pos, i), (pos, (i - 1) % 4), weight=1000)
        x, y = pos[0] + dir[0], pos[1] + dir[1]
        if grid[x, y] != "#":
            G.add_edge((pos, i), ((x, y), i), weight=1)

path_lengths = [
    nx.shortest_path_length(G, (start, 0), (end, i), "weight") for i in range(4)
]
print(min(path_lengths))

seen = set()
for i in range(4):
    for path in nx.all_shortest_paths(G, (start, 0), (end, i), "weight"):
        for p in path:
            seen.add(p[0])
print(len(seen))
