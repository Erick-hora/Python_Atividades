from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'curso.txt'

if not arquivo_existe(arq):
    cria_texto(arq)


while True:
    resposta = menu(['Verificar Cadastros', 'Cadastrar Pessoas', 'Sair'])
    sleep(.5)
    if resposta == 1:
        #Listando o conteúdo do arquivo
        ler_arquivo(arq)
    elif resposta == 2:
        cabecalho('Novo Cadastro')
        nome = str(input('Digite o nome: '))
        idade = leiaint('DIgite a idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Fechando o sistema... Até logo!')
        break
    else:
        print('\033[0;31mErro! Digite uma opção válida!\033[m')
