n = input("Enter a number: ")
sums=0
product=1
while(n>0):
    a = n%10
    sums =sums + a
    product = product * a
    n = n/10
print sums
print product

