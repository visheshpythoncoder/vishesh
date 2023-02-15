def readpin():
    file=open("pin.txt","r")
    data=file.read()
    file.close()
    return int(data)

def readbal():
    file=open("bal.txt","r")
    data=file.read()
    file.close()
    return int(data)

def writepin(data):
    file=open("pin.txt","w")
    file.write(str(data))
    file.close()
    
def writebal(data):
    file=open("bal.txt","w")
    file.write(str(data))
    file.close()

print("\t\tSTATE BANK OF INDIA\n")
print("press 1 : withdraw")
print("press 2 : check balance")
print("press 3 : pin change")
print("press 4 : deposit")
print("press 5 : exit")
print()
vl=int(input("enter a choice = "))
print("WELCOME TO SBI BANK : ...........")
if(vl==1):
    pas=int(input("Enter Pin  : "))
    pas1=readpin()
    if(pas==pas1):
        am=int(input("Enter Amount = "))
        bal=readbal()
        print()
        if(bal>=am):
            bal=bal-am
            print("TRANSACTION COMPLETE:")
            print()
            print("Current Balance : ",bal)
        else:
            print("Insufficient Amount entered")
    else:
        print("Incorrect Pin")
elif(vl==2):
    pas=int(input("Enter a pin : "))
    pas1=readpin()
    if(pas==pas1):
        bal=readbal()
        print("current balance : ",bal)
    else:
        print("incorrect pin")
elif(vl==3):
    pas=int(input("Enter a pin : "))
    pas1=readpin()
    if(pas==pas1):
        nm=int(input("enter a new pin :"))
        nm2=int(input("confirm new pin : "))
        if(nm==nm2):
         print("changed pin")
         writepin(nm)
        else:
            print("pin does't match")
    else:
        print("inccorect pin")
elif(vl==4):
    pas=int(input("Enter a pin : "))
    pas1=readpin()
    if(pas==pas1):
        i=int(input("enter amonut for deposit : "))
        bal=readbal()
        bal=i+bal
        writebal(bal)
        print("current balance : ",bal)
    else:
        print("incorrect pin")
elif(vl==6):
    print("thanks for visiing sbi...........")
else:
    print("invalid choice .....")




