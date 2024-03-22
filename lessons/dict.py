"""practice with dictionaries"""

ice_cream: dict[str,int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

# adding
ice_cream["mint"] = 3
print("after adding mint")
print(ice_cream)

# removing
ice_cream.pop("mint")
print("after remvoing mint")
print(ice_cream)

# accessing
print(ice_cream["vanilla"])
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

# updating a value
ice_cream["vanilla"] += 1
print("after adding one vanilla")
print(ice_cream)
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

print(ice_cream["pecan"])