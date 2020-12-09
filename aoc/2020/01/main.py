import os

here = os.path.abspath(os.path.dirname(__file__))
input_fp = os.path.join(here, "input.txt")

with open(input_fp, "r") as fp:
    expenses = {float(line) for line in fp.readlines()}


for first in expenses:
    second = 2020 - first
    if second in expenses:
        print(f"Answer {first} * {second} = {first * second}")
        break
else:
    print("None found")


for first in expenses:
    for second in expenses:
        third = 2020 - first - second
        if third in expenses:
            print(f"Answer {first} * {second} * {third} = {first * second * third}")
            break
else:
    print("None found")
