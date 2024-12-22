inp = open("input.txt").read().strip()
nums = list(map(int, inp.splitlines()))


def next_secret(n):
    n = ((n * 64) ^ n) % 16777216
    n = ((n // 32) ^ n) % 16777216
    n = ((n * 2048) ^ n) % 16777216
    return n


def price_deltas(prices):
    return [a - b for a, b in zip(prices[1:], prices)]


delta_groups = {}
p1 = 0
for n in nums:
    prices = [n % 10]
    for i in range(2000):
        n = next_secret(n)
        prices += [n % 10]
    p1 += n
    deltas = price_deltas(prices)
    seen_deltas = set()
    for i in range(4, len(prices)):
        delta_group = tuple(deltas[i - 4 : i])
        if delta_group in seen_deltas:
            continue
        seen_deltas.add(delta_group)
        delta_groups[delta_group] = delta_groups.get(delta_group, 0) + prices[i]

print(p1)
print(max(delta_groups.values()))
