from flask import request, current_app, render_template
from jinja2 import TemplateNotFound
import api.utils as utils
import api.request_handler as reqhandler

import api.db_helper as dbhelper

config_dict = current_app.config.get('HEFENG_API')  # weather_config(current_app)
api_key = config_dict.get('API_KEY')
weather_info_json_file = config_dict.get('WEATHER_INFO_JSON_FILE')
weather_info = utils.load_json_file(weather_info_json_file)
url_now = config_dict.get('BASE_URL_NOW') + api_key
url_city = config_dict.get('BASE_URL_CITY') + api_key
help_file = config_dict.get('HELP_FILE')
help_text = utils.read_file(help_file, 'r', 642, encoding='utf-8')
template_file = "weather.html"

def weather_config(app):
    config_dict = app.config.get('HEFENG_API')
    return config_dict

def handler(func):
    try:
        def inner(context_dict, **kargs):
            if kargs:
                dict_ = func(context_dict, args)
            else:
                dict_ = func(context_dict)
            template_file = context_dict.get('template_file')
            return render_template(template_file, **dict_)
        return inner
    except TemplateNotFound:
        abort(404)

# def dict_(context_dict, asciifunc):
#     dict_ = {}
#     for key, value in context_dict.items():
#         dict_[key] = value
#     def inner(**kargs):
#         return func(kargs)
#     return inner

@handler
# @dict_
def render_help(context_dict):
    dict_ = {}
    for key, value in context_dict.items():
        dict_[key] = value
    dict_["help_text"], dict_['message'] = utils.show_help(help_file)
    return dict_

@handler
def render_history(context_dict, **view):
    dict_ = {}
    for key, value in context_dict.items():
        dict_[key] = value
    result, dict_['message'] = do_history()
    dict_['weather_search_history'] = result
    return dict_

@handler
def render_search(context_dict, **view):
    dict_ = {}
    for key, value in context_dict.items():
        dict_[key] = value
    city = context_dict.get('city_data')
    dict_['city'] = city
    dict_['weather_result'] = context_dict.get('weather_result_data')
    print(dict_)
    return dict_

@handler
def render_login(context_dict, **view):
    dict_ = {}
    for key, value in context_dict.items():
        dict_[key] = value
    return dict_

def do_search(city):
    weather_result = message = None
    city_exists, message = reqhandler.city_exists(url_city, city)
    print("city exists?:", city_exists)
    if city_exists and message == "ok":
        weather_result = reqhandler.retrieve_weather_data_by_city(url_now % city, **weather_info)
        message = weather_result.get('message')
        if weather_result:
            dbhelper.insert_(weather_result)
    return weather_result, message

def do_history():
    result = message = None
    print(dbhelper.count_(), "--------------")
    if dbhelper.count_() != 0:
        result = dbhelper.search_()
        print(result, "----------------")
    else:
        #result = {"message": "Sorry, Not history records are found, please do some search and retry"}
        message = "Sorry, Not history records are found, please do some search and retry"
    return result, message
