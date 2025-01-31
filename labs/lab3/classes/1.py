class String:

    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input()
    
    def printString(self):
        print(self.str)

s1 = String()
s1.getString()
s1.printString()