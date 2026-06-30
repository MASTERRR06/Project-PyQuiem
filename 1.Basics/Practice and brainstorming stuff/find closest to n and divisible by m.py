n=int(input("Enter a number for n:\n"))
m=int(input("Enter a number for m :\n"))

lower=(n//m)*m ##(13/4)= (3*4)=12(since integer)
upper=lower+m ##(12+4)=16

if abs(n-lower)<abs (n-upper):
    ## (13-12)=1     (13-16)=-3
    result=lower
else:
    result = upper
print("The closest to "+str(n)+" divisible by "+str(m)+"="+str(result))

