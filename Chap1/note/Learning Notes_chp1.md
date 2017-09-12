## if ```_name__=="__main_"```

To understand this, get familiar with python script execution mechanism first.

When we run a .py script from the command line:

```
c.py

import math
def square(a):
	return math.sqrt(a)
square()
```

```
py scripta.py
```

python will do following things in sequence:

- set module name from "scripta" to be ```__main__```: **IMPORTANT: The interpreter keeps track of which scripts are running with **name**. When you run a script - no matter what you've named it - the interpreter calls it "**main**". That's how it keeps track of which script is the master file, the script that gets ...**
- do import module: **IMPORTANT: ”import module' actually RUNs all the executable operations within the script**
- handle function "square" definition
- run square function

That means, python will run the whole script. 

Then the problem comes when importing the "scripta" module to another script "scriptb". 

when you import scripta in you scriptb script, the whole codes in the scripta.py will be run, while you are simply not expecting that.

To avoid this problem, you can use this "if" statement to make the codes within it ONLY run for the script itself.

```
if __name__ == "__main__":
	square(2)
```

Now, when you import scripta module in scriptb, the square(2) function will be safe not to be picked up.

Now if go back to [29.4. __main__ — Top-level script environment — Python 3.6.2 documentation](https://docs.python.org/3/library/__main__.html), it might be easier to understand what it says about ```__main__```

> # 29.4. [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__) — Top-level script environment
>
> ------
>
> `'__main__'` is the name of the scope in which top-level code executes.A module’s __name__ is set equal to `'__main__'` when read fromstandard input, a script, or from an interactive prompt.
>
> A module can discover whether or not it is running in the main scope bychecking its own `__name__`, which allows a common idiom for conditionallyexecuting code in a module when it is run as a script or with `python-m` but not when it is imported:
>
> ```
> if __name__ == "__main__":
>     # execute only if run as a script
>     main()
>
> ```
>
> For a package, the same effect can be achieved by including a`__main__.py` module, the contents of which will be executed when themodule is run with `-m`.



**Reference**:

[python - What does if __name__ == "__main__": do? - Stack Overflow

[python - What does if __name__ == "__main__": do? - Stack Overflow](https://stackoverflow.com/questions/419163/what-does-if-name-main-do?rq=1)](https://stackoverflow.com/questions/419163/what-does-if-name-main-do?rq=1)

## ```__init__.py```

>[6. Modules — Python 3.6.2 documentation](https://docs.python.org/3/tutorial/modules.html#packages)
>
>The `__init__.py` files are required to make Python treat the directories
>as containing packages; this is done to prevent directories with a common name,
>such as `string`, from unintentionally hiding valid modules that occur later
>on the module search path. In the simplest case, `__init__.py` can just be
>an empty file, but it can also execute initialization code for the package or
>set the `__all__` variable, described later

for example, you have a folder structure as below:

folder_a\scripta.py

folder_b\scriptb.py

and you want to import scripta into scriptb, but the problem is that, folder_a is not a python package, you can not reference it like folder_a.scripta,  to solve it, python allows you to add ```"__init__.py"``` under "folder_a" to make it a package., thus the new folder structure will look like:

folder_a\scripta.py

```folder_a\__init_.py```

folder_b\scriptb.py

```folder_b\__init_.py```

## Run python script from another folder (TBD)

I have e.g. two scripts each under one folder,

bca/bulls_and_cows.py

test/test_bulls_and_cows.py

I'd like to call the first from the one under test folder.

It seems there are several ways to go:

1 modify sys.path in the test script, this works but not look good

```
import sys
sys.path.insert(0,'../.')
```

2 add ```__init__.py``` under test folder

```from bulls_and_cows import bulls_and_cows as bc```

then open a command, navigate to the "bca" folder, (not the "test" folder), run

```
python -m test.test_bulls_and_cows

or pytest
```

folder structure as below, under each folder add a ```__init__.py``` file (can be empty)

- BullsAndCows
  - main.py
  - ```__init__.py```
  - bca/
    - bulls_and_cows.py
    - ```__init__.py```
  - test/
    - local_setings.py
    - ```__init__.py```

# Data Structure

```
>>> a = [1,2]
>>> type(a)
<class 'list'>

>>> a = (1,2)
>>> type(a)
<class 'tuple'>

>>> a = {1,2}
>>> type(a)
<class 'set'>

>>> a = {1:2}
>>> type(a)
<class 'dict'>
```

## Nested Tuple

check if a value is in a nested tuple:

```
>>> commands = (                 
('h','help'),                 
('history'),                 
('exit','quit')                 
)
>>> cmd = "help"
>>> any(cmd == e[1] for e in commands)
True
>>> any(cmd == e[0] for e in commands)
False
```

```
>>> cmd='h'
>>> any(cmd in e for e in commands)
True
```



## List vs Tuple

In python, List is a virable-length array, it is **mutable**,  means you can change the values of its elements.

Tuple however is **immutable**, means values of its elements are not changable. 

```
>>> data_dict = {}
>>> tuple_a = (1,2)
>>> list_a = [1,2]
>>> data_dict[tuple_a] = "Tuple can be used as dictionry key"
>>> data_dict
{(1, 2): 'Tuple can be used as dictionry key'}
>>> data_dict[list_a] = "List cannot be used as dictionry key"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

## list.sort() vs sorted(list)

list.sort() doesn't create a new list, it simply sort the original list in place. Why? This is to save memory space.

sorted(list) however will create a new list which contains the items sorted already.

```
>>> list = [3,2,5,3]
>>> list.sort()
>>> list
[2, 3, 3, 5]

>>> list = [3,2,5,3]
>>> sorted(list)
[2, 3, 3, 5]
>>> list
[3, 2, 5, 3]
```



[Design and History FAQ — Python 3.6.2 documentation](https://docs.python.org/3/faq/design.html)

## dict

dict type is kind of like Map in java, key-value pairs.

its key is immutable, (so tuple can be a key while list cannot), how? A hash code will be generated for each key on process basis, that means, each time a new process starts, the hash code for that key is fixed. **thus dict key should be hashable object**

```
>>> dt = {"name":"test1","age":10}
>>> hash("name")
1239737502
>>> hash("age")
651310108
```

and the hash code varies with keys. These hash codes in the backend are serving to retrieve values from dict, something like the search by index for a list：

```
>>> dt = {"name":"test1","age":10}
>>> dt['name']
'test1'
>>> dt.get('name',"No record found")
'test1'

>>> dt.get('NonExisting',"No record found")
'No record found'
>>> dt['NonExisting']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'NonExisting'
>>>
```

One thing to note: **each time the program runs, retrieving items from a dictionary will show items in different orders**, the reason is, hash code for the same key varies from each program process. In Java there is TreeMap to maintain the sequence, **not sure yet how in python, need to find later**

## Collections

[8.3. collections — High-performance container datatypes — Python 2.7.13 documentation](https://docs.python.org/2/library/collections.html)

# Encoding

when opening a utf-8 file saved with BOM, there are first 3 characters you might want to skip, to skip them, use "uft-8-sig" as encoding:

```
open(self.weather_info_file,"r",624,'utf-8-sig')
```

[7.2. codecs — Codec registry and base classes — Python 3.6.2 documentation](https://docs.python.org/3/library/codecs.html#module-encodings.utf_8_sig)

# # hasattr, getattr 和 callable 方法

from thxiami: 关于如何实现用户指令查询功能，教练提供了另一种思路（详见上方代码），把指令对应的功能封装在实例方法里（），通过hasattr, getattr 和 callable 方法，根据给出的command name 判断实例是否有对应实例方法，有的话就调用，没有就说明时查询天气。这个方法很棒！学习啦！以下为根据教练的思路写的代码：

class User():
def **init**(self):
pass

```
def help(self):
    doc = "Help doc"
    print(doc)

```

```
user = User()

command_input = 'help'

command_func = getattr(user, command_input, None)

if command_func and callable(command_func):

command_func()

else:

... # 调用查询天气的函数

```

运行结果：

```
Help doc
```



# IO

## copy file

```
import shutil
shutil.copy(src,target)
```



# Performance

## try/except or not?

 When doing chap0 task, i was asking which is better to check if the user input number is an integer or not:  try/except or str.isdigit()?

I guess i can conclude that str.isdigit() would be better in this case as per [Design and History FAQ — Python 3.6.2 documentation](https://docs.python.org/3/faq/design.html) simply because **Actually catching an exception is expensive.**

> ## How fast are exceptions?
>
> A try/except block is extremely efficient if no exceptions are raised.  Actually catching an exception is expensive.  In versions of Python prior to 2.0 it was common to use this idiom:
>
> ```
> try:
>     value = mydict[key]
> except KeyError:
>     mydict[key] = getvalue(key)
>     value = mydict[key]
> ```
>
> This only made sense when you expected the dict to have the key almost all the time.  If that wasn’t the case, you coded it like this:
>
> ```
> if key in mydict:
>     value = mydict[key]
> else:
>     value = mydict[key] = getvalue(key)
>
> ```
>
> For this specific case, you could also use `value = dict.setdefault(key,getvalue(key))`, but only if the `getvalue()` call is cheap enough because itis evaluated in all cases.

# Modules

## operator module
we all know about operators like + * - / symbols , in python there are also modules which contain corresponding named operator functions like add(), sub(),mul()
```
>>> from operator import add,sub,mul
>>> add(1,2)
3
>>> sub(2,1)
1
>>> mul(2,3)
6
```

The interesting thing is, in python 3 there is no div() function. Checking the documentation and found that div in python 2 is replaced with truediv and floordiv in python 3.

```
>>> from operator import truediv, floordiv
>>> truediv(3,2)
1.5
>>> floordiv(3,2)
1
```

truediv is the old division format and can be expressed as 3 / 2 

floordiv is rounded, expressed as 3 // 2

```
>>> 3 / 2
1.5
>>> 3 // 2
1
```



## Variable Name and Environment

### Name bindings

in python, variable names binds to value, function etc. and it can rebinds to new value, functions, including even built-in names.

- rebinds to builtin names

```
>>> import math
>>> max(1,2)
2
>>> max = 5
>>> max
5
>>> max(1,2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
```

- multiple names binds to multiple values in a single statement

  ```
  >>> a, b = 1, 2
  >>> a, b
  (1, 2)
  >>> a
  1
  >>> b
  2
  ```

  this makes it very easy to swap two values:

  ```
  >>> a, b = 1, 2
  >>> b, a = a, b
  >>> a
  2
  >>> b
  1
  ```

  but you can not use one of the name for evaluating the other, since it's not defined yet:

  ```
  >>> i, j = 2, i * 2
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  NameError: name 'i' is not defined
  ```

  if defined this way, changing the value of one name doesn't affect other names:

  ```
  >>> a = 2
  >>> b, c = a *2, a *3
  >>> b
  4
  >>> c
  6
  >>> a = 3
  >>> b
  4
  >>> c
  6
  ```

  ## Functions

  ### pure function

  a function that takes some arguments and produce an output, e.g. max(1,2)

  most important, it produces the same output each time it is called

  ### non-pure function

  print is a non-pure function, because beyond its return value ** None**, it also produce additional output,that is what we see it displays on the console.

  ```
  >>> print(print(1),print(2))
  1
  2
  None None
  ```

  expression tree:

  print(print(1),print(2)) -> print			

  ​					-> print(1),print(2)    -> print (1)	-> print 1

  ​									    -> print (2)  -> print 2

  ### function names:

  "sum" is its 本命(intrinsic name), 

  "f" is its bound name

  ```
  >>> def sum (x,y):
  ...     return x+y
  ...
  >>> f = sum
  >>> f(1,2)
  3
  ```

  ### function as abstraction

  funtional abstraction has three attributes:

  - domain: the range of input arguments like x in square function
  - range:  the set of values it returns
  - intent: the relationship it computes between the input and output

  ```
  def square(x):
  	return x * x
  ```

  ​

  ## Reference

  [Get More Out Of Google](http://www.hackcollege.com/blog/2011/11/23/infographic-get-more-out-of-google.html)

  [Search Education – Google](https://www.google.com/intl/en-us/insidesearch/searcheducation/index.html)

  [Cheat Sheet To Using Google Search More Effectively - UltraLinx](https://theultralinx.com/2013/05/cheat-sheet-google-search-effectively/)

  ​


# Git

## revert an uncommitted change

git checkout <filename>

git reset --hard (reset all uncommitted changed, be careful)

## revert a committed change

[git - Revert changes to a file in a commit - Stack Overflow](https://stackoverflow.com/questions/2620775/revert-changes-to-a-file-in-a-commit)