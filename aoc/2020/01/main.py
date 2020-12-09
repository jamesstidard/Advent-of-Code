import os
import math
import itertools


HERE = os.path.abspath(os.path.dirname(__file__))
INPUT_FP = os.path.join(HERE, "input.txt")

with open(INPUT_FP, "r") as fp:
    EXPENSES = {float(line) for line in fp.readlines()}


def solve(*, target, size):
    for components in itertools.combinations(EXPENSES, size-1):
        remainder = target - sum(components)
        if remainder in EXPENSES:
            return (*components, remainder)
    else:
        raise ValueError("No Solution Found")


print("Part One")
components = solve(target=2020, size=2)
print(" + ".join(str(c) for c in components), "=", sum(components))
print(" * ".join(str(c) for c in components), "=", math.prod(components))


print("Part Two")
components = solve(target=2020, size=3)
print(" + ".join(str(c) for c in components), "=", sum(components))
print(" * ".join(str(c) for c in components), "=", math.prod(components))
