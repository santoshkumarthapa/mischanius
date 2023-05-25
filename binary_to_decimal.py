# algo
# 1*4^1 + 1*4^0 + 1*4^0 + 3*3^0 + 1*2^1 + 1*1^1
bin= '100011'
32,16,8,4,2,1
32+0+0+0+2+1
dec = 0
for p,i in enumerate(bin[::-1]):
    dec += int(i)*(2**p)
print(dec)