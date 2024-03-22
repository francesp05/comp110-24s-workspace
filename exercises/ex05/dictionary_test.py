"""Dictionary utility function unit tests."""

__author__ = "730672003"

import pytest
from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance
########################################################################################################################


def test_invert1() -> None:
    """Use case: Function should invert the key and the value."""
    test_a: dict[str, str] = {"home": "gnome"}
    assert invert(test_a) == {"gnome": "home"}


def test_invert2() -> None:
    """Use case: Function should invert the key and the value."""
    test_a: dict[str, str] = {"scarf": "glove", "hat": "cap"}
    assert invert(test_a) == {"glove": "scarf", "cap": "hat"}


def test_invert3() -> None:
    """Edge case: If user enters a int for key."""
    with pytest.raises(TypeError):
        test_a: dict[str, str] = {5, "dog"}
        invert(test_a)


########################################################################################################################


def test_count1() -> None:
    """Use case: Function should correctly add plants to dictionary by date."""
    test_lista: list[str] = ["vanilla", "chocolate", "mint", "chocolate", "strawberry", "mint", "vanilla", "vanilla"]
    assert count(test_lista) == {"vanilla": 3, "chocolate": 2, "mint": 2, "strawberry": 1}


def test_count2() -> None:
    """Use case: Function should correctly add plants to dictionary by date."""
    test_lista: list[str] = ["a", "a", "b"]
    assert count(test_lista) == {"a": 2, "b": 1}


def test_count3() -> None:
    """Edge case: of user inputs an empty list."""
    with pytest.raises(AssertionError):
        test_lista: list[str] = []
        assert count(test_lista)


########################################################################################################################


def test_favorite_color1() -> None:
    """Use case: Function should the color with the greatest amount of mentions."""
    test_a: dict[str, str] = {"a": "yellow", "b": "pink", "c": "pink"}
    assert favorite_color(test_a) == "pink"


def test_favorite_color2() -> None:
    """Use case: Function should the color with the greatest amount of mentions."""
    test_a: dict[str, str] = {"a": "yellow", "b": "purple"}
    assert favorite_color(test_a) == "yellow"


def test_favorite_color3() -> None:
    """Edge case: If user inputs an empty dict_kind."""
    with pytest.raises(ValueError):
        test_a: dict[str, str] = {}
        assert favorite_color(test_a)


########################################################################################################################


def test_alphabetizer1() -> None:
    """Use case: Function should return a dict with a letter at the key and list of strings as the values."""
    test_words: list[str] = ["orange", "kiwi", "apple", "avocado", "koala", "apricot"]
    assert alphabetizer(test_words) == {"o": ["orange"], "k": ["kiwi", "koala"], "a": ["apple", "avocado", "apricot"]}


def test_alphabetizer2() -> None:
    """Use case: Function should return a dict with a letter at the key and list of strings as the values."""
    test_words: list[str] = ["chemistry", "biology", "neuroscience", "biochemistry", "business"]
    assert alphabetizer(test_words) == {"c": ["chemistry"], "b": ["biology", "biochemistry", "business"], "n": ["neuroscience"]}


def test_alphabetizer3() -> None:
    """Edge case: If user enters an empty list."""
    with pytest.raises(AssertionError):
        test_words: list[str] = []
        assert alphabetizer(test_words)


########################################################################################################################


def test_update_attendance1() -> None:
    """Use case: Function should add student to the attendance if not there already."""
    test_dict: dict[str, list[str]] = {"monday": ["steve", "helen", "matthew"], "tuesday": ["kat", "john"]}
    update_attendance(test_dict, "tuesday", "bella")
    assert test_dict == {"monday": ["steve", "helen", "matthew"], "tuesday": ["kat", "john", "bella"]}


def test_update_attendance2() -> None:
    """Use case: Function should add student to the attendance if not there already."""
    test_dict: dict[str, list[str]] = {"friday": ["nate"], "monday": ["hannah", "gabriel"]}
    update_attendance(test_dict, "friday", "elena")
    assert test_dict == {"friday": ["nate", "elena"], "monday": ["hannah", "gabriel"]}


def test_update_attendance3() -> None:
    """Edge case: If user enters an empty dict."""
    with pytest.raises(TypeError):
        test_dict: dict[str, list[str]] = {}
        update_attendance(test_dict)