import json

from nltk.stem import PorterStemmer

from LinkedList import LinkedList


def addWord(word, docID):
    """
    Function to take a word and docID and add it to the existing inverted index list in inverted-index.json

    Parameters
    ----------
    word : string
        the word to be added
    docID : int
        the index of the document
    """
    with open('inverted-index.json') as jsonFile:
        data = json.load(jsonFile)  # loading data
    if word in data:
        data[word].append(docID)
        data[word].sort()
    else:
        data[word] = [docID]
    with open("inverted-index.json", "w") as outfile:
        json.dump(data, outfile)


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
    while high > low:
        mid = (high + low) / 2
        if query == arr[mid]:
            return mid
        else:
            if query > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1


def removeStopWords(word):
    """
    Parameters
    ----------
    word : string
        the word to be tested for being a stop word
    Returns
    ----------
    ans : boolean
        if the word is a stop word or not
    """
    file = open("stop_words.txt")
    arr = []
    for x in file:
        arr.append(x.strip())
        if binarySearch(arr, word) == -1:
            return False
        else:
            return True


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
    while arr1 is not None and arr2 is not None:
        if arr1.data == arr2.data:
            ans.insert(arr1.data)
            arr1 = arr1.next
            arr2 = arr2.next
        elif arr1.data > arr2.data:
            arr2 = arr2.next
        else:
            arr1 = arr1.next
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
    while arr1 is not None and arr2 is not None:
        if arr1.data > arr2.data:
            ans.insert(arr2.data)
            arr2 = arr2.next
        elif arr1.data < arr2.data:
            ans.insert(arr1.data)
            arr1 = arr1.next
        else:
            ans.insert(arr1.data)
            arr1 = arr1.next
            arr2 = arr2.next
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
    while arr1 is not None and arr2 is not None:
        if arr1.data == arr2.data:
            arr1 = arr1.next
            arr2 = arr2.next
        elif arr1.data > arr2.data:
            ans.insert(arr2.data)
            arr2 = arr2.next
        else:
            ans.insert(arr1.data)
            arr1 = arr1.next
    return ans


def invIndxCombiner(ansList):
    while len(ansList):
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
    ansList = []
    with open('k-gram.json') as jsonFile:
        kGramList = json.load(jsonFile)  # loading data
    word = "$" + query + "$"
    for i in range(len(query)):
        kGram = query[i:i + 3]
        ansList.append(kGramList[kGram])
    ansList = invIndxCombiner(ansList)
