from flask import Blueprint
bp_api = Blueprint('api', __name__,  static_folder='../local_files/')
from app.routes import colours, config


@bp_api.route("/")
def get_api():
    return "api"


@bp_api.app_errorhandler(404)
def handle_404(err):
    return str(err), 404


