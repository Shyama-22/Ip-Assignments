def fxn_val(l,x):
    ans=0                      
    for i in l:
        ans+=(x**i)

    return ans


def calculate_area(l,a,b,d):
    temp=a+d                  
    area=0
    while temp<=b:
        area+=(((temp-a)/6)*(fxn_val(l,a)+(4*fxn_val(l,(a+temp)/2))+fxn_val(l,temp)))
        
        a=temp
        temp=a+d
    return area    

print("ENTER LIST: ")
lst=[int(i) for i in input().split()]
a=int(input("ENTER LIMIT A->"))
b=int(input("ENTER LIMIT B->"))
d=int(input("ENTER COMMON DIFFERENCE D-->"))
if (b-a)%d==0:
    print("area is ",calculate_area(lst,a,b,d))
    
else:
    print("(b-a) is not divisble by d ABORTING////")
