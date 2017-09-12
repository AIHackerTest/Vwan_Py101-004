def f(*arg,**args):
    if (arg):
        print ("arg:",arg)
    if(args):
        print("args:",args)

d1 = {"11":"a11","12":"a12"}
d2 = {"21":"a21","22":"a22"}
# f(d1)
# f(*d1)
# f(**d1)
# # f(s1=1,s2=2)
# s1="test single arg"
# f(1)
# f([1])
# f(s1)

def foo(*args):
    print (args)
# foo('test1')
# foo(*('arg1', 'arg2'))
# foo(*d1)

def food(**args):
    print (args)
# food('test1') # error
# food(s='test1')
# food(d1) # error
# food(*d1)

def fa(x):
    print("----",x)

a = 'x'
result = fa(**{a:1})
result
