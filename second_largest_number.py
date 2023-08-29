# 1) Initialize the first as 0(i.e, index of arr[0] element
# 2) Start traversing the array from array[1],
#    a) If the current element in array say arr[i] is greater
#       than first. Then update first and second as,
#       second = first
#       first = arr[i]
#    b) If the current element is in between first and second,
#       then update second to store the value of current variable as
#       second = arr[i]
# 3) Return the value stored in second.


from copy import deepcopy
A = [1,3,6,2,8,10,0,4,7]

b = deepcopy(A)
b.sort()
print(b[-2])
first = second = A[0]

for i in A:
    if i > first:
        second = first
        first = i
print(first, second, )