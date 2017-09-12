from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, InputRequired

class LoginForm(FlaskForm):
    username = StringField("User Name", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember me?", default=False)
