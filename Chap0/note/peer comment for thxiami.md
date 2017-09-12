## 做帮别人挠痒痒的猴子 - thxiami 同学作业点评

根据 [Python 课程同学自评、互评参考维度](https://github.com/AIHackers/Py101-004/wiki/HbHackerStyle) 结合代码考察，参考thxiami同学对我作业点评的模板

### thxiami同学的作业地址：

初级版：[guess_easy.py](https://github.com/thxiami/Py101-004/blob/master/Chap0/project/guess_easy.py)
升级版：[guess_hard.py](https://github.com/thxiami/Py101-004/blob/master/Chap0/project/guess_hard.py)

教程和复盘：[Py101-004/Chap0/note at master · thxiami/Py101-004](https://github.com/thxiami/Py101-004/tree/master/Chap0/note)

### 闪光点

- Github Readme 清晰的目录文件说明、游戏规则、change log，很用心

  [Py101-004/Chap0/project at master · thxiami/Py101-004](https://github.com/thxiami/Py101-004/tree/master/Chap0/project)

-  坚持每日记录探索和复盘，非常详细，真心称赞，实在惭愧，我一天都没有记录过
  [Py101-004/Log_0w.md at master · thxiami/Py101-004](https://github.com/thxiami/Py101-004/blob/master/Chap0/note/Log_0w.md)

- 个人教程： Jupyter实现，描述+代码实践看得出来很认真的做了再写的，而且有模拟场景帮助理解，感受一下：

```
5 类和对象

什么是类？什么是对象？它们又有什么作用？先不着急，带着这些问题，我们来模拟一个场景。 你是高一的一位班主任，现在刚刚开学，班里面来了5个同学，因为你的程序员潜质，你把他们安排在0-9号座位，而不是1-10号。为了能快速认识同学，你使用命令创建了一份座次表(list)，方便你能根据座位号(index)辨认他们的名字。

student_list = ['李雷', '韩梅梅', '学生甲', '学生乙', '学生丙']

过了一天，名字还没记全呢。学校又做了一次体检，要求你记录他们的身高，并可能随时来问，你一拍大腿: 这没问题啊，我才学过字典啊，于是你又创建了一个身高对照表(dict)

height_dict = {'李雷':160, '韩梅梅': 170, '学生甲': 175, '学生乙': 172, '学生丙': 180} # 怪不得李雷和韩梅梅没有在一起
```
#### 更赞的以下两点：

- 初级版和升级版游戏都有优雅的程序组织方式，功能模块独立定义方法，用到```__name__```属性，不但可以独立运行文件，还可以作为模块导入其他py文件，很完整的实现。比如[初级版游戏](https://github.com/thxiami/Py101-004/blob/master/Chap0/project/guess_easy.py)的框架：

  ```
  def get_num()
  def guess(wanted_num, input_num)
  def play(allowable_count)
  def main()
  if __name__ == '__main__':
      main()
  ```

  ​

- [升级版游戏](https://github.com/thxiami/Py101-004/blob/master/Chap0/project/guess_hard.py)有完整的测试代码和测试数据，非常棒！看了他的代码后，我也在改写自己的初级版程序，便于测试。

  ```
  def generate_randnum()
  def get_num()
  def guess(wanted_num, input_num)
  def play(allowable_count)
  def test_generate_randnum()
  def test_of_guess():
      """
      guess() 函数的测试函数，测试通过规则:
      返回的A,B值与预期相符
      """
      wanted_num = '1234'
      test_input_num = [
          # 无重复
          ('5678', '0A0B'),
          ('5671', '0A1B'),
          ('5617', '0A1B'),
          ('5167', '0A1B'),
          ('5612', '0A2B'),
          ('5312', '0A3B'),
          ('4312', '0A4B'),
          ('1567', '1A0B'),
          ('4256', '1A1B'),
          ('4531', '1A2B'),
          ('3124', '1A3B'),
          ('5634', '2A0B'),
          ('1253', '2A1B'),
          ('1243', '2A2B'),
          ('1235', '3A0B'),
          ('1234', '4A0B'),
          # 有重复
          ('4444', '1A0B'),
          ('2244', '2A0B'),
          # 首位有0
          ('0000', '0A0B'),
      ]
  def test():
      test_generate_randnum()
      test_of_guess()
  def main()
  if __name__ == '__main__':
      #test()
      main()
  ```

  ​

- 代码注释和docstring非常完整，很方便其他人理解代码

  文件开头指明代码运行环境python3，（如果没记错的话，Python3全面支持Unicode，所以这一行应该可以省略了```# -*- coding:utf-8 -*-```）

  以及程序的基本信息

  ```
  #!/usr/bin/env python3
  # -*- coding:utf-8 -*-

  """
  Program name: Bulls And Cows
  Author: thxiami
  Github: https://github.com/thxiami/
  Edition：v1.0
  Edit date: 2017.08.14
  """
  ```

  各功能块都有相应的docstring:

  ```
  def generate_randnum():
      """
      函数用于生成符合游戏规则的随机数，并返回该数字的字符串
      游戏规则：随机数为 4 位，首位不为 0 且各数位不重复
      
      Args:
      
      Return：
          string : 符合游戏规则的随机数

      """
  ```

  关键的代码行有清晰的注释：

  ```
  	# 分两次生成随机数，第 1 次生成首位
      # 首位不为 0，故从 optional_numbers 中后 9 个数字随机选择 1 个数返回
      # 并从列表 optional_numbers 中删掉这个数字，防止后续取到重复数字
      first_num = optional_numbers.pop(randint(1, 9))
  ```

  ​

### 代码中的问题

- 升级版游戏

  这可能是一个会有争议的地方，关于用户输入的4位数判断规则，先看一个你的运行结果：

  0158 和 158 被视为两个不同的数字，前者是四位数，后者不是（这个没问题）。关键是前者，之所以判断是四位数，源自输入类型是str

  ```
  Please type in a 4 digit number.
   >0158
  1A3B
  第6次猜测，还有4次机会
  Please type in a 4 digit number.
   >158
  Only a 4 digit number is wanted! e.g. 5
  ```

  个人认为0158这种应该也被排除掉的。

  ```
  >>> a = 0158                       
    File "<stdin>", line 1           
      a = 0158                       
             ^                       
  SyntaxError: invalid token         
  >>> a = 158                        
  >>> a                              
  158                                
  ```

  ​

### 一些建议

- 【忽略我这段吧，刚明白此规范的docstring是为了pydoc和help来的，虽然我还是不喜欢这个规范】关于docstring，同学参考的使是[编码之前碎碎念(工程实践) — python-web-guide 0.1 文档](http://python-web-guide.readthedocs.io/zh/latest/codingstyle/codingstyle.html#id21)的规范，貌似也是google的规范，可是我发现我不太认同咋办，我感觉代码第一眼看过去多是注释，代码被喧宾夺主了，主要是两部分：
  - docstring在代码定义语句之下，代码体之上。当注释很长的时候，分隔的好远，比较跳跃感
  - docstring内空行太多，所以看着更长。

```
def guess(wanted_num, input_num):
    """
    判断给定的两个数字关系，根据判断结果打印必要信息并返回布尔值。
    
    Args：
        wanted_num (int): 程序给定的需要用户去猜测的数字，2位数
        input_num (int)：用户输入的数字,2位数
        
    Return:
        bool : True代表两个数字相等；False代表不相等
        
    Demo：
        result_bool = guess(10, 15), 程序会打印"大了"，并返回 False;
    """
    if input_num > wanted_num:
        print("大了")
        return False
```

我比较prefer的样式，但因为上面也是google的规范，所以应该我喜欢的这种是不太推荐的了，但还是想提出来看大家是因为认同还是follow google才选择上面的样式

```
"""
判断给定的两个数字关系，根据判断结果打印必要信息并返回布尔值。
Args：
    wanted_num (int): 程序给定的需要用户去猜测的数字，2位数
    input_num (int)：用户输入的数字,2位数
Return:
    bool : True代表两个数字相等；False代表不相等
Demo：
    result_bool = guess(10, 15), 程序会打印"大了"，并返回 False;
"""
def guess(wanted_num, input_num):
    if input_num > wanted_num:
        print("大了")
        return False

    elif input_num < wanted_num:
```

- 初级版游戏：判断输入是否合法用到isdigit方法，单纯的想探讨一下，try/except 和这种温和的方法哪种是best practice? 递归方法和循环判断哪种更推荐？感觉递归可能会慢一些把

  ```
  def get_num():
      # 获得用户输入
      input_num = input('Please type in a number.\n >')

      # 判断用户输入的合法性，当输入仅包含数字时返回该数字；其他情况要求用户重新输入
      if input_num.isdigit():
          return int(input_num)
      else:
          print('Only a number is wanted! e.g. 5')
          return get_num()
  ```

  **update**: I think i can conclude that str.isdigit() would be better as per [Design and History FAQ — Python 3.6.2 documentation](https://docs.python.org/3/faq/design.html) simply because **Actually catching an exception is expensive.**

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


- 关于if else: 昨天看王垠的[编程的智慧](http://www.yinwang.org/blog-cn/2015/11/21/programming-philosophy)中”优雅的代码“部分，他提到”优雅的代码在逻辑上大体看起来，是枝丫分明的树状结构（tree）“，体现在if else 控制语句中，就是if 语句几乎总是有两个分支。一个分支的代码看起来代码短小了，但逻辑上读起来大脑就费劲了，结合”大脑爱偷懒“的本性，我被他说服了，现在也觉得他说的有道理，准备借鉴实施。摘了一部分你的代码如下：

  ```
  	# 对玩家猜测次数进行判断
          if count > 10:
              print('您没有机会猜测，游戏结束')
              break

          # 获得玩家输入
          print(f'第{count}次猜测，还有{10 - count}次机会')
          input_number = get_num()

          # 对玩家猜测结果进行判断
          if guess(wanted_number, input_number) is True:
              break
  ```

  如果是王垠，他可能建议这么写：感受一下，您觉得是否认同?

  ```
  		# 对玩家猜测次数进行判断
          if count > 10:
              print('您没有机会猜测，游戏结束')
              break
          else:
              # 获得玩家输入
              print(f'第{count}次猜测，还有{10 - count}次机会')
              input_number = get_num()

              # 对玩家猜测结果进行判断
              if guess(wanted_number, input_number) is True:
                  break
              else:
                  count += 1
  ```

  ​

- 测试代码很赞，如果测试和代码能分开就更好了，另外很想探讨一下比较推荐的python test framework，目前我看下来的有pytest和python自带的unittest比较不错。

  将测试的代码放到单独的文件中，这样就不用手动切换main()和test()了。

  ```
  if __name__ == '__main__':
      #test()
      main()
  ```

  ​


### Reference

- [编程的智慧](http://www.yinwang.org/blog-cn/2015/11/21/programming-philosophy)