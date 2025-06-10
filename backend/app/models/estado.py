from app import db

class Estado(db.Model):
    """
    Representa a tabela 'estados' no banco de dados.
    """
    __tablename__ = 'estados'
    
    id_estado = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False, unique=True)
    uf = db.Column(db.String(2), nullable=False, unique=True)
    
    cidades = db.relationship('Cidade', backref='estado', lazy='dynamic')
