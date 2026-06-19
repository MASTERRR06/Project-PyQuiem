import math as mt

def circle(radius):
    area = mt.pi * radius**2
    circum= 2*mt.pi*radius
    return (area,circum)

a,c=(circle(int(input("Enter radius:"))))
print(a,c)