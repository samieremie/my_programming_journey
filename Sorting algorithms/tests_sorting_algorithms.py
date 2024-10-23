# This file is purely for testing the sorting algorithms

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort

test_list = [3, 5, 26, 10, 2, 1, 483, 24, 46, 273, 38, 238, 584, 4, 381]
test_list_2 = [1, 2, 4, 5, 6, 8, 9, 9]

# Tests bubble sort
print(f"This is the result of the bubble sort with a sorted list {bubble_sort(test_list_2)}")
print(f"This is the result of the bubble sort with an unsorted list {bubble_sort(test_list)}")

# Tests insertion sort
print(f"This is the result of insertion sort with an unsorted list {insertion_sort(test_list)}")
print(f"This is the result of insertion sort with a sorted list {insertion_sort(test_list_2)}")

# Tests merge sort
print(f"This is the result of merge sort with an unsorted list {merge_sort(test_list)}")
print(f"This is the result of merge sort with a sorted list {merge_sort(test_list_2)}")
