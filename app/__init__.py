from flask import Flask, render_template
# from flask_socketio import SocketIO
# from gevent import monkey
# monkey.patch_all()

# init socketio here
# add cors allowed origin

# ws_config = {
#     'cors_allowed_origins': '*'
# }
# socketio = SocketIO(**ws_config)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    # init the app into socket io
    # socketio.init_app(app)

    # default route
    @app.route('/')
    def index():
        return render_template('index.html')

    # blueprint routes
    from app.process import api
    app.register_blueprint(api.api)

    return app
