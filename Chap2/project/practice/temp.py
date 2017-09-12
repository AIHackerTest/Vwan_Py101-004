from functools import reduce
d = {"a":[{"b":{"c":"winning!"}}]}
k = "a.b.c"
import operator
keys = "a.b.c".split(".")
lastplace = reduce(operator.getitem, keys, d)
print(lastplace)
