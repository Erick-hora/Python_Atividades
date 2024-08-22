from ex115.lib.interface import cabecalho

def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def cria_texto(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')

    else:
        print(f'Arquivo {nome} criado com sucesso')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Problemas com a leitura do arquivo')
    else:
        cabecalho('Pessoas cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, n='desconhecido', i=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro dentro do arquivo')
    else:
        try:
            a.write(f'{n};{i}\n')
        except:
            print('Houve um erro ao escrever os dados')
        else:
            print(f'Registro de {n} finalizado')
