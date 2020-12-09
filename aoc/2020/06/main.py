import os


HERE = os.path.abspath(os.path.dirname(__file__))
INPUT_FP = os.path.join(HERE, "input.txt")


def all_groups_answers():
    with open(INPUT_FP, "r") as fp:
        group = []

        for line in fp.readlines():
            line = line.strip()
            is_answer = bool(line)

            if is_answer:
                group.append(line)
            elif not is_answer and len(group) > 0:
                yield group
                group = []
        else:
            # yield final group when
            # not followed by empty line
            if len(group) > 0:
                yield group


print("Part One")
counts = []

for group_answers in all_groups_answers():
    union = set()

    for answer in group_answers:
        union |= set(answer)

    counts.append(len(union))

print("Sum:", sum(counts))


print("Part Two")
counts = []

for group_answers in all_groups_answers():
    first_answer, *other_answers = group_answers
    common = set(first_answer)

    for answer in other_answers:
        common &= set(answer)

    counts.append(len(common))

print("Sum:", sum(counts))
