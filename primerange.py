def prime(n):
    flag = 0
    for i in range(2,n):
        if(n%i==0):
            flag = 1
            break
        if(flag==1):
            print "Not Prime"
        else:
            print "Prime"
a = input("Enter lower limit: ")
b = input("Enter upper limit: ")
i=a
while(i<=b):
    prime(i)
    i = i + 1
