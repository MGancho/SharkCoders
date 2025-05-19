from random import randint
from time import sleep

num_secret = randint(1,100)
num_secret2 = randint(1, 1000000)
jogar = int(input("Bora jogar ao jogo: maior ou menor? sim: 1 | não quero jgr com um robõ: 2 "))
tentativa = 0
jogadas = 0
tentativa2 = 0
jogadas2 = 10
if jogar == 1:
    sleep(1)
    print("ok, bora lá jogar!")
    while tentativa != num_secret:
        sleep(1)
        tentativa = int(input("qual é que achas que é esse número"))
        if tentativa < num_secret:
            sleep(1)
            print("é acima do número que colocaste")
            jogadas += 1
        if tentativa > num_secret:
            sleep(1)
            print("é abaixo do que pensaste")
            jogadas += 1
        if tentativa == num_secret:
            if jogadas <= 1:
                sleep(1)
                print(f"assim n tem piada, acertaste logo de primeira,")
                sleep(1.5)
                print("Nem sequer vale a pena fazeres o próximo, se vais só cheatar, mas se quiseres, toma aqui um pouco do código (a7)")
            if 1 < jogadas <= 5:
                sleep(1)
                print(f"conseguiste em algumas tentativas, estou impressionado")
                sleep(1.5)
                print("Se calhar queiras subir de nível? (r4)")

            if 5 < jogadas <= 10:
                sleep(1)
                print("ganhou, quer subir de nível? É porque existe um código para uma melhor versão ")

            if jogadas > 10:
                sleep(1)
                print(f"demoraste IMENSO")
                sleep(1.5)
                print(f"até a minha avó conseguia fazer melhor")
                sleep(1.5)
                print("mas podes tentar encontrar o código, se conseguires XD (y5)")
if jogar == 2547:
    sleep(1)
    print("passou uma cadela por ti chamada 'Kyra', que desafiou-te a jogares este jogo, mas mais difícil ")
    escolha = int(input("achas que estás à altura??? claro que sim 1 | nope 2"))
    if escolha == 1:
        print("ok, mas vai ser mais difícil")
    while tentativa2 != num_secret2:
        tentativa2 = int(input(f"Qual é o número que escolhes? não te esqueças que só tens {jogadas} tentativas"))


else:
    print("ok, não jogamos :[")
    sleep(0.5)
    print("o program vai encerrar daqui a pouco, mas enquanto isso, toma uma parte de um código secreto (k2)")