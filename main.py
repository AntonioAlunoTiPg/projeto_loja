# main.py
import tkinter as tk
from app.views.fornecedor_view import FornecedorView

def abrir_fornecedor():
    FornecedorView()

app = tk.Tk()
app.title("Sistema de Loja")
tk.Button(app, text="Cadastro de Fornecedor", command=abrir_fornecedor).pack()
app.mainloop()
