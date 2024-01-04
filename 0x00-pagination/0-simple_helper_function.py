#!/usr/bin/env python3
"""
The following module defines a function called 'index_range'.
This function calculates the range of indices that need to be considered
for a specific page when paginating data.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the range of indices for a specific page when paginating data.

    Parameters:
        page (int): The current page number.
        page_size (int): The number of items displayed per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices for
        the given page.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
