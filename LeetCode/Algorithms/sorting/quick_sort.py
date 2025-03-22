from random import randrange, shuffle
from typing import List

def quicksort(start: int, end: int, list: List[int]) -> None:
    if start >= end:
        return
    
    pivot_idx = randrange(start, end)
    list[end], list[pivot_idx] = list[pivot_idx], list[end]
    
    less_than_pointer = start
    
    for i in range(start, end):
        if list[i] < list[end]:
            list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
            less_than_pointer += 1
    
    list[end], list[less_than_pointer] = list[less_than_pointer], list[end]

    quicksort(start, less_than_pointer - 1, list)
    quicksort(less_than_pointer + 1, end, list)

# Test the quicksort function
list = [5, 3, 1, 7, 4, 6, 2, 8]
shuffle(list)
print("PRE SORT: ", list)
quicksort(0, len(list) - 1, list)
print("POST SORT: ", list)
