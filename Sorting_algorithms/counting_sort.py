# This is the counting sort algorithm

def counting_sort(list):
    """Simple sorting algorithm of linear time complexity.
    DISCLAIMER: To be used only when the max_value is quite small."""

    max_value = max(list)
    counts = []
    for i in range(0, max_value + 1):
        counts.append(0)
    
    for element in list:
        counts[element] += 1

    j = 0
    for i in range(0, len(counts)):
        while counts[i] != 0:
            list[j] = i
            j += 1
            counts[i] -= 1

    return list

# Version that receives negative input as well
def counting_sort_negative(list):
    """Version of counting sort that receives negative input as well."""
    min_value = min(list)
    max_value = max(list)
    range_of_values = max_value - min_value
    counts = []

    for i in range(0, range_of_values + 1):
        counts.append(0)

    for element in list:
        # Shift negative numbers to the right. The lowest number = 0 and so on.
        counts[element - min_value] += 1
    
    j = 0
    for i in range(0, len(counts)):
        while counts[i] != 0:
            # This will put the original not shifted value back into the list.
            list[j] = i + min_value
            j += 1
            counts[i] -= 1

    return list
