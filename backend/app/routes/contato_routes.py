from flask import jsonify, Blueprint, request
from app.models.contato import Contato
from app.models.telefone import Telefone
from app.schemas.contato_schema import contato_schema, contatos_schema
from app import db

contatos_bp = Blueprint('contatos_bp', __name__, url_prefix='/api')

# --- CREATE (Criar) ---
@contatos_bp.route('/contatos', methods=['POST'])
def create_contato():
    """Cria um novo contato. Requer 'nome' e uma lista de 'telefones'."""
    data = request.get_json()
    if not data or not data.get('nome') or not data.get('telefones'):
        return jsonify({'error': 'Dados insuficientes. "nome" e "telefones" (lista) são obrigatórios.'}), 400

    # Separa os dados de telefones dos dados do contato
    telefones_data = data.pop('telefones', [])
    
    # Cria o objeto Contato com os dados restantes
    novo_contato = Contato(
        nome=data.get('nome'),
        id_cidade=data.get('id_cidade')
    )
    
    # Cria e associa os objetos Telefone
    for tel_data in telefones_data:
        novo_telefone = Telefone(numero=tel_data.get('numero'), tipo=tel_data.get('tipo'))
        novo_contato.telefones.append(novo_telefone)
        
    db.session.add(novo_contato)
    db.session.commit()
    
    return contato_schema.jsonify(novo_contato), 201

# --- READ (Ler Todos) ---
@contatos_bp.route('/contatos', methods=['GET'])
def get_all_contatos():
    """Retorna uma lista de todos os contatos."""
    todos_os_contatos = Contato.query.order_by(Contato.nome).all()
    return contatos_schema.jsonify(todos_os_contatos), 200

# --- READ (Ler Um) ---
@contatos_bp.route('/contatos/<int:id_contato>', methods=['GET'])
def get_contato_by_id(id_contato):
    """Retorna um contato específico pelo seu ID."""
    contato = Contato.query.get_or_404(id_contato)
    return contato_schema.jsonify(contato), 200

# --- UPDATE (Atualizar) ---
@contatos_bp.route('/contatos/<int:id_contato>', methods=['PUT'])
def update_contato(id_contato):
    """Atualiza um contato existente."""
    contato = Contato.query.get_or_404(id_contato)
    data = request.get_json()

    contato.nome = data.get('nome', contato.nome)
    contato.id_cidade = data.get('id_cidade', contato.id_cidade)

    # Lógica para atualizar telefones: remove os antigos e adiciona os novos
    if 'telefones' in data:
        # O 'cascade="all, delete-orphan"' no modelo Contato trata da remoção do DB
        contato.telefones.clear()
        
        telefones_data = data.get('telefones', [])
        for tel_data in telefones_data:
            novo_telefone = Telefone(numero=tel_data.get('numero'), tipo=tel_data.get('tipo'))
            contato.telefones.append(novo_telefone)

    db.session.commit()
    return contato_schema.jsonify(contato), 200

# --- DELETE (Apagar) ---
@contatos_bp.route('/contatos/<int:id_contato>', methods=['DELETE'])
def delete_contato(id_contato):
    """Apaga um contato e todos os seus telefones associados."""
    contato = Contato.query.get_or_404(id_contato)
    db.session.delete(contato)
    db.session.commit()
    return '', 204
