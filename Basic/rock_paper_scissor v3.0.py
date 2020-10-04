

import random as rn
p2=None

print('***rock***')
print('***paper***')
print('***scissor***')

number=rn.randint(1, 3)
    
if(number == 1):
    p2='rock'
    print('Computer      :'+p2)
elif(number == 2):
    p2='paper'
    print('Computer      :'+p2)
elif(number ==3):
    p2='scissor' np.array[]

    print('Computer      :'+p2)

p1=input('Enter Player 1:')

if(p1 == 'rock' or p1 == 'paper' or p1 == 'scissor'):
         
    
    
    if(p1 == 'rock'):
        if(p2 == 'seissor'):
            print("p1 wins")
        if(p2 == 'paper'):
            print('p2 wins')
            
            
    elif(p1 == 'scissor'):
        if(p2 == 'rock'):
            print("p2 wins")
        if(p2 == 'paper'):
            print('p1 wins')
            
            
    elif(p1 == 'paper'):
        if(p2 == 'seissor'):
            print("p2 wins")
        if(p2 == 'rock'):
            print('p1 wins')
            
    if(p1==p2):
        print('draw!')
else:
    print('wrong input')
    
    




# =============================================================================
# if(p1 == 'rock'):
#     if(p2 == 'seissor'):
#         print("p1 wins")
#     if(p2 == 'paper'):
#         print('p2 wins')
#         
#         
# elif(p1 == 'scissor'):
#     if(p2 == 'rock'):
#         print("p2 wins")
#     if(p2 == 'paper'):
#         print('p1 wins')
#         
#         
# elif(p1 == 'paper'):
#     if(p2 == 'seissor'):
#         print("p2 wins")
#     if(p2 == 'rock'):
#         print('p1 wins')
#         
# if(p1==p2):
#     print('draw!')
# =============================================================================



