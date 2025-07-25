from app.database.conexao import conectar

def cadastrar_produto(nome, preco, categoria_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO produtos (nome, preco, categoria_id) VALUES (%s, %s, %s)",
        (nome, preco, categoria_id)
    )
    conn.commit()
    conn.close()
