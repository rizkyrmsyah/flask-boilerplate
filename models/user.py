from config import http, configuration
from helpers.alchemy import sql_alchemy as db
import datetime

class UserModel(db.Model):
    """Model for the users table"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email_verified_at = db.Column(db.DateTime(True))
    created_at = db.Column(db.DateTime(True), default=db.func.now())
    updated_at = db.Column(db.DateTime(True), default=db.func.now())

def __init__(self, name, email, password, email_verified_at):
    self.name = name
    self.email = email
    self.password = password 
    self.email_verified_at = email_verified_at
