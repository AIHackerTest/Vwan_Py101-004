# HTML Form

表单中的name属性很重要。

| <input type="text">   | Defines a one-line text input field      |
| --------------------- | ---------------------------------------- |
| <input type="radio">  | Defines a radio button (for selecting one of many choices) |
| <input type="submit"> | Defines a submit button (for submitting the form) |



Each input field must have a **name** attribute to be submitted.

If the **name** attribute is omitted, the data of that input field will not be sent at all.

```
 <select name="cars">
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="fiat">Fiat</option>
  <option value="audi">Audi</option>
</select> 
```



# Flask

**如何设置和启动flask:**

use 'export' on mac.

```
λ set FLASK_APP=weather_expert_app.py
λ set FLASK_DEBUG=1
λ flask run
 * Serving Flask app "weather_expert_app"
 * Forcing debug mode on
weather_expert_app
 * Restarting with stat
weather_expert_app
 * Debugger is active!
 * Debugger PIN: 451-597-413
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```



### converters

The following converters exist:

| string | accepts any text without a slash (the default) |
| ------ | ---------------------------------------- |
| int    | accepts integers                         |
| float  | like `int` but for floating point values |
| path   | like the default but also accepts slashes |
| any    | matches one of the items provided        |
| uuid   | accepts UUID strings                     |



To access parameters submitted in the URL (`?key=value`) you can use the`args` attribute:

```
searchword = request.args.get('key', '')
```



