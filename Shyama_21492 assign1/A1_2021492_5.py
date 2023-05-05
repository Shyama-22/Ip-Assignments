def getReverse(n):
    x=0
    while n>0:
        x+=(n%10)
        x=x*10
        
        n=n//10
    return x//10
    
    
def checkPalindrome(n):
    x=getReverse(n)
    if x==n:
        return True
    else:
        return False
    
def checkNarcissistic(n) :
    z=n
    l=0
    while z>0:
        l+=1
        z=z//10
        
    z=n
    sum_1 = 0
 
    while z>0 :
        sum_1 = sum_1 + (z % 10)**l
        z = z// 10
     
    return (n == sum_1)    
    
def findDigitSum(n):
    sum2=0
    while n>0:
        sum2+=(n%10)
        n=n//10
    return sum2

def findSquareDigitSum(n):
    sum3=0
    while n>0:
        sum3+=((n%10)**2)
        n=n//10
    return sum3
    
    
while True:
    print("---------MENU----------------")
    print("1. Get reverse Number ")
    print("2. Check Palindrome")
    print("3. Check Narcissistic ")
    print("4. Get Digit Sum")
    print("5. Get Square Digit Sum")
    print("6. To exit the program")
    
    ans=int(input("ENTER YOUR CHOICE: "))
    if ans==6:
        print(exit())
    n=int(input("ENTER NUMBER: "))
    if ans==1:
        print(getReverse(n))
    elif ans==2:
        print(checkPalindrome(n))
    elif ans==3:
        print(checkNarcissistic(n))
    elif ans==4:
        print(findDigitSum(n))
    elif ans==5:
        print(findSquareDigitSum(n))
    
    else:
        print("Wrong Option")