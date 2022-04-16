from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.bean import Bean

beans = Blueprint('beans', 'beans')