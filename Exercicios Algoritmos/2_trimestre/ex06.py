# Crie um vetor para armazenar alguns números que serão utilizados no cálculo da tabuada.
# a) Apresente todos os números informados e seu respectivo dobro.
tamanho = int(input("Qual o tamanho da tábuada necessário ? "))
lista = [""]*tamanho
p = 0
while p < len(lista):
    lista[p] = int(input("Digite os valores: "))
    p = p + 1
    dobro = lista * 2
print("Os números informados são {}" .format(lista))
print("O dobro desses números é {}" .format(dobro))
