def largest():
    num = input("Enter number of numbers: ") 
    n= input ("Enter number 1: ")
    maxi = n
    i = 2
    while(i<=num):
        n=input("Enter number " + str(i) + ": ")
        if(maxi<n):
            maxi = n
        i = i + 1
    print maxi
largest()
       
