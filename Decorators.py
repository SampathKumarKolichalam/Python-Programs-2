#We can change the behaviour of existing function directly using other function.
def div1(a,b):
    print(a/b)
def div2(fun):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return fun(a,b)
    return inner
div1=div2(div1)
div1(2,4)