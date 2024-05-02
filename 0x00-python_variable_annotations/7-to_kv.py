#!/usr/bin/env python3
""""This module contains the function for task 7"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This function takes a string k and an int or float v and returns a tuple
    """
    return (k, float(v**2))
