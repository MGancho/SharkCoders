nota1 = float(input("nota 1: "))
nota2 = float(input("nota 2: "))
total = nota1+nota2
print(f"a média do aluno foi {total/2}")
if total / 2 >= 60:
    print("Parabéns! Aluno aprovado :D")
else:
    print("Este aluno reprovou :[ ")