
p,q=[int(i) for i in input().split()]
m,n=[int(i) for i in input().split()]
lst=[]
lst1=[]
dd=0
ds=0
gdd=p
gds=q
for i in range(n):
    lst1.append(0)
for i in range(m):
    str1=input()
    lst.append(str1)
    for j in range(n):
        if str1[j]=='1':
            lst1[j]+=1
                 
lst2=lst1.copy()          
lst2.sort()
idx=n-1
for i in range(n):
    
    if i%2==0:
        dd+=lst2[idx]*gdd
        idx-=1
    else:
        ds+=lst2[idx]*gds
        idx-=1
    gdd+=1
    gds+=1
print()
print(dd,ds)        

lst3=[]


for i in range(n):
    lst3.append(lst1.index(max(lst1)))
    lst1[lst1.index(max(lst1))]=-1



for i in range(m):
    str2=lst[i]
    
    for j in range(n):
        if str2[j]=='1':
            for k in range(n):
                if lst3[k]==j:
                    if k%2==0:
                        
                        print("D",end="")
                    else:
                        print("S",end="")
        else:
            print(str2[j],end="")
    print()                       


            


