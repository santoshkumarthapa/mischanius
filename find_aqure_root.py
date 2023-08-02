# Find a nearest aqure root of number 
# example 144 O/P 12
#         9   O/P 3
#         8   O/P 2


number = 64
temp =0
sqrt = number//2

#Below code only work for perfect squre root
# while sqrt!=temp:
#     temp = sqrt
#     sqrt =(number//temp+temp)//2
# print("The square root of '%d' is '%f'", number, sqrt)

# this will give nearest squre root < number  
for i in range(2,72):
    if i*i<=number:
        print(i)
