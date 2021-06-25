from datetime import timedelta
from dotenv import load_dotenv, find_dotenv
import os

# Load environment
load_dotenv(find_dotenv())

# get absolute path static directory in root project
log_folder = os.path.abspath(os.path.join(
    os.path.dirname(os.path.dirname(__file__)), 'log'))

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_database = os.getenv("DB_DATABASE")
db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")

class Configuration(object):
    # Basic
    APP_DEBUG = os.getenv("APP_DEBUG") == "True"
    APP_PORT = int(os.getenv("APP_PORT", 5000))

    # MYSQL
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://"+db_username+":" + \
        db_password+"@"+db_host+":"+db_port+"/"+db_database
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("DB_TRACK_MODIFICATIONS")

    # MAILER
    MAIL_HOST = os.getenv("MAIL_HOST")
    MAIL_PORT = int(os.getenv("MAIL_PORT"))
    MAIL_ENCRYPTION = os.getenv("MAIL_ENCRYPTION")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
