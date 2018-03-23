# Crie um programa que peça uma nota de trabalho e uma de prova (as duas de 0 a 100).
# Se a média aritmética das notas for maior ou igual a 60, escreva “Aprovado”, se não, “Reprovado”.
nota1 = float(input("Digite a nota que você tirou no trabalho: "))
nota2 = float(input("Digite a nota que você tirou na prova: "))
soma = (nota1 + nota2) / 2
if soma>=6.0:
    print("Aprovado", soma)
else:
    print("Reprovado", soma)
