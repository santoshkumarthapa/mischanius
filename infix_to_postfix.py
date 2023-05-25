exp = "a+b*(c^d-e)^(f+g*h)-i"
exp = 'A+B*C+D'
output = "abcd^e-fgh*+^*+i-"
precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
stack = []
expression = ''

nn = 0

def is_empty(stack):
    return len(stack)==0

def isalpha(i):
    return i.isalpha()

for i in exp:
    if isalpha(i):
        expression+=i
    else:
        if len(stack)==0:
            stack.append(i)
        else:
            while(not is_empty(stack)):
                print(stack)
                temp = stack[-1].strip()
                if precedence[temp]> precedence[i]:
                    print('in')
                    ll = stack.pop()
                    expression+=ll
            
            stack.append(i)
print(expression)
print(stack)