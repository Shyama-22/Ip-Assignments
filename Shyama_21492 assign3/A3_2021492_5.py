class Student:
    isPlaced=False
    def __init__(self,name,cgpa,branch):
        self.name=name
        self.cgpa=cgpa
        self.branch=branch
    def getsPlaced(self):
        self.isPlaced=True
    def __repr__(self):
        return '{' + self.name + ', ' + self.cgpa + ', ' + self.branch + '}'    
    def apply(self,obj):
        if self.isPlaced==False and self.isEligible(obj,1)==True:
            obj.appliedStudents.append(self)

    def isEligible(self,objc,ans):
        flag=False
        if self.cgpa>=objc.reqcgpa:
            if self.isPlaced==False:
                for b in objc.branches:
                    if b==self.branch:
                        flag=True
                        if ans==0:
                            print("Student ",self.name," is eligible for Company ",objc.name)
                        return True
        if flag==False:
            if ans==0:
                print("Student ",self.name," is not eligible for Company ",objc.name)
            return False
class Company:
    appliedStudents=[]
    applicationsopen=True
    def __init__(self,name,reqcgpa,branches,pos_open):
        self.name=name
        self.reqcgpa=reqcgpa
        self.branches=branches
        self.pos_open=pos_open
    def CloseApplication(self):
        self.applicationsopen=False
        
    def hireStudents(self):
        self.appliedStudents.sort(key=lambda x: x.cgpa,reverse=True)
        print()
        print("Order: ")
        count=0
        for objs in self.appliedStudents:
            if self.applicationsopen==True:
                if objs.isEligible(self,1)==True:
                    print(objs.name)
                    objs.getsPlaced()
                    count+=1
                    if count==self.pos_open:
                        self.CloseApplication()
        
           
        print("The Company Has Hired: ",count)

print("Enter Number Of students ")
n=int(input())
objlst=[]

for i in range(n):
    
    print("Enter Name Of Student ",i+1)
    name=input()
    print("Enter Cgpa OF Student ",i+1)
    cgpa=float(input())
    print("Enter Branch OF Student ",i+1)
    branch=input()
    obj=Student(name,cgpa,branch)
    objlst.append(obj)

print("Enter Number OF Companies")
n1=int(input())
objlst2=[]

for i in range(n1):

    print("Name Of Company ",i+1)
    cname=input()
    print("Enter Required Cgpa for Company ",i+1)
    reqcgpa=float(input())
    print("Enter Space Separated Branches for Company ",i+1)
    brlst=[ i for i in input().split()]
    print("Enter No of Positions Open for Company ",i+1)
    nps=int(input())
    companyobj=Company(cname,reqcgpa,brlst,nps)
    
    for sobj in objlst:
        if sobj.isEligible(companyobj,0)==True:
            sobj.apply(companyobj)
    companyobj.hireStudents()

       