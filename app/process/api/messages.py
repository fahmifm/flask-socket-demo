from flask import request
from app.process.socket.handler import emit_message


def send_message():
    data = request.args.get('message')
    topic = request.args.get('topic', 'message')
    payload = {
        'data': data
    }
    emit_message(topic, payload, '/test')

    return '1'
