import os
from os.path import split


HERE = os.path.abspath(os.path.dirname(__file__))
INPUT_FP = os.path.join(HERE, "input.txt")

GROUP_DELIMITER = "\n\n"
LINE_DELIMITER = "\n"
LINE_ITEM_DELIMITER = " "

with open(INPUT_FP, "r") as fp:
    INPUT_DATA = fp.read().strip()

GROUPS = INPUT_DATA.split(GROUP_DELIMITER)
ITEMS = [
    [itm for lns in group.split(LINE_DELIMITER) for itm in lns.split(LINE_ITEM_DELIMITER)]
    for group in GROUPS
]

print(ITEMS)

group_items = []

for group in INPUT_DATA.split(GROUP_DELIMITER):
    group = group.replace(LINE_DELIMITER, LINE_ITEM_DELIMITER)
    items = group.split(LINE_ITEM_DELIMITER)

    group_items.append(items)

print(group_items)
