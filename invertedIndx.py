import json
import sys

from LinkedList import LinkedList
from helper import binarySearch, combineInvIndxAND

sys.tracebacklimit = -1

class InvertedIndex:
    """
        This class loads the inverted index from the json file and lets you access the posting list of 
        any given word
        """
    def __init__(self):
        """
        Function to load the inverted index

        Parameters
        ----------
        None

        Returns
        ----------
        None

        """
        self.invInd = {}
        with open('lists/inverted-index.json') as jsonFile:
            data = json.load(jsonFile)
        for x in data:
            temp = LinkedList()
            self.invInd[x] = temp
            for y in data[x]:
                temp.insert(y)

    def getInvInd(self, word):
        """
        Function to get posting list of any word

        Parameters
        ----------
        word: string
            word whose posting list we want
        Returns
        ----------
        invInd: LinkedList
            posting list of given word
        """
        return self.invInd[word]


class KGrams:
    """
    Class to load Kgrams from file and to return Kgrams and perform wildcard searches

    
    """
    def __init__(self):
        """
        Function to load kgrams into a dictionary

        Parameters
        ----------
        None

        Returns
        ----------
        None

        """
        self.kGrams = {}
        with open('lists/kgrams.json') as jsonFile:
            data = json.load(jsonFile)
        for x in data:
            temp = LinkedList()
            for y in data[x]:
                temp.insert(y)
            self.kGrams[x] = temp

    def getKGrams(self, word):
        """
        Function to return kgrams of given word

        Parameters
        ----------
        word: string
            the word whose kgrams we want
        Returns
        ----------
        kGrams: LinkedList
            the kGrams of given word
        """
        try: 
            return self.kGrams[word]
        except:
            print("BAD WILDCARD")
            raise KeyError
           

    def wildCardSearch(self,word):
        """
        Function to perform wildcard searches

        Parameters
        ----------
        word: string
            the word on which we want to perform wildcard searches
        Returns
        ----------
        ansList: LinkedList
            List of all possible words for the given wildcard search
        """
        ansList = LinkedList()
        if word[0]=='*':
            word = word[1:] + '$'
            for i in range(0, len(word)-2):
                if len(word)==3:
                    ansList = self.getKGrams(word[0:3])
                elif i==0:
                    ansList = combineInvIndxAND(self.getKGrams(word[0:3]), self.getKGrams(word[1:4]))
                else:
                    ansList = combineInvIndxAND(ansList,self.getKGrams(word[i:i+3]))
        elif word[-1]=='*':
            word = '$' + word[0:-1]
            for i in range(0, len(word)-2):
                if len(word)==3:
                    ansList = self.getKGrams(word[0:3])
                elif i ==0:
                    ansList = combineInvIndxAND(self.getKGrams(word[0:3]), self.getKGrams(word[1:4]))
                else:
                    ansList = combineInvIndxAND(ansList,self.getKGrams(word[i:i+3]))
        else:
            arr = ('$'+word+'$').split('*')
            tl1 = LinkedList()
            tl2 = LinkedList()
            for i in range(0,len(arr[0])-2):
                if len(arr[0])==3:
                    tl1 = self.getKGrams(arr[0][0:3])
                elif i==0:
                    tl1 = combineInvIndxAND(self.getKGrams(arr[0][0:3]), self.getKGrams(arr[0][1:4]))
                else:
                    tl1 = combineInvIndxAND(tl1,self.getKGrams(arr[0][i:i+3]))
            for i in range(0,len(arr[1])-2):
                if len(arr[1])==3:
                    tl2 = self.getKGrams(arr[1][0:3])
                elif i==0:
                    tl2 = combineInvIndxAND(self.getKGrams(arr[1][0:3]), self.getKGrams(arr[1][1:4]))
                else:
                    tl2 = combineInvIndxAND(tl2,self.getKGrams(arr[1][i:i+3]))
            ansList = combineInvIndxAND(tl1, tl2)
        return ansList

 
class StopWords:
    """
    Class to load stopwords and check if given word is a stop word

    """
    def __init__(self):
        """
        Function to load stopwords

        Parameters
        ----------
        None
        Returns
        ----------
        None
        """
        self.stopWord = []
        file = open("lists/stop_words.txt")
        for x in file:
            self.stopWord.append(x.strip())

    def ifStopWord(self, word):
        """
        Function to check if given word is stopword or not

        Parameters
        ----------
        word: string
            the word we want to check
        Returns
        ----------
        bool
            if word is stop word or not
        """
        return binarySearch(self.stopWord, word) != -1


class UniqueWords:
    """
    Class to load all unique words and check if given word is unique or not

    """
    def __init__(self):
        """
        Function to load all unique words from file

        Parameters
        ----------
        None

        Returns
        ----------
        None

        """
        self.uniqueWords = []
        file = open("lists/unique_words.txt")
        for x in file:
            self.uniqueWords.append(x.strip())
        self.uniqueWords.sort()

    def isUniqueWord(self, word):
        """
        Function to check if given word is unique or not

        Parameters
        ----------
        word: string
            the word we want to check
        Returns
        ----------
        bool
            the result of the search
        """
        return binarySearch(self.uniqueWords, word) != -1
