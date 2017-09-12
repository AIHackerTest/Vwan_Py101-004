
"""
Maintain blueprints
"""
from controller.weather.view import weather_view
from controller.weather_wtf.view_wtf import weather_view_wtf
from controller.login.view import login_form_wtf

blueprint_views = [
                weather_view,
                weather_view_wtf,
                login_form_wtf
                ]

print("---++++---",blueprint_views)
