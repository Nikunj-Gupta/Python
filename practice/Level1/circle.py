from math import pi
def area(r):
    return pi * r * r
def circum(r):
    return 2*pi*r
rad=input("Enter Radius: ")
print area(rad)
print circum(rad)
