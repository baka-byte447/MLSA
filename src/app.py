from flask import Flask
from routes import register_routes
import os

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=os.getenv('SECRET_KEY'),
    DEBUG=os.getenv('FLASK_DEBUG') == 'true'
)

register_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)