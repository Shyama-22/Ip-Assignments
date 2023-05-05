


print("Provide Polynomial Function details:")
deg=int(input("Enter the degree of the polynomial: "))

if deg==3:
    a=int(input("Coeff 1: "))
    b=int(input("Coeff 2: "))
    c=int(input("Coeff 3: "))
    d=int(input("Coeff 4: "))
   
elif deg==2:
    a=int(input("Coeff 1: "))
    b=int(input("Coeff 2: "))
    c=int(input("Coeff 3: "))
else:
    a=int(input("Coeff 1: "))
    b=int(input("Coeff 2: "))
    
    
    

l=int(input("Provide lower bound for x: "))
u=int(input("Provide upper bound for x: "))
step=int(input("Provide the steps in which you wish to increment: "))
print("\n")
print("----------------------------------------")
for i in range(l,u+1,step):

    if deg==3:
        ans=a*(i**3)+b*(i**2)+c*(i)+d
    elif deg==2:
        ans=a*(i**2)+b*(i)+c
    else:
        ans=a*(i)+b
    print("|",end="")    
    print(ans*"*")