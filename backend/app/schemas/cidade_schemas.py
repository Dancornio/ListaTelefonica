from app import ma
from app.models.cidade import Cidade
# --- CORREÇÃO AQUI ---
# O nome do ficheiro é 'estado_schema.py', não 'estado.py'.
from .estado_schema import EstadoSchema 

class CidadeSchema(ma.SQLAlchemyAutoSchema):
    """
    Schema para serializar o modelo Cidade.
    """
    class Meta:
        model = Cidade
        load_instance = True
        include_fk = True # Inclui o 'id_estado' no resultado JSON

    # Aninha o schema de Estado para mostrar os detalhes completos do
    # estado ao qual a cidade pertence, tornando a API mais rica.
    estado = ma.Nested(EstadoSchema)

# Instância para serializar um único objeto Cidade
cidade_schema = CidadeSchema()
# Instância para serializar uma lista de objetos Cidade
cidades_schema = CidadeSchema(many=True)
