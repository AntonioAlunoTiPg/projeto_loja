# fornecedor_view.py
import tkinter as tk
from app.controllers import fornecedor_controller

class FornecedorView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cadastro de Fornecedor")

        tk.Label(self.root, text="Nome:").pack()
        self.nome = tk.Entry(self.root)
        self.nome.pack()

        tk.Label(self.root, text="Contato:").pack()
        self.contato = tk.Entry(self.root)
        self.contato.pack()

        tk.Label(self.root, text="Email:").pack()
        self.email = tk.Entry(self.root)
        self.email.pack()

        tk.Button(self.root, text="Salvar", command=self.salvar).pack()

        self.root.mainloop()

    def salvar(self):
        fornecedor_controller.salvar_fornecedor(
            self.nome.get(), self.contato.get(), self.email.get()
        )
