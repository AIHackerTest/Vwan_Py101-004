from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, InputRequired

class WeatherForm(FlaskForm):
    city = StringField("City", validators=[InputRequired()])
    class Meta:
        csrf = False
