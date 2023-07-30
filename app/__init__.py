from flask import Flask

from config import Config


def create_app(config_class=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    # blueprints
    from app.mta import mta
    app.register_blueprint(mta)

    @app.route('/')
    def test():
        return 'It\'s working!'

    return app
