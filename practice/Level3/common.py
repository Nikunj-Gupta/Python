len1 = input("Enter length of list 1: ")
i=1
j=1
a=[]
b=[]
while(i<=len1):
    n1 = input("Enter an element: ")
    a.append(n1)
    i = i + 1 
len2 = input("Enter length of list 2: ")
while(j<=len2):
    n2 = input("Enter an element: ")
    b.append(n2)
    j = j + 1 
print a
print b
for x in a:
    for y in b:
        if(x == y):
            print "Common element found"
            print x
        
