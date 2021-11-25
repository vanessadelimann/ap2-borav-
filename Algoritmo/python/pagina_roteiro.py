import sqlite3

# As funções abaixo estão destinadas a tela do usuário onde será gerado o roteiro
def excluitags():
    con = sqlite3.connect("bancotag.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM tags;")
    con.commit()
    con.close()

def processamento():
    print('-----------------------------------------------------------------------')
    nome = str(input("Digite um nome pro roteiro: "))
    dias = str(input("Quantos dias de viagem?: "))
    cidade = str(input("Qual a cidade?: "))
    estado = str(input("Qual o UF?: "))
    finalidade = str(input("Qual o objetivo da viagem? (passeio/trabalho): "))

    confirma = input('Gostaria de informar alguma atividade? (sim/não): ')
    while confirma == 'sim':
        tag = input('O que gostaria de fazer durante a viagem?: ')
        confirma = input('Gostaria de informar alguma atividade? (sim/não): ')
        con = sqlite3.connect("bancotag.db")
        cursor = con.cursor()
        cursor.execute("INSERT INTO tags(tag) VALUES ('"+tag+"');")
        con.commit()
        con.close()
        
    print('----------------------------------------------')
    print('Roteiro: ', nome.upper())
    print('Dias da viagem: ', dias)
    print('Cidade: ', cidade)
    print('Finalidade: ', finalidade)
    print('----------------------------------------------')

    con2 = sqlite3.connect("bancotag.db")
    cursor2 = con2.cursor()
    cursor2.execute("SELECT tag FROM tags")
    banco2 = cursor2.fetchall()
    con2.close()

    for i in banco2:
        celula = ''.join(i)
        con3 = sqlite3.connect("banco_borave.db")
        cursor3 = con3.cursor()
        cursor3.execute("SELECT * FROM locaiscadastrados WHERE cidade='"+cidade+"' and estado='"+estado+"'and (tag1='"+celula+"' or tag2='"+celula+"' or tag3='"+celula+"' or tag4='"+celula+"' or tag5='"+celula+"')")
        banco3 = cursor3.fetchall()
        print(banco3[:10])
        con3.close()

    excluitags()

    con = sqlite3.connect("banco_borave.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO roteiro (nome, dias, cidade, estado, finalidade) VALUES ('"+nome+"','"+dias+"','"+cidade+"','"+estado+"','"+finalidade+"');")
    # preciso fazer com que o banco guarda oss locais que foram indicados 
    print()
    print("Roteiro salvo com sucesso!")
    print()
    con.commit()
    con.close()

    confirma = input('Deseja criar um novo roteiro?: ')
    if confirma == 'não' or confirma == 'nao':
        paginaInicial()



def listaRoteiro():
    print('-----------------------------------------------------------------------')
    print("Roteiros criados: ")
    print()
    con = sqlite3.connect("banco_borave.db")
    cursor = con.cursor()
    cursor.execute("SELECT id FROM roteiro;")
    banco = cursor.fetchall()
    con.close()
    for linha in banco:
        print(linha[0:1])

def excluiRoteiro():
    print('-----------------------------------------------------------------------')
    listaRoteiro()
    id = input("Informe o id a ser removido:")
    confirma = input('Você não tem como desfazer essa ação, tem certeza que deseja excluir o ID? : ')
    if confirma == 'sim':
        con = sqlite3.connect("banco_borave.db")
        cursor = con.cursor()
        cursor.execute("DELETE FROM roteiro WHERE id = "+str(id))
        print('ID excluido com sucesso!')
        con.commit()
        con.close()
        print("1. Sim")
        print("2. Não")
        print("3. Retornar a pagina inicial")
        excluir = input('Deseja excluir mais algum registro?: ')
        if excluir == 1:
            excluiRoteiro()
        elif excluir == 2:
            print("Até logo!")
        elif excluir == 3:
            paginaInicial()
        else:
            excluir = input('Digite uma opção válida: ')

def voltar():
    print('-----------------------------------------------------------------------')
    print('1. voltar')
    print('2. sair')
    confirma = int(input('Digite a opção desejada: '))
    conf = True
    while conf:
        if confirma==1:
            paginaInicial()
        elif confirma==2:
            break
        else:
            confirma = input('Digite uma opção válida: ')

def paginaInicial():
    print('-----------------------------------------------------------------------')
    print('             VOCÊ ESTÁ NA PAGINA DE CRIAÇÃO DE ROTEIRO')
    print()
    print("Digite a opção desejada: ")
    print('1. Criar roteiro')
    print('2. Buscar roteiro')
    print('3. Excluir registro')
    print('0. Sair')
    opcao = int(input())
    while opcao != 0:
        if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 0:
            opcao = int(input('Digite uma opção válida: '))
        elif opcao == 1:
            processamento()
        elif opcao == 2:
            listaRoteiro()
            voltar()
            break
        elif opcao == 3:
            excluiRoteiro()
        elif opcao == 0:
            break
