

def f2(func):
    print('Hello')
    return func

@f2
def f1():
    print(1+2)

# f2(f1)
#
# f1 = f2(f1)
# print(f1)

f1()
