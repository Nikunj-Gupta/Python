n = input("Enter a number: ")
a = []
while(n>0):
    a.append(n%10)
    n = n/10
a.reverse()
for i in a:
	print i
