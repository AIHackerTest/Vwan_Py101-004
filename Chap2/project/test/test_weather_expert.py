import pytest
from weather_expert import WeatherExpert as wex
import utils

class TestWeatherExpert(object):
    cities = ['北京']
    weather_info = ['basic.city','update.utc','now.cond.txt']
    weatherx = wex()
    #
    # def test_retrieve_weather_data_by_city(self):
    #     for city in TestWeatherExpert.cities:
    #         url = "https://free-api.heweather.com/v5/now?city=%s&key=742459bcd8b54244b1979cb30a4a4ac7" % city
    #         print( self.weatherx.retrieve_weather_data_by_city(city,TestWeatherExpert.weather_info))
