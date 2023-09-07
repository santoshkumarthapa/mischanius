#create a decorator from scrach



def outer_fun(fun, ll):
    
    def inner(a):
        print(a, ll)
        return fun()
    return inner

@outer_fun
def decor():
    print("decode function")    
    
#decor = outer_fun(decor, [1,2])

decor( [1,2], 10)
        