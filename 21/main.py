from functools import cache

inp = open("input.txt").read().strip()
codes = inp.splitlines()
keypad = ["789", "456", "123", " 0A"]
dirpad = [" ^A", "<v>"]


def dfs(pad, cur, dest):
    x, y = next((x, y) for y, r in enumerate(pad) for x, c in enumerate(r) if c == cur)
    x2, y2 = next(
        (x, y) for y, r in enumerate(pad) for x, c in enumerate(r) if c == dest
    )

    def g(x, y, seq):
        if (x, y) == (x2, y2):
            yield seq + "A"
        if x2 < x and pad[y][x - 1] != " ":
            yield from g(x - 1, y, seq + "<")
        if y2 < y and pad[y - 1][x] != " ":
            yield from g(x, y - 1, seq + "^")
        if y2 > y and pad[y + 1][x] != " ":
            yield from g(x, y + 1, seq + "v")
        if x2 > x and pad[y][x + 1] != " ":
            yield from g(x + 1, y, seq + ">")

    # Optimize for paths that have the least abount of zig-zagging between directions
    return min(g(x, y, ""), key=lambda pad: sum(a != b for a, b in zip(pad, pad[1:])))


@cache
def dp(code, robot, chain_length):
    if robot > chain_length:
        return len(code)
    pad = keypad if robot == 0 else dirpad
    pairs = zip("A" + code, code)
    return sum(dp(dfs(pad, cur, dest), robot + 1, chain_length) for cur, dest in pairs)


print(sum(dp(code, 0, 2) * int(code[:-1]) for code in codes))
print(sum(dp(code, 0, 25) * int(code[:-1]) for code in codes))
