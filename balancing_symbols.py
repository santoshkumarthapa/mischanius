# balance the symbol 
# input ()(()[()]), {{([][])})}
# push if bracket is open
# pop if test close bracket and A[i] matches yes

def is_symbol_balance(symbols):
    flag = False
    count = 0
    for symbol in symbols:
        if symbol in ['(', '{', '[']:
            count+=1
        else:
            count-=1

    if count==0:
        flag=True        
        
    return flag

print(is_symbol_balance('()()))'))
