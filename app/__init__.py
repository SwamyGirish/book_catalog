# app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()

bootstrap_instance = Bootstrap()

def create_app(config_type): # dev, test, prod
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)

    db.init_app(app) # bind database to flask app

    bootstrap_instance.init_app(app) # initialize bootstrap

    from app.catalog import main # import blueprint
    app.register_blueprint(main)  # register blueprint

    from app.auth import authentication # import authentication blueprint
    app.register_blueprint(authentication)

    return app