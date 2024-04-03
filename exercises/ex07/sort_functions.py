"""Functions that implement sorting algorithms."""

__author__ = ""

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    a = len(x)
    for b in range (1, a):
        sort = x[b]
        c = b - 1
        while c >= 0 and x[c] > sort:
            x[c + 1] = x[c]
            c -= 1
        x[c + 1] = sort
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    a = len(x)
    for b in range (a - 1):
        min_idx = b
        for d in range (b + 1, a):
            if x[d] < x[min_idx]:
                min_idx = d
        x[b], x[min_idx] = x[min_idx], x[b]
    return None
    