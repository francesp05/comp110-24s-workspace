"""Splitting a dictionary into two lists."""

__author__ = "730672003"


def get_keys(dict1: dict[str, int]) -> list[str]:
    """Return a list of the keys in a dictionary."""
    list1 = list()
    for x in dict1:
        list1.append(x)
    return list1


def get_values(dict1: dict[str, int]) -> list[int]:
    """Return a list of the values in a dictionary."""
    list1 = list()
    for x in dict1:
        list1.append(dict1[x])
    return list1