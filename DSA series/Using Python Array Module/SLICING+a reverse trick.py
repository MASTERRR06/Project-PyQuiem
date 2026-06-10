import array as arr
arr1 = arr.array('i',[1,2,3,4,5])
val=arr1[2:4] #if you know the start and end point since [start:end]
val=arr1[2:-1]#if you know the start but you have been given a rough idea for end point
val=arr1[::-1]#another reverse trick
for x in val:
    print(x,end=" ")