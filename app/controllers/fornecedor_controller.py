# fornecedor_controller.py
from app.models import fornecedor_model

def salvar_fornecedor(nome, contato, email):
    fornecedor_model.cadastrar_fornecedor(nome, contato, email)

