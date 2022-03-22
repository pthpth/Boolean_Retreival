import json
from LinkedList import LinkedList
from helper import binarySearch


class InvertedIndex:
    def __init__(self):
        self.invInd = {}
        with open('lists/inverted-index.json') as jsonFile:
            data = json.load(jsonFile)
        for x in data:
            temp = LinkedList()
            self.invInd[x] = temp
            for y in data[x]:
                temp.insert(y)

    def getInvInd(self, word):
        return self.invInd[word]


class KGrams:
    def __init__(self):
        self.kGrams = {}
        with open('lists/kgrams.json') as jsonFile:
            data = json.load(jsonFile)
        for x in data:
            temp = LinkedList()
            self.kGrams[x] = temp
            for y in data[x]:
                temp.insert(y)

    def getKGrams(self, word):
        return self.kGrams[word]


class StopWords:
    def __init__(self):
        self.stopWord = []
        file = open("lists/stop_words.txt")
        for x in file:
            self.stopWord.append(x.strip())

    def ifStopWord(self, word):
        return binarySearch(self.stopWord, word) != -1


class UniqueWords:
    def __init__(self):
        self.uniqueWords = []
        file = open("lists/unique_words.txt")
        for x in file:
            self.uniqueWords.append(x.strip())
        self.uniqueWords.sort()

    def isUniqueWord(self, word):
        return binarySearch(self.uniqueWords, word) != -1
