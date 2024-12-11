input = open("input.txt", "r").read().strip()
stones = [int(x) for x in input.split()]


def dp(stone, i, memo={}):
    if (stone, i) in memo:
        return memo[stone, i]
    if i == 0:
        memo[(stone, i)] = 1
        return 1

    s = str(stone)
    l = len(s)
    res = None

    if stone == 0:
        res = dp(1, i - 1, memo)
    elif l % 2 == 0:
        res = dp(int(s[: l // 2]), i - 1, memo) + dp(int(s[l // 2 :]), i - 1, memo)
    else:
        res = dp(stone * 2024, i - 1, memo)

    memo[(stone, i)] = res
    return res


print(sum(dp(stone, 25) for stone in stones))
print(sum(dp(stone, 75) for stone in stones))
