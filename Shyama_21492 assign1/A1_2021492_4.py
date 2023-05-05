print('''
choose a boolean expression:
1:b1 and not b1
2:(b1 or b2)and (b2 or not b3)
''')
n=int(input("please choose a no: "))
if n==1:
    
    
    
    for i in range(0,2):
        b1=i
        f1=(bool(b1) and (not bool(b1)))
        if f1==(True):
            print("Satisfactory")
            exit()
if n==2:


    flag = 0
    for i in range(0,2):
        b1=i
        for j in range(0,2):
            b2=j
            for k in range(1,2):
                b3=k
                f1=(bool(b1) or bool(b2))and( bool(b2) or (not bool(b3)))
                
                if f1==(True):
                    print("Satisfiable")
                    print(bool(b1),bool(b2),bool(b3))
                    exit()

print("Unsatisfiable")