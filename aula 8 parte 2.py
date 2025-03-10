velocidade = int(input("A que velocidade o seu carro passou pelo radar? "))
multa = velocidade - 80
if velocidade > 80:
    print('Estás acima do limite permitido. A multa foi gerada no valor de {} euros'.format(multa*2))
else:
    print("Dentro do limite, boa viagem.")