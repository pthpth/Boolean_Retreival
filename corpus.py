import json
from helper import binarySearch
from invertedIndx import StopWords
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer


class Corpus:
    """
    Class to go through all documents and make the list of unique words, kgrams, and stop words 

    """
    def __init__(self):
        """
        Function to load the lists incase a new document has to be added.

        Parameters
        ----------
        None

        Returns
        ----------
        None

        """
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
        """
        Function to 'dump' the list of unique words, inverted index, kgrams into their respective files

        Parameters
        ----------
        None

        Returns
        ----------
        None

        """
        with open("lists/inverted-index.json", "w") as outfile:
            json.dump(self.data, outfile)
        with open("lists/unique_words.txt", "w") as f:
            for x in self.uniqueWords:
                f.write(x + "\n")
        with open("lists/kgrams.json", "w") as outfile:
            json.dump(self.k_grams, outfile)

    def addUniqueWord(self, word):
        """
        Function to check if word is unique and add it to the list of unique words and 
        create kgrams if it is unique

        Parameters
        ----------
        word: string
            the word which we want to check if it is unique or not
        Returns
        ----------
        None

        """
        if binarySearch(self.uniqueWords, word) == -1:
            self.uniqueWords.append(word)
        self.uniqueWords.sort()
        temp="$"+word+"$"
        for i in range(len(temp)-2):
            kGram = temp[i:i + 3]
            if kGram in self.k_grams:
                if binarySearch(self.k_grams[kGram],word)==-1:
                    self.k_grams[kGram].append(word)
                    self.k_grams[kGram].sort()
            else:
                self.k_grams[kGram] = [word]
        
    def isStopWord(self, word):
        """
        Function to check if word is stopword or not

        Parameters
        ----------
        word: string
            the word we want to check
        Returns
        ----------
        bool
            if word is stop word or not
        """
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
