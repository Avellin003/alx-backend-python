#!/usr/bin/env python3
"""This function in takes a list of int and floats and returns float"""

from typing import List, Union
def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns a float
    """
    return sum(mxd_lst)
