numero = int(input(print("escolha um número")))
numero2 = int(input(print("Escolhe outro número")))
escolha = int(input(print("Queres ver os números pares(1) ou ímpares(2) ?")))
match escolha:
    case _ if escolha == 1:
        if numero % 2 != 0:
            numero += 1
        pares = range(numero,numero2,2)
        soma_p = sum(pares)
        print('a soma de todos os números pares entre estes 2 números é de {}', format(soma_p))
    case _ if escolha == 2:
        if numero % 2 == 0:
            numero += 1
        impares = range(numero,numero2,2)
        soma_i = sum(impares)
        print('a soma de todos os números ímpares entre estes 2 números é de {}',format(soma_i))
    case _:
        print("tente 1 para par ou 2 para ímpar")