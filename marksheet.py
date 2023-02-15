# marksheet
mark=[[23,43,54,24,65,76],[43,65,76,21,43,45],[76,23,43,54,76,90],[32,43,54,23,54,32],[45,65,23,43,65,76],[32,43,54,54,65,34],
[46,87,98,67,24,54],[34,54,23,65,76,78],[65,76,77,88,76,54],[43,87,78,43,21,50],[61,51,70,60,80,33]]
print("\t\tMARKSHEET")
print()
print("Press for Marks         = '1'")
print("Press for Result        = '2'")
print("Press for Whole Result  = '3'")
print()
en=int(input("Enter a Choice = "))
print()
if(en==1):
    roll=int(input("Enter Roll Number = "))
    print()
    print("press 0 : HINDI")
    print("press 1 : ENGLISH") 
    print("press 2 : MATHMATICS")
    print("press 3 : BIOLOGY")
    print("press 4 : CHEMISTRY")
    print("press 5 : PHYSICS")
    print()
    sc=int(input("Enter a Subject Code = "))
    if(sc==0):
        print("HINDI =",mark[roll][0])
    elif(sc==1):
        print("ENGLISH =",mark[roll][1])
    elif(sc==2):
        print("MATHMATICS =",mark[roll][2])
    elif(sc==3):
        print("BIOLOGY =",mark[roll][3])
    elif(sc==4):
        print("CHEMISTRY =",mark[roll][4])
    elif(sc==5):
        print("PHYSICS =",mark[roll][5])
    else:
        print("Enter Correct Code.......")
elif(en==2):
    roll=int(input("enter roll number = "))
    print("HINDI         =",mark[roll][0])
    print("ENGLISH       =",mark[roll][1])
    print("MATHMATICS    =",mark[roll][2])
    print("BIOLOGY       =",mark[roll][3])
    print("CHEMISTRY     =",mark[roll][4])
    print("PHYSICS       =",mark[roll][5])
elif(en==3):
    print("\t\tHIN-ENG-MATH-BIO-CHEM-PHY")
    print("Roll no 0:\t",mark[0][0:6])
    print()
    print("Roll no 1:\t",mark[1][0:6])
    print()
    print("Roll no 2:\t",mark[2][0:6])
    print()
    print("Roll no 3:\t",mark[3][0:6])
    print()
    print("Roll no 4:\t",mark[4][0:6])
    print()
    print("Roll no 5:\t",mark[5][0:6])
    print()
    print("Roll no 6:\t",mark[6][0:6])
    print()
    print("Roll no 7:\t",mark[7][0:6])
    print()
    print("Roll no 8:\t",mark[8][0:6])
    print()
    print("Roll no 9:\t",mark[9][0:6])
    print()
    print("Roll no 10:\t",mark[10][0:6])
else:
    print("Enter Correct Choice..........")

print("\n\n\n")

print("\t\tSBI BANK")
print()
print("Press For WITHDRAW      ='1'")
print("Press For CHECK BALANCE ='2'")
print("Press For CHANGE PIN    ='3'")
print("Press For EXIT          ='4'")
print()
vl=int(input("enter a choice = "))
print("WELCOME TO SBI BANK : ...........")
pas1=9162
bal=1325000
if(vl==1):
    pas=int(input("Enter Pin  : "))
    if(pas==pas1):
        sl=int(input("Enter Amount = "))
        print()
        if(bal>=vl):
            s=bal-sl
            print("TRANSACTION COMPLETE:")
            print()
            print("Current Balance : ",s)
        else:
            print("Insufficient Amount entered")
    else:
        print("Incorrect Pin")
elif(vl==2):
    pas=int(input("Enter Pin : "))
    if(pas==pas1):
        print("Current Balance = ",bal)
    else:
     print("Incorrect Pin")
elif(vl==3):
    pas=int(input("Enter Pin : "))
    if(pas==pas1):
        nw=int(input("Enter New Password : "))
        nw1=int(input("Confirm Password : "))
        if(nw==nw1):
            print("Changed Password")
        else:
            print("Password Not Match")
    else:
        print("Incorrect Pin")
elif(vl==4):
    print("EXIT.............")    
else:
    print("invalid choice")

print("\n\n\n")
