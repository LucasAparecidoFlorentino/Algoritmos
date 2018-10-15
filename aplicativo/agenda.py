from usuarios import *
from contato import *
import getpass

# Menu Principal Agenda ---

print("Conectando no Banco...")
conexao = sqlite3.connect("aula28.sqlite")

opcao = 0
while opcao != 2:
    print("""--- Menu Agenda ---
    1 - Entrar
    2 - Sair
""")

    opcao = int(input("Escolha uma das opções: "))
    if opcao == 1:
        print("\n--- Efetuar Login no Sistema ---\n")
        usuario = input("Por favor, informe o usuário: ")
        senha = getpass.getpass("Por favor, informe a senha: ")
        login(conexao, usuario, senha)
    elif opcao == 2:
        print("\nFechando o programa....\n")
        break

print("Fechando conexão com o Banco...")
conexao.close()
