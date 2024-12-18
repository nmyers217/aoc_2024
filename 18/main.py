import re
import networkx as nx

inp = open("input.txt").read()
coords = [(int(x), int(y)) for x, y in re.findall(r"(\d+),(\d+)", inp)]
W = H = 71
B = 1024
fallen = set(coords[:B])
G = nx.DiGraph()

for x in range(W):
    for y in range(H):
        if (x, y) in fallen:
            continue
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < W and 0 <= new_y < H and (new_x, new_y) not in fallen:
                G.add_edge((x, y), (new_x, new_y), weight=1)

print(nx.shortest_path_length(G, (0, 0), (W - 1, H - 1), "weight"))

for coord in coords[B + 1 :]:
    G.remove_node(coord)
    if not nx.has_path(G, (0, 0), (W - 1, H - 1)):
        x, y = coord
        print(f"{x},{y}")
        break
