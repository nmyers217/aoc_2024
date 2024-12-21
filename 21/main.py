import re

inp = open("input.txt").read()

inp = """
029A
980A
179A
456A
379A
""".strip()

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


def generic_calculate_sequence(code, pad, pad_vals):
    cur = pad_vals["A"]
    sequence = []

    for c in code:
        dest = pad_vals[c]
        # print(f"cur: {cur}, dest: {dest}, to press {c}")
        while cur != dest:
            # print(f"{pad[cur]} -> {pad[dest]}")
            x, y = cur
            x2, y2 = dest
            dx, dy = x2 - x, y2 - y

            if dx != 0 and pad[(x + dx, y)] is not None:
                if dx < 0:
                    cur = (x - 1, y)
                    sequence.append("<")
                else:
                    cur = (x + 1, y)
                    sequence.append(">")
                continue

            if dy != 0 and pad[(x, y + dy)] is not None:
                if dy < 0:
                    cur = (x, y - 1)
                    sequence.append("^")
                else:
                    cur = (x, y + 1)
                    sequence.append("v")
                continue

        sequence.append("A")
    return "".join(sequence)


def calculate_sequence(key_code):
    result = generic_calculate_sequence(key_code, keypad_coords, keypad_vals)
    print(result)
    result = generic_calculate_sequence(result, dirpad_coords, dirpad_vals)
    print(result)
    result = generic_calculate_sequence(result, dirpad_coords, dirpad_vals)
    print(result)
    return result


def score(code):
    seq = calculate_sequence(code)
    prefix = int(re.match(r"(.*)A", code).group(1))
    print(f"{len(seq)} * {prefix} = {prefix * len(seq)}")
    return len(seq) * prefix


# print(sum(score(code) for code in codes))

# TODO: this one is wrong because not every manhattan distance sequence has the same cost on the next pad :(
print(score(codes[3]))
