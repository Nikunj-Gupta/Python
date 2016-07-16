n = input("Enter number of numbers: ")
i=1
sum = 0
while(i<=n):
    num = input("Enter number " + str(i) + " : ")
    sum = sum + num
    i = i + 1
print ("Average is: " + str(sum/n))
