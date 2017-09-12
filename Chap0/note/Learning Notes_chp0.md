## Python的哲学

以此magic开头，打开终端，输入"import this"，学习Python的哲学：

```
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## Help

### pydoc，help and docstring

之前一直不喜欢看到官方推荐docstring放到function definition里面，看了文档才明白，原来是为了统一，以便生成pydoc 帮助, 如果硬性挪到外面的话，生成的Pydoc就失去意义了。（虽然如此，但还是不喜欢放在里面，看起来好别扭，离body那么远，还是喜欢java那种）

```
def play(self,num_of_trials):
    """
    Play the Game
    """
    return 1
```

生成的pydoc是这样的：

```
λ pydoc temp
Help on module temp:

NAME
    temp

FILE
    c:\users\vivia\onedrive\projects\openmind\py101-004-vwan\py101-004\chap0\project\bullsandcows\bca\temp.py

FUNCTIONS
    play(self, num_of_trials)
        Play the Game
```

如果把docstring放到外面，

```
"""
Play the Game

"""
def play(self,num_of_trials):

    return 1
```

pydoc则是这样的，显然docstring没啥作用

```
λ pydoc temp
Help on module temp:

NAME
    temp - Play the Game

FILE
    c:\users\vivia\onedrive\projects\openmind\py101-004-vwan\py101-004\chap0\project\bullsandcows\bca\temp.py

FUNCTIONS
    play(self, num_of_trials)
```



### pydoc not recognized issue

not sure why but if i manually type "pydoc" outside the python interpreter, it now says "Not recognized command", 

Solution:

```
py -m pydoc
```



## Python环境

### Python Version

2.7 or 3.6

### IDE/Editor

Atom

sublime

Anaconda

As you like...

### Console

Windows: [cmderdev/cmder: Lovely console emulator package for Windows](https://github.com/cmderdev/cmder), powershell(windows built-in)

Mac: iTerm2

### Notebook

[Jupyter](http://jupyter.org/install.html)

### Multiple Python 环境

You can install different versions of Python on same machine, by means of ;

- Anaconda: GUI界面切换
- [pyenv for mac](https://github.com/pyenv/pyenv), pywin(windows)，[python3.6自带的Python Launcher for Windows]([3. Using Python on Windows — Python 3.6.2 documentation](https://docs.python.org/3/using/windows.html#python-launcher-for-windows))
- virtualenv: switch between virtual python environments for same python version

#### Windows：

python3.6自带的Python Launcher for Windows:

run "py" from the console, by default python 3.6 is used.

```
PS C:\Users\vivia> py
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

If you want to switch to python 2.7, simply run "py -2.7"

```
PS C:\Users\vivia> py -2.7
Python 2.7.13 |Anaconda 4.3.1 (64-bit)| (default, Dec 19 2016, 13:29:36) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
>>>
```

