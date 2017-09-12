#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Program name: Weather Expert
Author: Vwan
Github: https://github.com/Vwan/Py101-004
Revision：v1.0
Edit date: 2017.08.15
"""

__title__ = "Weather Expert"
__version__ = "V1.0.0.1"
__author__ = "vwan<vivian_jh3@hotmail.com>"
__lisence__ = "MIT@2017-08"

import sys
import os
import requests
import utils
from collections import namedtuple
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter
import operator

class WeatherExpert(object):

    help_file = "../resource/help.txt"
    weather_info_json_file = "../resource/weather_info.json"
    city_names_file = "../resource/citynames.csv"
    url = "https://free-api.heweather.com/v5/now?city=%s&key=742459bcd8b54244b1979cb30a4a4ac7"
    api_key = "742459bcd8b54244b1979cb30a4a4ac7"
    # commands = (
    #             ('h','help'),
    #             ('history'),
    #             ('exit','quit')
    #             )
    Commands = namedtuple('Commands', 'help history exit')
    commands = Commands(('h', 'help'),'history',('exit', 'quit'))

    def __init__(self):
        self.history = {}
        self.weather_info = utils.load_json_file(
                            WeatherExpert.weather_info_json_file)
        self.commands_list = utils.convert_tuple_to_list(self.commands)
        self.cities = utils.load_all_cities_from_csv(self.city_names_file,
                                                    '英文', '中文')

    def retrieve_weather_data_by_city(self, city, **weather_info):
        try:
            resp = requests.get(self.url % city)
        except:
            result = None
        else:
            resp_data = resp.json()
            # check if city exits
            yesno, status = utils.city_exists(city, resp_data['HeWeather5'][0])
            if yesno == True :
                #result = utils.parse_json(resp_data['HeWeather5'][0],**weather_info)
                result = utils.parse_json_dot(resp_data['HeWeather5'][0],
                                                **weather_info)
            else:
                city = status
                result = None
        return city, result

    def run_cmd(self, cmd, commands):
        cmd_dict = {
            commands.help: lambda: print(utils.read_file(self.help_file, "r", 100, encoding='utf-8-sig')),
            commands.history: lambda: utils.show_history(self.history),
            commands.exit: lambda: (utils.show_history(self.history), sys.exit(0))
        }
        for k, v in cmd_dict.items():
            if cmd in k:
                cmd_dict.get(k)()
                break

    def run_city(self, cmd, count):
        city, result = self.retrieve_weather_data_by_city(
                                    cmd, **self.weather_info)
        if city == cmd:
            city_weather = utils.show_weather(city, result)
            print(f"The current weather for city: \"{cmd}\"\n{city_weather}")
            self.history[count] = city_weather
            count += 1
        else:
            print(
            "Not found any command or city that matches, please type 'help' for all commands"
            )
        return count

    def main(self):
        word_completer = WordCompleter(self.commands_list + self.cities)
        print("""
        - 输入城市名，返回该城市最新的天气数据；
        - 输入指令，获取帮助信息（一般使用 h 或 help）；
        - 输入指令，获取历史查询信息（一般使用 history）；
        - 输入指令，退出程序的交互（一般使用 quit 或 exit）；
        """)
        if self.weather_info == None:
            print(
            "Sorry Something went wrong and not found Available weather info, please try some time later"
            )
            sys.exit(0)
        else:
            count = 1
            while 1:
                try:
                    cmd = prompt(
                            "> Please enter a command or city:",
                            history = FileHistory("history.txt"),
                            auto_suggest = AutoSuggestFromHistory(),
                            completer = word_completer
                            )
                except BaseException as err:
                    #print(err)
                    print("please enter a valid city or command")
                    continue
                else:
                    if (utils.cmd_exists(cmd, self.commands)):
                        self.run_cmd(cmd, self.commands)
                    else:
                        count = self.run_city(cmd, count)

if __name__ == "__main__":
    WeatherExpert().main()
