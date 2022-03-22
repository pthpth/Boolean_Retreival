import json
from sqlite3 import Cursor
from tkinter.messagebox import NO
from webbrowser import get

from numpy import cumprod
from LinkedList import LinkedList
from helper import binarySearch, combineInvIndxAND


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
            for y in data[x]:
                temp.insert(y)
            self.kGrams[x] = temp

    def getKGrams(self, word):

        return self.kGrams[word]

    def wildCardSearch(self,word):
        ansList = LinkedList()
        if word[0]=='*':
            print("star in begin")
            word = word[1:] + '$'
            for i in range(0, len(word)-2):
                if len(word)==3:
                    ansList = self.getKGrams(word[0:3])
                elif i==0:
                    ansList = combineInvIndxAND(self.getKGrams(word[0:3]), self.getKGrams(word[1:4]))
                else:
                    ansList = combineInvIndxAND(ansList,self.getKGrams(word[i:i+3]))
        elif word[-1]=='*':
            print("star in end")
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
