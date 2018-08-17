"""
- O modo "r" é de leitura
- O modo "w" é de apagar tudo
- O modo "a" é de escrita
"""
print("Abrindo arquivo...")
arq = open("arquivos/nomes.txt", "a")

# print("Escrevendo no arquivo...")
#Escreve alguma coisa no arquivo
# arq.write("Rafael Zottesso\n")

nome = input("Informe seu nome completo: ")
# Armazena o nome digitado
arq.write(nome)
# Quebra a linha
arq.write("\n")

print("Fechando o arquivo")
# Salva as modificações e fecha o arquivo
arq.close()
