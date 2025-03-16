from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db
from routes import job_routes

app = Flask(__name__)
CORS(app, resources={r"/jobs/*": {"origins": "*"}})
app.config.from_object(Config)

db.init_app(app)

# Register Blueprints
app.register_blueprint(job_routes)

if __name__ == '__main__':
    app.run(debug=True)
