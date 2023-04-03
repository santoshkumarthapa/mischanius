# example 1234 -> 1+2+3+4 = 9

def sum_of_own_digit(n):
    sum = 0
    while n!=0:
        temp = n%10
        sum+=temp
        n = n//10
    return sum
print(sum_of_own_digit(567))