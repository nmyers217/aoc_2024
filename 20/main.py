import networkx as nx

inp = open("input.txt").read()
lines = inp.splitlines()
grid = {(x, y): c for y, line in enumerate(lines) for x, c in enumerate(line)}
G = nx.DiGraph()

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "#":
            continue
        G.add_node((x, y))
        if c == "S":
            start = (x, y)
        elif c == "E":
            end = (x, y)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) in grid and grid[(new_x, new_y)] != "#":
                G.add_edge((x, y), (new_x, new_y), weight=1)

# Doing floyd warshall or dijkstra seems super slow here, but idc because it makes the code look elegant
fw = dict(nx.all_pairs_shortest_path_length(G))
print(f"Shortest path length from {start} to {end}: {fw[start][end]}")
path = [p for p in nx.all_shortest_paths(G, start, end, weight="weight")][0]


def best_cheats(dist):
    result = {}
    for x, y in path:
        for x2, y2 in G.nodes:
            if (x, y) == (x2, y2):
                continue

            manhattan = abs(x2 - x) + abs(y2 - y)
            if manhattan > dist:
                continue

            head = fw[start][(x, y)]
            tail = fw[(x2, y2)][end]
            total = head + manhattan + tail
            time_saved = fw[start][end] - total
            if time_saved > 0:
                result[((x, y), (x2, y2))] = time_saved
    return result


print(len([v for v in best_cheats(2).values() if v >= 100]))
print(len([v for v in best_cheats(20).values() if v >= 100]))
