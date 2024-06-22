#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple, Dict, Union


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """teh function that calculate the range of indexes

    Args:
        page (int): the number of the page
        page_size (int): the size of the page

    Returns:
        Tuple[int, int]: a tuple of size two containing
          a start index and an end index
          corresponding to the range of indexes
    """
    return ((page - 1) * page_size, page_size * page)


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
        """get's specific pages from csb files

        Args:
            page (int, optional): page number. Defaults to 1.
            page_size (int, optional): page size. Defaults to 10.

        Returns:
            List[List]:  list of lists from the csv file
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        self.dataset()
        if self.__dataset:
            return self.__dataset[start_index: end_index]
        return []

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str, Union[int, List]]:
        """generate a HATEOAS like structure

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            Dict[str, Union[int, List]] a simple hyermedia response
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # data = self.get_page
        # next_page = page + 1 or None
        # prev_page = page - 1 or None
        # total_pages = len(self.__dataset)/page_size
        self.dataset()
        data = self.get_page(page, page_size)
        total_pages = round(len(self.__dataset)/page_size)
        next_page = page + 1 if page < total_pages else None,
        prev_page = page - 1 if page > 1 else None,
        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages}
