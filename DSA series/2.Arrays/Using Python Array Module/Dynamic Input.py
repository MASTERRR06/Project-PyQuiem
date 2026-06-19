from array import *
arr1=array('i',[])
n=int(input("Enter array size:"))
for i in range (0,n):
    arr1.append(int(input("Enter number:\n")))
for x in arr1:
    print(x,end=" ")