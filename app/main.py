from app import app, socketio
from app.routes import bp as api_bp

app.register_blueprint(api_bp, url_prefix='/api')

