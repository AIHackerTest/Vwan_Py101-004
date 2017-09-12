from flask import Flask
from view import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)

app.run()
