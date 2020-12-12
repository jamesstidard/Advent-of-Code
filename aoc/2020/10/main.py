import os


HERE = os.path.abspath(os.path.dirname(__file__))
INPUT_FP = os.path.join(HERE, "input.txt")

with open(INPUT_FP, "r") as fp:
    ALL_ADAPTERS_RATINGS = [int(line) for line in fp.readlines()]

OUTLET_RATING = 0
DEVICE_ADAPTER_RATING = max(ALL_ADAPTERS_RATINGS) + 3
LOWER_TOLERANCE = 3
UPPER_TOLERANCE = 0


def traverse(*, current_rating, remaining_adapters):
    if len(remaining_adapters) == 0:
        return

    all_candidates = {
        rating for rating in remaining_adapters
        if rating-LOWER_TOLERANCE <= current_rating <= rating+UPPER_TOLERANCE
    }

    if len(all_candidates) == 0:
        raise ValueError("Unable to solve")

    next_adapter = min(all_candidates)
    joltage_step = next_adapter - current_rating

    yield joltage_step

    next_remaining_adapters = list(remaining_adapters)
    next_remaining_adapters.remove(next_adapter)

    yield from traverse(
        current_rating=next_adapter,
        remaining_adapters=next_remaining_adapters
    )


print("Part One")
route = list(
    traverse(
        current_rating=OUTLET_RATING,
        remaining_adapters=ALL_ADAPTERS_RATINGS + [DEVICE_ADAPTER_RATING],
    )
)
one_steps = len([step for step in route if step == 1])
three_steps = len([step for step in route if step == 3])
print(f"{one_steps} * {three_steps} = {one_steps*three_steps}")
