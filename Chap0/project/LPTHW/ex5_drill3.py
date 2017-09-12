import math
import datetime

name="test"
pwd="password"

print (('My name is {0}').format(name))

print (('My name is {0},pwd is {1}').format (name,pwd))

print (('the value of pi is %5.3f') % math.pi)

print (('the value of pi is %r') % math.pi)

d = datetime.date.today()
print (('date is %r：') % d)
print (('date is %s:')  % d)
