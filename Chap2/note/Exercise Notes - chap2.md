# 初级版

## 需求

本章基础任务：完成一个在命令行界面下天气查询程序，实现以下功能：

- 输入城市名，返回该城市最新的天气数据；

- 输入指令，获取帮助信息（一般使用 h 或 help）；

- 输入指令，获取历史查询信息（一般使用 history）；

- 输入指令，退出程序的交互（一般使用 quit 或 exit）；

## 设计

 沿用chap1的框架，修改城市天气查询功能模块，由静态文件读取改为实时网站api查询。

采用和风天气api: [和风天气](https://www.heweather.com/documents/api/v5)，调用其**[实况天气-now | 和风天气](https://www.heweather.com/documents/api/v5/now)**以获取最新的天气数据。

请求格式：https://free-api.heweather.com/v5/now?city=cityname&key=742459bcd8b54244b1979cb30a4a4ac7  ，返回json格式的response

api_key: 742459bcd8b54244b1979cb30a4a4ac7  

因此，需要定义：

- 一个retrieve_weather_data_by_city(city,**argv)方法，获取json格式的天气数据；

  使用requests package

  **这里一个难点是**：如何设计存放需要获取到的具体天气数据，比如温度、风向、湿度等？

  **原则**，尽量不写死在底层code，不在多处定义这些数据。

  **方案**：设计一个实例变量weather_info, 存放api返回的json数据的key，这些key是程序目前需要的，以后可以增删改。将这个参数传给retrieve_weather_data_by_city方法```def retrieve_weather_data_by_city(self,city,*weather_info)```，该方法将根据json key挨个查询到对应的天气值，并返回一个dict。

  这个weather_info字典中的key是json 数据中的key, value是程序所需天气数据的文字表述。设计的目的是，查询到的天气数据结果有望转成以文字表述为key，这样可以在需要的时候dict.get('City')获取数据，而不是dict.get('basic.city')

  ```
  		self.weather_info = {
                              'basic.city':'City',
                              'now.cond.txt':'Weather',
                              'now.wind.dir':"WInd",
                              'now.tmp':"Temperature",
                              'basic.update.utc':'Last Updated On',
                              }
  ```

  但如何将这个字典作为变量传给retrieve_weather_data_by_city方法，并挨个执行其内元素：

  ```
  city,result = self.retrieve_weather_data_by_city(cmd,*self.weather_info)
  ```

  但问题是：result dict中的key仍然是‘basic.city'，因此需要rename key to "City"

  ```
  						# rename keys in result
                          for k,v in self.weather_info.items():
                              result[v] = result.pop(k)
                          print (result)
  ```

  **改进1：**[How to use *args and **kwargs in Python - SaltyCrane Blog](https://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/)

  因为 weather_info 是dict类型，所以可以直接用**kwargs**来传入，也无需前面的rename key操作了。

  ```
  def retrieve_weather_data_by_city(self,city,**weather_info)
  ```

  ```
  city,result = self.retrieve_weather_data_by_city(cmd,**self.weather_info)
  ```

  **改进2**：** weather_info dict仍然写死在脚本中，所以改为存入Json文件，然后从json文件中导入

  ```
  def load_json_file(file):
      """load json file and return data_dict
      :param file json file format
      """
      with open(file,"r",encoding="utf-8-sig") as file:
          data_dict = ast.literal_eval(file.read())
          #jsn = json.dumps(data_dict)
      return data_dict
  ```

  ​

- 一个parse_json(json_data)方法，解析json 格式的数据，提取需要的天气数据

  使用 json package

  这里的一个难点是：如何解析nested keys

  sample json string：

  ```
  [{'basic':
  {'city': '北京', 'cnty': '中国', 'id': 'CN101010100', 'lat': '39.90498734', 'lon': '116.40528870', 'update': {'loc': '2017-08-22 14:47', 'utc': '2017-08-22 06:47'}},
  'now': {'cond': {'code': '101', 'txt': '多云'}, 'fl': '34', 'hum': '73', 'pcpn': '0'
  , 'pres': '1007', 'tmp': '29', 'vis': '7', 'wind': {'deg': '184', 'dir': '南风', 'sc': '微风', 'spd': '9'}}, 'status': 'ok'}]
  ```

  需解析 basic.city, basic.update.utc

  用了个拙的办法，split后再循环，**不知道有没有比较简便的方法？**

  ```
  def parse_json(json_data,**required_data):
      extracted_data = {}
      for key,data in required_data.items():
          tmp = json_data
          if ("." in data):
              temp_keys = data.split(".")
              for temp_key in temp_keys:
                  tmp = tmp[temp_key]
              extracted_data[key] = tmp
          else:
              extracted_data[key] = json_data[data]
      return extracted_data
  ```

  其他设计和chap1的思路差不多。

  **改进3**：新增一个ObjectJson类，通过getattr直接获取用“."串起来的key的值

  关于解析json nested data的问题，前面在parse_data方法中用了判断"."并split，感觉不好。因为我认为完美的解析“.“应该是在更底层做，而不是接近客户端操作。举例来说，给定下面的json string, ```{"test":{"a":1,"b":2,"c":{"c1":"test1"}}}```, 如果要获得c1的值，我希望是这样json_object.test.c.c1, 而不是```json_object['test']['c']['c1']```,后者不太友好，前者更能体现面向对象的思想。遗憾的是，python貌似并不支持。

  网上搜索了下，很开心发现有和我一样喜好的，而且有了实现代码[Objectjson - JSON to nested object. - Python - Snipplr Social Snippet Repository](http://snipplr.com/view/71218/objectjson--json-to-nested-object/)

  }，只是他只能支持```json_object.test.c.c1```, 如果我把”test.c.c1"放到一个变量里，就没法用了，即不支持类似占位符似的处理。

  ```
  key = 'test.c.c1'
  json_object.'{key}'
  ```

  没有找到处理这个问题的方案。但是从getattr得到启发，我可以将key = 'test.c.c1'传进去，在里面进行拆分取值，然后客户端通过调用getattr方法，即可得到任意形式key的值。

  因此改写了他的代码：

  ```
  def __getattr__(self, key):
          data = self.json_data
          if "." in key:
              for k in key.split("."):
                  data = data[k]
              return data
          else:
              return data[key]
  ```

  测试一下：

  ```
  if __name__ == '__main__':
      j = ObjectJson('{"test":{"a":1,"b":2,"c":{"c1":"test1"}}}')
      fs = ['test','test.a','test.c.c1']
      for f in fs:
          attr = getattr(j,f)
          print(attr)
  ```

  结果：

  ```
  value: 1
  value: test1
  ```

  新增parse_json_dot函数，在主程序中替代之前的parse_json

  ```
  def parse_json_dot(json_data,**required_data):
      from objectjson import ObjectJson as objson
      extracted_data = {}
      j = objson(json_data)
      for key,data in required_data.items():
          extracted_data[key] = getattr(j,data)
      return extracted_data
  ```

  **新的问题：**如果json数据含有复杂数据如数组，做不到'test[0].a.c[0]'类似的，而实际生产数据中会有大量这种需求，重新改进，增加"[]"判断：

  ```
  if "[" in k:
                      index,name = self.parse_squared_key(k)
                      data = data[name][index]
  ```

  ```
  def parse_squared_key(self,key):
          start_index = key.index('[') + 1
          index = int(key[start_index:-1])
          name = key[0:start_index-1]
          return index, name
  ```

  这样就可以这么传数据了：

  fs = ['HeWeather5[0].basic.city','HeWeather5[0].daily_forecast[%d].date','HeWeather5[0].daily_forecast[%d].cond.txt_n']

  实际调用的时候再把 fs[1] % i  替换掉 %d， 但不知道为什么我做的时候没有成功替换 %d，代码放在objectjson.py中，欢迎大家来挑错并指正


  **新的问题：**前面的解决方案解决了getatt(j, 'basic.city')的问题，但是把原作者的 j.basic.city不小心给干掉了。。。重新加进去，改写。

  发现如果但用原作者的代码，并加入__getitem__属性方法，可以很好的实现j.basic[0].city[1]之类的结构:

  ```
  def __getitem__(self, index):
          return ObjectJson(self.json_data[index])
  ```

  python好强大，这次做下来觉得```__<attr>__```需要好好学习下。

  只是现在的问题是，我之前的代码就不起作用了，只好重新改，代码超臃肿现在，虽然能工作了，但是诚待改进，等把data model搞清楚了后再来改进：

  现在的code:

  ```
  def __getattr__(self, key):
          if "." in key:
              data = self.json_data
              key = key.split(".")
              for k in key:
                  if "[" in k:
                      left, index = self.parse_squared_key(k)
                      if left in data:
                          if isinstance(self.json_data[left][index], (list, dict)):
                              data = data[left][index]
                          else:
                              data = data[left]
                      else:
                          raise Exception('There is no json_data[\'{key}\'].'.format(key=k))
                  else:
                      data = data[k]
              return data
          else:
              if key in self.json_data:
                  if isinstance(self.json_data[key], (list, dict)):
                      return ObjectJson(self.json_data[key])
                  else:
                      return self.json_data[key]
              else:
                  raise Exception('There is no json_data[\'{key}\'].'.format(key=key))

  ```

  ​




### 思考

还需要考虑到的情况：

- 如何判断city exists?

  根据api的设计，如果city not exist, 会返回"unknown city" status

  ```
  {"HeWeather5":[{"status":"unknown city"}]}
  ```

- 如果用户输入空值，而程序又没能拒掉，导致传给api的city parameter为空```https://free-api.heweather.com/v5/now?city=&key=742459bcd8b54244b1979cb30a4a4ac7```

  ```
  {"HeWeather5":[{"status":"param invalid"}]}
  ```

  ​

  ## bug:

  1. 输入'y', 无任何显示，继续提示”please enter...."" - fixed

     commands[1]是个string，而不是tuple

     所以我在用'for any(cmd in e for e in commands)'时，y in 'history' 就是True了

```
    commands = (
                ('h','help'),
                ('history'),
                ('exit','quit')
                )
```

改为：但是有些死板，还需考虑更好的方法

```
def cmd_exists(cmd,commands):
    for command in commands:
        if(type(command) == type("str")):
            command = [command]
        if (cmd in command):
            return True
        else:
            continue
    return False
```




# 升级版

如果你已完成基础任务，还可以继续探索：

1. 之前只在输入城市名时查询天气，有没有可能指定时间，让程序定时查询天气？

   有几种理解：

   - 程序定时启动，自动输入城市名，调用api返回结果

     这种情况相对简单些，但是要改程序，将城市名运行作为程序启动参数传入

   - 程序手动启动，不退出，每隔一段时间如1h，自动输入城市名，调用api返回结果

     可能需要给程序加个schedule设置功能，设置内容包括：

     - 指定的时间：具体时间点，频次如每个小时	
     - 城市名
       加timer，在指定时间自动调用api

     ### 设计

     准备采取第二种方式，纯碎练手：程序手动启动，不退出，每隔一段时间如1h，自动输入城市名，调用api返回结果

     增加两个新命令和一个mode，config：

     schedule_config: json文件，允许用户修改city和schedule time (s for 固定时间，f for 频次)

     mode：将程序改为两种模式，m：手动，a: 自动。前者是初级版功能；后者为schedule模式，如果用户选择m,则和初级版功能一样；如选择a,则进入自动模式：程序先读取当前schedule_config设置，并提示用户是否修改；如用户有修改，将用户修改更新入schedule_config文件。然后自动按schedule运行。用户输入ctrl+c时中断

     - switch

       修改程序入口提示用户选择mode. 如用户选择m后，想切换到a，用此命令

     - schedule

       两种设置：s - 指定固定时间如 2017-8-20 15:00:00, f - 频次，如1s for every 1s, 1h for every 1h。

       用到sched,time模块

       frequency:

       ```
       self.scheduler.enter(float(duration),1,self.run_city,argument =(city_name,count))
       ```

       fixed time:

       ```
       self.scheduler.enterabs(datetime.now().timestamp(),1,self.run_city,argument =(city_name,count))
       ```

       **bug**

       - fixed time貌似不工作，虽然也有返回，但是像是读的frequency scheduler
       - frequency scheduler只工作一次，然后就hang着了。。。

2. 选一个国内 API 和国外 API 分别进行调用，了解不同的调用姿势。更进一步，如果你来设计 API ，你会怎么设计？

3. 给程序增加温度单位转换功能？