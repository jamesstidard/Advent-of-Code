import os
import re

POLICY_ONE_RE = re.compile(
    r"^(?P<min>\d\d*)-(?P<max>\d\d*) (?P<char>[a-z]): (?P<password>[a-z]+)$",
    re.MULTILINE,
)

POLICY_TWO_RE = re.compile(
    r"^(?P<first_position>\d\d*)-(?P<second_position>\d\d*) (?P<char>[a-z]): (?P<password>[a-z]+)$",
    re.MULTILINE,
)

here = os.path.abspath(os.path.dirname(__file__))
input_fp = os.path.join(here, "input.txt")

with open(input_fp, "r") as fp:
    CORRUPTED_PASSWORDS = fp.read()


valid_passwords = []
for line in POLICY_ONE_RE.finditer(CORRUPTED_PASSWORDS):
    min_ = int(line.group("min"))
    max_ = int(line.group("max"))
    char = line.group("char")
    pswd = line.group("password")

    count = len([c for c in pswd if c == char])

    if min_ <= count <= max_:
        valid_passwords.append(pswd)

print(f"policy 1 valid passwords found: {len(valid_passwords)}")


def safe_index(arr, index: int, default=None):
    try:
        return arr[index]
    except IndexError:
        return default


valid_passwords = []
for line in POLICY_TWO_RE.finditer(CORRUPTED_PASSWORDS):
    pos1 = int(line.group("first_position"))
    pos2 = int(line.group("second_position"))
    char = line.group("char")
    pswd = line.group("password")

    char1 = safe_index(pswd, pos1 - 1)
    char2 = safe_index(pswd, pos2 - 1)

    if (char1 == char) != (char2 == char):
        valid_passwords.append(pswd)

print(f"policy 2 valid passwords found: {len(valid_passwords)}")
