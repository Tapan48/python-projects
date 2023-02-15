import random





player=input("enter your name:")

## 1:rock
## 2: paper
## 3: scissor
##  (11) (22) (33) (1,2) (1,3) (2,1) (2,3) (3,1) (3,2) 

playerpoint=0
cmpoint=0

for i in range(3):
    
    playermove=random.randint(1,3)
    
    computermove=random.randint(1,3)
    
    
    if playermove==computermove:
        
        continue
    
    
    elif playermove==1 and computermove==2:
        cmpoint+=1
        
    
    elif playermove==2 and computermove==1:
        playerpoint+=1
        
    elif playermove==1 and computermove==3:
        
        playerpoint+=1
        
        
    elif playermove==3 and computermove==1:
        
        cmpoint+=1
        
        
    elif playermove==2 and computermove==3:
        cmpoint+=1
        
        
        
    elif playermove==3 and computermove==2:   
        
        playerpoint+=1  
        
        
if playerpoint==cmpoint:
    print("its a draw")
    
elif playerpoint>cmpoint: 
    print(f"congratulations {player} you won the game ")
    
    
else:
    print("computer won the game")       
                          
        
        
    
    
    
        
        
        
    
    
    
    







