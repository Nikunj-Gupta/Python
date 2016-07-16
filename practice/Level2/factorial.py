def fact(n):
    prod = 1
    i=1
    while(i<=n):
        prod = prod * i
        i = i + 1
    return prod
num = input("Enter a number: ")
print fact(num)
