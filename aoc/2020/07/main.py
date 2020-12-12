import os
import re


SHINY_GOLD = "shiny gold"
CONTAINER_BAG_RE = re.compile(
    r"^(?P<name>[a-z ]+) bags contain (?P<inner_bags>.+)$", re.MULTILINE
)
INNER_BAGS_RE = re.compile(r"(?P<count>\d+) (?P<name>[a-z ]+) bags?(,|\.)")

HERE = os.path.abspath(os.path.dirname(__file__))
INPUT_FP = os.path.join(HERE, "input.txt")


with open(INPUT_FP, "r") as fp:
    INPUT_DATA = fp.read()


CONTENTS = {}

for container in CONTAINER_BAG_RE.finditer(INPUT_DATA):
    outer_name = container.group("name")
    inner_bags = container.group("inner_bags")
    CONTENTS[outer_name] = {}

    for bag in INNER_BAGS_RE.finditer(inner_bags):
        name = bag.group("name")
        count = bag.group("count")
        CONTENTS[outer_name][name] = int(count)


def unpack_bags(bag):
    """
    yields a bag name for every instance of bag contained
    """
    children = CONTENTS.get(bag, {})

    for child, count in children.items():
        for _ in range(count):
            yield child
            yield from unpack_bags(child)


def unpack_types(bag):
    """
    yields a bag name for every type of bag contained
    """
    children = CONTENTS.get(bag, {})

    for child, _ in children.items():
        yield child
        yield from unpack_types(child)


def take_until(predicate, iterable):
    """
    take from interable up to, and including, when
    the predicate is satisfied.
    """
    for item in iterable:
        yield item

        if predicate(item):
            return


def is_gold(bag):
    return bag == SHINY_GOLD


print("Part One")
all_bags = list(CONTENTS.keys())
contains_gold = []

for bag in all_bags:
    inner_bags = unpack_types(bag)
    inner_bags = take_until(is_gold, inner_bags)
    if SHINY_GOLD in set(inner_bags):
        contains_gold.append(bag)

print("count:", len(contains_gold))


print("Part Two")
print("count:", len(list(unpack_bags(SHINY_GOLD))))
