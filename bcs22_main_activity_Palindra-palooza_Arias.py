import re

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, x):
        new = Node(x)
        if self.top is None:
            self.top = new
            self.top.next = None
        else:
            new.next = self.top
            self.top = new

    def pop(self):
        if self.top is None:
            print("Stack is empty")
        elif self.top.next is None:
            temp = self.top
            #print("Popped ELement is : ", data)
            #print("------------------------------------")
            self.top = None
            return temp.data
        else:
            temp = self.top
            #print("Popped Element is : ", self.top.data)
            #print("------------------------------------")
            self.top = temp.next
            return temp.data

    def display(self):
        if self.top is None:
            print("Stack is Empty")
            print("------------------------------------")
        else:
            print("Elements of the stack are: ")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next
            print("Top of the stack is: ", self.top.data)

class PalindromeChecker:
    def __init__(self):
        self.stack = Stack()

    def check(self, sentence):
        print("\noriginal sentence: ", sentence)

        clean_str = re.sub(r"[^a-zA-Z]", "", sentence.lower())
        for c in clean_str:
            self.stack.push(c)
        print("cleaned sentence: ", clean_str)
        
        reversed_str = ""
        for c in clean_str:
            reversed_str += self.stack.pop()
        print("reversed sentence: ", reversed_str)

        if clean_str == reversed_str:
            print("\nSentence is palindrome!\n")
        else:
            print("\nSentence is not palindrome!\n")
        

while(True):
    print("Enter the option below: ")
    print("1 - Palindrome Checker \n2 - Exit")
    option = int(input())
    if option == 1:
        print("Enter sentence: ")
        #sentence = "A man, a plan, a canal, Panama!"
        sentence = input()
        p = PalindromeChecker()
        p.check(sentence)
    else:
        print("Program will exit...")
        break


