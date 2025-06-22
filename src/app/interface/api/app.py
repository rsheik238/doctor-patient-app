from flask import Flask
from app.core.container import Container
from app.interface.api.routes import blueprints

container = Container()

def create_app():
    app = Flask(__name__)
    app.container = container
    for bp, prefix in blueprints:
        app.register_blueprint(bp, url_prefix=prefix)
    return app
