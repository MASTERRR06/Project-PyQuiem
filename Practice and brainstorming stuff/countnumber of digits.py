a= input("Enter a number\n")
temp = int(a)
c,rev=0,0
while temp!= 0:
    c_d=temp%10

    c+= 1
    temp=temp//10
print(" ")
print("the number of digits here are:"+str(c))