print('***rock***')
print('***paper***')
print('***scissor***')

p1=input('Enter Player 1:')

p2=input('Enter Player 2:')

if(p1 == 'rock'):
    if(p2 == 'seissor'):
        print("p1 wins")
    if(p2 == 'paper'):
        print('p2 wins')
        
if(p1 == 'scissor'):
    if(p2 == 'rock'):
        print("p2 wins")
    if(p2 == 'paper'):
        print('p1 wins')
        
if(p1 == 'paper'):
    if(p2 == 'seissor'):
        print("p2 wins")
    if(p2 == 'rock'):
        print('p1 wins')
elif(p1==p2):
    print('draw!')
if(p1 !=('rock' or 'paper' or 'scissor')):
    print('Wrong input')


# =============================================================================
# if(p1 == 'rock'  and p2 == 'scissor'):
#     print('p1 wins!!')
# elif(p1 == 'rock'  and p2 == 'paper'):
#     print('p2 wins!!')
# elif(p1 == 'scissor'  and p2 == 'rock'):
#     print('p2 wins!!')
# elif(p1 == 'scissor'  and p2 == 'paper'):
#     print('p1 wins!!')
# elif(p1 == 'paper'  and p2 == 'scissor'):
#     print('p2 wins!!')
# elif(p1 == 'paper'  and p2 == 'rock'):
#     print('p1 wins!!')
# #elif((p1 and p2)==('rock' or 'paper' or 'scissor')):
# elif(p1==p2):
#     print(' oops! draw')
# else:
#     print('You Entered Wrong!')    
# =============================================================================
