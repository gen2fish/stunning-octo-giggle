from flask import Flask
from app import api_bp
from model import db


app = Flask(__name__)
app.config.from_object("config")
app.register_blueprint(api_bp, url_prefix='/api')
db.init_app(app)

if __name__ == "__main__":
  app.run()
