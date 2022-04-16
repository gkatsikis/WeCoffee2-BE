from datetime import datetime
from api.models.db import db

class Bean(db.Model):
  __tablename__= 'beans'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  roaster = db.Column(db.String(100))
  varietals = db.Column(db.String(250))
  tasting = db.Column(db.String(250))
  origin = db.Column(db.String(100))
  region = db.Column(db.String(100))
  farmer = db.Column(db.String(100))
  create_at = db.Column(db.DateTime, default=datetime.utcnow)
  profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))

  def __repr__(self):
    return f"Bean('{self.id}', '{self.name}')"

  def serialize(self):
    bean = {b.name: getattr(self, b.name) for b in self.__table__.columns}
    return bean
  