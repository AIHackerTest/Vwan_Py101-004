
import random
from random import randint
import profile

def generate_random_r2():
    while True:
        num = random.sample(range(0,9),4)
        if (num[0] == 0):
            continue
        else:
            num = "".join(str(x) for x in num)
            break
    return num

def generate_random_r1():
    while True:
        num = randint(1000,9999)
        numlist = [int(i) for i in str(num)]
        if (len(set(numlist)) )>=4:
            break
    return num

from timeit import timeit
t1=timeit(generate_random_r1,number=1000)
t2=timeit(generate_random_r2,number=1000)
print (f"R1 duration:{t1}")
print (f"R2 duration:{t2}")

import cProfile
cProfile.run("generate_random_r1()")
cProfile.run("generate_random_r2()")

"""
below is commented, because the duration returned seemed quite long than actual, not sure why yet
"""
# if __name__ == '__main__':
#     from timeit import Timer
#     t1 = Timer("generate_random_r1()", setup="from __main__ import generate_random_r1")
#     print (f"R1 duration: {t1.timeit()}")
#     import profile
#     print (profile.run("generate_random_r1()"))
