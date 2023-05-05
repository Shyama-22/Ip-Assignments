class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
    def object_info(self):
        print(self.firstname," ",self.lastname," ",self.age)
    def __repr__(self):
        return '{' + self.firstname + ', ' + self.lastname + ', ' + str(self.age) + '}'


def sort_attribute(query):
    if query=="firstname":
        lst.sort(key=lambda x: x.firstname)
        print()
        print("Order: ")
        for obj in lst:
            print(obj.firstname," ",obj.lastname," ",obj.age)
    elif query=="lastname":
        lst.sort(key=lambda x: x.lastname)
        print()
        print("Order: ")
        for obj in lst:
            print(obj.firstname," ",obj.lastname," ",obj.age)        
    elif query=="age":
        lst.sort(key=lambda x: x.age)
        print()
        print("Order: ")
        for obj in lst:
            print(obj.firstname," ",obj.lastname," ",obj.age)
        

while True:
    print("Welcome to the application :)")
    n=int(input("Specify Number Of People to be enrolled: "))
    lst=[]
    for i in range(n):
        fname=input("Enter Firstname for Person  : ")
        lname=input("Enter Lastname for Person : ")
        age=int(input("Enter Age for Person : "))
        obj=Person(fname,lname,age)
        lst.append(obj)


    q=int(input("Specify Number Of Queries: "))
    for i in range(q):
        query=input("Query : ")
        sort_attribute(query)

    choice1=input("Thanks for using the Application, if you wish to restart, press “Y” else press “N” to exit:")
    if choice1=="N":
        print("Exits!")
        break    