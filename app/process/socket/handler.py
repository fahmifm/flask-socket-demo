from flask_socketio import emit
from app import socketio


namespace = '/test'


@socketio.on('my event', namespace=namespace)
def test_message(message):
    print(message)
    emit('my response', {'data': message['data']})


def emit_message(topic: str, data: dict, namespace: str):
    socketio.emit(topic, data, namespace=namespace)
