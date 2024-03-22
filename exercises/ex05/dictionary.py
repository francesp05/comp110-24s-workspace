"""Dictionary utility functions."""

__author__ = "730672003"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of given dictionary."""
    b: dict[str, str] = {}
    for x in a:
        b[a[x]] = x
        if a[x] == x:
            raise KeyError("Error! Multiple keys.")
    return b

        
def favorite_color(a: dict[str, str]) -> str:
    """Find the favorite (most frequent) color from a dict."""
    color_count: dict[str, int] = {}
    for name, color in a.items():
        color_count[color] = color_count.get(color, 0) + 1
    fav = max(color_count, key=color_count.get)
    favcolor: str = fav
    return favcolor


def count(list_a: list[str]) -> dict[str, int]:
    """Add items in a list to a dict as keys and number that the item appears as the value."""
    dict1: dict[str, int] = {}
    for x in list_a:
        if x in dict1:
            dict1[x] += 1
        else:
            dict1[x] = 1
    return dict1


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Create a dictionary with letters as the keys and words starting with that letter as the values."""
    categorized = {}
    for word in words:
        letter = word[0]
        if letter not in categorized:
            categorized[letter] = [word]
        else:
            categorized[letter].append(word)
    return categorized


def update_attendance(dict1: dict[str, list[str]], day: str, student: str) -> None:
    """Create and attendance log from the day a student attended."""
    if day not in dict1:
        dict1[day] = []
    dict1[day].append(student)