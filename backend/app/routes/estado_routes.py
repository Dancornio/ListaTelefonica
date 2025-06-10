from flask import jsonify, Blueprint
from app.models.estado import Estado
from app.schemas.estado_schema import estados_schema

# Cria um Blueprint para agrupar as rotas relacionadas
estados_bp = Blueprint(
    'estados_bp', 
    __name__, 
    url_prefix='/api' # Define que todas as rotas aqui começarão com /api
)

@estados_bp.route('/estados', methods=['GET'])
def get_estados():
    """
    Endpoint para retornar uma lista de todos os estados cadastrados,
    ordenados por nome.
    """
    # 1. Busca todos os registros de Estado no banco de dados
    todos_os_estados = Estado.query.order_by(Estado.nome).all()
    
    # 2. Usa o schema 'estados_schema' para converter a lista em JSON
    resultado_json = estados_schema.dump(todos_os_estados)
    
    # 3. Retorna a resposta formatada com status 200 OK
    return jsonify(resultado_json), 200