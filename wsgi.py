# from app import create_app, socketio
from app import create_app


app = create_app()

if __name__ == '__main__':
    # socketio.run(app)
    app.run()
