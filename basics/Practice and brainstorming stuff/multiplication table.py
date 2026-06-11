a=int(input("Enter a number:\n"))
temp = a
mtp=0
"""
for i in range(1,13):
    mtp = temp * i
    print(str(a)+"*"+str(i)+"="+str(mtp))
"""
i=0
while i<=12:
    mtp = temp * i
    print(str(a) + "*" + str(i) + "=" + str(mtp))
    i+=1
