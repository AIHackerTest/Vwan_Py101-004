
from api.utils import load_json_file
from flask import Flask
from config import load_config

def create_app(config_name):
    app = Flask(__name__)
    config = load_config(config_name)

    app.config.from_object(config)
    with app.app_context():
        from controller import blueprint_views
        for blueprint_view in blueprint_views:
            app.register_blueprint(blueprint_view)#,url_prefix="/weather")
    # print(app.url_map)
    # print(app.config)
    # print(app.config['SERVER_NAME'])
    return app
