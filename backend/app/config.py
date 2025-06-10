import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

class Config:
    """Configurações base da aplicação."""
    # Desativa o rastreamento de modificações do SQLAlchemy para economizar recursos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Pega a URL de conexão do banco de dados a partir das variáveis de ambiente
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:5RfSfPgu8MNmXK70@db.dbtvucmijlvmgvootqmb.supabase.co:5432/postgres')