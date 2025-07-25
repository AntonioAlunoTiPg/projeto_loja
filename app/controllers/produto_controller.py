from app.models import produto_model

def salvar_produto(nome, preco, categoria_id):
    produto_model.cadastrar_produto(nome, preco, categoria_id)
