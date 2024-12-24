import networkx as nx
from collections import deque

inp = open("input.txt").read().strip()

inp = """
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
""".strip()

wires, gates = inp.split("\n\n")
wire_values = {}

for wire in wires.splitlines():
    wire, value = wire.split(": ")
    wire_values[wire] = int(value)

queue = deque()
for gate in gates.splitlines():
    inputs, output = gate.split(" -> ")
    a, logic, b = inputs.split()
    queue.append((a, b, logic, output))

while queue:
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

    queue = next_queue


items = list([(k, v) for k, v in wire_values.items() if k.startswith("z")])
items.sort(reverse=True)
print(items)
print(int("".join(str(v) for k, v in items), 2))
