from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from app.config import Config

db = SQLAlchemy()
ma = Marshmallow()
cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    cors.init_app(app)
    ma.init_app(app)

    with app.app_context():
        from app.routes.cidade_routes import cidades_bp
        app.register_blueprint(cidades_bp)

        from app.routes.estado_routes import estados_bp
        app.register_blueprint(estados_bp)

        from app.routes.contato_routes import contatos_bp
        app.register_blueprint(contatos_bp)

        from app.routes.telefone_routes import telefones_bp
        app.register_blueprint(telefones_bp)

    return app
