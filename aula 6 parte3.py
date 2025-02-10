idade = int(input("qual a idade do atleta"))
if idade <= 9:
    print("Este atleta é mirim")
elif idade <= 14:
    print("Este atleta é infantil")
elif idade <= 19:
    print("Este atleta é junior")
elif idade <= 25:
    print("Este atleta é senior")
else:
    print("Este atleta é master")