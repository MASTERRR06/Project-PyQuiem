a= int(input("Enter a number:\n"))
temp = a
rev=0
while temp!=0:
    c_d=temp%10
    rev=(rev*10)+c_d
    temp=temp//10
if a == rev :
    print("The entered number is a palindrome")
else:
    print("The entered number is not a palindrome")