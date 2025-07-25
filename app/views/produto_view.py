import tkinter as tk
from tkinter import messagebox
from app.controllers import produto_controller

class ProdutoView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cadastro de Produto")

        tk.Label(self.root, text="Nome:").pack()
        self.nome = tk.Entry(self.root)
        self.nome.pack()

        tk.Label(self.root, text="Preço:").pack()
        self.preco = tk.Entry(self.root)
        self.preco.pack()

        tk.Label(self.root, text="Categoria ID:").pack()
        self.categoria = tk.Entry(self.root)
        self.categoria.pack()

        tk.Button(self.root, text="Salvar", command=self.salvar).pack()
        self.root.mainloop()

    def salvar(self):
        produto_controller.salvar_produto(
            self.nome.get(), self.preco.get(), self.categoria.get()
        )
        messagebox.showinfo("Sucesso", "Produto cadastrado!")
