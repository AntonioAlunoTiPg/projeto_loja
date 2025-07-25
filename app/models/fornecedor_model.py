# fornecedor_model.py
from app.database.conexao import conectar

def cadastrar_fornecedor(nome, contato, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO fornecedores (nome, contato, email) VALUES (%s, %s, %s)", (nome, contato, email))
    conn.commit()
    conn.close()
