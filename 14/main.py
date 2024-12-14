import re
import math

inp = open("input.txt", "r").read().strip()

W, H = 11, 7
W, H = 101, 103
seconds = 100
robots = []

for line in inp.split("\n"):
    x, y, vx, vy = map(int, re.findall(r"-?\d+", line))
    robots.append((x, y, vx, vy))


def advance(robots, seconds):
    for i in range(seconds):
        for j, (x, y, vx, vy) in enumerate(robots):
            x += vx
            y += vy
            if x < 0:
                x += W
            if x >= W:
                x -= W
            if y < 0:
                y += H
            if y >= H:
                y -= H
            robots[j] = (x, y, vx, vy)


advance(robots, seconds)

robot_pairs = [(x, y) for x, y, vx, vy in robots]
robot_pairs.sort()

# count the robots in each of the four quadrants, excluing the center row and column
quadrants = [0, 0, 0, 0]
half_w = W // 2
half_h = H // 2

for x, y in robot_pairs:
    if x < half_w and y < half_h:
        quadrants[0] += 1
    elif x >= half_w + 1 and y < half_h:
        quadrants[1] += 1
    elif x < half_w and y >= half_h + 1:
        quadrants[2] += 1
    elif x >= half_w + 1 and y >= half_h + 1:
        quadrants[3] += 1

print(math.prod(quadrants))

robots = []
for line in inp.split("\n"):
    x, y, vx, vy = map(int, re.findall(r"-?\d+", line))
    robots.append((x, y, vx, vy))

interactive = True
time = 0
# I incremented by 1000 at a time and found a tree at 81000 and found it this way by trial and error
time = 8000
advance(robots, time)
while interactive:
    advance(robots, 1)
    time += 1

    robots_str = ""
    for y in range(H):
        for x in range(W):
            found = False
            for r in robots:
                if r and r[0] == x and r[1] == y:
                    found = True
                    break
            if found:
                robots_str += "#"
            else:
                robots_str += "."
        robots_str += "\n"

    print(time)
    if "###############################" in robots_str:
        print(robots_str)
        print(input("waiting..."))
