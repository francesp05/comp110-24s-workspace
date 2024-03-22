"""Test my garden functions."""

__author__ = "730672003"

from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date


def test_add_by_kind1() -> None:
    """Use case: Function should correctly add plants to dictionary by kind."""
    test_dict: dict[str, list[str]] = {"herb": ["mint", "basil"]}
    test_kind: str = "herb"
    test_plant: list[str] = ["mint", "basil"]
    assert add_by_kind(test_dict, test_kind, test_plant) == {"herb": ["mint", "basil"]}


def test_add_by_kind2() -> None:
    """Edge case: If user enters an int instead of a str."""
    test: dict[int, list[str]] = {10: ["mint"]}
    test_kind: int = 10
    test_plant: list[str] = ["mint"]
    assert add_by_kind(test, test_kind, test_plant) == KeyError("Input flower type, not a number!")


def test_add_by_date1() -> None:
    """Use case: Function should correctly add plants to dictionary by date."""
    test: dict[str, list[str]] = {"april": ["mint", "basil", "oregano"]}
    test_month: str = "april"
    test_plant: list[str] = ["mint", "basil"]
    assert add_by_date(test, test_month, test_plant) == {"april": ["mint", "basil", "oregano"]}


def test_add_by_date2() -> None:
    """Edge case: of user inputs a list[int]."""
    test: dict[str, list[int]] = {"april": [1, 4, 12]}
    test_month: str = "april"
    test_plant: list[int] = [1, 4, 12]
    assert add_by_date(test, test_month, test_plant) == ValueError("Input plants to plant in month, not numbers!")


def test_lookup_by_kind_and_date1() -> None:
    """Use case: Function should return a str of a list of plants to plant in a certain month."""
    test_kinddict: dict[str, list[str]] = {"flower": ["marigold", "daisy", "daffodil"], "herb": ["mint", "basil", "oregano"]}
    test_datedict: dict[str, list[str]] = {"april": ["marigold", "mint"], "july": ["basil", "daisy"]}
    test_kind: str = "herb"
    test_month: str = "july"
    assert lookup_by_kind_and_date(test_kinddict, test_datedict, test_kind, test_month) == "Herbs to plant in July: ['basil']"


def test_lookup_by_kind_and_date2() -> None:
    """Edge case: If user inputs an empty dict_kind."""
    test_kinddict: dict[str, list[str]] = {}
    test_datedict: dict[str, list[str]] = {"april": ["marigold", "mint"], "july": ["basil", "daisy"]}
    test_kind: str = "herb"
    test_month: str = "july"
    assert lookup_by_kind_and_date(test_kinddict, test_datedict, test_kind, test_month) == "Error! User must input a populated dict."