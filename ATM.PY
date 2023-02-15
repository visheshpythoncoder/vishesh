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