If you want to get hold of the resulting response object inside the viewyou can use the [`make_response()`](http://flask.pocoo.org/docs/0.12/api/#flask.make_response) function.

Imagine you have a view like this:

```
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

```

You just need to wrap the return expression with[`make_response()`](http://flask.pocoo.org/docs/0.12/api/#flask.make_response) and get the response object to modify it, then return it:

```
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp
```



## Blueprint

## how does blueprint use flask app config

[Configuration Handling — Flask Documentation (0.12)](http://flask.pocoo.org/docs/0.12/config/)

### multiple submits on a single form



### Flask-WTF

```
pip install Flask-WTF
```

# Jinja Template

Objects:

- request

- session

- g

  function:

  - `flask.``get_flashed_messages`(*with_categories=False*, *category_filter=[]*)

### Template loading principle

在用flask blueprint的时候，发现template_folder folder怎么都找不到，

```
weather_view = Blueprint('weather_view', __name__, template_folder='client\\templates')
```

查看C:\python\Python36-32\Lib\site-packages\flask\helpers.py，试着打印其查找路径：

```
@locked_cached_property
    def jinja_loader(self):
        """The Jinja loader for this package bound object.

        .. versionadded:: 0.5
        """
        if self.template_folder is not None:
            print("----",os.path.join(self.root_path,self.template_folder))
            return FileSystemLoader(os.path.join(self.root_path,
                                                 self.template_folder))
```

发现顺序是这样的：

---- C:\Users\vivia\OneDrive\Projects\OpenMind\Py101-004-Vwan\Py101-004\Chap3\project\app\templates

---- C:\Users\vivia\OneDrive\Projects\OpenMind\Py101-004-Vwan\Py101-004\Chap3\project\app\**weather**\client\templates

对应的目录结构是这样的：

app\templates\

app\weather\templates\

### base and child template

通过在base template中添加 block 块，可以在运行时将child template中的内容拼接起来，达到reuse 和 concise的目的。

base

```
  {% block weather %}
                {% endblock %}
```

child

```
{% extends "base.html" %}
{% block weather %}
your contents
   {% endblock %}
```



### json

jinja提供了tojson filter, 可以将后端传过来的字典转换成json格式，但是后续如何使用这个json格式目前还没头绪

```
{# set weather_search_history = weather_search_history|tojson #}
```



# HTTP Methods

### post vs put 幂等

`POST`

The browser tells the server that it wants to *post* some newinformation to that URL and that the server must ensure the data isstored and only stored once.  This is how HTML forms usuallytransmit data to the server.

`PUT`

Similar to `POST` but the server might trigger the store proceduremultiple times by overwriting the old values more than once.  Now youmight be asking why this is useful, but there are some good reasonsto do it this way.  Consider that the connection is lost duringtransmission: in this situation a system between the browser and theserver might receive the request safely a second time without breakingthings.  With `POST` that would not be possible because it must onlybe triggered once.

# Dict

字典中的key是乱序的，如果希望按照一定顺序的key输出value，可以使用sorted方法, 将key排序。

```
keys = sorted(data_dict.keys(), reverse=True)
```

Scott教练指点，不需要调用keys()方法，应该是sorted方法会自动调用（没看到源码），更改如下：

```
keys = sorted(data_dict, reverse=True)
```



# 2017-09-05

### Flask WTForm

WTF 可以从后端设计前端form，挺诱人的，实践了一下: [Flask-WTF — Flask-WTF 0.14](https://flask-wtf.readthedocs.io/en/stable/)

首先安装flask-wtf package:

```
pip install Flask-WTF
```

创建一个FlaskForm子类的form class, form上创建一个label 和 input field;  

```
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, InputRequired

class WeatherForm(FlaskForm):
    city = StringField("City", validators=[InputRequired()])
    class Meta:
        csrf = False
```

StringField 方法会在form上创建一个City label, 以及city input field， 对应前端的jinja2 render如下：

```
{{form.city.label}} {{form.city(size=50)}}
```

运行时会自动生成下面的html tags

```
 <label for="city">City</label> 
 <input id="city" name="city" size="50" type="text" value="">
```

这就省却了手动创建了，爽。

而且可以在后端增加很多validation, 在render template之前先validate form data, 不过还没试。待以后试试， 先把官网的抄下来：

```
@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)
```

不过玩的时候遇到个坑，关于csrf security的，目前对这个毫不了解，必须disable csrf才能继续玩下去，没找到哪儿disable, 但是误打误撞在template file中加了下面的这个通过了：

```
{{ form.csrf_token }}
```



# 2017-09-06

### Jenkins

Reference

- [Welcome | Flask (A Python Microframework)](http://flask.pocoo.org/)
- [Quickstart — Flask Documentation (0.12)](http://flask.pocoo.org/docs/0.12/quickstart/) 

其它参考资料： [What is a Web Framework? - Jeff Knupp](https://www.jeffknupp.com/blog/2014/03/03/what-is-a-web-framework/)



[HTTP Methods - Flask](http://flask.pocoo.org/docs/0.12/quickstart/#http-methods)

[Accessing Request Data - Flask](http://flask.pocoo.org/docs/0.12/quickstart/#accessing-request-data)



[模板设计者文档 — Jinja2 2.7 documentation](http://docs.jinkan.org/docs/jinja2/templates.html)

- Jinja2 官方文档：[Welcome to Jinja2 — Jinja2 Documentation (2.9)](http://jinja.pocoo.org/docs/2.9/)
- 英文阅读困难，可参考：[欢迎来到 Jinja2 — Jinja2 2.7 documentation](http://docs.jinkan.org/docs/jinja2/index.html)
- Flask 官方文档对模板的说明：[Rendering Templates — Flask Documentation (0.12)](http://flask.pocoo.org/docs/0.12/quickstart/#rendering-templates)



- [Cascading Style Sheets - Wikipedia](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [HTML Styles - CSS](http://www.w3schools.com/html/html_css.asp)
- [CSS Tutorial](http://www.w3schools.com/css/)
- [CSS Fonts - w3school](http://www.w3schools.com/css/css_font.asp)


- [Bootstrap · The world's most popular mobile-first and responsive front-end framework.](http://getbootstrap.com/)
- 英文阅读困难，可参考：[Bootstrap 中文网](http://www.bootcss.com/)


[Growth Mindset vs. Fixed Mindset - YouTube](https://www.youtube.com/watch?v=KUWn_TJTrnU#t=11.370861)



Web 开发与前面的章节不同，不仅涉及到 Python 语言，还涉及到 HTML 页面等。

![img](http://openmindclub.qiniudn.com/web0_knowledge_map.png)

本章的知识地图：

- Flask 框架初接触

  - 使用 Flask 完成 HelloWorld 页面
    - 直接使用 return 返回页面内容

- 为网页添加路由

  - 使用 route( ) 修饰器
  - 为不同的链接定义不同的函数

- 搭建基本 HTML 页面

  - HTML 基础知识
  - HTML 页面最小必备要素
  - 使用 CSS 修饰 HTML 页面
  - 使用 Bootstrap 、UIkit 搭建页面（可选）

- 使用表单，实现互动

  - 使用 Html 原生表单组件
    - 常用的输入框 `<input />`, 按钮 `<button></button>`, 超链接 `<a></a>` 等  
    - 表单 `<form></form>`, 容器 `<div></div>`
    - 使用 CSS 美化表单
  - 使用 Flask-WTF 和 wtforms 扩展（可选）
    - 继承 Flask-WTF 的 FlaskForm 类来自定义表单
    - 定义表单项目
      - wtforms 的 StringField, SubmitField, SelectField 等等
    - 为表单增加验证器
      - wtforms.validators

- 网页模板的使用

  - 页面模板的定义
  - 为模板传入变量
  - 在模板中使用表单
    - {{ form.name.label }} {{ form.name }}

- 进阶任务：使用 Bootstrap 框架（可选）

  - 安装和使用 Bootstrap

  - 在页面模板中引用 Bootstrap

  - 引入 Flask-WTF 快速绘制表单

    ​

    基于 Python 的 Web 框架有哪些？

    ```
      有 Django 、Flask 、Tornado 等，课程推荐使用轻量级的 Flask 。
    ```

你还可以通过 Flask 插件 Flask-WTF 实现可交互的表单页面。此部分供学有余力的同学探索。

**安装：**

在命令行输入 `pip install Flask-WTF` 即可安装 Flask-WTF

**初次使用：**

Flask-WTF 最方便的地方，在于不用再手工定义表单的各个元素，直接定义表单的各个部分即可。

先在视图函数定义表单：

```
from flask_wtf import FlaskForm     # 导入 FlaskForm
from wtforms import TextField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):    # 继承 FlaskForm 表单
    name = TextField('name', validators=[DataRequired()])  # name 是字符输入框，加入了必须填写的验证器

```

在视图函数中，读取表单内容，并将表单内容传递入 `submit.html` 模板：

```
@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)

```

我们还需要在 `submit.html` 模板中，把表单“画”出来：

```
<form method="POST" action="/">
    {{ form.csrf_token }}
    {{ form.name.label }} {{ form.name(size=20) }}
    <input type="submit" value="Go">
</form>

```

参考资料：[Quickstart — Flask-WTF 0.14](https://flask-wtf.readthedocs.io/en/stable/quickstart.html)