from bottle import route, static_file, error

__author__ = "Aishwarya Sharma"


# Web App Entry point. Returns index.html
@route('/')
def index():
    return static_file("index.html", root="static")


# Route to serve static files. Uses regex to resolve filename.
@route('/:filename#.*#')
def static(filename):
    return static_file(filename, root="static")


# Route for 404 errors.
@error
def error():
    return static_file("404.html", root="static")
