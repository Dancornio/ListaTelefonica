from flask import jsonify, Blueprint, request
from app.models.cidade import Cidade
from app.schemas.cidade_schemas import cidade_schema, cidades_schema
from app import db

cidades_bp = Blueprint('cidades_bp', __name__, url_prefix='/api')

# --- CREATE ---
@cidades_bp.route('/cidades', methods=['POST'])
def create_cidade():
    """Cria uma nova cidade. Requer 'nome' e 'id_estado'."""
    data = request.get_json()
    if not data or not data.get('nome') or not data.get('id_estado'):
        return jsonify({'error': 'Dados insuficientes. "nome" e "id_estado" são obrigatórios.'}), 400

    nova_cidade = cidade_schema.load(data)
    db.session.add(nova_cidade)
    db.session.commit()
    
    return cidade_schema.jsonify(nova_cidade), 201

# --- READ (Todos) ---
@cidades_bp.route('/cidades', methods=['GET'])
def get_all_cidades():
    """Retorna todas as cidades. Permite filtrar por estado via query param 'id_estado'."""
    id_estado = request.args.get('id_estado', type=int)
    query = Cidade.query

    if id_estado:
        query = query.filter_by(id_estado=id_estado)
        
    todas_as_cidades = query.order_by(Cidade.nome).all()
    return cidades_schema.jsonify(todas_as_cidades), 200

# --- READ (Um) ---
@cidades_bp.route('/cidades/<int:id_cidade>', methods=['GET'])
def get_cidade_by_id(id_cidade):
    """Retorna uma cidade específica pelo seu ID."""
    cidade = Cidade.query.get_or_404(id_cidade, description=f"Cidade com ID {id_cidade} não encontrada.")
    return cidade_schema.jsonify(cidade), 200

# --- UPDATE ---
@cidades_bp.route('/cidades/<int:id_cidade>', methods=['PUT'])
def update_cidade(id_cidade):
    """Atualiza uma cidade existente."""
    cidade = Cidade.query.get_or_404(id_cidade)
    data = request.get_json()
    
    cidade.nome = data.get('nome', cidade.nome)
    cidade.id_estado = data.get('id_estado', cidade.id_estado)
    
    db.session.commit()
    return cidade_schema.jsonify(cidade), 200

# --- DELETE ---
@cidades_bp.route('/cidades/<int:id_cidade>', methods=['DELETE'])
def delete_cidade(id_cidade):
    """Remove uma cidade, se não houver contatos associados."""
    cidade = Cidade.query.get_or_404(id_cidade)
    
    if cidade.contatos.first():
        return jsonify({
            'error': f"Não é possível remover a cidade '{cidade.nome}', pois existem contatos associados a ela."
        }), 409 # Conflict

    db.session.delete(cidade)
    db.session.commit()
    return '', 204
