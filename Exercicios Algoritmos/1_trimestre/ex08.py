#Construa um programa que recebe três valores, A, B e C. Em seguida, apresente na tela somente o maior deles.
valora = float(input("Digite o valor a: "))
valorb = float(input("Digite o valor b: "))
valorc = float(input("Digite o valor c: "))
if valora>valorb and valora>valorc:
    print("O valor {} é o maior entre os 3" .format(valora))
if valorb>valora and valorb>valorc:
    print("O valor {} é o maior entre os 3" .format(valorb))
if valorc>valora and valorc>valorb:
    print("O valor {} é o maior entre os 3" .format(valorc))
