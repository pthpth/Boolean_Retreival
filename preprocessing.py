import numpy as np

from nltk.tokenize import word_tokenize
from LinkedList import LinkedList
import json
from main import binarySearch
from invertedIndx import UniqueWords

uniquewords=UniqueWords()
def editDistance(str1, str2):
    """
    Function to take two strings and return the levenshtein edit distance

    Parameters
    ----------
    str1: string
        string to be compared

    str2: string
        string being compared with
    Returns
    ----------
    ans : int
        the edit distance between the two strings
    """
    # Converting str1 to str2
    mat = np.zeros((len(str1) + 1, len(str2) + 1))
    for i in range(0, len(str1) + 1):
        mat[i][0] = i
    for i in range(0, len(str2) + 1):
        mat[0][i] = i
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                mat[i][j] = min(mat[i - 1][j] + 1, mat[i][j - 1] + 1, mat[i - 1][j - 1])
            else:
                mat[i][j] = min(mat[i - 1][j] + 1, mat[i][j - 1] + 1, mat[i - 1][j - 1] + 1)
    return mat[len(str1)][len(str2)]


def findRightWord(word):
    with open('unique-word') as jsonFile:
        kGramList = json.load(jsonFile)
    if uniquewords.isUniqueWord(word):

    else:
        return word



def booleanRet(query):
    tokens = word_tokenize(query)
    ans = LinkedList()
    for x in tokens:
        temp = findRightWord(x)
