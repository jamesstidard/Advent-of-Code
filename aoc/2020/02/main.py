import os
import re
import typing


class Entry(typing.NamedTuple):
    left: int
    right: int
    char: str
    password: str


HERE = os.path.abspath(os.path.dirname(__file__))
INPUT_FP = os.path.join(HERE, "input.txt")
ENTRY_RE = re.compile(
    r"^(?P<left>\d\d*)-(?P<right>\d\d*) (?P<char>[a-z]): (?P<password>[a-z]+)$",
    re.MULTILINE,
)

with open(INPUT_FP, "r") as fp:
    INPUT_DATA = fp.read()

ENTRIES = [
    Entry(
        left=int(line.group("left")),
        right=int(line.group("right")),
        char=line.group("char"),
        password=line.group("password")
    )
    for line in ENTRY_RE.finditer(INPUT_DATA)
]


def safe_index(arr, index: int, default=None):
    try:
        return arr[index]
    except IndexError:
        return default


def xor(a, b):
    return bool(a) != bool(b)


print("Part One")

valid_passwords = []
for entry in ENTRIES:
    count = len([c for c in entry.password if c == entry.char])

    if entry.left <= count <= entry.right:
        valid_passwords.append(entry.password)

print(f"valid passwords: {len(valid_passwords)}")


print("Part Two")

valid_passwords = []
for entry in ENTRIES:
    char1 = safe_index(entry.password, entry.left-1)
    char2 = safe_index(entry.password, entry.right-1)

    if xor(char1 == entry.char, char2 == entry.char):
        valid_passwords.append(entry.password)

print(f"valid passwords: {len(valid_passwords)}")
