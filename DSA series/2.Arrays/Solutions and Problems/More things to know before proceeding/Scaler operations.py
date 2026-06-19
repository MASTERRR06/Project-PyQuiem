import numpy as np
n=int(input("Enter number of elements for 1st array:"))
matrd=np.zeros(n,dtype=int)
for i in range (n):
    matrd[i]=int(input(f"Enter for n{i}:"))
print (matrd)
print("Add",matrd+5)
print("Subtract",matrd-5)
print("Multiply",matrd*5)
print("Division",matrd/5)