"""Lists."""

__author__ = "730672003"


def all(list_a: list[int], b: int) -> bool:
    """Determine if all values in a list(a) are the same as a given int(b)."""
    i = 0
    same = True
    if list_a == []:
        same = False
    else:
        while same and i < len(list_a):
            if list_a[i] == b:
                same = True
            elif list_a[i] != b:
                same = False
                break
            else:
                same = False
                break
            i += 1
    return same


def max(input: list[int]) -> int:
    """Determine max number in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_num = input[0]
    for x in input:
        if x > max_num:
            max_num = x
    return max_num


def is_equal(list_a: list[int], list_b: list[int]) -> bool:
    """Determine if list is the exact same as another list."""
    i = 0
    same = True
    if len(list_a) != len(list_b):
        same = False
    else:
        for x in list_a:
            if len(list_a) != len(list_b):
                same = False
            elif x == list_b[i]:
                same = True
                i += 1
            elif x != list_b[i]:
                same = False
                break
            else:
                same = False
                break
    return same


def extend(list_a: list[int], list_b: list[int]) -> None:
    """Add a list to another list."""
    i = 0
    while i < len(list_b):
        list_a.append(list_b[i])
        i += 1