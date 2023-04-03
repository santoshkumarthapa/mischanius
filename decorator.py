# # Pythin object/function is first order  where we can pass function as variable 
# def outer(x):
#     def inner(y):
#         return x + y
#     return inner

# add_five = outer(5)
# result = add_five(6)
# print(result)  # prints 11


# def greeting(name):
#     def hello():
#         return "Hello, " + name + "!"
#     return hello

# greet = greeting("Atlantis")
# print(greet())  # prints "Hello, Atlantis!"

# # Output: Hello, Atlantis!


# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner


# def ordinary():
#     print("I am ordinary")



def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner


@star
@percent
def printer(msg):
    print(msg)

printer("Hello")