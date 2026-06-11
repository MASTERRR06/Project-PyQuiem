"""
n=int(input("Enter a number:\n"))
temp=n
sum,c=0,0
while temp!=0:
    digit = temp%10
    c+=1
    temp//=10
temp = n
while temp!=0:
    digit = temp%10
    sum = sum+(digit**c)
    temp//=10
if sum == n:
    print("Armstrong it is")
else:
    print("Neh not Armstrong")
"""
##################ALTERNATE METHOD####################
n=(input("Enter a number:\n"))
temp=int(n)
c=len(n)
sum=0
while temp!=0:
    digit = temp%10
    sum = sum+(digit**c)
    temp//=10
if sum == int(n):
    print("Armstrong it is")
else:
    print("Neh not Armstrong")