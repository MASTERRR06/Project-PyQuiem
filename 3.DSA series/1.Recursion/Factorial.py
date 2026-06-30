def addnum(n):
    if n==0:
        return 1
    else:
        return n * addnum(n-1)
n=int(input("Enter number:"))
print(addnum(n))