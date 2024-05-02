#!/usr/bin/env python3
"""This module contains a function that takes a float and returns a function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This function takes a float and returns a function that multiplies a float by multiplier"""
    def multiplier_func(n: float) -> float:
        return n * multiplier
    return multiplier_func
