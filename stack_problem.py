Input = "xxy"
# output = "y"
Input = 'yy'
# output = ''
Input = 'xyyxzzzy'
# output= 'xxzy'

# The best suited solution is to use stack and push if there is no matching ele in the top of stack and pop if there any
# unimplemented 
stack = [] 

for i in Input:
    if stack:
        if i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    else:
        stack.append(i)
print(stack)