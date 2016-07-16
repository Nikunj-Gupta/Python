a=[]
length = input("Enter length of the list: ")
i = 1
while(i<=length):
    n = input("Enter a number: ")
    a.append(n)
    i = i + 1
pos1 = input("Enter position 1: ")
pos2 = input("Enter position 2: ")
swap = a[pos1]
a[pos1] = a[pos2]
a[pos2] = swap
print "New List : " + str(a)
