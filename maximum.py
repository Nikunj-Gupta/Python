i = 1
n = input("Enter number: ")
max = input("Enter number 1: ")
i = 2
while(i <= n):
    x = input("Enter number " + str(i) + " : ")
    if(x > max):
        max = x
    i  = i + 1
print max
