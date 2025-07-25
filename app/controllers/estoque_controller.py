from app.models import estoque_model

def salvar_estoque(produto_id, quantidade, data_entrada):
    estoque_model.cadastrar_estoque(produto_id, quantidade, data_entrada)
