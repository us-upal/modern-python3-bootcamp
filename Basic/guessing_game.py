
# handle user guesses
# if they guess correct ,tell them they won
# otherwise tell them if they too high or too low

# Bonus:let player play again if they want.

import random
ran_num=random.randint(1,10)

g=None

while g != ran_num:
    g=int(input('input the number from 1-10:'))
   
    if(g == ran_num):
        print('you won!')
    elif g > ran_num :
        print('too high')
    else:
        print('too low')

print(ran_num)