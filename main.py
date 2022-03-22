import json
from helper import combineInvIndxNOT, combineInvIndxOR
from nltk.stem import PorterStemmer
from invertedIndx import InvertedIndex, StopWords, KGrams
from helper import combineInvIndxAND
from preprocessing import Conversion,findRightWord

invertedInd = InvertedIndex()
stopWords = StopWords()
kGrams = KGrams()

def invIndxCombiner(ansList):
    while len(ansList) > 1:
        ansList = invIndxSort(ansList)
        ans = combineInvIndxOR(ansList[0], ansList[1])
        del ansList[0]
        del ansList[0]
        ansList.append(ans)
    return ansList[0]


def invIndxSort(query):
    query=sorted(query,key=lambda x: x.len)
    return query


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

def getPosting(word):
    if word[0]=='*' or word[-1]=='*' or len(word.split('*'))==2:
        temp=kGrams.wildCardSearch(word)
        return getInvertedIndx(temp)
    else:
        word=findRightWord(word)
        word=stemmer(word)
        return invertedInd.getInvInd(word)

def getInvertedIndx(wordList):
    cursor=wordList.head
    arr=[]
    while cursor!=None:
        temp=stemmer(cursor.data)
        arr.append(invertedInd.getInvInd(temp))
        cursor=cursor.next
    ans=invIndxCombiner(arr)
    return ans


if __name__=="__main__":
    query=input("Enter query: ")
    query=query.lower()
    obj = Conversion(len(query))
    ansList=obj.infixToPostfix(query)
    stack=[]
    for x in ansList:
        if x=="and":
            temp=combineInvIndxAND(stack[-1],stack[-2])
            del stack[-1]
            del stack[-1]
            stack.append(temp)
        elif x=="or":
            temp=combineInvIndxOR(stack[-1],stack[-2])
            del stack[-1]
            del stack[-1]
            stack.append(temp)
        elif x=="not":
            temp=combineInvIndxNOT(stack[-1],42)
            del stack[-1]
            stack.append(temp)
        else:
            x=getPosting(x)
            stack.append(x)
    ans=stack[0]
    cursor=ans.head
    docs = {}
    if ans.len!=0:
        print("FOUND ", ans.len, " DOCUMENTS SATISFYING USER QUERY")
        with open('lists/names.json') as jsonFile:
            docs = json.load(jsonFile)
        while cursor!= None:
            print(docs[str(cursor.data)])
            cursor = cursor.next
    else: 
        print("NO DOCUMENTS SATISFYING USER QUERY WERE FOUND")
