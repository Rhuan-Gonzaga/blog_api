from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Instanciando o banco
db = SQLAlchemy()

def criando_app():
  app = Flask(__name__)
  app.config.from_object('app.config.Config')
  db.init_app(app)

  with app.app_context():
    from app import routes
    db.create_all()
  return app