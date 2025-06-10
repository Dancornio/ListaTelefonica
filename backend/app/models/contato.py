from app import db

class Contato(db.Model):
    """
    Representa a tabela 'contatos' no banco de dados.
    """
    __tablename__ = 'contatos'
    
    id_contato = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    
    # Chave estrangeira que liga o contato a uma cidade (pode ser nula)
    id_cidade = db.Column(db.Integer, db.ForeignKey('cidades.id_cidade'), nullable=True)
    
    # Relação com telefones (um contato pode ter muitos telefones)
    # A opção 'cascade="all, delete-orphan"' garante que, quando um contato
    # é apagado, todos os seus telefones associados também são.
    telefones = db.relationship('Telefone', backref='contato', lazy='dynamic', cascade="all, delete-orphan")
