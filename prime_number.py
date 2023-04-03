# A natural number greater than one has not any other divisors except 1 and itself. In other word we can say which has only two divisors 1 and number itself. For example: 5

# Their divisors are 1 and 5.

def is_prime(n):
    count = 0
    if n == 1:
        return True
    for i in range(2, n):
        if n%i==0:
            count+=1
            break
    if count==0:
        return True
    else:
        return False
print(is_prime(7))




