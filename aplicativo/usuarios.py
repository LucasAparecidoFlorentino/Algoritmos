import sqlite3
from contato import *

########### FUNÇÕES ################

def criar_tabela_usuario(conexao):

    # Cria o cursor para operar o banco
    cursor = conexao.cursor()


    ################### Monta o SQL a ser executado ###########
    sql = """
        CREATE TABLE IF NOT EXISTS usuario(
            nome text,
            login text,
            senha text
        );
    """

    cursor.execute(sql)


def inserir_usuario(conexao, nome, login, senha):

    # Cria o cursor para operar o banco
    cursor = conexao.cursor()


    ########## Inserindo um registro ###############33


    sql = "INSERT INTO usuario VALUES ('{}', '{}', '{}');".format(nome, login, senha)

    # sql = """
    #     INSERT INTO usuario VALUES(
    #         'Lucas Florentino',
    #         'lucas',
    #         '123'
    #     );
    # """


    #Executa o sql
    cursor.execute(sql)

    # Salvar as modificações
    # O commit deve ser feito depois de INSERT, UPDATE, DELETE
    conexao.commit()

# Listar os registros de usuário
def listar_usuarios(conexao):

    cursor = conexao.cursor()

    # Monta o SQL
    sql = "SELECT rowid, * FROM usuario;"

    # Executa o SQL
    cursor.execute(sql)

    # Armazena os dados do select
    usuarios = cursor.fetchall()

    #Percorrer a lista com os registros
    #Estou chamando de "u" cada item dessa lista
    for usr in usuarios:
        print( "{}: {}".format(usr[0], usr[1]))

def buscar_usuario(conexao, busca):

    cursor = conexao.cursor()

    sql = "SELECT * FROM usuario WHERE nome LIKE '%{}%';".format(busca)

    cursor.execute(sql)

    usuarios = cursor.fetchall()

    for usr in usuarios:
        print(usr[1])

def excluir_usuario(conexao,id):

    cursor = conexao.cursor()

    sql = "DELETE FROM usuario WHERE rowid = {};".format(id)

    cursor.execute(sql)

    conexao.commit()

def alterar_usuario(conexao, id):

    cursor = conexao.cursor()

    n = input("Nome: ")
    l = input("Login: ")
    s = input("Senha: ")

    sql = "UPDATE usuario SET nome = '{}', login = '{}', senha = '{}' WHERE rowid = {}; ".format(n, l, s, id)

    cursor.execute(sql)

    conexao.commit()

def login(conexao, login, senha):

    cursor = conexao.cursor()

    sql = "SELECT rowid, * FROM usuario WHERE login LIKE '{}' AND senha LIKE '{}';".format(login, senha)

    cursor.execute(sql)

    usuario = cursor.fetchall()

    if usuario:
        for usr in usuario:
            print( "\n\033[47m\033[34m--- Bem Vindo! --- {} ---\033[0;0m\n".format(usr[1]))
            return menu_contato()

    else:
        print("\n\033[47m\033[30m--- Usuário inválido! ---\033[0;0m\n")
        print("\033[47m\033[30m--- Retornando para o Menu Agenda ---\033[0;0m\n")
        return

def menu_usuario():
    conexao = sqlite3.connect("aula28.sqlite")

    opcao = 0

    while opcao != 6:
        print("""
        Em relação aos usuários do sistema, você deseja ...
        1- Inserir
        2- Listar
        3- Buscar
        4- Excluir
        5- Alterar
        6- Sair do programa
        """)

        opcao = int(input("Qual a opção desejada ? "))

        if opcao == 1:
            n = input("Nome: ")
            l = input("Login: ")
            s = input("Senha: ")

            inserir_usuario(conexao, n, l, s)

        elif opcao == 2:
            listar_usuarios(conexao)

        elif opcao == 3:
            print("--- Buscar registro ---")
            busca = input("Qual o nome do usuário a ser buscado ? ")
            buscar_usuario(conexao, busca)

        elif opcao == 4:
            id = int(input("Qual id você quer excluir ? "))
            excluir_usuario(conexao, id)

        elif opcao == 5:
            listar_usuarios(conexao)
            id = int(input("Qual contato você quer alterar ? "))
            alterar_usuario(conexao, id)

        elif opcao == 6:
            print("Saindo do programa")
            break

        else:
            print("Opção inválida ! ")
            print("=-=" * 10)

    # Fechando conexão (ligação) com o banco
    conexao.close()
