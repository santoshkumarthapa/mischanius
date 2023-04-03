# find a pair of digit where sum of 2 number is present in the array
#Example n = 8 
#         list = [1,2,3,4,5,6,7,8]
#         op = [[1,7], [2,7], [3,5]]

# find a index of pair of digit where sum of 2 number is present in the array
#Example n = 8 
#         list = [1,2,3,4,5,6,7,8]
#         op = [[0,6], [1,5], [2,4],(1,8),(5,9)]


x = 8
arr = [1,2,3,4,5,6,7,8,6,2]
final = []
Dict = {}
for i, y in enumerate(arr):
    if x-y in arr and x/y!=2:
        if i<len(arr)//2-1:
           Dict[(y,x-y)]=1
           final.append([y,x-y])
        else:
            Dict[(x-y, y)]=1
            final.append([x-y, y])
print(Dict.keys())
dd = {}
for i in range(len(arr)):
    if x-arr[i] in arr and x/arr[i]!=2:
        if i<len(arr)//2-1:
           dd[(i,arr.index(x-arr[i]))] =1
        else:
            dd[(arr.index(x-arr[i]),i)] =1
print(dd.keys())