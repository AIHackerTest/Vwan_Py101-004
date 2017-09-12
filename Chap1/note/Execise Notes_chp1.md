# 天气通CLI版

## 需求

CLI 版天气通需要完成的功能有：

1. 输入城市名，返回该城市的天气数据；所有的城市天气数据保存在\resource\weather_info.txt静态文件中。
2. 输入指令，打印帮助文档（一般使用 h 或 help）；
3. 在退出程序之前，打印查询过的所有城市。
4. 输入指令，退出程序的交互（一般使用 quit 或 exit）；

## 设计

### 功能1：输入城市名，返回该城市的天气数据

读取weather_info.txt文件，将文件数据转换成dict数据类型。

**思考**

可能的问题：

1. 性能问题：如果文件过大，一次性读入内存会影响程序性能，如何解决

   解决：用buffering，csv reader, Collections(教练提示), To try later

2. 除了dict数据类型，还有其他可以用吗？Database, but it's beyond me so far

3. weather_info.txt文件是否格式正确，比如有些城市可能没有天气数据

   如果直接用dict[key]会报错，改用dict.get(key), 如果得到空数据，则设为'未知天气'

   ```
   def show_weather(self,city,weather_info):
           city_weather = weather_info.get(city)
           # set to Unknown if weather is empty from the source data
           if city_weather == "":
               city_weather = "未知天气"
           return city_weather
   ```

   ​

4. weather_info.txt文件中是否有重复城市？不一致数据？dict will by default return the the last duplicated city's weather data

5. weather_info.txt文件是否存在，是否可用？try/except FileNotFoundError, 不知道是否由别的好办法？

6. weather_info.text是否空文件？```os.stat("file").st_size == 0```

7. UFT-8 BOM issue: 

   - 用utf-8 encoding读weather_info 文件的时候，最前面会隐含三个字符，将encoding改为“uft-8-sig"即可忽略那三个字符

   - 即使改成'uft-8-sig' encoding, 当文件为空时，想通过文件大小 == 0 来判断，结果失败，因为那三个字符python仍然计算在内

     目前没有找到更好的办法，只好先写死了：

     ```
     if os.stat(filename).st_size > 3: 
     ```

#### 实现

天气数据作为类实例变量了，其实应该不好，作为load_weather_data的返回值会比较好，这里为了练习，先这么用着了，回头再想想，也看看其他同学如何处理的。

```
	def load_weather_data(self,filename):
        try:
            with open(filename,"r",624,'utf-8-sig') as file:
                if os.stat(filename).st_size > 3: # not including BOM chars
                    data_list = [list(x.rstrip().split(",")) for x in list(file)]
                    self.weather_info = dict(data_list)
                else:
                    self.weather_info = None
        except FileNotFoundError:
            self.weather_info = None

    def __init__(self):
        self.load_weather_data(self.weather_info)
```



### 功能2：输入指令 help, 打印帮助文档

帮助文件\resource\help.txt, 用户输入help时，读取该文件，返回文件内容，注意unicode字符

### 功能3：输入指令 history，打印查询历史

功能1的指令和结果需要能保存在一个变量里，这样查询history的时候可以调用

历史纪录包括：

- 历次查询的城市名 + 天气，可能重复

考虑到程序扩展（如日后需求可能增加要求打印第N次查询结果），设计一个dict数据类型保存历史纪录。

```
history = {}
def show_history(self,history):
        if (len(self.history) == 0):
            print ("Not history records are found, please do some search and retry")
        else:
            for k,v in self.history.items():
                print(f"{k} {v}")
```

#### 思考

可能的问题：当前的设计中，history变量保存在内存中，当程序退出后即消失。如果用户在重新运行程序后仍然想知道以往查询记录的话就会返回“No records"了。

解决方法：将history记录保存到文件中。未实现。

### 功能4：输入指令quit，退出程序交互

调用sys.exit(0)，退出程序

问题：

does sys.exit(0) work for all platforms? Yes

## 隐含功能5：输入指令既非城市也非合法命令

如果有效判断用户输入是城市还是命令？

初步设计是，所有的命令存放在commands set中

```
commands = (
                ('h','help'),
                ('history'),
                ('exit','quit')
           )
```

程序先判断用户输入是否在commands中：

```
if (not any(cmd in e for e in self.commands))
```

如果不在，则将用户输入当作是城市，获取其天气数据city_weather

如果city_weather == None, 则断定用户输入既不是城市也不是合法指令。

```
		   count = 1
            while True:
                cmd = input("> Please enter a command or city:")
                # check if user input is in the commands tuple,
                # if not, check if it's a valid city name and return city weather_info
                # if city not found, print non-match hints
                if (not any(cmd in e for e in self.commands)):
                    city_weather = self.show_weather(cmd,self.weather_info)
                    if city_weather != None:
                        print(f"The weather for city \"{cmd}\" : {city_weather} ")
                        self.history[count] = cmd + " " + city_weather
                        count += 1
                    else:
                        print("Not found any command or city that matches, please type 'help' for all commands")
                elif cmd in list(self.commands[0]): # command help
                    help_text = self.read_file(self.help_file,"r",1,'utf-8-sig')
                    print(help_text)
                elif cmd == self.commands[1]: # command history
                    self.show_history(self.history)
                elif cmd in list(self.commands[2]): # command quit
                    yesno = input("Are you sure to quit? (y/n)> ")
                    if (yesno in ['y','Y']):
                        sys.exit(0)
                    else:
                         continue
```

