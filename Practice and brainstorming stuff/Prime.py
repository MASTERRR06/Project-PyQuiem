
n=int(input("Enter a number:\n"))
temp = n
if temp < 2:
    print("Not Prime")
elif temp==2:
    print("Prime number")
else:
    i = 2
    while  i < temp :
        if n%i == 0:
            print("not a Prime number")
            break
        i+=1
    else:
        print("Prime number")


