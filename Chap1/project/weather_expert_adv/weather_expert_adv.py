#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Program name: 问天
Author: thxiami
Github: https://github.com/thxiami/
Edition：v1.0
Edit date: 2017.08.15
"""
from history import History
from user import User
from command import Command
from utils import (data_from_file,
                    weather_search,
                    get_user_input,
                   )

def response_by_input(command,user, weather_info_dt):
    """
    根据用户请求的关键词返回对应的结果
    """
    # 根据用户请求调用不同函数调用不同函数
    if user.key_type == 'city':
        weather_result = weather_search(user.key, weather_info_dt)
        # 如果查到了结果
        if weather_result is not None:
            print(weather_result)
            user.history.add_records(weather_result)
    else:# 不是指令，那用户输入的请求就是中文
        command_func = getattr(command, user.key, None)
        try:
            if command_func and callable(command_func):
                command_func()
        except:
            command_func(user)


def run(data_path):
    """
    主函数，调用后运行天气查询程序
    """


    # 读取天气数据
    weather_info_dt = data_from_file(data_path)

    # 初始化用户请求实例，需传入
    user = User()
    command = Command()
    while True:
        # 获得用户输入的查询字符串
        prompt = '请输入城市名或指令,输入 help 获得帮助信息：  >'
        user_input = get_user_input(prompt)

        user.key = user_input[0]
        user.key_type = user_input[1]
        # print (user.key)
        # print (user.key_type)

        # 根据用户请求调用不同函数调用不同函数
        response_by_input(command,user, weather_info_dt)


def main():
    data_path = 'weather_info.txt'
    run(data_path)


if __name__ == '__main__':
    main()
