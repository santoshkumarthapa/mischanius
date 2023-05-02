def append_at_beginning_front(x,l):
    return [x + ele for ele in l]

def bit_string(n):
   
    if n==0: return []
    if n == 1: return ["0", "1"]
    else:
        return (append_at_beginning_front("0", bit_string(n-1))+append_at_beginning_front("1",bit_string(n-1)))
    
print(bit_string(5))