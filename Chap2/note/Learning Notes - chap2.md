

## Static,Class and Instance Attributes

> Generally speaking, instance variables are for data unique to each instance
> and class variables are for attributes and methods shared by all instances
> of the class:

attributes这里指变量和方法

### class and instance variable

类变量和实例变量，类变量相当于其他语言如Java的静态变量。

```
class Test(object):
    id = 10
    def __init__(self,ids):
        self.id = ids

if __name__ == '__main__':
    te = Test(1)
    print(f"instance id: {te.id}")
    print(f"class id: {Test.id}")
	
```

结果：

```
instance id: 1
class id: 10
```

类变量需要初始化的```id = 10```，不然如果直接写```id```就会报错：

```
instance id: 1
Traceback (most recent call last):
  File "C:\Users\vivia\OneDrive\Projects\OpenMind\Py101-004-Vwan\Py101-004\Chap2\project\practice\class_instance_variable.py", line 9, in <module>
    print(f"class id: {Test.id}")
AttributeError: type object 'Test' has no attribute 'id'
```

###  class method, instance method, static method

通过annotation @classmethod, @staticmethod 来标注method类别。

class method 和 static method，区别之一是，static method 定义时无需传入self变量。

二者都可以用类的实例来调用，挺奇怪的**，放个疑问这里，待补**

```
class Test(object):
    id = 10
    def __init__(self,id):
        self.id = id

    def test_instance_method(self):
        return self.id

    @classmethod
    def test_class_method(self):
        return self.id

    @staticmethod
    def test_static_method():
        return Test.id

if __name__ == '__main__':
    te1 = Test(1)
    te2 = Test(2)
    print(f"instance id: {te1.id}")
    print(f"class id: {Test.id}")

    print('instance method call from instance 1:',te1.test_instance_method())
    print('instance method call from instance 2:',te2.test_instance_method())
    #print('instance method call from class:',Test.test_instance_method()) # should fail

    print('class method call from instance 1:',te1.test_class_method())
    print('class method call from instance 2:',te2.test_class_method())
    print('class method call from class:',Test.test_class_method())

    print('static method call from instance 1:',te1.test_static_method())
    print('static method call from instance 2:',te2.test_static_method())
    print('static method call from class:',Test.test_static_method())

```

运行结果：

```
instance id: 1
class id: 10
instance method call from instance 1: 1
instance method call from instance 2: 2
class method call from instance 1: 10
class method call from instance 2: 10
class method call from class: 10
static method call from instance 1: 10
static method call from instance 2: 10
static method call from class: 10

```

