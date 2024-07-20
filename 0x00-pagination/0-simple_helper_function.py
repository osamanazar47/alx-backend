#!/usr/bin/env python3
"""Module for task 0"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing start and end indexes"""
    start = int((page - 1) * page_size)
    end = int(start + page_size)
    t = (start, end)
    return t
