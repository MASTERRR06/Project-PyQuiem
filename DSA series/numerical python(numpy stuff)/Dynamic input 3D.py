import numpy as np
depth=int(input("Enter number for depth:"))
rows=int(input("Enter number of rows:"))
cols=int(input("Enter number of cols:"))
mat3d=np.zeros((depth,rows,cols),dtype=int)
for d in range (depth):
    for i in range(rows):
        for j in range (cols):
            mat3d[i,j]=int(input(f"Enter element for depth{d}, row {i},col {j}:"))
print("\n",mat3d)