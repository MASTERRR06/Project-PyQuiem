a= input("Enter a number\n")
temp = int(a)
sum=0
while temp!= 0:
    c_d=temp%10
    sum=sum+c_d
    temp=temp//10
print(str(sum))