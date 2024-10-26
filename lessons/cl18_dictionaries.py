"""Examples of dictionary syntax with Ice cream Shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}


# len evalutaes to the number of entries
print(len(ice_cream))  # Prints 3

# add key value entry by directly assinging to a key
ice_cream["mint"] = 3

# access entries by their key
print(ice_cream["chocolate"])  # prints 12

# test if "pbj" is a key in ice_cream
has_pbj: bool = "pbj" in ice_cream  # in is a built in function in python

# to remove, we use the pop method and give a key
ice_cream.pop(
    "strawberry"
)  # if you were to print this, it would return 4 (the value associated with "strawberry")

# to iterate over every key in a loop, use for in
for flavor in ice_cream:  # flavor can be replaced with any other name, it is arbitrary
    tally: int = ice_cream[flavor]
    print(f"{flavor} has {tally} order")
