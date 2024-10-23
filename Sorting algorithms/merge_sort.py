# The merge sort algorithm
def merge(list_1, list_2, merged_list):
    """
    Function that merges two lists into one.
    Sorts the elements when merging from small to big.
    """
    # Three indexes initialized with 0
    i, j, k = 0, 0, 0
    # The merge and sort part
    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:
            merged_list[k] = list_1[i]
            i += 1
            k += 1
        else:
            merged_list[k] = list_2[j]
            j += 1
            k += 1
    # One of these two loops activate once we reach the end of list_1 or list_2
    while i < len(list_1):
        merged_list[k] = list_1[i]
        i += 1
        k += 1
    while j < len(list_2):
        merged_list[k] = list_2[j]
        j += 1
        k += 1
    return merged_list

def get_middle(list):
    """Help function that gets the middle of a list."""

    # Perform floor division
    middle = len(list) // 2
    return middle

def merge_sort(list):
    """The merge sort algorithm."""
    n = len(list)
    if n < 2:
        return list
    else:
        # Get the middle of the list
        middle = get_middle(list)

        # Divide the two lists into left and right
        left_list = list[:middle]
        right_list = list[middle:]

        # Recursive call on left and right of merge_sort.
        # This will divide the lists even further till we get lists of one element.
        merge_sort(left_list)
        merge_sort(right_list)

        # Once we are done dividing the lists we merge and sort them.
        merge(left_list, right_list, list)
        return list

