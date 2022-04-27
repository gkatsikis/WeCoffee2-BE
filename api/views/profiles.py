from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token
from api.models.user import User
from api.models.profile import Profile

profiles = Blueprint('profiles', 'profiles')

@profiles.route('/', methods=["GET"])
def index():
  profiles = Profile.query.all()
  return jsonify([profile.serialize() for profile in profiles]), 200

@profiles.route('/<id>', methods=["GET"])
def ShowOne(id):
  profile = Profile.query.filter_by(id=id).first()
  profile_data = profile.serialize()
  return jsonify(profile=profile_data), 200