import numpy as np
rows=int(input("Enter rows:"))
cols=int(input("Enter cols:"))
matr2d=np.zeros((rows,cols),dtype=int)
for i in range (rows):
    for j in range (cols):
        matr2d[i,j]=int(input(f"Enter for rows{i},col{j}:"))
print(matr2d)
print(matr2d[::-1,::-1],end=" ")
