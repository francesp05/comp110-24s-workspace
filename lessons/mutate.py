"""Mutating functions."""

__author__ = "730672003"


a: list[int] = [1, 2, 3]


def manual_append(a: list[int], b: int) -> None:
    """Manually append."""
    a.append(b)


manual_append(a, 2)
print(a)


def double(a: list[int]) -> None:
    """Double numbers in list."""
    i = 0
    while i < len(a):
        a[i] *= 2
        i += 1


double(a)
print(a)