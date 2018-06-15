# Crie um vetor e armazene os números de 1 a 100. Cada número deve ocupar uma posição do vetor (lista).
# Mostre na tela todos os números do vetor em ordem crescente (1 a 100).
lista = [""]*100
p = 0

while p < len(lista):
    lista[p] = p + 1
    p = p + 1

# b) Mostre na tela todos os números do vetor em ordem decrescente (100 a 1).
# lista = ['']*100
# p = len(lista) - 1
# while p >= 1:
#     lista[p] = p
#     print(lista[p])
#     p = p - 1

# c) Mostre na tela o dobro de todos os números.
# lista = ['']*100
# p = 1
# p2 = 2
# while p < len(lista):
#     lista[p] = p
#     print("Número {} o dobro é {}" .format(p, p2))
#     p = p + 1
#     p2 = p * 2

# d) Apresente na tela a soma de todos os números.
# soma = 0
# p = 0
# while p < len(lista):
#     soma = soma + lista[p]
#     p = p + 1
# print("A soma da lista é", soma)

# e) Apresente na tela a média geral dos valores contidos na lista.
# soma = 0
# p = 0
# while p < len(lista):
#     soma = soma + lista[p]
#     p = p + 1
# print("A média geral dos valores é", soma/len(lista))

# f) Mostre na tela a quantidade de números pares.
par = 0
p = 0
while p < len(lista):
    if lista[p] %2 == 0:
        par = par + 1

    p = p + 1
print("A quantidade de números pares é", par)
