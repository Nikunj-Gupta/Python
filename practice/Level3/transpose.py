length = input("Enter length: ")
i=1
a=[]
final =[]
while(i<=length):
    n=input("Enter list: ")
    a.append(n)
    i = i + 1
for x in range(0,len(a)):
    for y in range(len(a[0])):
        final.insert(a[y][x])
for f in final:
    print f
