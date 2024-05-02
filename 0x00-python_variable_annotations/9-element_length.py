#!/usr/bin/env python3
from typing import Iterable, List, Sequence, Tuple
"""this function takes a list of sequences and returns a
list of tuples"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuples
    """
    return [(i, len(i)) for i in lst]
