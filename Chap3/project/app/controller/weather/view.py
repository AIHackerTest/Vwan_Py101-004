from flask import Blueprint, render_template, abort, request, current_app
from jinja2 import TemplateNotFound
from api.utils import (load_json_file,
                            read_file,
                            reverse_dict,
                            show_help)
import json
from controller.baseview import (
                                weather_config,
                                render_help, render_history, render_search, do_search
                                )

weather_view = Blueprint('weather_view', __name__, template_folder='templates')

history = {}
weather_view.count = 1

@weather_view.route('/', methods=['GET'])
def home():
    return render_template('weather.html')

@weather_view.route('/', methods=['POST'])
def view():
    try:
        if 'help' in request.form:
            return render_help({
                                    "template_file":"weather.html",
                                    "help_text":'help_text'})
        elif 'history' in request.form:
            return render_history({
                                    "template_file":"weather.html",
                                    "weather_search_history":'weather_search_history',
                                    "history_data":history
                                    })
        elif 'search' in request.form:
            city = request.form['city'].strip()
            result, message = do_search(city)
            if not message:
                history[weather_view.count] = result
                weather_view.count += 1
            return render_search({
                            "template_file":"weather.html",
                            "city_data":city,
                            "city":"city",
                            "weather_result":'weather_result',
                            "weather_result_data":result,
                            "message":message})
        else:
            pass
    except TemplateNotFound:
        abort(404)
