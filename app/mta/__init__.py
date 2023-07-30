from flask import Blueprint

mta = Blueprint('mta', __name__)

from app.mta import routes
