a=input("enter no of rows: ")
b=input("Enter no of columns: ")
ls=[]
result=[]
s=0
rowc=0
colc=0
for i in range(0,a):
    for j in range(0,b):
        p=input("enter element: ")
        ls.append(p)

    result.append(ls)
    ls=[]

for i in range(0,a):
    for j in range(0,b):
        rowc+=result[i][j]
    print "Row "+str(i+1)+": "+str(rowc)
    rowc=0
for j in range(0,b):
    for i in range(0,a):
        colc+=result[i][j]
    print "Column "+str(j+1)+": "+str(colc)
    colc=0

print result
