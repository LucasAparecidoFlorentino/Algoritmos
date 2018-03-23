# Construa um programa que mostre menu exatamente como o exemplo abaixo e implemente as funções necessárias:
#     == Menu de Opções ==
#     1. Somar 2 números
#     2. Potência de um número
# 3. Raiz de grau N
# == Opção escolhida:
print(" == Menu de Opções == ")
print("1. Somar 2 números. ")
print("2. Potência de um número. ")
print("3. Raiz de grau N: ")
opcao = int(input("Escolha sua opção: "))
print(" == Opção escolhida: ", opcao)

if 1 == opcao:
    valor1 = float(input("Digite um valor: "))
    valor2 = float(input("Digite outro valor: "))
    soma = valor1 + valor2
    print("O resultado é ", soma)
if 2 == opcao:
    valor1 = float(input("Digite um valor: "))
    potência = valor1 ** 2
if 3 == opcao:
    raiz_de_grau = int(input("Digite o grau da raiz: "))

else:
    print("Opção inválida")
