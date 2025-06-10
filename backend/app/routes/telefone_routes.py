from flask import jsonify, Blueprint, request
from app.models.telefone import Telefone
from app.schemas.telefone_schema import telefone_schema, telefones_schema
from app import db

telefones_bp = Blueprint('telefones_bp', __name__, url_prefix='/api')

# --- READ (Ler Todos) ---
@telefones_bp.route('/telefones', methods=['GET'])
def get_all_telefones():
    """
    Retorna uma lista de todos os telefones.
    Pode ser filtrado por contato com o parâmetro de consulta ?id_contato=<id>.
    """
    id_contato = request.args.get('id_contato', type=int)
    query = Telefone.query

    if id_contato:
        query = query.filter_by(id_contato=id_contato)
    
    todos_os_telefones = query.all()
    return telefones_schema.jsonify(todos_os_telefones), 200

# --- READ (Ler Um) ---
@telefones_bp.route('/telefones/<int:id_telefone>', methods=['GET'])
def get_telefone_by_id(id_telefone):
    """Retorna um telefone específico pelo seu ID."""
    telefone = Telefone.query.get_or_404(id_telefone)
    return telefone_schema.jsonify(telefone), 200

# --- CREATE (Criar) ---
@telefones_bp.route('/telefones', methods=['POST'])
def create_telefone():
    """Cria um novo telefone. Requer 'numero' e 'id_contato'."""
    data = request.get_json()
    if not data or not data.get('numero') or not data.get('id_contato'):
        return jsonify({'error': 'Dados insuficientes. "numero" e "id_contato" são obrigatórios.'}), 400
    
    novo_telefone = telefone_schema.load(data)
    db.session.add(novo_telefone)
    db.session.commit()
    return telefone_schema.jsonify(novo_telefone), 201

# --- UPDATE (Atualizar) ---
@telefones_bp.route('/telefones/<int:id_telefone>', methods=['PUT'])
def update_telefone(id_telefone):
    """Atualiza um telefone existente."""
    telefone = Telefone.query.get_or_404(id_telefone)
    data = request.get_json()
    
    telefone.numero = data.get('numero', telefone.numero)
    telefone.tipo = data.get('tipo', telefone.tipo)
    
    db.session.commit()
    return telefone_schema.jsonify(telefone), 200

# --- DELETE (Apagar) ---
@telefones_bp.route('/telefones/<int:id_telefone>', methods=['DELETE'])
def delete_telefone(id_telefone):
    """Apaga um telefone pelo seu ID."""
    telefone = Telefone.query.get_or_404(id_telefone)
    db.session.delete(telefone)
    db.session.commit()
    return '', 204