#!/usr/bin/env python3

"""
Program name: Weather Expert
Author: Vwan
Github: https://github.com/Vwan/Py101-004
Revision：v1.0
Edit date: 2017.08.21
"""

import sys
import os
import requests

class weather_expert(object):

    help_file = "../resource/help.txt"

    history = {}
    commands = (
                ('h','help'),
                ('history'),
                ('exit','quit')
                )
    weather_info = {}

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
        self.load_weather_data(self.weather_info_file)

    def read_file(self,filename,mode,buffer,encoding=None):
        with open(filename,mode,buffer,encoding) as file:
            return file.read()

    def show_history(self,history):
        if (len(self.history) == 0):
            print ("Not history records are found, please do some search and retry")
        else:
            for k,v in self.history.items():
                print(f"{k} {v}")

    def _city_exists(self,city):
        if self.weather_info.get(city, None) is not None:
            return True
        else:
            return False

    def _cmd_exists(self,cmd):
        if any(cmd in e for e in self.commands):
            return True
        else:
            return False

    def show_weather(self,city,weather_info):
        city_weather = weather_info.get(city)
        # set to Unknown if weather is empty from the source data
        if city_weather == "":
            city_weather = "未知天气"
        return city_weather

    #def get_all_commands(filename):

    def main(self):
        print("""
        Welcome to Weather Expert
        Enter a city name and return the weather information for the city
        Enter command "h" or "help" and return the help text
        Enter command "history" and return the list of search history records
        Enter commdnd "exit" or "quit",display the history and exit the Program
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
                # check if user input is in the commands tuple,
                # if not, check if it's a valid city name and return city weather_info
                # if city not found, print non-match hints
                if (self._cmd_exists(cmd)):
                    if cmd in list(self.commands[0]): # command help
                        help_text = self.read_file(self.help_file,"r",1,'utf-8-sig')
                        print(help_text)
                    elif cmd == self.commands[1]: # command history
                        self.show_history(self.history)
                    elif cmd in list(self.commands[2]): # command quit
                        yesno = input("Are you sure to quit? (y/n)> ")
                        if (yesno in ['y','Y']):
                            self.show_history(self.history)
                            sys.exit(0)
                        else:
                             continue
                elif self._city_exists(cmd) == True:
                        city_weather = self.show_weather(cmd,self.weather_info)
                        print(f"The weather for city \"{cmd}\" : {city_weather} ")
                        self.history[count] = cmd + " " + city_weather
                        count += 1
                else:
                    print("Not found any command or city that matches, please type 'help' for all commands")


if __name__ == "__main__":
    weather_expert().main()
