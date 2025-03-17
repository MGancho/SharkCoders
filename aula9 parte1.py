velocidade = int(input("A que velocidade o seu carro passou pelo radar? "))
match velocidade:
    case _ if velocidade <= 80:
        print("dentro do limite. Boa Viagem")
    case _ if velocidade > 80:
        multa = velocidade - 80
        print(f"Estás acima do limite de velocidade. A multa foi gerada de {multa * 2} euros")
