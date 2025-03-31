def soma (numero):
    total = 0
    for x in numero:
        total += x
    return (total)
def subtracao (numero):
    total = 0
    for x in numero:
        total -= x
    return (total)
def multiplicacao (numero):
    total = 1
    for x in numero:
        total *= x
    return (total)
def divisao(numero):
    total = numero[0]
    for x in numero[1:]:
        total /= x
    return total
def resto(numero):
    total = numero[0]
    for x in numero[1:]:
        total %= x
    return total
