def binarySearch(arr, query):
    """
    Implementation of binary search to find the query
    Parameters
    ----------
    arr : list
        the list in which the query has to be found
    query : string
        the word which is to be found
    Returns
    ---------
    index: index of query in arr
            -1 if not found
    """
    low = 0
    high = len(arr) - 1
    mid = 0
    while high >= low:
        mid = int((high + low) / 2)
        if query == arr[mid]:
            return mid
        else:
            if query > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


print(binarySearch([1, 2, 3, 4, 5, 6, 7], 7))
