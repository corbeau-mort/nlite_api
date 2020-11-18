from flask import Flask
from flask_socketio import SocketIO
#from app import routes


socketio = SocketIO()

def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__, static_url_path='/local_files/')
    app.debug = debug
    app.config['SECRET_KEY'] = 'secret!'

    from app.routes import bp_api
    app.register_blueprint(bp_api, url_prefix="/api")

    @app.route("/")
    def get_home():
        return "home"

    socketio.init_app(app)
    return app


if __name__ == '__main__':
    my_app = create_app(True)
    socketio.run(my_app, debug=True)

