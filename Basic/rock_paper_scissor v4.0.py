

import random as rn
p2=None

print('***rock***')
print('***paper***')
print('***scissor***')
player_wins=0
com_wins=0

number=rn.randint(1, 3)
while player_wins <2 and com_wins < 2: 
    print(f'=====[player ={player_wins}]====||====[computer={com_wins}]====================')  
    if(number == 1):
        p2='rock'
        print('Computer      :'+p2)
    elif(number == 2):
        p2='paper'
        print('Computer      :'+p2)
    elif(number ==3):
        p2='scissor'

        print('Computer      :'+p2)

    p1=input('Enter Player 1:')

    if(p1 == 'rock' or p1 == 'paper' or p1 == 'scissor'):
            
        
        
        if(p1 == 'rock'):
            if(p2 == 'seissor'):
                print("you wins")
                player_wins += 1
            if(p2 == 'paper'):
                print('computer wins')
                com_wins += 1
                
                
        elif(p1 == 'scissor'):
            if(p2 == 'rock'):
                print("computer wins")
                com_wins += 1
            if(p2 == 'paper'):
                print('you wins')
                player_wins += 1
                
                
        elif(p1 == 'paper'):
            if(p2 == 'seissor'):
                print("computer wins")
                com_wins += 1
            if(p2 == 'rock'):
                print('you wins')
                player_wins += 1
                
        if(p1==p2):
            print('draw!')
    else:
        print('wrong input')
    print('=================================')    




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



