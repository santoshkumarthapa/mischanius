#aaaapppgbbaapbbb ——> a4p3gb2a2pb3

str1 = 'aaaapppgbbaapbbb'
ll = []
p = ''
for j,i in enumerate(str1):
    if not ll:
        ll.append(i)
    else:
        print(j)
        print(ll)
        print(j-2)
        if ll[j-2] == i:
            ll.append(i)
        else:
           p = p+ll[j-1]+str(len(ll)) 
           print(p)
           #ll = []
print(p)
        