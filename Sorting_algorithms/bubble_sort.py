# The bubble sort algorithm
def my_swap(x, y, list):
    """Hulp function that swaps two elements in a list"""
    list[x], list[y] = list[y], list[x]

def bubble_sort(list):
    """Function that implements the bubble sort algorithm."""
    for unsorted_idx in range(len(list), 0, -1):
        swap_this_inner_loop = False
        for inner_idx in range(1, unsorted_idx):
            if list[inner_idx - 1] > list[inner_idx]:
                my_swap(inner_idx - 1, inner_idx, list)
                swap_this_inner_loop = True
        if swap_this_inner_loop == False:
            return list
    return list