[pywin](): however failed "pip install pywin", Need to check later. :
```
PS C:\Users\vivia> pip install pywin
Collecting pywin
  Downloading pywin-0.3.1.zip
    Complete output from command python setup.py egg_info:
    Downloading http://pypi.python.org/packages/source/d/distribute/distribute-0.6.35.tar.gz
    Extracting in c:\users\vivia\appdata\local\temp\tmpftwtve
    Now working in c:\users\vivia\appdata\local\temp\tmpftwtve\distribute-0.6.35
    Building a Distribute egg in c:\users\vivia\appdata\local\temp\pip-build-ggvj6m\pywin
    Traceback (most recent call last):
      File "setup.py", line 248, in <module>
        scripts = scripts,
      File "c:\python\python27\lib\distutils\core.py", line 111, in setup
        _setup_distribution = dist = klass(attrs)
      File "c:\users\vivia\appdata\local\temp\tmpftwtve\distribute-0.6.35\setuptools\dist.py", line 225, in __init__
        _Distribution.__init__(self,attrs)
      File "c:\python\python27\lib\distutils\dist.py", line 287, in __init__
        self.finalize_options()
      File "c:\users\vivia\appdata\local\temp\tmpftwtve\distribute-0.6.35\setuptools\dist.py", line 257, in finalize_opt
ions
        ep.require(installer=self.fetch_build_egg)
      File "c:\users\vivia\appdata\local\temp\tmpftwtve\distribute-0.6.35\pkg_resources.py", line 2027, in require
        working_set.resolve(self.dist.requires(self.extras),env,installer))
      File "c:\users\vivia\appdata\local\temp\tmpftwtve\distribute-0.6.35\pkg_resources.py", line 2237, in requires
        dm = self._dep_map
      File "c:\users\vivia\appdata\local\temp\tmpftwtve\distribute-0.6.35\pkg_resources.py", line 2466, in _dep_map
        self.__dep_map = self._compute_dependencies()
      File "c:\users\vivia\appdata\local\temp\tmpftwtve\distribute-0.6.35\pkg_resources.py", line 2499, in _compute_depe
ndencies
        common = frozenset(reqs_for_extra(None))
      File "c:\users\vivia\appdata\local\temp\tmpftwtve\distribute-0.6.35\pkg_resources.py", line 2496, in reqs_for_extr
a
        if req.marker_fn(override={'extra':extra}):
      File "c:\users\vivia\appdata\local\temp\tmpftwtve\distribute-0.6.35\_markerlib\markers.py", line 109, in marker_fn
        return eval(compiled_marker, environment)
      File "<environment marker>", line 1, in <module>
    NameError: name 'sys_platform' is not defined
    c:\users\vivia\appdata\local\temp\pip-build-ggvj6m\pywin\distribute-0.6.35-py2.7.egg
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "c:\users\vivia\appdata\local\temp\pip-build-ggvj6m\pywin\setup.py", line 4, in <module>
        use_setuptools()
      File "distribute_setup.py", line 152, in use_setuptools
        return _do_download(version, download_base, to_dir, download_delay)
      File "distribute_setup.py", line 132, in _do_download
        _build_egg(egg, tarball, to_dir)
      File "distribute_setup.py", line 123, in _build_egg
        raise IOError('Could not build the egg.')
    IOError: Could not build the egg.

    ----------------------------------------
```
#### Mac：
[pyenv](https://github.com/pyenv/pyenv)

## Python 2 and Python 3 Comparision

### print

in python3, print is a function, it takes arguments e.g.:

> print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
>
>    Print *objects* to the text stream *file*, separated by *sep* and
>    followed by *end*.  *sep*, *end*, *file* and *flush*, if present,
>    must be given as keyword arguments.

```
>>> for i in range(4):
...     print (i,end='|')
...
0|1|2|3|
```

it still supports the old string formats like:

```
>>> age = 16
>>> print("Age is %d" % age)
Age is 16
```

if string.format is used, be sure not to forget the brackets also: (I don't like this design in Python3, not look good with so many brackets:-()

```
name="test"
pwd="password"

print (('My name is {0}').format(name))
```

it also support below simpler format (f"{variable}"):

```
>>> numbers = [0,1,2]
>>> print(f"The nubmers are:{numbers}")
>>> 'The numbers are:[0, 1, 2, 3, 4, 5]'
```

in python2, print is normally used as a statement, like 'print "test" ', But the point is, it also supports print as a function like in python3, however it needs to import a module ```from __future__ import print_function```:

> print(*objects, sep=' ', end='\n', file=sys.stdout)
>
>    Print *objects* to the stream *file*, separated by *sep* and
>    followed by *end*.  *sep*, *end* and *file*, if present, must be
>    given as keyword arguments.

```
λ py -2.7
Python 2.7.13 |Anaconda 4.3.1 (64-bit)| (default, Dec 19 2016, 13:29:36) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
>>> from __future__ import print_function
>>> a = [1,2,3]
>>> print(a,sep='|')
[1, 2, 3]                     
```

### open

in python 2, open file api is taking few arguments, mostly used, name and mode

```
open(name[, mode[, buffering]])
```

in python3, it adds quite some more arguments,

```
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

the encoding parameter will be very useful when handling non-english characters. previsoully in python2 we use codecs modeule to handle it.

### exec, execfile

execfile() is removed from Python3, an alternative is using exec:

for example: 

in python3:

```
exec(open('./ex1.py'),read())
```

or 

```
from past.builtins import execfile

execfile('myfile.py')
```



in python2, you can use both:

```
execfile('../ex1.py')
exec(open('./ex1.py'),read())
exec(compile(open('myfile.py').read()))
```

### input(), raw_input()

in python3,  raw_input() is removed, instead input() is used.

somewhere it says:

> If the user e.g. puts in an integer value, the input function returns this integer value. If the user on the other hand inputs a list, the function will return a list.

but when i try it from the console, I don't see any difference between input() and raw_input(), am I missing anything?

   Python2:

     >>> a = raw_input("enter two number and add:")
    enter two number and add:1+2
    >>> print(a)
    1+2
    >>> type(a)
    <type 'str'>
Python3:

```
>>> a = input("Enter two numbers and add:")
Enter two numbers and add:1+2
>>> type(a)
<class 'str'>
>>> print(a)
1+2
```



### range()

in python2, if you run "range(3)", you will get:

```
[0,1,2,3]
```

this is because the type of range(3) is ```<type 'list'>```

in python3 however, if you run the same, you will get:

```
range(0,3)
```

its type now is ```<type 'range'>```

why this change?

as per Python official, saving space is the main purpose:

>  In many ways the object returned by "range()" behaves as if it is a list, but in fact it isn't. It is an object which returns the successive items of the desired sequence when you iterate over it, but it doesn't really make the list, thus saving space

There are several ways if you want to iterate and get the items:
- using function 'list()'
```
>>> list(range(3))
[0, 1, 2]
```
- using for loop

  ```
  >>> for i in range(5):
  ...     print (i)
  ...
  0
  1
  2
  3
  4
  ```
- using iter()
```
>>> numbers = range(3)
>>> it = iter(numbers)
>>> it
<range_iterator object at 0x030B67D0>
>>> next(it)
0
>>> next(it)
1
>>> next(it)
2
```

This change also has impacts on some other built-in methods, like keys() in dictionary:

```
>>> dict = {1:"first",2:"second"}
>>> dict.keys()
dict_keys([1, 2])
>>> list(dict.keys())
[1, 2]
```
### division ("/")

in python2, value returned from division depends on its operands. e.g. if both are "int", then it returns int:

```
>>> 5/3
1
```

else if one of it is float, then float is returned:

```
>>> 5/3.0
1.6666666666666667
```

in python3, division will always return float value:

```
>>> 5/3
1.6666666666666667
```

### internet Access
in python 2, **"urllib2"** module is used for retrieving Urls
```
>>> import urllib2
>>> html = urllib2.urlopen('http://www.bing.com')
```

in python3, it's changed to "urllib.request" module:

```
>>> from urllib.request import urlopen
>>> html = urlopen('http://www.bing.com')
```

### html parsing

```
# Python 2 only:
from HTMLParser import HTMLParser

# Python 2 and 3 (after ``pip install future``)
from html.parser import HTMLParser

# Python 2 and 3 (alternative 2):
from future.moves.html.parser import HTMLParser
```

### new modules

in python3, there are some new modules added e.g.:

- statistics:

  ```
  >>> import statistics
  >>> data = [1,2,3,4]
  >>> statistics.mean(data)
  2.5
  >>> statistics.median(data)
  2.5
  >>> statistics.variance(data)
  1.6666666666666667
  ```



### Python launcher for Windows

支持多python环境，

```
py -3.6
py -2.7
```

### Virtual Environments and Packages

This is new in python3, supporting multiple virtual environments for running under same python version, but in each virtual environment, you can load different python module and packages.

### Exception Hanlding

TBD

## Collections

### Dictionary

```
>>> dict = {1:"first",2:"second"}
>>> dict.keys()
[1, 2]
>>> for k,v in dict.items():
...     print k,v
...
1 first
2 second
```

## Random

### random.sample()

used to generate unique numbers;

```
>>> num = random.sample(range(1,9),4)
>>> print (num)
[7, 1, 3, 8]
```

将这几个数字组合成一个四位数：

```
>>> print (("").join(str(x) for x in num))
7138
```

## Performance

there are some useful built-in functions in python for calculating the duration of your code running;

### timeit

for example you want to check how long it takes to run your function, or you want to compare two algorithms:

```
	def generate_random_r1():
    while True:
        num = randint(1000,9999)
        numlist = [int(i) for i in str(num)]
        if (len(set(numlist)) )>=4:
            break
    return num

from timeit import timeit
t1=timeit(generate_random_r1,number=1)
print (f"t1 duration:{t1}")
```

result is:

```t1 duration:2.7940966024918055e-05```

[26.6. timeit — Measure execution time of small code snippets — Python 2.7.13 documentation](https://docs.python.org/2/library/timeit.html#examples)

### profiler

[26.4. The Python Profilers — Python 2.7.13 documentation](https://docs.python.org/2/library/profile.html)

This is very useful if you want to see how each function behaves in your script. There are several ways to use it:

- use cProfile module (recommended as it is written in C and fast)

  ```
  import cProfile
  cp1 = cProfile.run("generate_random_r1()")
  ```

  result looks like: 

  ```
  27 function calls in 0.000 seconds

     Ordered by: standard name

     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
          1    0.000    0.000    0.000    0.000 <string>:1(<module>)
          1    0.000    0.000    0.000    0.000 ComparePerf_Generate_Num_Function.py:16(generate_random_r1)
          3    0.000    0.000    0.000    0.000 ComparePerf_Generate_Num_Function.py:19(<listcomp>)
          3    0.000    0.000    0.000    0.000 random.py:172(randrange)
          3    0.000    0.000    0.000    0.000 random.py:216(randint)
          3    0.000    0.000    0.000    0.000 random.py:222(_randbelow)
          1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
          3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
          3    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
          1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
          5    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
  ```

- use profile module (written in python)

```
print (profile.run("generate_random_r1()")
```

result is: same as above

- use cProfile from command line together with pstats module

  ```
  python -m cProfile -o timeStats.profile <your.py file>
  python -m pstats timeStats.profile
  ```

  ​

[performance - Measure time elapsed in Python? - Stack Overflow](https://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python)

## Some Issues and Solutions:

1 " TypeError: not all arguments converted during string formatting"

The above error occurs when I try to run below in python3.

```
print (('My name is {0}, my age is {1}') % (my_name,my_age))
```

The reason it fails is that, I mixed "%" with the "{}" placeholders, the "{}" is for format() function.

To solve it,

```
 print (('My name is {0}, my age is {1}').format (my_name,my_age))
```

## Useful Materials

[Early vs. Beginning Coders – Zed A. Shaw](https://zedshaw.com/2015/06/16/early-vs-beginning-coders/)

[Dreyfus model of skill acquisition - Wikipedia](https://en.wikipedia.org/wiki/Dreyfus_model_of_skill_acquisition)

[如何掌握所有的程序语言 - 王垠](http://www.yinwang.org/blog-cn/2017/07/06/master-pl)

[如何学习一门新的编程语言？——在学习区刻意练习 - 阳志平的网志](http://www.yangzhiping.com/tech/learn-program-psychology.html)

[The 2 Biggest Mistakes I Made When Learning to Code](http://www.suneelius.com/2012/09/07/the-2-biggest-mistakes-i-made-when-learning-to-code/)

[阳志平：如何建立好的学习习惯系统？](http://mp.weixin.qq.com/s/4okD7C7YwpZvEB7IKi1yCw)

[Zoom.Quiet：如何快速掌握 Pythonic 要义？](http://mp.weixin.qq.com/s?__biz=MzA4ODM4ODQ3MQ==&mid=2651930614&idx=1&sn=b6bc35abc67520b684869c4ad1dd8169&chksm=8bcf79eebcb8f0f84f2306d8cb9fa7206887d6cdc357be17c0f3f25bed2f603c256f325aafdc#rd)

[Python 课程往期优秀实践索引](https://github.com/OpenMindClub/Share/wiki/IdxGoodPracticePyCourse)

[Python 课程同学自评、互评参考维度](https://github.com/AIHackers/Py101-004/wiki/HbHackerStyle)

[提问的智慧 - Eric S. Raymond, Rick Moen](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md)

[好问题的反面案例](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md#%E4%B8%8D%E8%AF%A5%E9%97%AE%E7%9A%84%E9%97%AE%E9%A2%98)

[Porting Python 2 Code to Python 3](https://docs.python.org/3/howto/pyporting.html)

[Python3 in One Picture](http://openmindclub.qiniucdn.com/res/map/py3in1pic.jpg)

[极简 Python 上手导念 | Zoom.Quiet Personal Static Wiki](http://wiki.zoomquiet.io/pythonic/MinimalistPyStart)

[Python教程 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)

[Master Technical Job Skills with Live Learning Platform - LiveEdu.tv](https://www.liveedu.tv/)

[Le Peuple Migrateur (Original Motion Picture Soundtrack)专辑](http://music.163.com/album/112951?userid=79139154)

## Tools

这期课程推荐的工具如下，建议你依此配置，尤其终端。

- Python 版本：Python 3.6.2
- 终端： 
  - Mac OS : iTerm2 
    - [pip 9.0.1 : Python Package Index](https://pypi.python.org/pypi/pip)
    - [Homebrew — The missing package manager for macOS](https://brew.sh/)
    - 配置趁手的 iTerm2 : [iTerm2 + Oh My Zsh + Solarized color scheme + Meslo powerline font + [Powerlevel9k\] - (macOS)](https://gist.github.com/kevin-smets/8568070)
    - 探索 CLI 更多用法：[快乐的 Linux 命令行](https://billie66.github.io/TLCL/)
  - Windows : cmder
- 编辑器： Atom
- 笔记工具：Jupyter Notebook,[nbviewer](https://github.com/jupyter/nbviewer)
- 版本管理工具：Git
- 搜索工具：Google
- 技术文档离线查阅工具：
  - Mac OS : [Dash for macOS - API Documentation Browser, Snippet Manager](https://kapeli.com/dash)
  - Windows : [Zeal - Offline Documentation Browser](https://zealdocs.org/)