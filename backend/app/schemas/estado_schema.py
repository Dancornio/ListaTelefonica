from app import ma
from app.models.estado import Estado

class EstadoSchema(ma.SQLAlchemyAutoSchema):
    """
    Schema para serializar o modelo Estado.
    """
    class Meta:
        model = Estado
        load_instance = True # Permite carregar dados para uma instância do modelo
        
        # Define explicitamente os campos a serem expostos na API
        fields = ('id_estado', 'nome', 'uf')

# Instância para serializar um único estado
estado_schema = EstadoSchema()
# Instância para serializar uma lista de estados
estados_schema = EstadoSchema(many=True)
