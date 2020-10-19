number=dict(first=1,second=2,thrird=3)
print(number)
sq={key:value **2 for key,value in number.items()}
print(sq)

str1='abc'
str2='123'

combo={str1[i]:str2[i] for i in range (0,len(str1))}
print(combo)

s='ABCDE'
ss='abcde'
combo2={s[i]:ss[i] for i in range(0,len(s))}
print(combo2)

#with conditional
num=[0,1,2,3,4,5,6,7,8,9,10]
num={i:('even' if i%2==0 else 'odd') for i in num}
print(num)