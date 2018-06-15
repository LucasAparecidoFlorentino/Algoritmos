# Faça um programa que peça para o usuário informar o tamanho de um vetor.
# Em seguida, crie este vetor e preencha ele com números digitados pelo usuário.
# Por fim, apresente na tela os números digitados.
tamanho = int(input("Qual o tamanho do vetor necessário: "))
lista = [""]*tamanho
p = 0
while p < len(lista):
    lista[p] = int(input("Digite os valores: "))
    p = p + 1
print("Os números digitados foram", lista)
