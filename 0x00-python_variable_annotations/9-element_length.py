#!/usr/bin/env python3
"""
Mmodule contains annonated function's parameters and return values with a
 appropriate types
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples with length of each element in the list"""
    return [(i, len(i)) for i in lst]
