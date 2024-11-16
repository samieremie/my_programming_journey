# The insertion sort algorithm
def my_swap(x, y, list):
    """Hulp function that swaps two elements in a list"""
    list[x], list[y] = list[y], list[x]
    
def insertion_sort(list):
    """Function that implements insertion sort"""
    for i in range(0, len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j - 1]:
                my_swap(j, j - 1, list)
            else:
                break
    return list



