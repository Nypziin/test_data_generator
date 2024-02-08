from random import randint


def gerar_informacoes(lista):

    nome = ['Jéss', 'Natan', 'Breno', 'Medeiras', 'Fernando']
    email = ['marquin@gmail.com', 'xgamer@gmail.com', 'doguinho@gmail.com', 'gatinho@gmail.com', 'supergamer@gmail.com']
    telefone = ['11999999999', '21888888888', '15777777777', '22666666666', '13555555555']
    cidade = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Aracajú']
    estados = ['Paraná', 'Amazônia', 'Acre', 'Espírito Santo', 'Tocantins']

    informacoes = [nome, email, telefone, cidade, estados]

    informacao = []

    for numero in set(lista):
        informacao.append(informacoes[int(numero) - 1][randint(0, 4)])

    return informacao


def gerar_arquivo(lista):

    try:
        with open('dados.txt', 'r') as arquivo:
            pass
    except (FileExistsError, FileNotFoundError):
        with open('dados.txt', 'w') as arquivo:
            print('Criando o arquivo...')
    finally:
        with open('dados.txt', 'a') as arquivo:
            print('Adicionando os dados...')
            for i in lista:
                arquivo.write(f'{i}\n')
            arquivo.flush()


