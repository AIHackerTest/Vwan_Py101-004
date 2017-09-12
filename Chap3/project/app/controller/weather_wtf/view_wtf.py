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
from wtf_forms.weather_form import WeatherForm

weather_view_wtf = Blueprint('weather_view_wtf', __name__, template_folder='templates', url_prefix='/wtf')

history = {}
weather_view_wtf.count = 1

@weather_view_wtf.route('/', methods=['GET'])
def home():
    form = WeatherForm()
    return render_template('weather_wtf.html', form=form)

@weather_view_wtf.route('/', methods=['POST'])
def view():
    try:
        form = WeatherForm()
        #if form.validate_on_submit():
        if 'help' in request.form:
            return render_help({
                                "template_file":"weather_wtf.html",
                                "help_text":'help_text',
                                "form": form})
        elif 'history' in request.form:
            return render_history({
                                    "template_file":"weather_wtf.html",
                                    "weather_search_history":'weather_search_history',
                                    "history_data":history,
                                    "form": form})
        elif 'search' in request.form:
            city = form.city.data
            result, message = do_search(city)
            if not message:
                history[weather_view_wtf.count] = result
                weather_view_wtf.count += 1
            return render_search({
                            "template_file":"weather_wtf.html",
                            "city_data":city,
                            "city":"city",
                            "weather_result":'weather_result',
                            "weather_result_data":result,
                            "message":message,
                            "form": form})
        else:
            pass
    except TemplateNotFound:
        abort(404)
