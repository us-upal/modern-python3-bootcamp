import random as rm

def flip_coin():
    a=rm.randint(0,1)
    if a==0:
        print('head')
    print('tales')

def is_odd(n):
    if n%2 == 0 : 
        return False
    return True

#default parameter
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def math(a,b,fn=sub):  #here sub is not invoked but used so there is no parenthesis.
    return fn(a,b)

print(math(1,2))

flip_coin() #function invoked
print(is_odd(5 ))