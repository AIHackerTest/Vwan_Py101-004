import pytest
from utils import city_exists
import json
import ast

class TestUtils(object):
    cities = ['北京']
    weather_info = ['basic.city','update.utc','now.cond.txt']
    json_file = "../resource/result.json.txt"



    def test_city_exists(self):
        data = self.load_json_file(TestUtils.json_file)
        for city in TestUtils.cities:
            assert city_exists(city,data) == True
