import tkinter as tk
from app.views.produto_view import ProdutoView
from app.views.fornecedor_view import FornecedorView
# Importe outras views conforme necessário

def abrir_produto():
    ProdutoView()

def abrir_fornecedor():
    FornecedorView()

app = tk.Tk()
app.title("Sistema de Loja")

tk.Button(app, text="Produto", command=abrir_produto).pack()
tk.Button(app, text="Fornecedor", command=abrir_fornecedor).pack()
# Adicione mais botões para outras views

app.mainloop()
