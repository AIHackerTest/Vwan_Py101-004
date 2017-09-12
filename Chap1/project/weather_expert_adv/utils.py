#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
存放需要调用的函数
- 从天气信息文件获得数据的函数
- 天气查询函数
- 获得用户合法输入的函数
- 中文检查函数
"""

import csv
from command import Command

command = Command()

def data_from_file(path):
    """
    从本地 txt 文件中读取格式为"city, weather"的数据
    以 {city:weather} 这样的键值对保存至 dict 中，并返回

    :param path: (str), 含有天气数据的 txt 文件绝对路径
    :return: (dict), key:value = city:weather 的 dict

    """
    dt = {}
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for city, weather in reader:
            dt[city] = weather
    print(dt)
    return dt


def weather_search(city, data_dt):
    """
    根据城市名查询对应的天气

    :param city: (str), 中文城市名
    :param data_dt: (dict), 以{city:weather} 格式存储城市天气信息的字典
    :return: 如果查到，返回 "city:weather" 格式的字符串;
              如果没查到，返回 None
    """
    weather = data_dt.get(city, None)

    if weather is None:
        print('抱歉，没有找到该城市，请确认城市名称输入正确')
        return None

    else:
        search_result = '{}:{}'.format(city, weather)
        return search_result


def iscommand(user_input):
    """

    :param user_input:
    :return:
    """
    # command_set = set(command_function_dt.keys())
    if user_input in command.commands:
        return True
    else:
        return False


def iscity(user_input):
    """
    检测字符是否只含有中文

    :param user_input:(str), 需要判断的字符串
    :return: 字符串全部为中文返回 True；否认返回False
    """

    for i in user_input:
        # 使用中文十六进制的 Unicode 字符集范围判断
        if i < '\u4e00' or i > '\u9fa5':
            return False

    return True


def get_user_input(prompt):
    """
    用于获得用户输入的合法命令或城市名，并返回

    """

    # 判断用户输入的合法性
    # 当输入的命令在命令集中或输入为中文时返回；
    # 当输入其他情况要求用户重新输入
    # 当出现异常时报错并退出程序

    while True:
        try:
            # 获得用户输入
            user_input = input(prompt)
        except Exception as err:
            from sys import exit
            print('你输入了什么？！..！@#￥%……&')
            print('Error:', err)
            exit(0)

        else:
            # 用户输入了命令
            if iscommand(user_input):
                return user_input, 'command'
            # 用户输入了中文
            elif iscity(user_input):
                return user_input, 'city'
            # 非命令非中文
            else:
                print('输入非法')
                continue


if __name__ == '__main__':
    test_time()
    # test_cprofile()
    # test_file_readtimes()
