import array as arr
arr1 = arr.array('i',[1,2,3,4,5])
copyarr=arr.array(arr1.typecode,(x for x in arr1))
for x in copyarr:
    print(x,end=",")