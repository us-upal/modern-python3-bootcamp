# print('this block is all-right')
# try:
#     upal
# except NameError as err:
#     print(err)
# print('this block is also all-right') 

try:
    num=int(input('pls enter number>>>'))
except:
    print('thats not a fucking number')
else:
    print(f'ok,you entered {num}')
finally:
    print('this block is run no matter what!')