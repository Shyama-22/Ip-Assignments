initial_cost=int(input("ENTER INITIAL COST: "))
dep_rate=int(input("Enter depreciation rate: "))
val_perkm=50
dist=6000
maintain_cost=initial_cost*(0.01)
loss=0
profit=0                                                   
val_eachyear=initial_cost
year=0
for i in range(1,16):
    if i>1:
        val_perkm+=val_perkm*(0.1) 
    if i>5:
        maintain_cost=maintain_cost+maintain_cost*(0.5)
    
    val_eachyear-=val_eachyear*(dep_rate/100) 
    profit=val_perkm*dist
    loss+=maintain_cost                          
    
    if val_eachyear-loss<profit:
        break
    year+=1
       
print(year-1,"( you sell the car after ",year-1," years )")        
                