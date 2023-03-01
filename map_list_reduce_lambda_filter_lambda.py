# Example of Lambda
ll = lambda x: x*x
print(ll(2))

# Example of Map
map_object = map(ll, range(10))
print(list(map_object))

filter_object = filter(lambda x:x%2==0, range(10))
print(list(filter_object))


def call(func):

    def inner(*args, **kwargs):
        func(*args, **kwargs)
    return inner

@call
def calling_function(*args, **kwargs):
     print(args)

print(calling_function(range(10)))   




ll = [2,3,4,5,6,10,8,7,9]
sumof = 12
add = []
add1 = []
for i in ll[:len(ll)//2]:
    if sumof-i in ll:
        add.append([i, sumof-i])

for i in ll:
    if sumof-i in ll:
        add1.append([i, sumof-i])
print(add)
print(add1)


from collections import Counter
d1 = {'key1': 50, 'key2': 100, 'key3':200}
d2 = {'key1': 200, 'key2': 100, 'key4':300}
new_dict = Counter(d1) + Counter(d2)
print(new_dict)



ll = [1,2]

pp = [x+1 if x%2==0 else 'dev' for x in ll]
print(pp)