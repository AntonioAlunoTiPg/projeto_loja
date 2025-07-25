# app/views/produto_view.py
import tkinter as tk
from tkinter import messagebox

class ProdutoView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Controle de Loja")

        tk.Label(self.root, text="Nome do Produto:").pack()
        self.nome_entry = tk.Entry(self.root)
        self.nome_entry.pack()

        tk.Label(self.root, text="Preço:").pack()
        self.preco_entry = tk.Entry(self.root)
        self.preco_entry.pack()

        tk.Button(self.root, text="Salvar", command=self.salvar).pack()

    def salvar(self):
        nome = self.nome_entry.get()
        preco = self.preco_entry.get()
        self.controller.salvar_produto(nome, preco)
        messagebox.showinfo("Sucesso", "Produto salvo com sucesso!")

    def iniciar(self):
        self.root.mainloop()
