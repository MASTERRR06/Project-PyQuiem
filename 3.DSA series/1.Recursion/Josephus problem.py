def jps(n,k):
    if n==1:
        return 0
    else:
        return (jps(n-1,k)+k)%n
def survive(n,k):
    survivor = jps(n,k)
    print(f"Survivor at position {survivor+1}.")


n=int(input("Enter number1:"))
k=int(input("Enter number2:"))
survive(n,k)

