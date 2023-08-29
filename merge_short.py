# Merge short is one of the most optimized algorith to sort the array
# It work on  the concept of devide and concord 
# It will devide the array in to 2 untill and unless we have lenth of array is one 
# Once we have devided the array then we have to merge the array while comparing the element 

def merge_short(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_short(left)
        merge_short(right)
        # once we have lenth of left or right < 1 then below code execute 
        i = j = k = 0
        # count i is for  left array
        # count j in for right array
        # count k is for main array where we have to assign the sorted value          
        
        while i < len(left) and  j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i = i+1
            else:
                arr[k] =right[j]
                j = j+1
            k = k+1
        
        # store left over element in the arra 
        # what if we have 10 element then half will 5 and then again half will be 4 and 3 then
        # we are stoing last element in the array
        while i < len(left):
            arr[k] = left[i]
            i = i+1
            k = k+1
        while j < len(right):
            arr[k] = right[j]
            j = j+1
            k = k+1        
A = [1,3,6,2,8,10,0,4,7]

merge_short(A)
print(A)    