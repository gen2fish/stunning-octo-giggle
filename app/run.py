from flask import Flask
from app import api_bp
from flask_httpauth import HTTPBasicAuth
from model import db
import logging

logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)
auth = HTTPBasicAuth()
app.config.from_object("config")
app.register_blueprint(api_bp, url_prefix='/api')
db.init_app(app)

if __name__ == "__main__":
  app.run(debug=True)
