n = input("Enter number: ")
sums = 0
prod = 1
while(n>0):
    sums = sums + (n%10)
    prod = prod * (n%10)
    n = n/10
print "Sum = " + str(sums) 
print "Product = " + str(prod)
