import array as arr
arr = arr.array('i',[1,2,3,4,5])
left = 0
right = len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
for x in arr:
    print(x,end=" ")
    
