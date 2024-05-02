#!/usr/bin/env python3
""""This module contains the function for task 7"""


from typing import Union
def to_kv(k: str, v: Union[int, float]) -> tuple:
    return k, float(v**2)