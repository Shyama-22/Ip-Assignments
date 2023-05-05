from datetime import datetime


class BankAccount:
    def __init__(self,username,passw,currbal):
        self.username=username
        self.passw=passw
        self.currbal=currbal
        #file create 
        self.filename=username+".txt"
        fp=open(self.filename,'a')
        fp.close()
    def authenticate(self,counter,secretpassword):
        try:
            assert counter<3
            return self.passw==secretpassword
        except AssertionError:
            if self.passw==secretpassword:
                return True
            else:
                return("Too many wrong attempts!!")
                
    def deposit(self):
        fp=open(self.filename,'a')
        counter=2
        sp=input("Provide your secret password: ")
        while counter<=3:
            flag=self.authenticate(counter,sp)
            if flag==True:
                ansd=int(input("Enter Amount To Be Deposited: "))
                self.currbal+=float(ansd)
                strans=str(datetime.now())+" The Amount Of Rupees "+str(ansd)+" has been added Current Balance -> "+str(self.currbal)
                fp.write(strans+"\n")
                break
            elif flag==False:
                sp=input("Provide your secret password: ")
                counter+=1
            else:   
                print(self.authenticate(counter,sp))
                break    
                
                
        fp.close()        
    def withdraw(self):
        fp=open(self.filename,'a')
        counter=1
        sp=input("Provide your secret password: ")
        while counter<=3:
            flag=self.authenticate(counter,sp)
            if flag==True:
                answ=int(input("Enter Amount To Be Withdrawn: "))
                if self.currbal<answ:
                    print("Account Balance Low Cannot Be Debited at This time")
                else:
                    self.currbal-=float(answ)
                    strans2=str(datetime.now())+" The Amount Of Rupees "+str(answ)+" has been Debited Current Balance -> "+str(self.currbal)
                    fp.write(strans2)
                    break
            elif flag==False:
                sp=input("Provide your secret password: ")
                counter+=1
            else:   
                print(self.authenticate(counter,sp))
                break    
            
        fp.close()
    def bankstatement(self):
        fp=open(str(self.filename),'r')
        counter=1
        sp=input("Provide your secret password: ")
        while counter<3:
            if self.authenticate(counter,sp)==True:
               
                for i in fp:
                    print(i)
                
                break
            elif self.authenticate(counter,sp)==False:
                
                counter+=1
            else:
                print(self.authenticate(counter,sp))
                break    
        fp.close()

print("/////////////////Welcome to Bank of IIITD ","\n")
nm=input("Enter Name: ")
ps=input("Enter Password: ")
sb=float(input("Starting balance for your account: "))
obj=BankAccount(nm,ps,sb)
while True:
    print("Select your option-> ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Bank Statement")

    option=int(input("Enter your choice: "))
    if option==1:
        
        obj.deposit()
    elif option==2:
        
        obj.withdraw()
    elif option==3:
        obj.bankstatement()
    p=input("Do you wish to continue?Yes/No: ")
    if p=="No":
        break