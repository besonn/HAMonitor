from flask import Flask

from com.model import db

from views.home import bp as home_bp

def create_app(app_name):
    app = Flask(app_name)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(home_bp)
    db.init_app(app)
    return app
