from flask import Flask
from flask_cors import CORS
from helpers import sql_alchemy
from flask_mail import Mail
import routes

cors = CORS()
mail = Mail()

def create_app(configuration):
    app = Flask(
        __name__.split(',')[0],
        static_url_path='/static',
        static_folder='../static'
    )

    # load configuration
    app.config.from_object(configuration)

    # register route blueprint
    app.register_blueprint(routes.index.blueprint)
    ##

    # init app
    cors.init_app(app, resources={r"/*": {"origins": "*"}})
    sql_alchemy.init_app(app)
    mail.init_app(app)

    return app
