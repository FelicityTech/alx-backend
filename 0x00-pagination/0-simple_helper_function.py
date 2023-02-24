#!/usr/bin/env python3
"""
This file contains the index_range function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple:
    """This functions return a tuple of size two containing a 
    start index and an end index corresponding to range of 
    index to return in a list for those particular pagination parameters
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    
    return(start_index, end_index)