# This is the quick sort algorithm

def quick_sort(list):
    """Function that implements the quick sort"""
    if len(list) <= 1:
        return list
    else:
        pivot = list[-1]
        left = []
        right = []
        for i in range(0, len(list) - 1):
            if list[i] > pivot:
                right.append(list[i])
            else:
                left.append(list[i])
                
        left = quick_sort(left)
        right = quick_sort(right)
        return left + [pivot] + right
