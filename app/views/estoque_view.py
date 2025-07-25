import tkinter as tk
from tkinter import messagebox
from app.controllers import estoque_controller

class EstoqueView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Entrada de Estoque")

        tk.Label(self.root, text="ID do Produto:").pack()
        self.produto_id = tk.Entry(self.root)
        self.produto_id.pack()

        tk.Label(self.root, text="Quantidade:").pack()
        self.quantidade = tk.Entry(self.root)
        self.quantidade.pack()

        tk.Label(self.root, text="Data de Entrada (YYYY-MM-DD):").pack()
        self.data = tk.Entry(self.root)
        self.data.pack()

        tk.Button(self.root, text="Salvar", command=self.salvar).pack()
        self.root.mainloop()

    def salvar(self):
        estoque_controller.salvar_estoque(
            int(self.produto_id.get()),
            int(self.quantidade.get()),
            self.data.get()
        )
        messagebox.showinfo("Sucesso", "Estoque atualizado com sucesso!")
