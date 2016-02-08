from bottle import run
from routes import *

__author__ = "Aishwarya Sharma"

if __name__ == "__main__":
    # Starting Server
    run(host="localhost", port=80, debug=True)
