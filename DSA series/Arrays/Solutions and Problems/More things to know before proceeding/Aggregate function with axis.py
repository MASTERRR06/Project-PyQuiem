import numpy as np
rows=int(input("Enter size for rows:"))
cols=int(input("Enter size for cols:"))
matrd=np.zeros((rows,cols),dtype=int)
for i in range (rows):
    for j in range(cols):
        matrd[i,j]=int(input(f"Enter for rows{i},cols{j}:"))
print (matrd)
print (matrd.sum(axis=0))
print (matrd.min(axis=0))
print (matrd.max(axis=0))
print (matrd.mean(axis=0))
print (matrd.sum(axis=1))
print (matrd.min(axis=1))
print (matrd.max(axis=1))
print (matrd.mean(axis=1))
###axis=0 for columns & axis=1 for rows
