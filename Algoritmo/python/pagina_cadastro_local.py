import sqlite3
# As funções abaixo são destinadas ao cadastro dos locais

def listaTags():
    print('-----------------------------------------------------------------------')
    # lista as Tags cadastradas no banco de dados
    print("Tags mais usadas:")
    con = sqlite3.connect("banco_borave.db")
    cursor = con.cursor()
    cursor.execute("SELECT tag1, tag2, tag3, tag4, tag5 FROM locaiscadastrados;")
    banco = cursor.fetchall()
    con.close()
    for linha in banco:
        print(linha[:])

def listaId():
    print('-----------------------------------------------------------------------')
    # lista os IDs dos locais para auxilio no Update ou remoção dos cadastros
    print("LOCAIS CADASTRADOS")
    con = sqlite3.connect("banco_borave.db")
    cursor = con.cursor()
    cursor.execute("SELECT id, nome, categoria, descricao, endereço, cidade, estado, whatsapp, instagram, email, site FROM locaiscadastrados;")
    banco = cursor.fetchall()
    con.close()
    for linha in banco:
        print(linha[:])


def cadastraLocal(): 
    print('-----------------------------------------------------------------------')
    nome = str(input("Insira o nome do local: "))
    categoria = str(input("Qual a categoria do local?: (publico/privado) "))
    descricao = str(input("Qual a descrição do local?: "))
    endereco = str(input('Qual o endereço?: '))
    cidade = str(input('Qual a cidade?: '))
    estado = str(input('Qual o UF?: '))
    whatsapp = str(input('Qual o contato do whatsapp? '))
    instagram = str(input('Qual o instagram?: '))
    email = str(input('Qual o e-mail?: '))
    site = str(input('Qual a site?: '))

    listaTags()
    tag = str(input("Utilize tags para linkar seu local: "))
    tagOp = str(input("Gostaria de adicionais mais alguma tag? Você pode usar até 5 tags para linkar seu local."))
    tag2, tag3, tag4, tag5 = '', '', '', ''
    if (tagOp == "sim"):
        tag2 = str(input("Digite uma tag: "))
        tagOp = input('Deseja adicionar mais alguma tag?: ')
        if (tagOp == "sim"):
            tag3 = str(input("Digite uma tag: "))
            tagOp = input('Deseja adicionar mais alguma tag?: ')
            if (tagOp == "sim"):
                tag4 = str(input("Digite uma tag: "))
                tagOp = input('Deseja adicionar mais alguma tag?: ')
                if (tagOp == "sim"):
                    tag5 = str(input("Digite uma tag: "))

    con = sqlite3.connect("banco_borave.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO locaiscadastrados (nome, categoria, descricao, endereço, cidade, estado, whatsapp, instagram, email, site, tag1, tag2, tag3, tag4, tag5) VALUES ('"+nome+"','"+categoria+"','"+descricao+"','"+endereco+"','"+cidade+"','"+estado+"', '"+whatsapp+"','"+instagram+"','"+email+"', '"+site+"','"+tag+"','"+tag2+"','"+tag3+"','"+tag4+"','"+tag5+"');")
    print("Dados inseridos com sucesso!")
    con.commit()
    con.close()
    confirma = input('Deseja cadastrar mais algum lugar?: ')
    if confirma == 'não' or confirma =='nao':
        inicioPaginaCadastroLugar()

