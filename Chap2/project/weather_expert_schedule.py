#!/usr/bin/env python3

"""
Program name: Weather Expert
Author: Vwan
Github: https://github.com/Vwan/Py101-004
Revision：v1.0
Edit date: 2017.08.15
"""

import sys
import os
import requests
import utils
import sched
import time
from datetime import datetime

class WeatherExpert(object):

    help_file = "../resource/help.txt"
    weather_info_json_file = "../resource/weather_info.json"
    schedule_config_file = "../resource/schedule.json"
    url = "https://free-api.heweather.com/v5/now?city=%s&key=742459bcd8b54244b1979cb30a4a4ac7"

    commands = (('h', 'help'), ('history'), ('exit', 'quit'), ('schedule'), ('switch'))


    def __init__(self):
        self.history = {}
        self.weather_info = utils.load_json_file(
            WeatherExpert.weather_info_json_file)
        self.scheduler = sched.scheduler(time.time, time.sleep)

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
                result = utils.parse_json(resp_data['HeWeather5'][0],
                                          **weather_info)
            else:
                city = status
                result = None
        return city, awaitresult


    def run_cmd(self, cmd, commands):
        if cmd in list(self.commands[0]): # command help
            help_text = utils.read_file(self.help_file,"r", encoding='utf-8-sig')
            print(help_text)
        elif cmd in [self.commands[1]]:  # command history
            utils.show_history(self.history)
        elif cmd in [self.commands[3]]:  # command schedule
            return utils.schedule(self.schedule_config_file)
        elif cmd in [self.commands[4]]:  # command switch
            return utils.switch()
        elif cmd in list(self.commands[2]): # command quit
            yesno = input("Are you sure to quit? (y/n)> ")
            if (yesno in ['y', 'Y']):
                utils.show_history(self.history)
                sys.exit(0)

    def run_city(self, city_name, count):
        city,result = self.retrieve_weather_data_by_city(
                            city_name, **self.weather_info)
        if city == city_name:
            # rename keys in result
            # for k,v in self.weather_info.items():
            #     result[v] = result.pop(k)
            city_weather = utils.show_weather(city, result)
            print(f"The current weather for city: \"{city}\"\n{city_weather}")
            self.history[count] = city_weather
            count += 1
        else:
            print(
            f"Not found any command or city that matches with '{city_name}', please type 'help' for all commands"
            )
        return count

    def run_city_scheduled_frequency(self, city_name, frequency, count):
        if ('h' == frequency[-1]):
            duration = float(frequency.strip('h')) * 60 * 60
        elif ('m' == frequency[-1]):
            duration = float(frequency.strip('m')) * 60
        elif ('s' == frequency[-1]):
            duration = float(frequency.strip('s'))
        else:
            return "Error parsing run frequncy setting, please enter command 'schedule' and reset"

        print(
        f"Starting to retrieve weather at frequency {frequency}.....press ctrl+c to stop"
        )
        self.scheduler.enter(
            float(duration),
            1,
            self.run_city,
            argument =(city_name, count)            )

    def run_city_scheduled_time(self, city_name, schedule_time, count):
        #dt = datetime.strftime(schedule_time, "%Y-%m-%d %H:%M:%S")
        print(
        f"Starting to retrieve weather at {schedule_time}.....press ctrl+c to stop"
        )
        self.scheduler.enterabs(
            datetime.now().timestamp(),
            1,
            self.run_city,
            argument =(city_name,count))

    def main(self):
        print("""
        - 输入城市名，返回该城市最新的天气数据；
        - h/help: 获取帮助信息
        - history:获取历史查询信息
        - schedule:设置schedule
        - switch: 切换交互模式 (m / a)
        - exit/quit:退出程序的交互
        """)
        if self.weather_info == None:
            print(
            "Sorry Something went wrong and not found Available weather info, please try some time later"
            )
            sys.exit(0)
        else:
            history_count = 1
            mode = input("> Please select a mode(m for manual, a for auto):")
            while True:
                if (mode == 'm'):
                    print("You are now in Manual Mode")
                    while True:
                        try:
                            cmd = input("   > Please enter a command or city:")
                        except:
                            print("please enter a valid city or command")
                            continue
                        else:
                            if utils.cmd_exists(cmd, self.commands):
                                mode = self.run_cmd(cmd, self.commands)
                                if cmd == "switch":
                                    break
                            else:
                                history_count = self.run_city(cmd, history_count)
                elif mode == 'a':
                    print("You are now in Auto Mode")
                    schedule = utils.schedule(self.schedule_config_file)
                    if schedule != None:
                        frequency = schedule.get('frequency')
                        fixed_time = schedule.get('fixed_time')
                        city = schedule.get('city')
                        while 1:
                            try:
                                if (frequency != ''):
                                    self.run_city_scheduled_frequency(
                                        city, frequency,history_count)
                                elif (fixed_time != ''):
                                    self.run_city_scheduled_time(
                                        city, fixed_time,history_count)
                                else:
                                    print(
                                    """You have both fixed time and frequency set to None in the schedule config file,
                                    please modify and retry""")

                                self.scheduler.run()
                                sys.stdin.read()
                                mode = utils.switch()
                                break
                            except (KeyboardInterrupt):
                                scheduler.exit()
                else:
                    mode = input(
                    "> Please select a mode(m for manual, a for auto):")
                    print("Please enter a valid mode (a/m)")
                    continue

if __name__ == "__main__":
    WeatherExpert().main()
