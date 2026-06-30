import numpy as np
n=int(input("Enter number of elements for 1st array:"))
n1=int(input("Enter number of elements 2nd array:"))
matrd=np.zeros(n,dtype=int)
for i in range (n):
    matrd[i]=int(input(f"Enter for n{i}:"))
matrd1=np.zeros(n1,dtype=int)
for j in range (n1):
    matrd1[j]=int(input(f"Enter for n1{j}:"))

print (matrd)
print (matrd1)
print("Subtract",matrd-matrd1)

###same thing while you do * and /