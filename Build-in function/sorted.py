# #sorted

# nums=[3,2,1]
# print(sorted(nums))
# print(nums)
import math
songs=[
    {'title': 'dusty blue','playcount':24},
    {'title': 'love and hate','playcount':15},
    {'title': 'I rather dance with you','playcount':98},
    {'title': 'money money1','playcount':100}
]
print(sorted(songs,key=lambda s:s['playcount']))

print(abs(-2.5)) 

print(math.fabs(-2))