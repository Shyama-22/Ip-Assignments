def NT(n,ndarr):
    print("Normal Traversal:",end=" ")
    for i in range(n):                                #
        for j in range(n):
            print(ndarr[i][j],end=" ")
    print()            

def AT(n,ndarr):
    print("Alternating Traversal:",end=" ")
    ptr=-1
    for i in range(n):
        if i%2==0:
            for j in range(n):
                ptr+=1
                print(ndarr[i][ptr],end=" ")
            
           
        else:
            for j in range(n):
                print(ndarr[i][ptr],end=" ")
                ptr-=1
    print()

def ST(n,ndarr):
    print("Spiral Traversal: ",end=" ")
    sr=0;er=n-1;sc=0;ec=n-1
    while ec>=sc and er>=sr:
        #first row of rem rows asc
        for i in range(sc,ec+1):
            print(ndarr[sr][i],end=" ")
        sr+=1
        
        #last col of rem col asc
        for i in range(sr,er+1):
            print(ndarr[i][ec],end=" ")
        ec-=1
        
        #last row of rem rows desc
        for i in range(ec,sc-1,-1):
            print(ndarr[er][i],end=" ")
        er-=1

        #first col of rem col desc
        for i in range(er,sr-1,-1):
            print(ndarr[i][sc],end=" ")
        sc+=1

def BT(n,ndarr):
    print("Boundary Traversal: ",end=" ")
    sr=0;er=n-1;sc=0;ec=n-1
   
    for i in range(sc,ec+1):
        print(ndarr[sr][i],end=" ")
    sr+=1
        
      
    for i in range(sr,er+1):
        print(ndarr[i][ec],end=" ")
    ec-=1
        
     
    for i in range(ec,sc-1,-1):
        print(ndarr[er][i],end=" ")
    er-=1

     
    for i in range(er,sr-1,-1):
        print(ndarr[i][sc],end=" ")
    sc+=1

def DTRL(n,ndarr):
    print("Diagonal traversal from right to left : ",end=" ")
    temp=n-1
    for k in range(2*n-1):
        
        if k<n:
            i=0
            j=k
        else:
            if k%(n-1)==0:
                i=n-1
            else:
                i=k%(n-1)
            j=n-1
            
        if k<n:
            for z in range(k+1):
                print(ndarr[i][j],end=" ")
                i+=1
                j-=1
        else:
            
            for z in range(temp):
                print(ndarr[i][j],end=" ")
                i+=1
                j-=1
            temp-=1                    
        
def DTLR(n,ndarr):
    print("Diagonal traversal from left to right : ",end=" ")
    temp=n-1
    for k in range(2*n-1):
        
        if k<n:
            i=k
            j=0
        else:
            if k%(n-1)==0:
                j=n-1
            else:
                j=k%(n-1)
            i=n-1
            
        if k<n:
            for z in range(k+1):
                print(ndarr[i][j],end=" ")
                i-=1
                j+=1
        else:
            
            for z in range(temp):
                print(ndarr[i][j],end=" ")
                i-=1
                j+=1
            temp-=1 
def invertt(matrix):
    for i in matrix:
        i.reverse()
    return matrix

while True:

    n=int(input("ENTER SIZE OF NXN MATRIX: "))    #arr[5][3]=[[1,2,3],[4,5,6],[7,8,9],[4,5,3],[6,2,4]]
    print("ENTER THE MATRIX:")                      #arr[2][0]=7        #arr=[[1,2,4],[6,4,4]]
    matrix=[]                                       
    for i in range(n):
        x=input()
        a=[int(j) for j in x.split()]
        matrix.append(a)

    while True:
        print("-------------MENU-------------------------------")
        print("1. Normal Traversal")
        print("2. Alternating Traversal")
        print("3. Spiral Traversal")
        print("4. Boundary Traversal")
        print("5. Diagonal Traversal (From Right To Left)")
        print("6. Diagonal Traversal (From Left To Right)")
        print("7. Enter New Matrix")
        print("8. Exit")
        choice=int(input("Enter Choice: "))
        if choice==1:
            NT(n,matrix)
        elif choice==2:
            AT(n,matrix)
        elif choice==3:
            ST(n,matrix)
        elif choice==4:
            BT(n,matrix)
        elif choice==5:
            DTRL(n,matrix)
        elif choice==6:
            DTRL(n,invertt(matrix))
        elif choice==7:
            break                        
        elif choice==8:
            exit()
        print()
