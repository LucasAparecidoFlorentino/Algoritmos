"""
- O modo "r" é de leitura
- O modo "w" é de apagar tudo
- O modo "a" é de escrita
"""

arquivo = open("arquivos/nomes.txt", "r")

conteudo = arquivo.readlines()

l = 0

while l < len(conteudo):
    print(conteudo[l])
    l+=1

# A mesma coisa com for

for linha in conteudo:
    print(linha)



arquivo.close()

# Vetores, arquivos, função, estudar para prova

# Opção 1 = Cadastrar palavras
#  // 2 = Listar palavras
#  // 3 = Sair
