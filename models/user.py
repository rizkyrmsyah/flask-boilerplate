from settings import http, configuration
from helpers.alchemy import sql_alchemy as db
import datetime

class UserModel(db.Model):
    """Model for the users table"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(True), default=db.func.now())
    updated_at = db.Column(db.DateTime(True), default=db.func.now())

def __init__(self, email, password):
    self.email = email
    self.password = password 
