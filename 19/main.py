from functools import cache

inp = open("input.txt").read()
towels, designs = inp.split("\n\n")
towels = towels.split(", ")
designs = designs.splitlines()


@cache
def total(design):
    if not design:
        return 1
    return sum(total(design[len(t) :]) for t in towels if design.startswith(t))


totals = [total(d) for d in designs]
print(len([t for t in totals if t > 0]))
print(sum(total(d) for d in designs))
