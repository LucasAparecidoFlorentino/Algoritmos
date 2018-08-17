
opcao = 0
while opcao != 3:
    print(""" ===== Menu de Palavras =====
    Opção 1 = Cadastrar Palavras
    Opção 2 = Listar Palavras
    Opção 3 = Sair""")

    opcao = int(input("Qual a opção desejada ? "))

    if opcao == 1:
        arq = open("arquivos/nomes.txt", "a")
        nome = input("Informe as palavras desejadas para cadastro: ")
        arq.write(nome)
        arq.write("\n")

    elif opcao == 2:
        arq = open("arquivos/nomes.txt", "r")
        conteudo = arq.readlines()
        l = 0
        while l < len(conteudo):
            print(conteudo[l])
            l+=1

    elif opcao == 3:
        print("Finalizando")
    else:
        print("Opção inválida. Tente novamente !")
print("Fim do programa !")
