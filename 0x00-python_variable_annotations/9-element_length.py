#!/usr/bin/env python3
'''task_9
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Measures the length of a list of sequences.
    '''
    return [(i, len(i)) for i in lst]
