import os

HERE = os.path.abspath(os.path.dirname(__file__))
INPUT_FP = os.path.join(HERE, "input.txt")

with open(INPUT_FP, "r") as fp:
    INSTRUCTIONS = [
        line.split(" ")
        for line in fp.readlines()
    ]


def run(instructions):
    accumulator = 0
    current_pos = 0
    visited = set()

    while current_pos not in visited:
        end_of_program = current_pos == len(instructions)

        if end_of_program:
            return accumulator

        op, value = instructions[current_pos]
        visited.add(current_pos)

        if op == "acc":
            accumulator += eval(value)
            current_pos += 1
        elif op == "jmp":
            current_pos += eval(value)
        elif op == "nop":
            current_pos += 1
        else:
            raise NotImplementedError("unknown op", op)
    else:
        raise RecursionError(accumulator)


print("Part One")
try:
    _ = run(INSTRUCTIONS)
except RecursionError as e:
    print("accumulator:", e.args[0])


print("Part Two")
swaps = {
    "nop": "jmp",
    "jmp": "nop",
}
candidates_positions = (
    number for number, (instr, _) in enumerate(INSTRUCTIONS) if instr in swaps
)
for position in candidates_positions:
    instr, value = INSTRUCTIONS[position]
    permutation = list(INSTRUCTIONS)
    permutation[position] = (swaps[instr], value)

    try:
        accumulator = run(permutation)
    except RecursionError:
        pass
    else:
        print("accumulator:", accumulator)
        break
else:
    print("No solution found")
