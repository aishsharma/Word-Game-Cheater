from bottle import run
import cherrypy
from routes import *

__author__ = "Aishwarya Sharma"

if __name__ == "__main__":
    # Starting Server
    run(server="cherrypy", host="localhost", port=8080, debug=True)
