ll = [5, -7, 3,1, -5,-2,9, 10, 12,15]


for ith , value in enumerate(ll):
    for jth, value1 in enumerate( ll[:]):
       if value < 0 and value1 > 0:
           print(value, value1)
           ll[ith], ll[jth] = value1, value
           break
           
print(ll)



def rearrangePosNegWithOrder(arr, size):
	i = 0
	j = 0
	while(j < size):
		if(arr[j] >= 0):
			j += 1
		else:
			for k in range(j,i,-1):
				temp = arr[k]
				arr[k] = arr[k - 1]
				arr[k - 1] = temp
			i += 1
			j += 1
	return arr

# driver code
arr = [5, -7, 3,1, -5,-2,9, 10, 12,15]
size = len(arr)
aux = rearrangePosNegWithOrder(arr, size)
for i in aux:
	print(i,end=" ")

# This code is contributed by Vibhu Karnwal
