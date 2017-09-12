#!/usr/bin/env python3

"""
Program name: Weather Expert
Author: Vwan
Github: https://github.com/Vwan/Py101-004
Revision：v1.0
Edit date: 2017.08.15
"""

import datetime
from weather_base import WeatherBase
class WeatherForecast(WeatherBase):

    url = "https://free-api.heweather.com/v5/forecast"#forecast?city=%s&key=742459bcd8b54244b1979cb30a4a4ac7"
    # def __init__(self):
    #     super(self)

    def doFuture(self):
        try:
            number_of_days = input("> please enter the number of days advance today: ")
            today = datetime.now()
            print(today)
        except Exception as err:
            print(err)

if __name__ == "__main__":
    import os
    dir = os.path.dirname(__file__)
    weather_json_file = os.path.join(dir,"weather_forecast.json")
    WeatherBase(weather_json_file,"forecast").main()
