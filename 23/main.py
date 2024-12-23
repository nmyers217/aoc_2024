import networkx as nx

inp = open("input.txt").read().strip()
lines = inp.splitlines()
G = nx.Graph()
for line in lines:
    a, b = line.split("-")
    G.add_edge(a, b)
unique_triangles = [
    clique for clique in nx.enumerate_all_cliques(G) if len(clique) == 3
]
has_a_t_node = [
    nodes for nodes in unique_triangles if any(node.startswith("t") for node in nodes)
]

print(len(has_a_t_node))
print(",".join(sorted(max(nx.find_cliques(G), key=len))))
