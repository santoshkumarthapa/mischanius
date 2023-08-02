# THOSE NUMBERS WHICH SUM OF THE CUBE OF ITS DIGITS IS EQUAL TO THAT NUMBER ARE KNOWN AS ARMSTRONG NUMBERS. FOR EXAMPLE 153 SINCE 1^3 + 5^3 + 3^3 = 1+ 125 + 9 =153
# OTHER ARMSTRONG NUMBERS: 370,371,407 ETC.
# IN GENERAL DEFINITION:
# THOSE NUMBERS WHICH SUM OF ITS DIGITS TO POWER OF NUMBER OF ITS DIGITS IS EQUAL TO THAT NUMBER ARE KNOWN AS ARMSTRONG NUMBERS.
# EXAMPLE 1: 153
# TOTAL DIGITS IN 153 IS 3
# AND 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# Example 2: 1634
# Total digits in 1634 is 4
# And 1^4 + 6^4 + 3^4 +4^4 = 1 + 1296 + 81 + 64 =1634
# Examples of Armstrong numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834, 1741725

def find_length(n):
    i=0
    while n!=0:
       n = n//10
       i+=1
    return i

def is_armstrong(n):
    length = find_length(n)
    sum = 0
    i = 0
    m=n
    temp = 0
    while n!=0:
        temp = n%10
        n = n//10
        ll = 0 
        for i in range(length):
            temp =temp*temp
            ll+=temp
            #print(ll)
        sum+=ll
    if sum==m:
        print(f'{n} is armstrong number') 
is_armstrong(153)