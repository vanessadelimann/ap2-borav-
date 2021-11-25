from pagina_cadastro_local import *
from pagina_roteiro import *

print('-----------------------------------------------------------------------')
print('                       BEM VINDO AO BORAVÊ')
print('1. Pagina lugares')
print('2. Pagina roteiro')
print('3. login')
print('4. Cadastre-se')
print('0. Sair')
opcao = int(input('Digite a opção desejada: '))
while opcao != 0:
    if opcao == 1:
        inicioPaginaCadastroLugar()
        break
    elif opcao == 2:
        paginaInicial()
        break
    elif opcao == 3:
        print('Em breve')
    elif opcao == 4:
        print('Em breve')
    elif opcao == 0:
        break
    else:
        opcao = int(input('Digite uma opção válida: '))
print('Até a proxima! :)')
print('-----------------------------------------------------------------------')   
