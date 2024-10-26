pets: list[str] = ["Louie", "Bo", "Bear"]
# Tell every pet they're a good boy!
for a in pets:
    # a is the element whereas pets is the whole list from which the element is derived from.
    print(f"Good boy, {a}!")

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
    # has to be length of names because 2nd argument will not be be included in the range.
    print(f"{idx}: {names[idx]}")
# always use idx for index.
