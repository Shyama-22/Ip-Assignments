def get_key(val,my_dict):
    for key, value in my_dict.items():
         if val == value:
             return key
 
    return "key doesn't exist"

def find_Major(val1):
    d={1:'C', 2:'C#', 3:'D', 4:'D#', 5:'E' , 6:'F',7:'F#' ,8:'G' ,9:'G#' ,10:'A',11:'A#',12:'B',13:"C'"}
    
    major_scale="WWHWWWH"
    
    ans=val1
    key1=get_key(val1,d)            
    for i in range(7):
        
        if major_scale[i]=='W':
            key1+=2
        elif major_scale[i]=="H":
            key1+=1
        if key1==13:
            ans+=" "+d[key1]    
        else:
            ans+=" "+d[key1%13]
    return ans

def find_Minor(val1):
    d={1:'C', 2:'C#', 3:'D', 4:'D#', 5:'E' , 6:'F',7:'F#' ,8:'G' ,9:'G#' ,10:'A',11:'A#',12:'B',13:"C'"}
    
    
    minor_scale="WHWWHWW"
    ans=val1
    key1=get_key(val1,d)
    for i in range(7):         
        
        if minor_scale[i]=='W':
            key1+=2
        elif minor_scale[i]=="H":
            key1+=1
        if key1==13:
            ans+=" "+d[key1]    
        else:
            ans+=" "+d[key1%13]
    return ans

def noteCreate():
    d={1:'C', 2:'C#', 3:'D', 4:'D#', 5:'E' , 6:'F',7:'F#' ,8:'G' ,9:'G#' ,10:'A',11:'A#',12:'B'}
    f=open('scalemajor.txt','w')
    for i in d.values():
        f.write(find_Major(i) + '\n')

    f.close()    
    f=open('scaleminor.txt','w')
    for i in d.values():
        f.write(find_Minor(i) + '\n')
    f.close()    

def majorNotes(root):
    
    f=open('scalemajor.txt','r')
    for i in f:
        if i[0]==root:
            print('Major Scale In The Key Of ',root,' is:')
            print(i)
            break
    f.close()

def minorNotes(root):
    f=open('scaleminor.txt','r')
    for i in f:
        if i[0]==root:
            print('Minor Scale In the key Of ',root,' is:')
            print(i)
            break
    f.close()


noteCreate()
while True:
    key=input("Enter the root note: ")
    scale=input("Enter the type of scale (Major/Minor): ")
    if scale=="Major":
        majorNotes(key)
    else:
        minorNotes(key)

    ch=input("Do you want to exit? (yes/no)")
    if ch=="yes":
        break
            

