# num=zip([1,2,3],['one','two','three'])

# print(dict(num))
# #{1: 'one', 2: 'two', 3: 'three'}

# print(list(num))
# # [(1, 'one'), (2, 'two'), (3, 'three')]

num2=[(1, 'one'), (2, 'two'), (3, 'three')]
print(list(zip(*num2)))
#[(1, 2, 3), ('one', 'two', 'three')]
 
mid=[90,80,70]
final=[91,81,71]
students=['udyan','saha','upal']

final_grades=[max(pair) for pair in zip(mid,final)]

print(final_grades)