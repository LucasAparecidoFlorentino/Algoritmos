# Um professor precisa armazenar em uma lista os nomes dos alunos presentes em um minicurso.
# Faça um programa para armazenar 5 nomes e permitir que o professor digite o nome da cada um.
# Em seguida, apresente na tela todos os nomes informados.
lista = [""]*5
p = 0
while p < len(lista):
    lista[p] = input("Digite o nome dos alunos: ")
    p = p + 1
print("Os nomes informados foram", lista)
