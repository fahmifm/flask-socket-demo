from flask import request
# from app.process.socket.handler import emit_message
import socketio
# from flask_socketio import SocketIO


class Websocket(object):
    def __init__(self, url, namespaces):
        self.sio = socketio.Client()
        self.sio.connect(url)

    def emit(self, topic, data=None, namespace=None):
        payload = {
            'data': data
        }
        self.sio.emit(topic, payload, namespace)


# ws = Websocket('https://devws.jublia.com')
# socketio.Client()

url = 'https://devws.jublia.com'
# url = 'http://localhost:5555'
namespaces = ['/video']
headers = {
    'j-api-key': 'imserver'
}

# sio = socketio.Client()
# sio.connect(url, headers=headers, namespaces=namespaces)


def send_message():
    data = request.args.get('message')
    topic = request.args.get('topic', 'message')

    # ws.emit(topic, data, '/video')
    sio.emit(topic, {"data": data}, namespace='/video')

    return '1'


def guest_join():
    ext_id = request.args.get('ext_id')
    meeting_id = request.args.get('meeting_id')
    meeting_token = request.args.get('meeting_token')
    data = {
        'topic': meeting_id,
        'message': {
            'action': 'guest_join',
            'data': {
                'attendee_name': '',
                'attendee_company': 'Tesla',
                'attendee_profile': '',
                'attendee_position': '',
                'attendee_language': 'en',
                'ext_attendee_id': ext_id,
                'is_allowed': True,
                'meeting_token': meeting_token
            }
        }
    }

    # ws.emit(topic, data, '/video')
    sio.emit('guest_join', data, namespace='/video')
    return '1'
