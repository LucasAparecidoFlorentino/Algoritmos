import sqlite3

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


def inserir_usuario(conexao):

    # Cria o cursor para operar o banco
    cursor = conexao.cursor()


    ########## Inserindo um registro ###############33

    nome = input("Digite seu nome: ")

    usuario = input("Digite seu nome de usuário: ")

    senha = input("Digite sua senha: ")

    sql = "INSERT INTO usuario VALUES ('{}', '{}', '{}');".format(nome, usuario, senha)

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

def buscar_usuario(conexao):

    cursor = conexao.cursor()

    sql = "SELECT * FROM usuario WHERE nome LIKE '%Florentino%';"

    cursor.execute(sql)

    usuarios = cursor.fetchall()

    for usr in usuarios:
        print(usr[1])



############## P R I N C I P A L ###################

conexao = sqlite3.connect("aula28.sqlite")

# listar_usuarios(conexao)
# inserir_usuario(conexao)
buscar_usuario(conexao)








# Fechando conexão (ligação) com o banco
conexao.close()
