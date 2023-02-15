print("\n")

nm = int(input("enter a number = "))
nm1=1
for i in range(1,1001):
 if(nm%2==0):
     print("even number")
     print()
     nm=int(input("enter number = "))
 elif(nm%2>=1):
    print("odd number")
    print()
    nm=int(input("enter number = "))   
 else:
    print("invalid number")
print("\n\n")
