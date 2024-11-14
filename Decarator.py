def fun(a, b):
    return a / b

def dec(fun):
    def inner(a, b):
        if a > b:
            a, b = b, a
        return fun(a, b)
    return inner

fun = dec(fun)
print(fun(2, 4))

# The inner function, in this code, returns the result of calling fun(a, b).

# Here's a breakdown:

# Decorator Function (dec): The dec function is a decorator that takes a function fun as an argument and returns the inner function.

# Inner Function (inner):

# Inside inner, it checks if a > b. If true, it swaps a and b to ensure a is always less than or equal to b.
# Then, it calls the original function fun with the (potentially swapped) values of a and b.
# Return Value: The inner function returns the result of fun(a, b), which in this case is a / b.