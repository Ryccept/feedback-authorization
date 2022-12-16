"""Seed file to make sample data for DB."""
from models import db, User, Feedback, connect_db
from app import app
 
#Create all tables:
db.drop_all()
db.create_all()
