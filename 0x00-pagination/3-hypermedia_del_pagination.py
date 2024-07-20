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
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset


    def get_hyper_index(self, index: int = None, page_size: int = 10) -> dict:
        """
        Returns a dictionary with these keys index,
        next_index, page_size and data
        """
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.dataset()
        total_items = len(dataset)
        if index is None:
            index = 0
        if index >= total_items:
            return {
                'index': index,
                'next_index': None,
                'page_size': 0,
                'data': []
            }
        end_index = min(index + page_size, total_items)
        page_data = dataset[index:end_index]
        next_index = end_index if end_index < total_items else None
        h_dict = {
            'index': index,
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data
        }

        return h_dict


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing start and end indexes"""
    start = int((page - 1) * page_size)
    end = int(start + page_size)
    t = (start, end)
    return t