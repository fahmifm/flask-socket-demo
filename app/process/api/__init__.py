from flask import Blueprint
from app.process.api import messages


api = Blueprint('test', __name__, url_prefix='/api')

api.add_url_rule('/send', view_func=messages.send_message)
api.add_url_rule('/guest_join', view_func=messages.guest_join)
