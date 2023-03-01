# Perfect number is a positive number which sum of all positive divisors excluding that number is equal to that number. For example 6 is perfect number since divisor of 6 are 1, 2 and 3.  Sum of its divisor is
# 1 + 2+ 3 =6

# Note: 6 is the smallest perfect number.

# Next perfect number is 28 since 1+ 2 + 4 + 7 + 14 = 28
# Some more perfect numbers: 496, 8128
ll = []
def perfect_number(n):
    sum1 = 0
    i = 1
    while i<n:
        
        if n%i==0:
            sum1 += i
            
        i += 1
    if sum1==n:
       return n
 
for i in range(10000):        
    perfect = perfect_number(i)
    if perfect:
        ll.append(perfect)
print(ll)