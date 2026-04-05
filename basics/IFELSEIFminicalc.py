num1= input("Enter a number : \n")
num1 = int (num1)
num2= input("Enter another number : \n")
num2= int (num2)
operator= input ("Enter any one of the operator +,-,*,/,%,** : ")

if operator == "+" :
    print(num1+num2)
elif operator == "-" :
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
elif operator == "%":
    print(num1%num2)
elif operator == "**":
    opt = int(input("Choose 1,2,3 or 4 :\n"))
    if opt == 1:
        print("1st number to the power of second number = " +str(num1**num2))
    elif opt == 2:
        print("2nd number to the power of first number = " +str(num2**num1))
    elif opt == 3:
        print("1st number to the power of itself = " +str(num1**num1))
    elif opt == 4:
        print("2nd number to the power of itself = " +str(num2**num2))
    else:
        print("Wrong Option")
else:
    print("Invalid Input")