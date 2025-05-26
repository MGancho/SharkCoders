from random import randint

lista = [

]
def sorteio(lista):
    lista2 = [

    ]
    a = randint(1,20)
    b = randint(1, 20)
    c = randint(1, 20)
    d = randint(1, 20)
    e = randint(1, 20)
    f = randint(1, 20)
    g = randint(1, 20)
    h = randint(1, 20)
    i = randint(1, 20)
    j = randint(1, 20)
    y = 0

    while y != 10:
        if y == 0:
            lista.append(a)
            y += 1
        if y == 1:
            lista.append(b)
            y += 1
        if y == 2:
            lista.append(c)
            y += 1
        if y == 3:
            lista.append(d)
            y += 1
        if y == 4:
            lista.append(e)
            y += 1
        if y == 5:
            lista.append(f)
            y += 1
        if y == 6:
            lista.append(g)
            y += 1
        if y == 7:
            lista.append(h)
            y += 1
        if y == 8:
            lista.append(i)
            y += 1
        if y == 9:
            lista.append(j)
            y += 1
        if y == 10:
            print(lista)
    

sorteio([])