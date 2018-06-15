# Faça um programa para armazenar 6 números inteiros para uma loteria, permitindo que o usuário informe os números sorteados.
# Depois de preencher, informe uma mensagem e os números sorteados.
lista = [""]*6
p = 0
while p < len(lista):
    lista[p] = int(input("Digite os números sorteados: "))
    p = p + 1
print("Os números sorteados foram:", lista)
print("Parabéns, você ganhou")
