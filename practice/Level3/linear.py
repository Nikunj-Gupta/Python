length = input("Enter length: ")
i=1
a=[]
while(i<=length):
    n = raw_input("Enter an element: ")
    a.append(n)
    i = i + 1
check = raw_input("Enter number to be checked: ")
if (check in a):
    print "YES"
else:
    print "NO"
