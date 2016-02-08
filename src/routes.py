from bottle import route, error, post, request
from jinja2 import Environment, FileSystemLoader
from database import word_matcher
import os

__author__ = "Aishwarya Sharma"


# Specifies that our templates are located in the "templates" folder inside
# the "src" python package
path_to_templates = os.path.dirname(os.path.abspath(__file__)) + "/templates"
template_env = Environment(
    loader=FileSystemLoader(path_to_templates, followlinks=True))


# Web App Entry point. Returns index.html
@route('/')
@route('/index')
@route('/home')
def index():
    return template_env.get_template("home.html").render()


# Searching for words matching given criteria.
@post('/search')
def search():
    try:
        char_list = str(request.forms.get('charSet')).strip().lower()
        word_length = int(str(request.forms.get('wordLength')).strip())
    except ValueError:
        print("Had a value error")
        return template_env.get_template("search_error.html").render()

    if char_list == "":
        print("Char list is empty")
        return template_env.get_template("search_error.html").render()

    words = word_matcher.get_matching_words(char_list, word_length)

    if words is None or len(words) == 0:
        print("No Matching words found")
        return template_env.get_template("search_error.html").render()

    return template_env.get_template("search_results.html").render(words=words)


# Route for 404 errors.
@error(404)
def error404(error):
    return template_env.get_template("404.html").render()
