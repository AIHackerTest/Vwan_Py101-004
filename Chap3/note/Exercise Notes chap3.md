# 需求：

1. 完成一个

   网页版天气查询程序

   - 实现以下功能：
     - 基本功能
       - 输入城市名，获取该城市最新天气情况
       - 点击「帮助」，获取帮助信息
       - 点击「历史」，获取历史查询信息
     - 部署在命令行界面
   - 让你的 Web 应用适配移动端，让用户在手机上使用，也有良好的体验。

# 设计

后端：Flask web framework

前端：js/jquery, bootstrap, Jinja templates



## 后端

虽然是个小型web app，考虑到以后扩展和练手，用flask blueprint进行模块隔离，app config 存放静态config数据并隔离测试/开发/生成环境。

####目录结构：

app / api / 函数方法,, 存放文件读写，weather api request相关的公用方法，以后有时间转成rest

app / config: config 文件 for development/production

app / static: js, css

app / templates: 默认templates

app / weather:  weather 模块的blueprint

​			/ templates/ : blueprint specific templates

​			/ view.py: blueprint 主程序

app / init.py: 初始化app

​	/ run.py: 创建并运行app

#### app config

[Configuration Handling — Flask Documentation (0.12)](http://flask.pocoo.org/docs/0.12/config/)

每个环境分别创建一个py 文件，比如development.py如下：除了系统自带的设置外，将本app要用到的和风天气api添加了进去

```
class DevelopmentConfig(Config):
    #SERVER_NAME = 'DEVELOPMENT'
    DEVELOPMENT = True
    TESTING = True
    DEBUG = True
    EXPLAIN_TEMPLATE_LOADING = True
    HEFENG_API = {
                "HELP_FILE": "app/static/help.txt",
                "WEATHER_INFO_JSON_FILE": "app/static/weather_info.json",
                "API_KEY": "742459bcd8b54244b1979cb30a4a4ac7",
                "BASE_URL_NOW":"https://free-api.heweather.com/v5/now?city=%s&key=",
                "BASE_URL_CITY":"https://free-api.heweather.com/v5/city?city=%s&key="
                }

```

那程序如何使用各个环境呢？

在```config\__init__.py```文件中，定义了Load_config方法（参考的网上，个人觉得这个方法不错，不过他将方法的参数值存放在系统变量里，这里为了简单，就没采纳，实际生成环境中不知道是否是像他那样设计的）。

```
def load_config(env):
    if env == 'PRODUCTION':
        from .production import ProductionConfig
        return ProductionConfig
    elif env == 'DEVELOPMENT':
        from .development import DevelopmentConfig
        return DevelopmentConfig
    else:
        from .default import Config
        return Config
```

这样，init.py在设置app的时候就可以调用这个方法，将环境变量传进去了

```
def create_app(config_name):
    app = Flask(__name__)
    config = load_config(config_name)
    app.config.from_object(config)
```

run.py是程序入口，这里会创建一个app, 并执行

```
app = create_app("DEVELOPMENT")
app.run()
```

然后是具体的模块weather_view了， 处理进出的request route, template render.

创建一个blueprint，并在init.py中register

```
weather\view.py
weather_view = Blueprint('weather_view', __name__, template_folder='templates')
```

```
app\init.py
with app.app_context():
        from app.weather.view import weather_view
        app.register_blueprint(weather_view)#,url_prefix="/weather")
```

设置routes，并render template

```
@weather_view.route('/', methods=['POST'])
def view():
    try:
        # if request.form.validate_on_submit():
        if 'help' in request.form:
            result = show_help(help_file)
            return render_template('weather.html', help_text=result)
        elif 'history' in request.form:
            if len(history) != 0:
                result = reverse_dict(history)
            else:
                result = {"message": "Sorry, Not history records are found, please do some search and retry"}
            return render_template('weather.html', weather_search_history=result)
```



### 遇到的坑：

1. 加入config后，输入localhost:5000总是返回"The request url is not found on the server...", 无任何debug信息

   注释掉config中的#SERVER_NAME = 'DEVELOPMENT'一行就好了，还没有想通是什么原因，server_name应该是需要的啊

2. 在weather\view.py中试图使用flask的current_app, 总是失败“RuntimeError: working outside of application context", 原因是默认情况下current_app是request context的，你可以在route绑定的方法中用，但不能在其外。

   解决方法貌似有几种：[flask - How to access app.config in a blueprint? - Stack Overflow](https://stackoverflow.com/questions/18214612/how-to-access-app-config-in-a-blueprint)

   - 重载blueprint的 record decorator，

     ```
     weather_view.config_dict = {}
     @weather_view.record
     def record_config(setup_state):
         app = setup_state.app
         weather_view.config_dict = dict([(key, value) for key, value in app.config.items()])
         #print(config_dict)
     ```

     但卡在如何将方法中的config_dict变量值传出来，总是为空，暂时解决不了，放弃。

   - 重载register方法：没有试过

   - 在创建app时，设置current_app的scope是app_context: 成功。

     ```
     with app.app_context():
             from app.weather.view import weather_view
             app.register_blueprint(weather_view)
     ```

     在view.py中访问app config:

     ```
     config_dict = current_app.config.get('HEFENG_API')
     ```

     ### 改进

     - 看到有同学在任务提交处comment，最好由前端来处理数据的展示，觉得很有道理，改写了后端代码，改为传递相应的dict数据，而非拼接好的html string。

     这样在前端，需要用到jinja处理dict的模式了，(不喜欢这种前端，代码看着不清爽，写起来也麻烦)

     ```
     {% if weather_result %}
         {% if weather_result.get('City') %}
           <strong> The current weather for {{city}} is:</strong><p>
           {% for key, value in weather_result.items() %}
             <b>{{key}}</b> : {{value}} <br>
           {% endfor %}
         {% else %}
           <i class="glyphicon glyphicon-warning-sign"><i><font color="red"><strong>{{weather_result.get('message')}}</strong><br></font>
         {% endif %}
       {% endif %}
     ```

     **问题：**其实如果后端可以传递给前端json格式的数据，就更有好了，可适应各种前端。可是，查了试了一大通，发现貌似jinja json用的不多？虽然有个tojson filter，但是我还没找到如何loop json strings，暂时搁浅了，回头看下别的同学怎么处理的

     - 有同学展示使用base and chile template模式，觉得蛮好的，改写前端，将显示结果的代码挪到新的html文件中

       ```
       {% extends "base.html" %}
       {% block weather %}
       {% if weather_result %}
           {% if weather_result.get('City') %}
             <strong> The current weather for {{city}} is:</strong><p>
             {% for key, value in weather_result.items() %}
               <b>{{key}}</b> : {{value}} <br>
             {% endfor %}
           {% else %}
             <i class="glyphicon glyphicon-warning-sign"><i><font color="red"><strong>{{weather_result.get('message')}}</strong><br></font>
           {% endif %}
         {% endif %}
       ```

       base.html

       ```
       {% block weather %}
                       {% endblock %}
                       {% block history %}
                       {% endblock %}
                       {% block help %}
                       {% endblock %}
       ```


- 统一管理和注册blueprint

  之前是在init.py文件中单独导入weather_view注册的。考虑到以后会有多个blueprint，这样挨个导入不友好。

  新建controller folder, 将之前的weather folder挪进去；controller的```__init__.py```文件中导入各个blueprint放到列表中，然后在init.py中循环注册：

  ```
  from controller.weather.view import weather_view

  blueprint_views = [
                  weather_view
                  ]
  ```

  init.py

  ```
  with app.app_context():
          from controller import blueprint_views
          for blueprint_view in blueprint_views:
              app.register_blueprint(blueprint_view)
  ```

- 主view.py程序很臃肿，逻辑和业务没有分开，尝试用decorator重写。不过重写后仍然感觉不像是可以通用的模板，应该还可以优化，暂时还没优化头绪。

  在baseview.py中添加handler方法，作为decorator， 主要是处理render_template的通用框架。

  ```
  def handler(func):
      try:
          def inner(context_dict, **kargs):
              if kargs:
                  dict_ = func(context_dict, args)
              else:
                  dict_ = func(context_dict)
              print(dict_, "+++++")
              return render_template(template_file, **dict_)
          return inner
      except TemplateNotFound:
          abort(404)
  ```

  然后定义各个功能的render程序：context_dict中存放将在template中传入前端的contexts，以及需要的业务数据

  ```
  @handler
  def render_history(context_dict, **view):
      dict_ = {}
      context_history = context_dict.get('context_history')
      history_data = context_dict.get('history_data')
      result = do_history(history_data)
      dict_[context_history] = result
      return dict_
  ```

  在blueprint view中这么调用：

  ```
  if 'help' in request.form:
              return render_help({"context":'help_text'})
          elif 'history' in request.form:
              return render_history({"context_history":'weather_search_history',
                                      "history_data":history})
          elif 'search' in request.form:
              city = request.form['city'].strip()
              result, city_exists = do_search(city)
              if city_exists:
                  history[weather_view.count] = result
                  weather_view.count += 1
              return render_search({
                              "city":city,
                              "context_city":"city",
                              "context_result":'weather_result',
                              "weather_result_data":result })
  ```

  **问题：**

  - 在decorator和主view程序中都用了try..except，感觉应该可以在主view程序中去掉。
  - 持续优化

## 前端

前端到处是坑，繁琐，实在是搞不好，页面大小布局就只将就能用就好。

** 目录结构：**

app\static\ 存放静态文件，如css, js 及json数据文件等

app\templates: global html files

app\<blueprint>\templates: blutprint specific html files.

因为内容不多，单一页面即可解决，设计base.html 和 weather.html(child) 放在weather\templates folder下

**具体页面设计：**

利用bootstrap的container-fluid流布局，并加上meta标签 ```<meta name="viewport" content="width=device-width, initial-scale=1">```， 据说可以支持mobile显示，（还没试。。。）

页面主要由表单构成，input + 若干submit button，比较简单。

比较难处理的是Input field的用户友好性：

- autocomplete：form input 有个autocomplete属性，设为on，即可实现，就是不是很好看
- dropdown list with pre-populated city names 需要从后端传入city List json，没有合适的api，单从文件中读取不是很实际，暂时放弃
- combobox with autocomplete：网上搜到twitter typeahead input, 漂亮，既支持用户自定义输入，还可以根据用户输入自动显示可选列表，降低用户输错几率。

**问题/坑：**

- 如果判断是哪个submit button 的提交？

  感觉应该有很多种方式：

  - 目前处理是在后端，通过判断前端传过来的submit button的name，如

  ```
  if 'help' in request.form:
  ```

  这种方式和前端绑定了，万一前端button name改变了，后端就不work了，应该不是好的处理方式

  - 放到前端处理，通过js，在post之前先拿到是哪个button submit的，然后后端做相应处理，但问题是flask如何处理，它咋知道传过来的是help还是history? 除非route到不同的url?
  - 还有额?


- how to pass html content to Jinja template?[Template Designer Documentation — Jinja2 Documentation (2.10-dev)](http://jinja.pocoo.org/docs/dev/templates/#html-escaping)

  两种方法，

  1. 在template html 文件中，设置{{cityname**|safe**}}， 可自动escape一些特殊符号

  2. use flask Markup

     ```
     from flask import Markup
     value = Markup('<strong>The HTML String</strong>')
     ```

- 加了 typeahead text 的css后，发现表单中的label, input, button都不能顶对齐了，特难看，找了好久，解决：by default, vertical-align的值是top, 但却没有top align，换成baseline就可以了。

  ```
    input {
        position: relative;
        vertical-align: baseline !important;
        background-color: transparent;
    }
  ```

- typeahead css放到自定义的app\static\custom\app.css中时不工作，只能先放到base.html inline了，不知道为何