def atualizaLocal():
    print('-----------------------------------------------------------------------')
    listaId()
    id = input("Informe o id do local que deseja atualizar:")
    nome = input("Insira o nome do local: ")
    categoria = input("Qual a categoria do local?: (publico/privado) ")
    descricao = input("Qual a descrição do local?: ")
    endereco = input('Qual o endereço?: ')
    cidade = input('Qual a cidade?: ')
    estado = input('Qual o estado?: ')
    whatsapp = input('Qual o contato do whatsapp? ')
    instagram = input('Qual o instagram?: ')
    email =  input('Qual o e-mail?: ')
    site = input('Qual a site?: ')

    listaTags()
    tag = str(input("Utilize tags para linkar seu local: "))
    tagOp = str(input("Gostaria de adicionais mais alguma tag? Você pode usar até 5 tags para linkar seu local."))
    tag2, tag3, tag4, tag5 = '', '', '', ''
    if (tagOp == "sim"):
        tag2 = str(input("Digite uma tag: "))
        tagOp = input('Deseja adicionar mais alguma tag?: ')
        if (tagOp == "sim"):
            tag3 = str(input("Digite uma tag: "))
            tagOp = input('Deseja adicionar mais alguma tag?: ')
            if (tagOp == "sim"):
                tag4 = str(input("Digite uma tag: "))
                tagOp = input('Deseja adicionar mais alguma tag?: ')
                if (tagOp == "sim"):
                    tag5 = str(input("Digite uma tag: "))

    con = sqlite3.connect("banco_borave.db")
    cursor = con.cursor()
    cursor.execute("UPDATE locaiscadastrados SET nome=?, categoria=?, descricao=?, endereço=?, cidade=?, estado=?, whatsapp=?, instagram=?, email=?, site=?, tag1=?, tag2=?, tag3=?, tag4=?, tag5=? WHERE id=?",(nome, categoria, descricao, endereco, cidade, estado, whatsapp, instagram, email, site, tag, tag2, tag3, tag4, tag5, id))
    print("Dados atualizados com sucesso!")
    con.commit()
    con.close()
    confirma = input('Deseja atualizar mais algum lugar?: ')
    if confirma == 'não' or confirma =='nao':
        inicioPaginaCadastroLugar()

def exclui():
    print('-----------------------------------------------------------------------')
    listaId()
    id = input("Informe o id a ser removido:")
    confirma = input('Você não tem como desfazer essa ação, tem certeza que deseja excluir o ID? : ')
    if confirma == 'sim':
        con = sqlite3.connect("banco_borave.db")
        cursor = con.cursor()
        cursor.execute("DELETE FROM locaiscadastrados WHERE id ="+str(id))
        print('ID excluido com sucesso!')
        con.commit()
        con.close()
        print("1. Sim")
        print("2. Não")
        print("3. Retornar a pagina inicial")
        excluir = input('Deseja excluir mais algum registro?: ')
        if excluir == 1:
            exclui()
        elif excluir == 2:
            print("Até logo!")
        elif excluir == 3:
            inicioPaginaCadastroLugar()
        else:
            excluir = input('Digite uma opção válida: ')

def voltar():
    print('-----------------------------------------------------------------------')
    print('1. voltar')
    print('2. sair')
    confirma = int(input('Digite a opção desejada: '))
    conf = True
    while conf == True:
        if confirma==1:
            inicioPaginaCadastroLugar()
        elif confirma==2:
            print('Até logo!')
            conf = False
        else:
            confirma = input('Digite uma opção válida: ')
        

def inicioPaginaCadastroLugar():
    print('-----------------------------------------------------------------------')
    print('                VOCÊ ESTÁ NO GERENCIADOR DE CADASTRO')
    print()
    print("Digite a opção desejada: ")
    print('1. Cadastrar um lugar')
    print('2. Atualizar dados')
    print('3. Consultar locais cadastrados')
    print('4. Excluir um registro')
    print('0. Sair')
    opcao = int(input())
    while opcao != 0:
        if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 0:
            opcao = int(input('Digite uma opção válida: '))
        elif opcao == 1:
            cadastraLocal()
        elif opcao == 2:
            atualizaLocal()
        elif opcao == 3:
            print('----------------------------------------------')
            listaId()
            print('----------------------------------------------')
            voltar()
            break
        elif opcao == 4:
            exclui()
        elif opcao == 0:
            print('Até logo!')
            break
