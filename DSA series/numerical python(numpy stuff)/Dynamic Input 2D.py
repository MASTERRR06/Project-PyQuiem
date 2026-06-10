import numpy as np
rows=int(input("Enter number of rows:"))
cols=int(input("Enter number of cols:"))
mat2d=np.zeros((rows,cols),dtype=int)
for i in range(rows):
    for j in range (cols):
        mat2d[i,j]=int(input(f"Enter element for row {i},col {j}:"))
print("\n",mat2d)