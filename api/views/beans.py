from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.bean import Bean

beans = Blueprint('beans', 'beans')

@beans.route('/', methods=["POST"])
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]
  bean = Bean(**data)
  db.session.add(bean)
  db.session.commit()
  return jsonify(bean.serialize()), 201

@beans.route('/', methods=["GET"])
def index():
  beans = Bean.query.all()
  return jsonify([bean.serialize() for bean in beans]), 200

@beans.route('/<id>', methods=["GET"])
def show(id):
  bean = Bean.query.filter_by(id=id).first()
  bean_data = bean.serialize()
  return jsonify(bean=bean_data), 200

@beans.route('/<id>', methods=["PUT"])
@login_required
def update(id):
  data = request.get_json()
  profile = read_token(request)
  bean = Bean.query.filter_by(id=id).first()

  if bean.profile_id != profile["id"]:
    return 'Forbidden', 403

  for key in data:
    setattr(bean, key, data[key])

  db.session.commit()
  return jsonify(bean.serialize()), 200

@beans.route('<id>', methods=["DELETE"])
@login_required
def delete(id):
  profile = read_token(request)
  bean = Bean.query.filter_by(id=id).first()

  if bean.profile_id != profile["id"]:
    return 'Forbidden', 403

  db.session.delete(bean)
  db.session.commit()
  return jsonify(message="Success"), 200