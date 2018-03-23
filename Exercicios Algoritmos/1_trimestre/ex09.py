# Construa um programa que recebe três valores, A, B e C. Em seguida, apresente na tela os números em ordem crescente.
valora = int(input("Digite o valor A: "))
valorb = int(input("Digite o valor B: "))
valorc = int(input("Digite o valor C: "))
if valora<valorb and valora<valorc and valorb<valorc:
    print(valora, valorb, valorc)
if valora<valorb and valora<valorc and valorb>valorc:
    print(valora, valorc, valorb)
if valorb<valorc and valorb<valora and valorc>valora:
    print(valorb, valorc, valora)
if valorb<valorc and valorb<valora and valorc<valora:
    print(valorb, valorc, valora)
if valorc<valora and valorc<valorb and valorb>valora:
    print(valorc, valora, valorb)
if valorc<valora and valorc<valorb and valorb<valora:
    print(valorc, valorb, valora)
