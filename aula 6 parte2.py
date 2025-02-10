kWh = float(input("quantos kwh foram consumidos neste mês"))
instalacao = int(input("E qual foi a instalação (Residencial[1], Comercial [2] ou Industrial [3]): "))
if instalacao == 1:
    if kWh <= 500 :
        print(f"por ter consumido {kWh} kWh, a instalação terá de pagar {kWh * 0.40}")
    if kWh > 500:
        print(f"por ter consumido {kWh} kWh, a instalação terá de pagar {kWh * 0.65} ")
elif instalacao == 2:
    if kWh <= 1000 :
        print(f"por ter consumido {kWh} kWh, a instalação terá de pagar {kWh * 0.55}")
    if kWh > 1000:
        print(f"por ter consumido {kWh} kWh, a instalação terá de pagar {kWh * 0.60} ")
elif instalacao == 3:
    if kWh <= 5000 :
        print(f"por ter consumido {kWh} kWh, a instalação terá de pagar {kWh * 0.55}")
    if kWh > 5000:
        print(f"por ter consumido {kWh} kWh, a instalação terá de pagar {kWh * 0.60} ")
else:
    print(f"só pode ser o número 1, 2 ou 3. Tente Novamente")