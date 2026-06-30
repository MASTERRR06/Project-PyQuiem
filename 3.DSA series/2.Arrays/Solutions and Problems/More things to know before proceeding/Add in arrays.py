import numpy as np

class Arrayadd:
    def __init__(self):
        self.n=int(input("Enter number of elements for 1st array:"))
        self.n1=int(input("Enter number of elements 2nd array:"))
        self.matrd=np.zeros(self.n,dtype=int)
        for i in range (self.n):
            self.matrd[i]=int(input(f"Enter for n{i}:"))
        self.matrd1=np.zeros(self.n1,dtype=int)
        for j in range (self.n1):
            self.matrd1[j]=int(input(f"Enter for n1{j}:"))

        print (self.matrd)
        print (self.matrd1)
        print("Add",self.matrd+self.matrd1)
obj = Arrayadd()
