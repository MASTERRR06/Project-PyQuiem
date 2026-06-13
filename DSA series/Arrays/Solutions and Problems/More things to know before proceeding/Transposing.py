import numpy as np
rows=int(input("Enter size for rows:"))
cols=int(input("Enter size for cols:"))
matrd=np.zeros((rows,cols),dtype=int)
for i in range (rows):
    for j in range(cols):
        matrd[i,j]=int(input(f"Enter for rows{i},cols{j}:"))

print(matrd)
nwshp=matrd.T
print(nwshp)
