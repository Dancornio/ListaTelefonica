from app import db
from sqlalchemy import CheckConstraint

class Telefone(db.Model):
    """
    Representa a tabela 'telefones' no banco de dados.
    """
    __tablename__ = 'telefones'
    
    id_telefone = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(20), nullable=False)
    tipo = db.Column(db.String(20)) # Ex: 'celular', 'trabalho', 'casa', 'principal', 'outro'
    
    # Chave estrangeira que liga este telefone a um contato específico.
    id_contato = db.Column(db.Integer, db.ForeignKey('contatos.id_contato'), nullable=False)

    __table_args__ = (
        CheckConstraint(tipo.in_(['Principal', 'Celular', 'Trabalho', 'Casa', 'Outro']), name='telefones_tipo_check'),
    )
