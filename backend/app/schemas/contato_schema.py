from app import ma
from app.models.contato import Contato
from .cidade_schemas import CidadeSchema    # Importa o schema da cidade
from .telefone_schema import TelefoneSchema # Importa o schema do telefone

class ContatoSchema(ma.SQLAlchemyAutoSchema):
    """
    Schema para serializar o modelo Contato, incluindo suas relações.
    """
    class Meta:
        model = Contato
        load_instance = True
        include_fk = True
        include_relationships = True

    # Aninha os schemas relacionados para que a API retorne os detalhes
    # da cidade e a lista de telefones junto com os dados do contato.
    cidade = ma.Nested(CidadeSchema)
    telefones = ma.Nested(TelefoneSchema, many=True)

# Instância para serializar um único contato
contato_schema = ContatoSchema()
# Instância para serializar uma lista de contatos
contatos_schema = ContatoSchema(many=True)