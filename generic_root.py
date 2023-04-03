# Meaning of generic root:
# It sum of digits of a number unit we don't get a single digit. For example:
# Generic root of 456: 4 + 5 + 6 = 15 since 15 is two digit numbers so 1 + 5 = 6
# So, generic root of 456 = 6

# use 2 while loop first for out loop where we check total of inner loop

def generic_root(n):
    sum = 0
    while n>=10:
        while n!=0:
            temp = n%10
            sum+=temp
            n = n//10
        if sum>=10:
            n=sum
            sum=0
        else:
            break
    return sum
print(generic_root(731))
            