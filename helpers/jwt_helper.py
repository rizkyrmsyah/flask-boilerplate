from config import configuration, http
from datetime import datetime, timedelta
from flask_jwt_extended import create_access_token
from flask_jwt_extended import current_user
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

jwt_manager = JWTManager()