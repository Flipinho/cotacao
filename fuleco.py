import sqlite3
xd='s'
while xd != 'n':

    nome = str(input("Digite um nome:"))
    sobrenome = str(input("Digite um sobrenome:"))
    endereco = str(input("Digite um endereço:"))

# Se o banco não existir ele cria e conecta, se não so conecta
    banco = sqlite3.connect('banquinho.db')
    cursor = banco.cursor()
# Cria tabela no banco de dados do arquivo acima se a tabela não existir

    cursor.execute('''CREATE TABLE IF NOT EXISTS fuleco
               (nome text, sobrenome text, endereco text)''') 

#Inserindo dados na tabela 
    cursor.execute(f'''INSERT INTO fuleco VALUES ('{nome}','{sobrenome}','{endereco}')''')

#Valida as alteraçoes feitas
    banco.commit()
    
    xd = input('Deseja inserir mais dados?(s/n)')