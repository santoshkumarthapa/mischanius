# Following steps describe how to convert decimal to binary

# Step 1: Divide the original decimal number by 2
# Step 2: Divide the quotient by 2
# Step 3: Repeat the step 2 until we get quotient equal to zero.

# Equivalent binary number would be remainders of each step in the reverse order.


dec = 35
bin = ''
while dec:
    bin +=str(dec%2)
    dec = dec//2
    print (dec) 
print(bin[::-1])   
    