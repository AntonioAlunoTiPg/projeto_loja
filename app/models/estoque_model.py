def cadastrar_estoque(produto_id, quantidade, data_entrada):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO estoque (produto_id, quantidade, data_entrada) VALUES (%s, %s, %s)",
        (produto_id, quantidade, data_entrada)
    )
    conn.commit()
    conn.close()
