ID=0

class LaundaryService:
    def __init__(self,name,contact,email,toc,branded,season,id):
        self.name=name
        self.contact=contact
        self.email=email
        self.toc=toc
        self.branded=branded
        self.season=season
        self.id=id
    def customerDetails(self):
        print()
        print()
        print("The Customer Specific Details: ")
        print()
        print("Customer Id: ",self.id)
        print("Customer Name: ",self.name)
        print("Contact : ",self.contact)
        print("Email: ",self.email)
        print("Type Of Cloth: ",self.toc)
        print("Branded or Not?: ",self.branded)
    def calculateCharge(self):
        if self.toc=="Cotton":
            charge=50
        elif self.toc=="Silk":
            charge=30
        elif self.toc=="Woolen":
            charge=90
        elif self.toc=="Polyester":
            charge=20                   
        
        if self.branded==1:
            charge=charge*1.5

        if self.season=="Winter":
            charge=charge/2
        else:
            charge=charge*2
        
        return charge

    def FinalDetails(self):
        self.customerDetails()
        charge1=self.calculateCharge()
        if charge1>=200:
            print("Total Charge: ",charge1)
            print("To be returned in 4 Days!")
        else:
            print("Total Charge: ",charge1)
            print("To be returned in 7 Days!")

while True:
    ID+=1
    name=input("Name Of Customer: ")
    con=input("Contact No: ")
    em=input("Email: ")
    toc=input("Type Of Cloth: ")
    brand=input("Branded? 0:No , 1:Yes :")
    season=input("Season: ")

    cs=LaundaryService(name,con,em,toc,brand,season,ID)


    cs.FinalDetails()

    choice=input("Do you want to enter more? yes/no ")
    if choice=="no":
        break

