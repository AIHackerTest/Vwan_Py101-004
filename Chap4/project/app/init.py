
from api.utils import load_json_file
from flask import Flask
from config import load_config
import api.db_helper as dbhelper

def setup_db(db_name, table_name):
    dbhelper.setup(db_name, table_name)

def create_app(config_name):
    app = Flask(__name__)
    config = load_config(config_name)
    app.config.from_object(config)
    db_name = app.config.get('SQLITE_DB')['DB_NAME']
    table_name_weather = app.config.get('SQLITE_DB')['TABLE_NAME_WEATHER']
    setup_db(db_name, table_name_weather)
    with app.app_context():
        from controller import blueprint_views
        for blueprint_view in blueprint_views:
            app.register_blueprint(blueprint_view)
    # print(app.url_map)
    # print(app.config)
    # print(app.config['SERVER_NAME'])
    return app
