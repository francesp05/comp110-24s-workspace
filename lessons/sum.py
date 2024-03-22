"""Summing the elements of a list using different loops."""

__author__ = "730672003"


def w_sum(vals: list[float]) -> float:
    """Return sum of list using while loop."""
    i = 0
    sum: float = 0.0
    while i < len(vals):
        sum += vals[i]
        i = i + 1
    return sum


print(w_sum([1.1, 0.9, 1.0]))


def f_sum(vals: list[float]) -> float:
    """Return sum of list using for loop."""
    sum: float = 0.0
    for x in vals:
        sum += x
    return sum
    

print(f_sum([1.1, 0.9, 1.0]))


def f_range_sum(vals: list[float]) -> float:
    """Return sum of list using for in range loop."""
    idx = 0
    sum: float = 0.0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum
    

print(f_range_sum([1.1, 0.9, 1.0]))
