# Faça um algoritmo que peça um número e se ele for par some 5, se não, some 8.
numero = int(input("Digite um número inteiro: "))
resultado = numero % 2
if resultado == 0:
    print(numero + 5)
else:
    print(numero + 8)
