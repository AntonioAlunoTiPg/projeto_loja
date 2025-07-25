from app.database.conexao import conectar

def cadastrar_categoria(nome, descricao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO categorias (nome, descricao) VALUES (%s, %s)",
        (nome, descricao)
    )
    conn.commit()
    conn.close()
