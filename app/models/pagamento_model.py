from app.database.conexao import conectar

def cadastrar_pagamento(valor, forma, data):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO pagamentos (valor, forma_pagamento, data_pagamento) VALUES (%s, %s, %s)",
        (valor, forma, data)
    )
    conn.commit()
    conn.close()
