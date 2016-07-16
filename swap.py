n = input("Enter a number: ")
a = []
i = 1
pos1 = 0
pos2 = 0
while(i<=n):
    z = input("Enter number " + str(i) + ":")
    a.append(z)
    i = i + 1
print "Original: " + str(a)
maxi = a[0]
mini = a[0]
for s in range(1,n):
    if(maxi > a[s]):
        maxi = a[s]
        pos1 = s
for t in range(1,n):
    if(mini < a[t]):
        mini = a[t]
        pos2 = t
swap = a[pos1]
a[pos1] = a[pos2]
a[pos2] = swap
print "New: " + str(a)
