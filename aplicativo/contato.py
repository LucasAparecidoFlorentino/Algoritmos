import sqlite3

########### Funções ###########

def criar_tabela_contato(conexao):

    cursor = conexao.cursor()

    sql = """
        CREATE TABLE IF NOT EXISTS contato(
        nome TEXT,
        telefone_residencial TEXT,
        celular TEXT,
        email TEXT,
        usuario INTEGER
        );
    """

    cursor.execute(sql)

    conexao.commit()

def inserir_contato(conexao, nome, telefone_residencial, celular, email, usuario):

    cursor = conexao.cursor()

    sql = "INSERT INTO contato VALUES ('{}', '{}', '{}','{}', {});".format(nome, telefone_residencial, celular, email, usuario)

    cursor.execute(sql)

    conexao.commit()

def listar_contatos(conexao):

    cursor = conexao.cursor()

    sql = "SELECT rowid, * FROM contato;"

    cursor.execute(sql)

    contatos = cursor.fetchall()

    for ctt in contatos:
        print("{}: {}: {}: {}: {}: {}".format(ctt[0], ctt[1], ctt[2], ctt[3], ctt[4], ctt[5]))

def buscar_contato(conexao, busca):

    cursor = conexao.cursor()

    sql = "SELECT * FROM contato WHERE nome LIKE '%{}%';".format(busca)

    cursor.execute(sql)

    contatos = cursor.fetchall()

    for ctt in contatos:
        print(ctt[3])

def excluir_contato(conexao,id):

    cursor = conexao.cursor()

    sql = "DELETE FROM contato WHERE rowid = {};".format(id)

    cursor.execute(sql)

    conexao.commit()

def alterar_contato(conexao, nome, telefone_residencial, celular, email, usuario):

    cursor = conexao.cursor()

    sql = "UPDATE nome, telefone_residencial, celular, email, usuario, FROM contato WHERE rowid = {}; ".format(id)

    cursor.execute(sql)

    conexao.commit()

def menu_contato():
    opcao = 0

    while opcao != 6:
        print("""
        Em relação aos contatos ...
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
            tr = input("Telefone Residencial: ")
            c = input("Celular: ")
            ema = input("Email: ")
            usuario = input("Usuário: ")
            inserir_contato(conexao, n, tr, c, ema, usuario)

        elif opcao == 2:
            listar_contatos(conexao)

        elif opcao == 3:
            busca = input("Qual o nome do contato a ser buscado para saber seu email ? ")
            buscar_contato(conexao, busca)

        elif opcao == 4:
            id = int(input("Qual contato você quer excluir ? "))
            excluir_contato(conexao, id)

        elif opcao == 5:
            listar_contatos(conexao)
            id = int(input("Qual contato você quer alterar ? "))
            alterar_contato(conexao, id)

        elif opcao == 6:
            print("Saindo do programa")

        else:
            print("Opção Inválida")
            print("=-=" * 10)


######### Principal ##########

conexao = sqlite3.connect("aula28.sqlite")

menu_contato()
