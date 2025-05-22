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
    sleep(1)
    print("terás de descobrir o número que pensei (entre 0 e 100)")
    sleep(0.5)
    print("e se não acertares, eu direi se o número está acima ou abaixo")
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
                print("Nem sequer vale a pena fazeres o próximo, se vais só cheatar, mas se quiseres, toma aqui um pouco do código (2b=7)")
            elif 1 < jogadas <= 5:
                sleep(1)
                print(f"conseguiste em algumas tentativas, estou impressionado")
                sleep(1.5)
                print("Se calhar queiras subir de nível? (1b=4)")

            elif 5 < jogadas <= 10:
                sleep(1)
                print("ganhou, quer subir de nível? É porque existe um código para uma melhor versão, e está aqui uma parte do código (y=8)")

            elif jogadas > 10:
                sleep(1)
                print(f"demoraste IMENSO")
                sleep(1.5)
                print(f"até a minha avó conseguia fazer melhor")
                sleep(1.5)
                print("mas podes tentar encontrar o código, se conseguires XD (g=5)")
elif jogar == 52478:
    sleep(1)
    print("passou uma Coelho por ti chamado 'Gubby', que desafiou-te a jogares este jogo, mas mais interessante.")
    sleep(1)
    print("se ganhares, ficas com a herança do dono do Gubby")
    sleep(1)
    escolha = int(input("achas que estás à altura??? claro que sim 1 | nope 2"))
    if escolha == 1:
        print("ok,mas se perderes, terás de servir o Gubby para sempre (n leste os termos e condições todos)")
        print("e btw, não é de 1 a 100, mas sim de 1 a 1000000")
    while tentativa2 != num_secret2:
        tentativa2 = int(input(f"Qual é o número que escolhes? não te esqueças que só tens {jogadas2} tentativas"))
        if tentativa2 < num_secret2:
            jogadas2 -= 1
            sleep(1)
            print("Está abaixo")
        if tentativa2 > num_secret2:
            jogadas2 -= 1
            sleep(1)
            print("Está acima")
        elif tentativa2 == num_secret2 and jogadas2 > 0:
            sleep(1)
            print("Conseguiste vencer o modo Gubby :D")
        elif jogadas2 == 0:
            sleep(1)
            print("Tu perdeste, Womp Womp, you are a failure, L, n conseguiste ganhar o modo Gubby")
    else:
        print("Bruh")
        sleep(1)
        print("Tiraste do teu tempo para descobrir o código secreto ")
        sleep(1)
        print("Só para quando receberes a chance de jogar um modo mais díficil")
        sleep(1)
        print("'Ummm, não quero, só quis desperdiçar tempo que poderia estar a usar para fazer outras coisas melhores para dizer que não queria utilizar o código")
        sleep(1)
        print("que falta de respeito")
        sleep(1)
        print("nem mereces voltar a colocar o código")
        sleep(1)
        print("agora")
        sleep(0.25)
        print("vou")
        sleep(0.25)
        print("fechar")

else:
    print("ok, não jogamos :[")
    sleep(2)
    print("o programa vai encerrar daqui a pouco, mas enquanto isso, toma uma parte de um código secreto (u=2)")
    sleep(4)
