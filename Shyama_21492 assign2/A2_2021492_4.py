
f=open('Admin\RegisteredStudents.txt','r')
list=[]
i=0
for line in f:
    w1=""                            
    i=0
    for word in line.strip().split():
        if i==0:
            w1+=word+"_"
        else:
            w1+=word
        i+=1    
        
    
    list.append(w1)    
f.close()
f=open('Admin\AnswerKey.txt','r')
list1=[]
for line in f:
    list1.append(line.strip())

f.close()
lst3=[]
for i in range(0,20):
    temp=str(i+1)+" "+"-"
    lst3.append(temp)
                                
for name in list:
    f=open(' Student\ '.strip()+name+ r'.txt','r')
    list2=[]
    for line in f:
        list2.append(line.strip())
        
    ct=0
    na=0

    for i in range(0,20):
        
        
        if list1[i]==list2[i]:
            ct+=1
        elif list2[i]==lst3[i]:
            na+=1
          
    f.close()                        
    score=ct*4-(20-na-ct)
    a,b=name.split("_")
    final_ans=str(a)+" "+str(b)+" "+str(score)+"\n"
    f=open('Admin\FinalReport.txt','a')
    
    f.writelines(final_ans)
    f.close()
              
    
    


    

          
  
   
        
            