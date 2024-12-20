def fun(a,b):
    return a/b 
# @decorator
def decoratorFun(fun):
    def inner(a,b):
        if a<b:
            a,b=b,a 
        return fun(a,b)
    return inner

func=decoratorFun(fun)
print(func(3,4))
            