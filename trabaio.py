while True:
    try:
        numiro = int(input("Insira o seu numero de funcionario:"))
        salario = float(input("Insira o quanto você ganha por hora:"))
        shalalala = int(input("Insira quantas horas você trabalha:"))
        break
    except(ValueError):
        print('Digite um numero sua anta !!')


receba = salario * shalalala
recebav2 = receba * 5
recebav3 = receba * 20

if shalalala >= 14:
    print("PARA DE MENTIR, TA MALUCO")
elif shalalala >= 1:
    print(f"Bem vindo funcionario {numiro}")
    print(f"Voce ganha R$.{receba} por dia")
    print(f"Voce ganha R$.{recebav2} por semana")
    print(f"Voce ganha R$.{recebav3} por mes")
elif shalalala <= 0:
    print("Preguiçoso")
