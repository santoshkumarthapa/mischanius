# Perform bubble short

lst = [1,3,6,2,8,10,0,4,7]

for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i] < lst[j]:
            lst[j], lst[i] = lst[i], lst[j]
print(lst)