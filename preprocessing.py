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
    ans: int
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
    """
    This function is for spelling check. If the word is not in the dictionary, it finds thee closest word using the 
    levenshtein edit distance.

    Parameters
    ----------
    word: string
        word to run spelling check on
    
    Returns
    ----------
    w: string
        the word closest to the given word in terms of edit distance. If there are multiple words with same edit distance,
        it returns the first such word.
    """
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
    """
    This class converts the query with boolean operators such as 'AND', 'OR', etc into something we can work with.
    Essentially we are converting the infix expression into postfix expression

    """
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
        """
        Function to remove the topmost element in list

        Parameters
        ----------
        None

        Returns
        ----------
        ans: int
            the edit distance between the two strings
        """
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
 
    def push(self, op):
        """
        Function to push an element into a list

        Parameters
        ----------
        op: char
            the character to push into the list
        Returns
        ----------
        None

        """
        self.top += 1
        self.array.append(op)
 
    def isOperand(self, ch):
        """
        Function to check if the element is an operand or not

        Parameters
        ----------
        ch: char
            the character to check if it is operand or not
        Returns
        ----------
        bool
            whether the char was a operand or not
        """
        return not(ch=="and" or ch=="or" or ch=="not" or ch=="(" or ch==")")
 
    def notGreater(self, i):
        """
        Function to check the order of preference of operators

        Parameters
        ----------
        i: char
            the operator which we will compare to the operator in the top of the list
        Returns
        ----------
        bool
            whether the precedence of current operator is less than or greater than the operator
            in the top of the list.
        """
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False
 
    def infixToPostfix(self, exp):
        """
        Function to convert infix expression to postfix expression

        Parameters
        ----------
        exp: string
            the expression we want to convert into postfix format
        Returns
        ----------
        output: List
            converted postfix expression
        """
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
 
