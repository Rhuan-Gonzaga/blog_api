from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_app(app)

    with app.app_context():
        from app.routes import routes  # Importe o blueprint
        app.register_blueprint(routes)  # Registre o blueprint
        db.create_all()  # Crie as tabelas, se não existirem

    return app
