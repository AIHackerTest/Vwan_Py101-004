from flask import Blueprint, render_template, abort, request, current_app, session, url_for, redirect
from jinja2 import TemplateNotFound
from wtf_forms.login_form import LoginForm
from controller.baseview import render_login
from controller.weather.view import view as weather_view

login_form_wtf = Blueprint('login_form_wtf', __name__, template_folder='templates')

history = {}
@login_form_wtf.route('/', methods=['GET'])
def login():
    form = LoginForm()
    return render_login({
                        "template_file":"login.html",
                        "form": form})

@login_form_wtf.route('/', methods=['GET', 'POST'])
def view():
    try:
        form = LoginForm()
        # if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if username == "admin" and password == "admin":
            session['user'] = username
            if 'login' in request.form:
                #print(url_for(weather_view()))
                return render_template("/weather/weather.html", username=username)
            else:
                return render_login({
                                    "template_file":"login.html",
                                    "form": form})
        if 'user' in session:
            return render_template("/weather/templates/weather.html", form=form)

    except TemplateNotFound:
        abort(404)
