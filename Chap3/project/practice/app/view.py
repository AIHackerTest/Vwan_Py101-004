from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__, template_folder='client/templates')

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)

@simple_page.route('/', methods=['GET'])
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)
