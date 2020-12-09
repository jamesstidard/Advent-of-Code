import os
import math

here = os.path.abspath(os.path.dirname(__file__))
input_fp = os.path.join(here, "input.txt")

with open(input_fp, "r") as fp:
    forest = [line.strip() for line in fp.readlines()]


slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

counts = []

for right_step, down_step in slopes:
    tree_count = 0
    x, y = 0, 0

    while True:
        if y >= len(forest):
            break

        wrapped_x = x % len(forest[y])

        if forest[y][wrapped_x] == "#":
            tree_count += 1

        x, y = x+right_step, y+down_step

    counts.append(tree_count)

print(math.prod(counts))
