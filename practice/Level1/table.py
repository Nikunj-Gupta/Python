def table(n):
    i=0
    while(i<=10):
        print (str(n) + " * " + str(i) + " = " + str(n*i))
        i=i+1
num = input("Enter a number: ")
table(num)
