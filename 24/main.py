import networkx as nx
import graphviz as gv
from collections import deque
from collections import defaultdict

inp = open("input.txt").read().strip()
wires, gates = inp.split("\n\n")
wires = [w.split(": ") for w in wires.splitlines()]
gates = gates.splitlines()


def get_wire_values(wires, gates):
    wire_values = {}

    for wire, value in wires:
        wire_values[wire] = int(value)

    queue = deque()
    for gate in gates:
        inputs, output = gate.split(" -> ")
        a, logic, b = inputs.split()
        queue.append((a, b, logic, output))

    iterations = 0
    while queue:
        iterations += 1
        next_queue = deque()

        for i in range(len(queue)):
            a, b, logic, output = queue.popleft()

            if wire_values.get(a) is None or wire_values.get(b) is None:
                next_queue.append((a, b, logic, output))
                continue

            if logic == "AND":
                wire_values[output] = wire_values[a] and wire_values[b]
            elif logic == "OR":
                wire_values[output] = wire_values[a] or wire_values[b]
            elif logic == "XOR":
                wire_values[output] = 1 if wire_values[a] != wire_values[b] else 0

        if iterations > 1000:
            break

        queue = next_queue

    return wire_values


def get_n(wire_values, key):
    items = list([(k, v) for k, v in wire_values.items() if k.startswith(key)])
    # print(items)
    items.sort(reverse=True)
    return "".join(str(v) for k, v in items)


wire_values = get_wire_values(wires, gates)
print(int(get_n(wire_values, "z"), 2))


def output_graph():
    G = nx.DiGraph()

    for wire, value in wires:
        G.add_node(wire)

    for gate in gates:
        inputs, output = gate.split(" -> ")
        a, logic, b = inputs.split()
        G.add_edge(a, output)
        G.add_edge(b, output)

    print("digraph G {")
    for edge in G.edges:
        print(" -> ".join(edge))
    print("}")


# output_graph()


def swap(gates, a, b):
    for i, gate in enumerate(gates):
        inputs, output = gate
        if output == a:
            gates[i] = (inputs, b)
        elif output == b:
            gates[i] = (inputs, a)


gates = [gate.split(" -> ") for gate in gates]
gates = [(tuple(a.split()), b) for a, b in gates]
num_z = sum(v.startswith("z") for _, v in gates)
pairs = []
bit, adder, c1, c2, carry = ["__" for _ in range(5)]
while len(pairs) < 4:
    lookup = {output: (a, op, b) for (a, op, b), output in gates}
    reverse_lookup = defaultdict(
        str, {frozenset((a, op, b)): output for (a, op, b), output in gates}
    )
    for i in range(num_z):
        if i == 0:
            adder = reverse_lookup[frozenset(("x00", "XOR", "y00"))]
            carry = reverse_lookup[frozenset(("x00", "AND", "y00"))]
        else:
            bit = reverse_lookup[frozenset((f"x{i:02}", "XOR", f"y{i:02}"))]
            adder = reverse_lookup[frozenset((bit, "XOR", carry))]
            if adder:
                c1 = reverse_lookup[frozenset((f"x{i:02}", "AND", f"y{i:02}"))]
                c2 = reverse_lookup[frozenset((bit, "AND", carry))]
                carry = reverse_lookup[frozenset((c1, "OR", c2))]

        if not adder:
            a, op, b = lookup[f"z{i:02}"]
            if frozenset((a, "XOR", carry)) in reverse_lookup:
                pairs.append((bit, a))
                swap(gates, bit, a)
                break
            if frozenset((b, "XOR", carry)) in reverse_lookup:
                pairs.append((bit, b))
                swap(gates, bit, b)
                break
        elif adder != f"z{i:02}":
            pairs.append((adder, f"z{i:02}"))
            swap(gates, adder, f"z{i:02}")
            break
print(",".join(sorted([x for y in pairs for x in y])))
