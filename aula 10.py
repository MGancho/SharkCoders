from random import randint
tentativa = int(input("adivinhe o número de 1 a 5 que eu pensei: "))
numsecret = randint(1,5)
print(f"o Pytho escolheu o número {numsecret}")
if numsecret == tentativa:
    print("correcto!")
else:
    print("errado")