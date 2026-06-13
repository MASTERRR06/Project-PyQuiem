import numpy as np
n=int(input("Enter number of elements for 1st array:"))
matrd=np.zeros(n,dtype=int)
for i in range (n):
    matrd[i]=int(input(f"Enter for n{i}:"))
print(matrd)
nshwp=np.split(matrd,3 )
print (nshwp)
