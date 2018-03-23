# Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.
valora = float(input("Digite o valor a: "))
valorb = float(input("Digite o valor b: "))
valorc = float(input("Digite o valor c: "))
soma = valora + valorb
if soma<valorc:
    print("A soma de {} + {} é menor que {}" .format(valora, valorb, valorc))
else:
    print("A soma de {} + {} é maior que {}" .format(valora, valorb, valorc))
