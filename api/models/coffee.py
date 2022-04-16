from datetime import datetime
from api.models.db import db

class Beans(db.Model):
  __tablename__= 'beans'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  roaster = db.Column(db.String(100))
  