from app.models import pagamento_model

def salvar_pagamento(valor, forma, data):
    pagamento_model.cadastrar_pagamento(valor, forma, data)
