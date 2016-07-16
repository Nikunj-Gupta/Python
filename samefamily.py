def samefamily(name1,name2):
    if(name1[1] == name2[1]):
        return True
    else:
        return False
name1 = ("Nikunj","Gupta")
name2 = ("Kushagra","Gupta")
x = samefamily(name1,name2)
if (x == True):
    print ("Same Family")
else:
    print ("Different Family")

