n=int(input("enter a number:\n"))
temp= n
mul=1
if temp<0:print("this input not allowed here")
else:
    while temp!=0:
        mul*=(temp)
        temp-=1
    print("Factorial : "+str(mul))