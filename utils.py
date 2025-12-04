from typing import Generic, Iterable, TypeVar


DELTA_4 = [(0, -1), (0, 1), (-1, 0), (1, 0)]

DELTA_8 = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


_T = TypeVar("_T")


def enumerate_grid(grid: Iterable[Iterable[_T]]):
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            yield (i, j, val)
