import json
import re
from helper import binarySearch

from invertedIndx import InvertedIndex, StopWords, KGrams
from LinkedList import LinkedList
from helper import combineInvIndxAND

invertedInd = InvertedIndex()
stopWords = StopWords()
kGrams = KGrams()


def combineInvIndxNOT(arr1, arr2):
    """
        Function to combine the 2 inverted index list with NOT operator

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
    arr1.cursor = arr1.head
    arr2.cursor = arr2.cursor
    while arr1.cursor is not None and arr2.cursor is not None:
        if arr1.cursor.data == arr2.cursor.data:
            arr1 = arr1.cursor.next
            arr2 = arr2.cursor.next
        elif arr1.data > arr2.data:
            ans.insert(arr2.cursor.data)
            arr2 = arr2.cursor.next
        else:
            ans.insert(arr1.cursor.data)
            arr1 = arr1.cursor.next
    return ans


def invIndxCombiner(ansList):
    while len(ansList) > 1:
        ansList = invIndxSort(ansList)
        ans = combineInvIndxAND(ansList[0], ansList[1])
        del ansList[0]
        del ansList[0]
        ansList.append(ans)
    return ansList[0]


def invIndxSort(query):
    query.sort(lambda x: x.len)
    return query


def retKGrams(query):
    ans = LinkedList()
    ansList = []  # loading data
    word = "$" + query + "$"
    for i in range(len(query)):
        kGram = query[i:i + 3]
        ansList.append(kGrams[kGram])
    ansList = invIndxCombiner(ansList)


# def queryProcessing(query):
#     temp = query


def __main__():
    print('hi')
    # Process query terms and check for spelling mistakes
    # Keep track of operations between the query terms
    # Retrieve the Linked list for the query terms
    # Merge the linked lists based on query operations
    # Return the names of the docs with docId

query = input("Search: ")
if query[0]=='*' or query[-1]=='*' or len(query.split('*'))==2:
    cursor = kGrams.wildCardSearch(query).head
    while cursor!=None:
        print(cursor.data)
        cursor=cursor.next
