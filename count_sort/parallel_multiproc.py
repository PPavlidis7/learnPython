import multiprocessing as mp
import time

import count_sort.number_generator as numbers_generator
from count_sort.serial import CountSortSequential


''' Try with multiprocess'''
class CountSortParallel(CountSortSequential):
    def __init__(self, size_of_numbers):
        super().__init__(size_of_numbers)
        self.size_of_numbers = size_of_numbers
        self.total_process = 11
