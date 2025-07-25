import tkinter as tk
from tkinter import messagebox
from app.controllers import categoria_controller

class CategoriaView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cadastro de Categoria")

        tk.Label(self.root, text="Nome da Categoria:").pack()
        self.nome = tk.Entry(self.root)
        self.nome.pack()

        tk.Label(self.root, text="Descrição:").pack()
        self.descricao = tk.Entry(self.root)
        self.descricao.pack()

        tk.Button(self.root, text="Salvar", command=self.salvar).pack()
        self.root.mainloop()

    def salvar(self):
        categoria_controller.salvar_categoria(
            self.nome.get(), self.descricao.get()
        )
        messagebox.showinfo("Sucesso", "Categoria cadastrada com sucesso!")
