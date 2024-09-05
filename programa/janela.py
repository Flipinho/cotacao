import tkinter as tk
from tkinter import Toplevel
from formulario import janelinha
from cotacao import janela_da_rua

def abrir_nova_janela():
    new_janela = Toplevel(janela_principal)
    new_janela.title("nova janela")
    new_janela.geometry("300x200")
    new_janela.configure(background="DarkBlue")

    label_new = tk.Label(new_janela,text='Esta é uma nova janela')
    label_new.pack(pady=20)

    bt_new = tk.Button(new_janela,text='fechar', command=new_janela.destroy)
    bt_new.pack(pady=10)

def abrir_formulario():
    janelinha(janela_principal)
    
def abrir_cotacao():
    janela_da_rua(janela_principal)

    #criando a principal
janela_principal = tk.Tk()
janela_principal.title("Janela principal")
janela_principal.geometry("400x700")
janela_principal.configure(background="Crimson")

botao = tk.Button(janela_principal,text='abrir qualquer coisa',command=abrir_nova_janela)
botao.pack(pady=50)
botaoxd = tk.Button(janela_principal,text='abrir formulario',command=abrir_formulario)
botaoxd.pack(pady=50)
botaozd = tk.Button(janela_principal,text='abrir cotação',command=abrir_cotacao)
botaozd.pack(pady=50)


janela_principal.mainloop()