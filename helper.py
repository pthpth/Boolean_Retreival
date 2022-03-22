from LinkedList import LinkedList

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

    
def combineInvIndxNOT(arr1,maxInd):
    ans=LinkedList()
    cursor1=arr1.head
    i=0
    while cursor1!=None and i!=maxInd:
        if cursor1.data==i:
            cursor1=cursor1.next
            i=i+1
        elif cursor1.data>i:
            ans.insert(i)
            i=i+1
        else:
            cursor1=cursor1.next
    while i<maxInd:
        ans.insert(i)
        i=i+1
    return ans


def combineInvIndxAND(arr1, arr2):
    """
    Function to combine the 2 inverted index list with AND operator

    Paramters
    ----------
    arr1: LinkedList
    arr2: LinkedList
    Returns
    --------
    ans : LinkedList
        The resulting inverted index list
    """
    ans = LinkedList()
    cursor1 = arr1.head
    cursor2 = arr2.head
    while cursor1!=None and cursor2!=None:
        if cursor1.data == cursor2.data:
            ans.insert(cursor1.data)
            cursor1 = cursor1.next
            cursor2 = cursor2.next
        elif cursor1.data > cursor2.data:
            cursor2 = cursor2.next
        else:
            cursor1 = cursor1.next
    return ans


def combineInvIndxOR(arr1, arr2):
    """
        Function to combine the 2 inverted index list with OR operator

        Parameters
        ----------
        arr1: LinkedList
        arr2: LinkedList
        Returns
        --------
        ans : LinkedList
            The resulting inverted index list
        """
    ans = LinkedList()
    cursor1 = arr1.head
    cursor2 = arr2.head
    while cursor1!=None and cursor2!=None:
        if cursor1.data == cursor2.data:
            ans.insert(cursor1.data)
            cursor1 = cursor1.next
            cursor2 = cursor2.next
        elif cursor1.data > cursor2.data:
            ans.insert(cursor2.data)
            cursor2 = cursor2.next
        else:
            ans.insert(cursor1.data)
            cursor1 = cursor1.next
    while cursor1!=None:
        ans.insert(cursor1.data)
        cursor1=cursor1.next
    while cursor2!=None:
        ans.insert(cursor2.data)
        cursor2=cursor2.next
    return ans
