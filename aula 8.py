Numero_escolhido = int(input("escolha e escreva um número inteiro:"))
divisores = []
for i in range(1, Numero_escolhido + 1):
    if Numero_escolhido % i == 0:
        divisores.append(i)
if len(divisores) == 2:
    print(f"{Numero_escolhido} é um número primo")
else:
    print(f"{Numero_escolhido} não é um número primo")
