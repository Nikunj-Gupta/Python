d1 = [1,"january",2015]
date = []
i = 1
while(i<=3):
    d2 = input("Enter the date: ")
    date.append(d2)
months = ["january","february","march","april","may","june","july","august","september","october","november","december"]
days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
def islater(d1,d2):
    if(d1>d2):
        return True
    else:
        return False
def nextmonth(a1):
    if(a1==months[0]):
        return months[1]           
    elif(a1==months[1]):
        return months[2]
    elif(a1==months[2]):
        return months[3]
    elif(a1==months[3]):
        return months[4]
    elif(a1==months[4]):
        return months[5]
    elif(a1==months[5]):
        return months[6]
    elif(a1==months[6]):
        return months[7]
    elif(a1==months[7]):
        return months[8]
    elif(a1==months[8]):
        return months[9]
    elif(a1==months[9]):
        return months[10]
    elif(a1==months[10]):
        return months[11]
    elif(a1==months[11]):
        return months[0]
def daysinmonth(a1):
    def leapyear(y):
        if(y%100==0):
                if(y%400==0):
                    return True
        elif(y%4==0):
            return True
        else:
            return False
    if(a1==months[0]):
        return 31           
    elif(a1==months[1]):
        if(leapyear(a1)==True):
            return 29
        else:
            return 28
    elif(a1==months[2]):
        return 31
    elif(a1==months[3]):
        return 30
    elif(a1==months[4]):
        return 31
    elif(a1==months[5]):
        return 30
    elif(a1==months[6]):
        return 31
    elif(a1==months[7]):
        return 31
    elif(a1==months[8]):
        return 30
    elif(a1==months[9]):
        return 31
    elif(a1==months[10]):
        return 30
    elif(a1==months[11]):
        return 31
