produto1 = input("1º produto: ")
valor1 = float(input("valor do 1º produto: "))
quantidade1 = int(input("quantidade do 1º produto: "))
produto2 = input("2º produto: ")
valor2 = float(input("valor do 2º produto: "))
quantidade2 = int(input("quantidade do 2º produto: "))
produto3 = input("3º produto: ")
valor3 = float(input("valor do 3º produto: "))
quantidade3 = int(input("quantidade do 3º produto: "))
print(f"produto:{produto1}; valor: {valor1}; quantidade: {quantidade1}; total: {valor1*quantidade1}")
print(f"produto:{produto2}; valor: {valor2}; quantidade: {quantidade2}; total: {valor2*quantidade2}")
print(f"produto:{produto3}; valor: {valor3}; quantidade: {quantidade3}; total: {valor3*quantidade3}")
print(f"valor total do stock: {valor1*quantidade1+valor2*quantidade2+valor3*quantidade3} euros" )