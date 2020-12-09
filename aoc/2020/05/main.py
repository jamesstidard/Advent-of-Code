import os


HERE = os.path.abspath(os.path.dirname(__file__))
INPUT_FP = os.path.join(HERE, "input.txt")

with open(INPUT_FP, "r") as fp:
    INPUT_DATA = [line.strip() for line in fp.readlines()]

ROWS = 128
COLUMNS = 8


def one(iterable):
    """Unwraps and asserts single element iterable, else raises"""
    [thing] = list(iterable)
    return thing


def bisect(lower, upper):
    delta = upper - lower
    mid = lower + (delta // 2)
    return (lower, mid), (mid, upper)


def seat_position(binary_space_partition):
    row_range = (0, ROWS)
    column_range = (0, COLUMNS)

    for char in binary_space_partition[:7]:
        if char == "B":
            _, row_range = bisect(*row_range)
        elif char == "F":
            row_range, _ = bisect(*row_range)
        else:
            raise NotImplementedError(char)

    for char in binary_space_partition[7:]:
        if char == "L":
            column_range, _ = bisect(*column_range)
        elif char == "R":
            _, column_range = bisect(*column_range)
        else:
            raise NotImplementedError(char)

    row = one(range(*row_range))
    column = one(range(*column_range))

    return row, column


def seat_id(binary_space_partition):
    row, column = seat_position(binary_space_partition)
    return row * 8 + column


print("Part One")
print("Highest Seat ID:", max(seat_id(bsp) for bsp in INPUT_DATA))


print("Part Two")
taken_seats = [seat_id(bsp) for bsp in INPUT_DATA]
first_seat = min(taken_seats)
last_seat = max(taken_seats)
all_seats = range(first_seat, last_seat+1)
availabile_seats = set(all_seats) - set(taken_seats)
print("Available Seat", one(availabile_seats))
