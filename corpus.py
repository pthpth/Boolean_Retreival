import json


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
