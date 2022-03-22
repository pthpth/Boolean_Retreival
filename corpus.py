import json
from helper import binarySearch
import os
from invertedIndx import StopWords
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer


class Corpus:
    def __init__(self):
        self.stopWords = []
        self.uniqueWords = []
        self.k_grams={}
        with open('lists/kgrams.json') as jsonFile:
            self.k_grams = json.load(jsonFile)
        with open('lists/inverted-index.json') as jsonFile:
            self.data = json.load(jsonFile)
        file = open("lists/unique_words.txt")
        for x in file:
            self.uniqueWords.append(x.strip())
        self.uniqueWords.sort()
        file = open("lists/stop_words.txt")
        for x in file:
            self.stopWords.append(x.strip())
        self.stopWords.sort()
    def stemmer(self, query):
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

    def close(self):
        with open("lists/inverted-index.json", "w") as outfile:
            json.dump(self.data, outfile)
        with open("lists/unique_words.txt", "w") as f:
            for x in self.uniqueWords:
                f.write(x + "\n")
        with open("lists/kgrams.json", "w") as outfile:
            json.dump(self.k_grams, outfile)

    def addUniqueWord(self, word):
        if binarySearch(self.uniqueWords, word) == -1:
            self.uniqueWords.append(word)
        self.uniqueWords.sort()
        temp="$"+word+"$"
        for i in range(len(temp)-2):
            kGram = temp[i:i + 3]
            if kGram in self.k_grams:
                if binarySearch(self.k_grams[kGram],temp[1:-2])==-1:
                    self.k_grams[kGram].append(temp[1:-2])
                    self.k_grams[kGram].sort()
            else:
                self.k_grams[kGram] = [temp[1:-2]]
        



    def isStopWord(self, word):
        return binarySearch(self.stopWords, word) != -1

    def addWord(self, word, docID):
        """
        Function to take a word and docID and add it to the existing inverted index list in inverted-index.json

        Parameters
        ----------
        word : string
            the word to be added
        docID : int
            the index of the document
        """
        # loading data
        if word in self.data:
            if binarySearch(self.data[word], docID) == -1:
                self.data[word].append(docID)
            self.data[word].sort()
        else:
            self.data[word] = [docID]


if __name__ == "__main__":
    cp = Corpus()
    stop = StopWords()
    print(cp.stopWords)
    print(binarySearch(cp.stopWords, "is"))
    t = RegexpTokenizer(r'\w+')
    for p in range(42):
        print(p)
        file = open(f"data/{str(p)}.txt")
        lines = file.readlines()
        for x in lines:
            z = t.tokenize(x)
            for y in z:
                y = y.lower()
                if cp.isStopWord(y) is False:
                    cp.addUniqueWord(y)
                    y = cp.stemmer(y)
                    cp.addWord(y, p)
    cp.close()
