import numpy as np
n=int(input("Enter number of elements:"))
matrd=np.zeros(n,dtype=int)
for i in range (n):
    matrd[i]=int(input(f"Enter for n{i}:"))
print (matrd)
print((matrd<=4))