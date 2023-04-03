# Find the largest digit of its own digits

def largest_digit(n):
    max = 1
    while n!=0:
        temp = n%10
        if temp >=max:
            max=temp
            
        n = n//10
    return max

print(largest_digit(145901))