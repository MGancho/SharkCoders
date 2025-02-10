ordenado = float(input("Digite o valor do ordenado so salário:"))
if ordenado < 500:
    print(f"O valor do salário passará de {ordenado} a {ordenado + ordenado * 0.15}")
elif 500 <= ordenado <= 1000:
    print(f"o valor do salário passará de {ordenado} a {ordenado + ordenado * 0.10}")
else:
    print(f"o valor do salário passará de {ordenado} a {ordenado + ordenado * 0.05}")