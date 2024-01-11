#!/usr/bin/env python3
"""A type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by a number """

    def multiplier_function(number: float) -> float:
        """Function that return a number(float) by a multiplier"""
        return number * multiplier

    return multiplier_function
