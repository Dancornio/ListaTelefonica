# app/models/cidade.py
from app import db

class Cidade(db.Model):
    __tablename__ = 'cidades'
    
    id_cidade = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    id_estado = db.Column(db.Integer, db.ForeignKey('estados.id_estado'), nullable=False)
    
    # Esta relação causa o erro se o modelo 'Contato' não for conhecido
    contatos = db.relationship('Contato', backref='cidade', lazy='dynamic')
