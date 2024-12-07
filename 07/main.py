import re

input = open("input.txt", "r").read().strip()
lines = [[int(x) for x in re.findall(r"\d+", line)] for line in input.split("\n")]


def solve(test, nums, concat=False):
    def recurse(i, total):
        if i == len(nums):
            return total == test
        return (
            recurse(i + 1, total + nums[i])
            or recurse(i + 1, total * nums[i])
            or (concat and recurse(i + 1, int(f"{total}{nums[i]}")))
        )

    return recurse(0, 0)


part_one, part_two = 0, 0
for test, *nums in lines:
    if solve(test, nums):
        part_one += test
    if solve(test, nums, True):
        part_two += test

print(part_one)
print(part_two)
