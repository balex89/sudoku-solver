from flask import Flask


def init_routes():
    from app import routes


app = Flask(__name__)
init_routes()
