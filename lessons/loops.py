def characters(msg: str) -> None:
    index: int = 0
    while index < len(msg):
        print(msg[index])
        index = (
            index + 1
        )  # If this line was not included, it would be an infinte loop. So, always make sure there is a way that the conditions is eveutally False so that we can exit the loop.


characters(msg="Howdy")
