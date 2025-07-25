import tkinter as tk
from tkinter import messagebox
from app.controllers import pagamento_controller

class PagamentoView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Registro de Pagamento")

        tk.Label(self.root, text="Valor:").pack()
        self.valor = tk.Entry(self.root)
        self.valor.pack()

        tk.Label(self.root, text="Forma de Pagamento:").pack()
        self.forma = tk.Entry(self.root)
        self.forma.pack()

        tk.Label(self.root, text="Data (YYYY-MM-DD):").pack()
        self.data = tk.Entry(self.root)
        self.data.pack()

        tk.Button(self.root, text="Salvar", command=self.salvar).pack()
        self.root.mainloop()

    def salvar(self):
        pagamento_controller.salvar_pagamento(
            float(self.valor.get()), self.forma.get(), self.data.get()
        )
        messagebox.showinfo("Sucesso", "Pagamento registrado!")
