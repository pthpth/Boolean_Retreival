import json
from helper import binarySearch
from nltk.stem import PorterStemmer
from invertedIndx import InvertedIndex, StopWords, KGrams
from LinkedList import LinkedList

invertedInd = InvertedIndex()
stopWords = StopWords()
kGrams = KGrams()


def stemmer(query):
    """
    Parameters
    ---------
    query: string
        the word of which the stem word is to be found

    Returns
    ---------
    ans : string
        the stem word of the query
    """
    ps = PorterStemmer()
    return ps.stem(query)


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
    arr1.cursor = arr1.head
    arr2.cursor = arr2.head
    while arr1.cursor is not None and arr2.cursor is not None:
        if arr1.cursor.data == arr2.cursor.data:
            ans.insert(arr1.cursor.data)
            arr1 = arr1.cursor.next
            arr2 = arr2.cursor.next
        elif arr1.cursor.data > arr2.cursor.data:
            arr2 = arr2.cursor.next
        else:
            arr1 = arr1.cursor.next
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
    arr1.cursor = arr1.head
    arr2.cursor = arr2.head
    while arr1 is not None and arr2 is not None:
        if arr1.cursor.data > arr2.cursor.data:
            ans.insert(arr2.cursor.data)
            arr2.cursor = arr2.cursor.next
        elif arr1.cursor.data < arr2.cursor.data:
            ans.insert(arr1.cursor.data)
            arr1.cursor = arr1.cursor.next
        else:
            ans.insert(arr1.cursor.data)
            arr1 = arr1.cursor.next
            arr2 = arr2.cursor.next
    return ans


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
        del ansList[1]
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
