#!/usr/bin/env python3
"""Pagination helper fun.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """to retreive index range from a given page
    """

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
