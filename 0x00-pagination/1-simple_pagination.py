#!/usr/bin/env python3
"""This file contains the Server class"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> tuple:
    """This functions return a tuple of size two containing a 
    start index and an end index corresponding to range of 
    index to return in a list for those particular pagination parameters
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    
    return(start_index, end_index)

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
            """This function uses index_range to find the correct indexes 
            to paginate the dataset correctly and return the appropriate page of
            the dataset
            """
            assert isinstance(page, int) and page  > 0 and\
                isinstance(page_size, int) and page_size > 0
            data = self.dataset()
            page_data = index_range(page, page_size)
            return data[page_data[0]:page_data[1]]