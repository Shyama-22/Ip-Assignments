def RAT(n):
    for i in range(1,n+1):
        counter=1
        for j in range(1,i+1):
            print(counter,end=" ")
            counter+=1
        print()    

def ISO(n):
    space=n-1
    for i in range(n):
        counter=1
        for j in range(space):
            print(" ",end="")
        for k in range(2*(i)+1):
            print(counter,end="")
            counter+=1
        space-=1    
        print()       
    

def Kite(n):
    space=n-1
    for i in range(n):
        counter=1
        for j in range(space):
            print(" ",end="")
        for k in range(2*(i)+1):
            print(counter,end="")
            counter+=1
        space-=1    
        print()
    space=1
    for i in range(n-1,0,-1):
        counter=1
        for j in range(space):
            print(" ",end="")
        for k in range(2*(i)-1):
            print(counter,end="")
            counter+=1
        space+=1
        print() 

def H_kite(n):
    for i in range(1,n+1):
        counter=1
        for j in range(1,i+1):
            print(counter,end=" ")
            counter+=1
        print()
    for i in range(n,1,-1):
        counter=1
        for j in range(1,i):
            print(counter,end=" ")
            counter+=1
        print()    

def X(n):
    temp=n
    space=0
    for i in range(n):
        counter=1
        for k in range(space):
            print(" ",end="")
        for j in range(2*temp-1):
            print(counter,end="")
            counter+=1
        space+=1
        temp-=1    

        print()
    space-=2
    temp=3
    for i in range(n-1):
        counter=1
        for k in range(space):
            print(" ",end="")
        for j in range(temp):
            print(counter,end="")
            counter+=1
        space-=1
        temp+=2
        print()        


print("PATTERN LIST \n1. Right-angled triangle\n2. Isosceles triangle\n3. Kite\n4. Half Kite\n5. X")    
s=input("Enter number you want to print : ")
n=int(input("Enter Size: "))
print(s)
if s=='1':
    RAT(n)
elif s=="2":
    ISO(n)
elif s=="3":
    Kite(n)
elif s=="4":
    H_kite(n)
elif s=="5":
    X(n)
else:
    print("You entered a wrong choice ")