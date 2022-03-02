#use all logical operator
a = 5
b = 2
c = 3

print(a>b and a>c)
print(a<b and a<c)
print(a<b and a>c)


a = 5
b = 2
c = 100

print(a>b and c)


a = 8
b = 5
c = 6


print(a>b or a>c)
print(a<c or a<b)
print(a>b or a<c)


a = 10
b = 5

print(not(a>b))
print(not(a<b))

