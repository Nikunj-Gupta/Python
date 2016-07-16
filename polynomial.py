def poly(lst,n):
    result = 0
    for i in range(3):
        term = lst[i] * (n**i)
        result = result + term
    return result
x = input("Enter a number: ")
lst = [1,2,3]
print "value is: " + str(poly(lst,x))
