from app import ma
from app.models.telefone import Telefone

class TelefoneSchema(ma.SQLAlchemyAutoSchema):
    """
    Schema para serializar o modelo Telefone.
    """
    class Meta:
        model = Telefone
        load_instance = True
        include_fk = True # Inclui 'id_contato' no resultado JSON

# Instância para serializar um único telefone
telefone_schema = TelefoneSchema()
# Instância para serializar uma lista de telefones
telefones_schema = TelefoneSchema(many=True)
