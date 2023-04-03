# A number is called strong number if sum of the factorial of its digit is equal to number itself. For example: 145 since
# 1! + 4! + 5! = 1 + 24 + 120 = 145

def is_strong_number(n):
    sum = 0
    # sum=1
    var1 = n
    while n!=0:
        j = 1
        r = n%10
        for k in range(1,r+1):
           j = j*k
        sum+=j
        n = n//10
    print(sum)
    if sum==var1:
        print("strong number")
    else:
        print("not a string number")
is_strong_number(40585)