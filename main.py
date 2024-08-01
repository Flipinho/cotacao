import requests
from tkinter import * 

def pegar_cotacoes():
        requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
        rqs_list = requisicao.json()
        dolarAtual =  rqs_list['USDBRL']['bid']
        euroAtual =  rqs_list['EURBRL']['bid']
        btcAtual =  rqs_list['BTCBRL']['bid']

        texto = f'''
            dolar: {dolarAtual}
            euro: {euroAtual}
            btc: {btcAtual}'''
        #print(texto)
        texto_resposta["text"] = texto


        def limpar():
            texto_resposta["text"] = ""


root = Tk()
root.title("cotaaa")
root.geometry('400x566')
texto = Label(root, text= "aperte o botao para exibir as cotocao")
texto.grid(column=0, row=0, padx=10, pady=10)
botao = Button(root, text="buscar cotaçoes", command=pegar_cotacoes)
botao.grid(column= 0, row=1, padx=10, pady=10)
texto_resposta = Label(root, text="")
texto_resposta.grid(column=0,row=2,padx=10,pady=10)
root.mainloop()