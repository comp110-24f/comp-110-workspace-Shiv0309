"""CQ04: Importing functions from different files."""

__author__ = "730767271"


def get_coords(xs: str, ys: str) -> None:
    index1: int = 0
    while index1 < len(xs):
        index2: int = 0
        while index2 < len(ys):
            print("(" + str(xs[index1]) + "," + str(ys[index2]) + ")")
            index2 += 1
        index1 += 1


get_coords("12", "34")
