#!/usr/bin/env python3
""" defines a fucntion that returns the range of response"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """teh function that calculate the range of indexes

    Args:
        page (int): the number of the page
        page_size (int): the size of the page

    Returns:
        Tuple[int, int]: a tuple of size
        two containing a start index and an end index
        corresponding to the range of indexes
    """
    return ((page - 1) * page_size, page_size * page)
