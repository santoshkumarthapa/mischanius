x1 = 100050
y1 = 100050
x2 = 'Hello'
y2 = 'Hello'
x3 = (1,2,3,4)
y3 = (1,2,3,4)
x4 = (1,2,3,4)
y4 = (1,2,3,4)

print(id(x1), id(y1))
print(x1 is  y1)  # prints False

print(id(x2), id(y2))
print(x2 is y2)  # prints True


print(id(x3), id(y3))
print(x3 is y3)  # prints False
print(x3 == y3)


print(id(x4), id(y4))
print(x4 is y4)  # prints False
print(x4 == y4)