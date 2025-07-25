from app.models import categoria_model

def salvar_categoria(nome, descricao):
    categoria_model.cadastrar_categoria(nome, descricao)
