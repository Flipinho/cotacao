from tkinter import ttk, messagebox, Label, Entry, Button, Tk
import sqlite3

# Criando a interface 
janela = Tk()
janela.title("formulario")
janela.geometry("400x400")

nome_label = Label(janela, text="Nome")
nome_label.grid(column=0, row=0)
txtnome = Entry(janela)
txtnome.grid(column=0, row=1)

end_label = Label(janela, text="Endereço")
end_label.grid(column=0, row=2)
txtend = Entry(janela)
txtend.grid(column=0, row=3)

fone_label = Label(janela, text="Telefone")
fone_label.grid(column=0, row=4)
txtfone = Entry(janela)
txtfone.grid(column=0, row=5)

def salva():
    bd = sqlite3.connect('agenda.bd') 
    cv = bd.cursor()
    cv.execute("Create table if not exists contatos(nome text, endereco text, fone text)")

    n = txtnome.get()
    e = txtend.get()
    p = txtfone.get()

    if not (n and e and p):
        messagebox.showinfo("Campos vazios","Todos os campos devem ser preenchidos")
    else:
        cv.execute("Insert Into contatos values(?,?,?)",(n,e,p))
        bd.commit()
        messagebox.showinfo("salvo","Dados salvos com sucesso")
        bd.close()

btsalva = Button(janela, text="Guardar", command=salva)
btsalva.grid(column=0, row=6)

janela.mainloop()