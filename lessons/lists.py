"""basic list syntax"""

# initialize an empty list
grocery_list: list[str] = list() #<-- LIST CONSTRUCTOR
grocery_list: list[str] = [] #<-- literal

# add item to a list
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")

print("After appending: ")
print(grocery_list)

# create an already populated list
grocery_list2: list[str] = ["bananas","milk","bread"]
print("Populated list: ")
print(grocery_list2)

grocery_list2.append("eggs")
print(grocery_list2)

# indexing
print("First element of list")
print(grocery_list[0])

grocery_list[1] = "almond milk"
print("After change print grocery list")
print(grocery_list)

# you can have duplicates
grocery_list.append("bananas")
print(grocery_list)

# measuring length
print("Length of list: ")
print(len(grocery_list))

# removing and item
grocery_list.pop(1)
print("after removing almond milk:")
print(grocery_list)

# function name: display
# parameter: list[str]
# return nothing
# print the list

# def display(stuff: list[str] ) -> None:
#     print(stuff)

# display(grocery_list)

def create(stuff: str, stuff2: str) -> list[str]:
    stuff1: list[str] = [stuff,stuff2]
    return stuff1

print(create("deez","nutz"))
