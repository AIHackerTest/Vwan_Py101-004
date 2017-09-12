#!/usr/bin/env python3

"""
Program name: Weather Expert
Author: Vwan
Github: https://github.com/Vwan/Py101-004
Revision：v1.0
Edit date: 2017.08.15
"""

import sys
sys.path.insert(0,'../.')
import os
import requests
import utils

class WeatherBase(object):

    help_file = "../resource/help.txt"
    base_url = "https://free-api.heweather.com/v5/"

    api_key = "742459bcd8b54244b1979cb30a4a4ac7"
    commands = (
                ('h','help'),
                ('history'),
                ('exit','quit'),
                ('future')
                )

    def __init__(self,weather_config_file,weather_data_type):
        self.history = {}
        self.weather_info = utils.load_json_file(weather_config_file)
        self.weather_data_type = weather_data_type
        #self.request_param = request_param

    def retrieve_weather_data(self,url,param,**weather_info):
        city = param['city']
        try:
            resp = requests.get(url,params = param)
        except BaseException as error:
            print('An exception occurred: {}'.format(error))
            result = None
        else:
            resp_data = resp.json()
            # check if city exits
            yesno, status = utils.city_exists(city,resp_data['HeWeather5'][0])
            print(yesno,status)
            if yesno == True :
                #result = utils.parse_json(resp_data['HeWeather5'][0],**weather_info)
                result = utils.parse_json_dot(resp_data['HeWeather5'][0],**weather_info)
            else:
                city = status
                result = None
        return city,result


    def run_cmd(self,cmd,commands):
        if cmd in list(self.commands[0]): # command help
            help_text = utils.read_file(self.help_file,"r",1,'utf-8-sig')
            print(help_text)
        elif cmd in [self.commands[1]]: # command history
            utils.show_history(self.history)
        elif cmd in [self.commands[3]]: # command future
            self.doFuture()
        elif cmd in list(self.commands[2]): # command quit
            yesno = input("Are you sure to quit? (y/n)> ")
            if (yesno in ['y','Y']):
                utils.show_history(self.history)
                sys.exit(0)

    def doFuture():
        pass

    def run_city(self,url,param,count):
        city,result = self.retrieve_weather_data(url,param,**self.weather_info)
        print("----",result)
        if city == param['city']:
            # rename keys in result
            # for k,v in self.weather_info.items():
            #     result[v] = result.pop(k)
            city_weather = utils.show_weather(city,result)
            print(f"The current weather for city: \"{city}\"\n{city_weather}")
            self.history[count] = city_weather
            count += 1
        else:
            print("Not found any command or city that matches, please type 'help' for all commands")
        return count

    def main(self):
        print("""
        - 输入城市名，返回该城市最新的天气数据；
        - 输入指令，获取帮助信息（一般使用 h 或 help）；
        - 输入指令，获取历史查询信息（一般使用 history）；
        - 输入指令，退出程序的交互（一般使用 quit 或 exit）；
        """)
        if self.weather_info == None:
            print("Sorry Something went wrong and not found Available weather info, please try some time later")
            sys.exit(0)
        else:
            count = 1
            while True:
                try:
                    cmd = input("> Please enter a command or city:")
                except:
                    print("please enter a valid city or command")
                    continue
                else:
                    if (utils.cmd_exists(cmd,self.commands)):
                        self.run_cmd(cmd,self.commands)
                    else:
                        url = self.base_url + self.weather_data_type
                        request_param = {"city":cmd,"key":self.api_key}
                        count = self.run_city(url,request_param,count)

if __name__ == "__main__":
    import os
    dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))# this is so silly, how to refine?
    print(dir)
    weather_json_file = os.path.join(dir,"resource/weather_info.json")
    WeatherBase(weather_json_file,"now").main()
