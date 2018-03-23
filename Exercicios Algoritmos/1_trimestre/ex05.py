# Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. Dica: utilize o operador módulo (resto da divisão).
numero = int(input("Digite um número inteiro: "))
resultado = numero % 2
if resultado == 0:
    print("Este número é par", resultado)
else:
    print("Este número é impar", resultado)
