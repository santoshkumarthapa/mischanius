# Input: N = 1500 
# Output: Perfect square = 1521, Steps = 21 
# For N = 1500 
# Closest perfect square greater than N is 1521. 
# So steps required is 21. 
# Closest perfect square less than N is 1444. 
# So steps required is 56. 
# The minimum of these two is 1521 with steps 21.

# If N is a perfect square then print N and steps as 0.
# Else, find the first perfect square number > N and note its difference with N.
# Then, find the first perfect square number < N and note its difference with N.
# And print the perfect square resulting in the minimum of these two differences obtained and also the difference as the minimum steps.
number =1500
sqrt = 1500//2
max = 0
min = 0

for i in range(sqrt):
    if i*i <=number:
        max=i*i

for i in range(sqrt):
    if i*i >=number:
        min=i*i
        break

nearest_square =  min-number if number-max > min-number else number-max
print(nearest_square) 




from math import sqrt, floor

def isPerfect(N):
    if (sqrt(N) - floor(sqrt(N)) != 0):
        return False
    return True

print(isPerfect(1501))