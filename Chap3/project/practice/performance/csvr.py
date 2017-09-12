import csv
csvfile = "weather_info0.csv"

def get_weather1(location):
    with open(csvfile, 'rt',encoding='utf-8-sig') as f: # ’t‘指以文本模式读入，在python3中，'r'和'rt'没有区别，但是「explicit is better than implicit」
        f_csv = csv.reader(f) # csv.reader()读入，返回一个csv.reader对象，是一个迭代器，使用for循环取出后，为一个多行列表。
        headers = next(f_csv) # 跳过迭代器的第一行，先前我们加入了location,weather表头
        for row in f_csv: # row是一个多行列表
            if row[0] == location: # 逐行对列表进行判定，当判定为用户输入地址时
                return row[1] # 返回天气信息。

def get_weather2(location):
    with open(csvfile,"r",624,'utf-8-sig') as f:
        data_list = [list(x.rstrip().split(",")) for x in list(f)]
        return dict(data_list)[location]

def get_weather3(location):
    with open(csvfile,"r",624,'utf-8-sig') as f:
        for line in f.readlines():
            content = line.split(",")
            if location in content:
                return content[1]

location = '北京4284'
print(get_weather1(location))
print(get_weather2(location))
print(get_weather3(location))
import timeit
import dis
t1 = timeit.timeit("get_weather1(location)", setup="from __main__ import get_weather1, location", number=1)
t2 = timeit.timeit("get_weather2(location)", setup="from __main__ import get_weather2, location", number=1)
t3 = timeit.timeit("get_weather3(location)", setup="from __main__ import get_weather3, location", number=1)
print("t1: ",t1)
print("t2: ",t2)
print("t3: ",t3)
#dis.dis(get_weather3)
# dis.show_code(get_weather2)

def foo():
    a = 2
    b = 3
    return a + b

foo.__code__
# foo.func_code
