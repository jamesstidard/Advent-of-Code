import os

here = os.path.abspath(os.path.dirname(__file__))
input_fp = os.path.join(here, "input.txt")

with open(input_fp, "r") as fp:
    instructions = fp.readlines()


accumulator = 0
current = 0
visited = set()

while True:
    if current in visited:
        break
    else:
        visited.add(current)

    try:
        op, value = instructions[current].split(" ")
    except IndexError:
        break

    if op == "acc":
        accumulator += eval(value)
        current += 1
    elif op == "jmp":
        current += eval(value)
    elif op == "nop":
        current += 1
    else:
        raise NotImplementedError("unknown op", op)

print(accumulator)
