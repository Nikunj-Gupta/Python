def poly(lst,n):
    result = 0
    for i in range(len(lst)):
        term = lst[i] * (n**i)
        result = result + term
    return result
lst = []
x = input("Enter x: ")
z = input("Enter a number")
lst.append(z)
print "value is: " + str(poly(lst,x))                                
