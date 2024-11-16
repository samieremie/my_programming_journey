# This file is purely for testing the sorting algorithms

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from counting_sort import counting_sort, counting_sort_negative

test_list = [3, 5, 26, 10, 2, 1, 483, 24, 46, 273, 38, 238, 584, 4, 381]
test_list_2 = [5, 26, 10, 2, 1, -483, 24, 46, 273, 38, 238, 584, 4, -62, -2, -1, 0, 234]

# These are basic tests meant to test the basic functionality only. 
# They are not testing all capabilities and possible issues of the algorithms.

# Tests bubble sort
print(f"This is the result of the bubble sort with a positive list {bubble_sort(test_list[:])}")
print(f"This is the result of the bubble sort with a negative numbers list {bubble_sort(test_list_2[:])}\n")

# Tests insertion sort
print(f"This is the result of insertion sort with a positive list {insertion_sort(test_list[:])}")
print(f"This is the result of insertion sort with a negative numbers list {insertion_sort(test_list_2[:])}\n")

# Tests merge sort
print(f"This is the result of merge sort with a positive list {merge_sort(test_list[:])}")
print(f"This is the result of merge sort with a negative numbers list {merge_sort(test_list_2[:])}\n")

# Tests quick sort
print(f"This is the result of quick sort with a positive list {quick_sort(test_list[:])}")
print(f"This is the result of quick sort with a negative numbers list {quick_sort(test_list_2[:])}\n")

# Tests counting sort
print(f"This is the result of counting sort with a positive list {counting_sort(test_list[:])}")

# Tests counting sort negative
print(f"This is the result of counting sort negative with a positive list {counting_sort_negative(test_list[:])}")
print(f"This is the result of counting sort with a negative numbers list {counting_sort_negative(test_list_2[:])}\n")