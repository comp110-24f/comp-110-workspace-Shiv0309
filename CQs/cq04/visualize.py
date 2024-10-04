"""CQ04: Importing functions from different files."""

__author__ = "730767271"


from CQs.cq04.concatenation import concat

if __name__ == "__main__":
    x: str = "123"
    y: str = "abc"
    print(concat(x, y))

from CQs.cq04.coordinates import get_coords

get_coords(x, y)
