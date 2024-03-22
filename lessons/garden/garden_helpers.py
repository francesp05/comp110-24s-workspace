"""Some functions for my garden plan!"""

__author__ = "730672003"

# # Want to get: {"flower": ["marigold", "zinnia", "daisy"], "vegetable": ["carrots"]}
# by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
# # print(by_kind["flower"])                              ##print flower list
# # print(by_kind["flower"][1])                           ##print zinnia at index 1

# new_plant: str = "elderberry"
# new_plant_kind: str = "fruit"

# # if the kind is alr in dict ("flower" was in by_kind, so I did this)
# by_kind[new_plant_kind].append(new_plant)   #dict at new-plant-kind, add new-plant

# # if the kind is not in the dict (eg. "fruit" is not in by_kind)
# by_kind[new_plant_kind] = []    #create key value in dict as a list
# by_kind[new_plant_kind].append(new_plant)   #append new-plant to list(key)

# # if statment to account for if kind is in the dict or not already --- combining the above
# if new_plant_kind in by_kind:
#     by_kind[new_plant_kind].append(new_plant)
# else:
#     by_kind[new_plant_kind] = []
#     by_kind[new_plant_kind].append(new_plant)

# put into function format


def add_by_kind(dict1: dict[str, list[str]], kind: str, plant: str) -> None:
    """Add plant to dictionary by type."""
    if kind in dict1:
        dict1[kind].append(plant)
    else:
        dict1[kind] = []
        dict1[kind].append(plant)


by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}


def add_by_date(dict1: dict[str, list[str]], month: str, plant: str) -> None:
    """Add plant under date to sow seeds."""
    if month in dict1:
        dict1[month].append(plant)
    else:
        dict1[month] = []
        dict1[month].append(plant)


def lookup_by_kind_and_date(dict_kind: dict[str, list[str]], dict_month: dict[str, list[str]], kind: str, month: str) -> str:
    """Lookup plants to plant by kind and month to plant. Return str with list."""
    assert kind in dict_kind
    assert month in dict_month

    kinds_list: list[str] = dict_kind[kind]     # get a list of all plants of specific kind input

    month_list: list[str] = dict_month[month]           # get a list of all plants planted in a specific month

    # go through both list and find elements that appear in both

    # kind_list = ["marigold", "daisy"]       # month_list = ["daisy", "rose"]

    combined_list: list[str] = []
    for plant in kinds_list:
        for other_plant in month_list:
            if plant == other_plant:
                combined_list.append(other_plant)
# "<kind>s to plant in <month>: <combined_list>"
    if len(combined_list) > 0:
        f"{kind}s to plant in {month}: {combined_list}"
    else:
        return f"No {kind}s to plant in {month}."