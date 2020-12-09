import os
import math

HERE = os.path.abspath(os.path.dirname(__file__))
INPUT_FP = os.path.join(HERE, "input.txt")
TREE = "#"


with open(INPUT_FP, "r") as fp:
    FOREST = [line.strip() for line in fp.readlines()]


def toboggan(*, start=(0, 0), slope):
    x, y = start
    x_step, y_step = slope

    while y < len(FOREST):
        # wrap around the x axis
        x = x % len(FOREST[y])

        yield FOREST[y][x]

        x, y = x+x_step, y+y_step


def count_trees(route):
    return len([tile for tile in route if tile == TREE])


print("Part One")
route = toboggan(slope=(3, 1))
print("trees encountered:", count_trees(route))


print("Part Two")

ALL_SLOPES = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]
tree_counts = []

for slope in ALL_SLOPES:
    route = toboggan(slope=slope)
    tree_counts.append(count_trees(route))

print(" * ".join(str(c) for c in tree_counts), "=", math.prod(tree_counts))
