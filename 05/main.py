input = open("input.txt", "r").read().strip()
sections = input.split("\n\n")
order_rules = {
    (int(l), int(r)) for l, r in [s.split("|") for s in sections[0].split("\n")]
}
updates = [[int(x) for x in line.split(",")] for line in sections[1].split("\n")]


def is_correct(update):
    for i in range(len(update) - 1, 0, -1):
        for j in range(i):
            if (update[j], update[i]) not in order_rules:
                return False
    return True


def get_middles(updates):
    return [update[len(update) // 2] for update in updates]


def make_correct(update):
    for i in range(len(update) - 1, 0, -1):
        for j in range(i):
            if (update[j], update[i]) not in order_rules:
                update[j], update[i] = update[i], update[j]
    return update


correct_updates = [update for update in updates if is_correct(update)]
incorrect_updates = [update for update in updates if not is_correct(update)]
fixed_updates = [make_correct(update) for update in incorrect_updates]

print(sum(get_middles(correct_updates)))
print(sum(get_middles(fixed_updates)))
