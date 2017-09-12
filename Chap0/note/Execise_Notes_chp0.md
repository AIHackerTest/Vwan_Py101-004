## 升级版游戏设计

### 需求

升级版猜数字小游戏，实现以下功能：

1. 程序内部用 0-9 生成一个 4 位数，每个数位上的数字不重复，且首位数字不为零，如 1942
2. 用户输入 4 位数进行猜测，程序返回相应提示

用 A 表示数字和位置都正确，用 B 表示数字正确但位置错误
用户猜测后，程序返回 A 和 B 的数量
比如：2A1B 表示用户所猜数字，有 2 个数字，数字、位置都正确，有 1 个数字，数字正确但位置错误

3. 猜对或用完 10 次机会，游戏结束

### 设计与实现

#### 功能1：程序内部用 0-9 生成一个 4 位数，每个数位上的数字不重复，且首位数字不为零，如 1942

##### 设计

通过一个单独的函数来实现，generate_random()， 用到random.randint(a,b)方法

首位数字不为零：a 从1000开始

每个数位上的数字不重复：将数字转换成列表，再转换成set，判断该set的长度，如果恒等于4，则意味着各数字不重复

循环随机数的产生，直到符合条件的数出现

###### 实现

按上述设计，实现代码R1。后来浏览其他同学的作业，发现random.sample()函数可以生成不重复的数字，感觉也不错，实现代码R2。

但是不清楚二者性能如何，搜索到用Python的Timer模块以及profiler来进行比较。具体比较方法见下文。

通过性能比较，R1的运行时间和内部调用似乎都优于R2，所以采用R1实现。

R1: generate_random():

```
def generate_random():
    while True:
        rand = randint(1000,9999)
        numlist = [int(i) for i in str(rand)]
        if (len(set(numlist)) )>=4:
            break
    print(f"{rand}")
    return rand
```

R2: generate_random():

```
def generate_random():
    while True:
        num = random.sample(range(0,9),4)
        if (num[0] == 0):
            continue
        else:
            num = "".join(str(x) for x in num)
            break
    print(f"{num}")
    return num
```
###### R1和R2算法性能比较
使用timeit 模块比较两个方法的运行时间；使用cProfile or profile比较两个方法的内部调用情况；

duration：

```
from timeit import timeit
t1=timeit(generate_random_r1,number=1000)
t2=timeit(generate_random_r2,number=1000)
print (f"R1 duration:{t1}")
print (f"R2 duration:{t2}")
```

运行时间结果：R1优于R2
```
R1 duration:0.009045698960256242
R2 duration:0.013645008516330928
```

profile：R1调用次数少于R2

```
import cProfile
cProfile.run("generate_random_r1()")
cProfile.run("generate_random_r2()")
```

结果：

R1:

```
         19 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 ComparePerf_Generate_Num_Function.py:16(generate_random_r1)
        2    0.000    0.000    0.000    0.000 ComparePerf_Generate_Num_Function.py:19(<listcomp>)
        2    0.000    0.000    0.000    0.000 random.py:172(randrange)
        2    0.000    0.000    0.000    0.000 random.py:216(randint)
        2    0.000    0.000    0.000    0.000 random.py:222(_randbelow)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        2    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
```

R2:

```
         31 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        5    0.000    0.000    0.000    0.000 ComparePerf_Generate_Num_Function.py:12(<genexpr>)
        1    0.000    0.000    0.000    0.000 ComparePerf_Generate_Num_Function.py:6(generate_random_r2)
        3    0.000    0.000    0.000    0.000 _weakrefset.py:70(__contains__)
        2    0.000    0.000    0.000    0.000 abc.py:178(__instancecheck__)
        4    0.000    0.000    0.000    0.000 random.py:222(_randbelow)
        1    0.000    0.000    0.000    0.000 random.py:282(sample)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        4    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        4    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
```



#### 功能2：验证用户输入的数字并返回结果提示

##### 设计

通过一个单独的函数来实现，verify_number(n1,n2), 其中n1,n2 分别用户输入值和系统产生的随机数，最终实现采用R3

R1: 将n1,n2分别转换成list, 通过zip(list1,list2) 取两个列表对应值的差，组成新list

计算新list中数字0的个数（count0)，如果为4，则4A0B；否则，取list1和list2的交集的长度，减去count0，即为数字正确但位置错误数

##### 实现

verify_number()：

R1：

```
def verify_number(n1,n2):
    numlist1 = [int(i) for i in str(n1)]
    numlist2 = [int(i) for i in str(n2)]
    numlist = [x - y for x,y in zip(numlist1,numlist2)]
    count0 = numlist.count(0)
    count1 = 0;
    if count0 != 4:
        count1 = len(set(numlist1) & set(numlist2)) - count0
    return count0,count1
```

R2：通过判断两个列表是否相同来判断输入是否正确；这样可以省却zip操作。具体性能是否有提高没有去试，偷懒先。

```
def verify_number(n1,n2):
    numlist1 = [int(i) for i in str(n1)]
    numlist2 = [int(i) for i in str(n2)]
    if (numlist1 == numlist2):
        return len(numlist1),0
    else:
        numlist = [x - y for x,y in zip(numlist1,numlist2)]
        counta = numlist.count(0)
        return counta,len(set(numlist1) & set(numlist2)) - counta
```

R3：直接先判断两个数字是否相等。

```
def verify_number(n1,n2):
    if (n1 == n2):
        return len(str(n1)),0
    else:
        numlist1 = [int(i) for i in str(n1)]
        numlist2 = [int(i) for i in str(n2)]
        numlist = [x - y for x,y in zip(numlist1,numlist2)]
        counta = numlist.count(0)
        return counta,len(set(numlist1) & set(numlist2)) - counta
```

#### 功能3：游戏结束规则

通过循环允许用户输入10次数字，如果输入非数字，重新提示输入，并算作一次计数

如果输入的是数字，调用verify_number()方法，如果为4A0B，则提示用户输入正确，退出游戏

否则继续提示用户输入，计数增加，超出10次，游戏结束

##### 实现

client:

```
# generate a random number
rand = generate_random()
print("Welcome to Bulls and Cows, you have 10 trials to guess right the system random number, enjoy!")
count = 1
while count <= 10:
    try:
        number = input(f"{count}:Please enter a 4-digit number:")
    except:
        print ("Please enter a number! ")
    else:
        counta,countb = verify_number(number,rand)
        if counta == 4:
            print(f"{counta}A{countb}B, Congratulations!")
            break
        else:
            print (f"Sorry, your guess right is:{counta}A{countb}B, try again to make it 4A0B! ")
    count += 1
```

##### 思考
1. 是使用range()还是while loop来判断用户猜测数字的次数
```
for count in range(1,10):
```
之前的while loop:
```
count = 1
while True:
  ....
  count += 1
```
但问题是，这样设计的话，如果用户输入的数字超出范围或不是数字，就没法忽略不算作一次计数。
如果从用户角度出发的话，这种输错应该不计数才比较友好，所以还是决定用while loop来实现。


### 运行结果：

![Advanced BandC Result 1.png](https://github.com/Vwan/Py101-004/blob/master/Chap0/resource/Advanced%20BandC%20Result%201.png?raw=true)

![Advanced BandC Result 2.png](https://github.com/Vwan/Py101-004/blob/master/Chap0/resource/Advanced%20BandC%20Result%202.png?raw=true)
