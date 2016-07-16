length = input("Enter limit: ")
i = 1
a = []
rows = input("Enter the number of rows: ")
columns = input("Enter the number of columns: ")
while(i<=length):
    n = input("Enter a list: ")
    a.extend(n)
    i = i + 1
for x in range(0,rows):
    for y in range(0,columns):
        sum_row += a[x][y]
    print "sum of row " + str(x) + " = " + str(sum_row)
