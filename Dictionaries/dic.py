#=============CREATING DICTIONARY==========================
student=dict(name='upal',
            id='1821359',
            dept='ece')
#print(student)
#=============ACCESSING DICTIONARY==========================
#print(student['name']) #thats not variable its string

#=============ITERATING DICTIONARY==========================
for i in student.values():
    print(i)
#===========================================================
for j in student.keys():
    print(j)
print(student.items()) #dict_items.... returns tuples

for k,v in student.items():
    print(f'key is {k} & value is {v}') #nice gesture


a='relationship status' in student
print(a) #falsen|| cheaks keys 

b='single' in student.values()
print(b)
#=============waiting DICT method==========================
num=dict(one=1,two=2,three=3)
print(num)
num1=num.copy()
num.clear()
print(num)
print(num1)

xxx={}.fromkeys(['pornstar:'],['Romi rain'])
print(xxx.get('pornstar'))

print(student.get('name')) 
#============POP items and update==========================
student.pop('dept')
print(student)
#updating
st=dict(dept='ece',
        contact='01705933999')
student.update(st)
print(student)
#override
st=dict(dept='cse')
student.update(st)
print(student)

