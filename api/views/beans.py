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

  