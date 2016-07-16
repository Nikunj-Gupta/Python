n = input("Enter n: ")
i = 1
a = []
sum = 0
while(i <= n):
    x = input("Enter number" + str(i) + ": ")
    a.append(x)
    sum = sum + x
    i = i + 1
a.reverse()
print "List = " + str(a)
print "sum = " + str(sum)
