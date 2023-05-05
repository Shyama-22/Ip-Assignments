def SWC(ans):
    f=open('question1_input.txt','r')
    
    count=0
    for line in f:
        for word in line.split():
            if(word==ans):
                count+=1
    
    f.close()
    return count

def AUW():
    f=open('question1_input.txt','r')
    unique = []
    for line in f:
        for word in line.split():
            if word not in unique:
                unique.append(word)

    for word in unique:
        print(word,end=" ; ")
    f.close()    
                     
             
def AWC():
    f=open('question1_input.txt','r')
    d = {}
    for line in f:
        for word in line.split():
            if word not in d.keys():     
                x=SWC(word)
                
                d[word]=x
    print("WORD COUNTS: ")
    for i in d:
        print(i," : ",d[i])
    f.close()    

def RW():
    fin = open("question1_input.txt", "rt")
    a=input('Enter the word to be replaced: ')
    b=input('Enter the word that will replace : ')

    data = fin.read()
    
    data = data.replace(" "+a, " "+b)
    
    fin.close()
    
    fin = open("question1_input.txt", "wt")
    
    fin.write(data)
    
    fin.close()
    print('Replaced Successfully')

while(True):
    print('----------------------------------------------------------')
    print('Enter Your Choice')
    print('1. Display specific Word Count')
    print('2. Display all unique words')
    print('3. Display all words count')
    print('4. Replace Word')
    print('5. Quit')
    choice=int(input())
    if choice==1:
        wd=input("ENTER WORD: ")
        x=SWC(wd)
        print('WORD COUNT: ',x)
    elif choice==2:
        AUW()
    elif choice==3:
        AWC()
    elif choice==4:
        RW()    
    elif choice==5:
        break

      
    

