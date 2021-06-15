import logging.config

from flask import Flask


def init_routes():
    from app import routes
    routes.init()


logging.config.fileConfig('app/logging.conf')

app = Flask(__name__)
init_routes()
