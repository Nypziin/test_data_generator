from app import gerar_informacoes, gerar_arquivo

while True:
    print('''
Seja bem vindo ao Gerador de Dados de Testes - Para finalizar basta digitar "parar"
-----------------------------------------------------------------------------------
Escolha uma ou mais opções abaixo para serem geradas aleatóriamente:
[1] - Nome
[2] - Email
[3] - Telefone
[4] - Cidade
[5] - Estado
''')

    opcao = input("Digite suas opções (ex: 1, 2, 4): ")

    if opcao == 'parar':
        break

    opcoes = list(filter(lambda x: 1 <= x <= 5, map(lambda x: int(x), opcao.split(','))))

    print('-----------------------------------------------------------------------------------')

    quer_arquivo = input("Gostaria de salvar os dados em um arquivo de texto (s/n)? ")

    print('-----------------------------------------------------------------------------------')

    print(*gerar_informacoes(opcoes), sep='\n')

    print('-----------------------------------------------------------------------------------')

    if quer_arquivo == 's':
        gerar_arquivo(gerar_informacoes(opcoes))

    print('-----------------------------------------------------------------------------------')