[Python Tutorial: class method vs static method - 2017](http://www.bogotobogo.com/python/python_differences_between_static_method_and_class_method_instance_method.php)

# Json

use json module

## load json file

```
	def load_json_file(self,file):
        with open(file,"r",encoding="utf-8-sig") as file:
            jsn = json.loads(file.read())
        return jsn
```

json file format:

```
{'HeWeather5': [{'basic': {'city': '北京', 'cnty': '中国', 'id': 'CN1
01010100', 'lat': '39.90498734', 'lon': '116.40528870', 'update': {'loc': '2017-08-22 14:47', 'utc': '2017-08-22 06:47'}}, 'now': {'cond': {'code': '101', 'txt': '多云'}, 'fl': '34', 'hum': '73', 'pcpn': '0'
, 'pres': '1007', 'tmp': '29', 'vis': '7', 'wind': {'deg': '184', 'dir': '南风', 'sc': '微风', 'spd': '9'}}, 'status': 'ok'}]}
```

but issue comes, when parsing above data, 

```
 json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)

c:\python\python36-32\lib\json\decoder.py:355: JSONDecodeError
```

**问题**出在，json源文件中用的是单引号，但是**json.loads accepts only double quotes for json properties**，

**解决方法：**

use ast package

```
data_dict = ast.literal_eval(file.read())
jsn = json.dumps(data_dict) # jsn string
```

[python - JSON ValueError: Expecting property name: line 1 column 2 (char 1) - Stack Overflow](https://stackoverflow.com/questions/25707558/json-valueerror-expecting-property-name-line-1-column-2-char-1)

# Lambda

目前只是初浅的认识，函数式编程。

简单的讲，lambda就是个匿名函数，当函数不复杂，你不想单独定义(def f)的时候，可以使用lambda，

```
>>> f = lambda x: x * 2
>>> f(2)
4
```

还有，如果有很多个if else, 其他语言用switch case 而python不支持的情况下，可以用dict + lambda来实现

比如，我的commands set 

```
Commands = namedtuple('Commands', 'help history exit')
    commands = Commands(('h', 'help'),'history',('exit', 'quit'))
```

不同的命令执行不同的action，用if else的话是这样：

```
if cmd in commands.history:
	do sthing
elif cmd in commands.help:
	do somt
elif cmd in commands.exit:
	do something
```

其实看着也挺清爽的，不过还是Lambda看着更酷，虽然我还不知道Lambda性能如何

```
cmd_dict = {
            commands.help: lambda: print(utils.read_file(self.help_file, "r", 100, encoding='utf-8-sig')),
            commands.history: lambda: utils.show_history(self.history),
            commands.exit: lambda: (utils.show_history(self.history), sys.exit(0))
        }
        for k, v in cmd_dict.items():
            if cmd in k:
                cmd_dict.get(k)()
                break
```

**存在的问题：**

- lambda 表达式中不支持assignment, 即没法写 x = 1 之类的，不爽。搜了下也只找到map[x]=y的那种可以用operator.setitem(map,x,y)来实现
- 不支持多行；如果多行的话还是先去def一个函数吧

# Function 

### variable arguments

#### ```*args```

```
def f(*args):
    for arg in args:
        print(arg)
```

调用的时候：

```
>>>f('b','c')
b
c
```

```
>>> list = ['b','c']
>>> f(list)
['b', 'c']
```

上面看到，list作为一个变量参数传了进去。那如果我们希望将list中的值依次传进去呢，需要用到*操作符

```
>>> f(*list)
b
c
```

```**kargs```

与```*args```的区别在于，后者是keyworded,就是可以传入参数名（必须是string)和值，如

```
def f(**kargs)
f(k=1,s=2)
```

假设我们有个dict类型的变量，我们想将其key和value对传入函数中，便可以用```**kargs```

```
>>> d = {"1":"a","2":"b"}
>>> def f1(**args):
...     for k,v in args.items():
...             print(k,v)
...
>>> f1(**d)
1 a
2 b
```



[How to use *args and **kwargs in Python - SaltyCrane Blog](https://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/)

# Scheduler

## sched, time

https://docs.python.org/3/library/sched.html

还没有研究透，占个坑

# keyboard interruption

如何在程序运行中捕捉到键盘输入，如ctrl+c中断操作：

```
                            try:
                                dosomething()
                                sys.stdin.read()
                            except (KeyboardInterrupt):
```



# Reference

[API Providers - Apigee](https://apigee.com/providers)

[API Store](http://apistore.baidu.com/)

[Requests: HTTP for Humans — Requests 2.18.4 documentation](http://docs.python-requests.org/en/master/)

[API — Flask Documentation (0.12)](http://flask.pocoo.org/docs/0.12/api/#incoming-request-data)

- 腾讯云 API 服务：[云 API - 腾讯云](https://www.qcloud.com/product/api)，可重点参考：[API 文档 - 帮助与文档 - 腾讯云](https://www.qcloud.com/document/api)
- 百度 API Store：[API Store_为开发者提供最全面的 API 服务](http://apistore.baidu.com/)
- 百度人工智能 API 服务：[百度大脑](http://ai.baidu.com/index/)
- 京东 API 数据服务：[API 数据*免费数据*数据定制_京东万象官网—综合数据开放平台](http://wx.jcloud.com/)
- 常用的 SAAS 服务比较网站，多数提供了 API：[SDK.CN - 中国领先的开发者服务平台](https://www.sdk.cn/)
- 常见金融类、征信类数据 API 服务：[大数据交易平台 - 199IT 数据导航网站 --Hao.199it.com](http://hao.199it.com/jiaoyi.html)
- 创业公司常用的第三方服务 API ：[北京创业工具箱 - 阳志平的网志](http://www.yangzhiping.com/info/startup.html)

# Weather API

[心知天气 - 天气数据 API 和BI - 冷暖自心知](http://www.thinkpage.cn/)

[Weather API- OpenWeatherMap](http://openweathermap.org/api)

[彩云天气API](http://wiki.swarma.net/index.php/%E5%BD%A9%E4%BA%91%E5%A4%A9%E6%B0%94API/v2)



[Weather API - Free Weather API JSON and XML - Developer API Weather For Website - Apixu](https://www.apixu.com/)

[Weather API- OpenWeatherMap](http://openweathermap.org/api)

[Dark Sky API](https://darksky.net/dev/)

[Yahoo! Weather RSS feed](http://developer.yahoo.com/weather/)

[和风天气 | 更专业的天气数据服务](http://www.heweather.com/)	