#!/usr/bin/python3
# calculate the peak in the array

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using binary search.

    :param list_of_integers: List of unsorted integers.
    :return: A peak in the list.
    """
    low, high = 0, len(list_of_integers) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if mid is a peak
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]

        # If the element to the left is greater, search in the left subarray
        elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            high = mid - 1

        # If the element to the right is greater, search in the right subarray
        else:
            low = mid + 1

    # This should not be reached if the list is not empty
    return None
