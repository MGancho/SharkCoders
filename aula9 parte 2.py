numero = int(input(print("escolha um número")))
numero2 = int(input(print("Escolhe outro número")))
escolha = int(input(print("Queres ver os números pares(1) ou ímpares(2) ?")))
match escolha:
    case _ if escolha == 1:
        if numero % 2 == 0:
            for x in range(numero,numero2,2):
                result = sum(range(numero,numero2,2))
                print('a soma de todos os números pares entre estes 2 números é de {}', format(result))
        if numero % 2 != 0:
            for x in range(numero+1,numero2,2):
                result = sum(range(numero+1,numero2,2))
                print('a soma de todos os números pares entre estes 2 números é de {}',format(result))
    case _ if escolha == 2:
        if numero % 2 == 0:
            for x in range(numero+1,numero2,2):
                result = sum(range(numero+1,numero2,2))
                print('a soma de todos os números ímpares entre estes 2 números é de {}',format(result))
        if numero % 2 != 0:
            for x in range(numero,numero2,2):
                result = sum(range(numero,numero2,2))
                print('a soma de todos os números ímpares entre estes 2 números é de {}', format(result))
    case _:
        print("tente 1 para par ou 2 para ímpar")