from flask import Blueprint, render_template, request
from functions import *
main_blueprint = Blueprint('main_bluerint', __name__, template_folder='templates', url_prefix='/')


@main_blueprint.route('/')
def main_page():
    return render_template("index.html")


@main_blueprint.route('/search')
def search_page():
    substr = request.args.get('s')
    posts = search_posts(substr)
    return render_template("post_list.html", posts=posts, substr=substr)

