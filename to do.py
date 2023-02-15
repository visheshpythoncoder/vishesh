jan=list(range(1,32))
feb=list(range(1,29))
mar=list(range(1,32))
apr=list(range(1,31))
may=list(range(1,32))
jun=list(range(1,31))
jul=list(range(1,32))
aug=list(range(1,32))
sep=list(range(1,31))
oct=list(range(1,32))
nov=list(range(1,31))
dec=list(range(1,32))

data=[jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec]

def todo():
    file=open("abc.txt","w")
    file.write(str(a))
    file.close()
    return str(a)

date=int(input("enter a date : "))
if(date>0 and date<=31):
    month=int(input("enter a month : "))
    if(month>0 and month<=12):
        for i in range(date,data): 
            a=input("enter your program : ")
            a=todo()
            print(date+"/"+month+"/2023")
    else:
        print("invalid month")
else:
    print("invalid date")