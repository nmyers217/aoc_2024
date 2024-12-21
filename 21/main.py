import re

inp = open("input.txt").read()

# inp = """
# 029A
# 980A
# 179A
# 456A
# 379A
# """.strip()

codes = inp.splitlines()
dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
keypad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]
dirpad = [
    [None, "^", "A"],
    ["<", "v", ">"],
]
keypad_coords = {
    (
        x,
        y,
    ): keypad[y][x]
    for y in range(4)
    for x in range(3)
}
keypad_vals = {keypad[y][x]: (x, y) for y in range(4) for x in range(3)}
dirpad_coords = {
    (
        x,
        y,
    ): dirpad[y][x]
    for y in range(2)
    for x in range(3)
}
dirpad_vals = {dirpad[y][x]: (x, y) for y in range(2) for x in range(3)}


def calculate_all_sequences(code, keypad_coords, keypad_vals):
    def recurse(code, seq, cur):
        if not code:
            return [seq]

        dest = keypad_vals[code[0]]

        if cur == dest:
            return recurse(code[1:], seq + "A", cur)

        sequences = []

        x, y = cur
        x2, y2 = dest
        dx, dy = x2 - x, y2 - y

        if dx > 0 and keypad_coords.get((x + 1, y)):
            sequences.extend(recurse(code, seq + ">", (x + 1, y)))
        if dy < 0 and keypad_coords.get((x, y - 1)):
            sequences.extend(recurse(code, seq + "^", (x, y - 1)))
        if dy > 0 and keypad_coords.get((x, y + 1)):
            sequences.extend(recurse(code, seq + "v", (x, y + 1)))
        if dx < 0 and keypad_coords.get((x - 1, y)):
            sequences.extend(recurse(code, seq + "<", (x - 1, y)))

        return sequences

    return recurse(code, "", keypad_vals["A"])


def calculate_shortest_sequence(key_code):
    sequences = calculate_all_sequences(key_code, keypad_coords, keypad_vals)
    sequences = [
        item
        for sublist in [
            calculate_all_sequences(seq, dirpad_coords, dirpad_vals)
            for seq in sequences
        ]
        for item in sublist
    ]
    sequences = [
        item
        for sublist in [
            calculate_all_sequences(seq, dirpad_coords, dirpad_vals)
            for seq in sequences
        ]
        for item in sublist
    ]
    return min(sequences, key=len)


def score(code):
    seq = calculate_shortest_sequence(code)
    prefix = int(re.match(r"(.*)A", code).group(1))
    print(f"{len(seq)} * {prefix} = {prefix * len(seq)}")
    return len(seq) * prefix


print(sum(score(code) for code in codes))
