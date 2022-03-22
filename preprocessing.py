import numpy as np

from invertedIndx import UniqueWords

uniquewords = UniqueWords()


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
    # Initiating the matrix with correct dimensions along with the first row and column
    mat = np.zeros((len(str1) + 1, len(str2) + 1))
    for i in range(0, len(str1) + 1):
        mat[i][0] = i
    for i in range(0, len(str2) + 1):
        mat[0][i] = i
    # Comparing the three previous terms and checking minimum of the
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                mat[i][j] = min(mat[i - 1][j] + 1, mat[i][j - 1] + 1, mat[i - 1][j - 1])
            else:
                mat[i][j] = min(mat[i - 1][j] + 1, mat[i][j - 1] + 1, mat[i - 1][j - 1] + 1)
    # Returning edit distance
    return mat[len(str1)][len(str2)]
    # While implementing function keep a track of len(str1)-len(str2) so we can reduce usage of editDistance()


def findRightWord(word):
    min = 127
    if uniquewords.isUniqueWord(word):
        return word
    else:
        for wd in uniquewords.uniqueWords:
            if abs(len(wd) - len(word)) > min:
                continue
            elif editDistance(wd,word)<min:
                min = editDistance(wd, word)
                w = wd
        print("Did you mean", w.title(), "?")
        return w

class Conversion:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
        self.output = []
        self.precedence = {'and': 2, 'or': 1, 'not': 3}
 
    def isEmpty(self):
        return True if self.top == -1 else False
 
    def peek(self):
        return self.array[-1]
 
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
 
    def push(self, op):
        self.top += 1
        self.array.append(op)
 
    def isOperand(self, ch):
        return not(ch=="and" or ch=="or" or ch=="not" or ch=="(" or ch==")")
 
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False
 
    def infixToPostfix(self, exp):
        temp=exp
        exp=""
        for j in range(len(temp)):
            if temp[j]=="(" :
                exp=exp+"("+" "
            elif temp[j]==")":
                exp=exp+" "+")"
            else:
                exp=exp+temp[j]
        for i in exp.split():
            if self.isOperand(i):
                self.output.append(i)
 
            elif i == '(':
                self.push(i)
 
            elif i == ')':
                while((not self.isEmpty()) and
                      self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
 
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
 
        while not self.isEmpty():
            self.output.append(self.pop())
 
        return self.output
 
