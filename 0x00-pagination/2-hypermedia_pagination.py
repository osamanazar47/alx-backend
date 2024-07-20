#!/usr/bin/env python3
"""Module for task 2"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Takes two integer arguments page with
        default value 1 and page_size with default value 10."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns a dictionary containing the pagination
        key-value pairs"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        data = self.dataset()
        total_items = len(data)
        total_pages = (total_items + page_size - 1) // page_size
        start, end = index_range(page, page_size)
        page_data = data[start:end]
        h_dict = {'page_size': len(page_data), 'page': page}
        h_dict['data'] = page_data
        h_dict['next_page'] = page + 1 if page < total_pages else None
        h_dict['prev_page'] = page - 1 if page > 1 else None
        h_dict['total_pages'] = total_pages
        return h_dict


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing start and end indexes"""
    start = int((page - 1) * page_size)
    end = int(start + page_size)
    t = (start, end)
    return t
