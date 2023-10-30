#Agenda em Python
import os 
#variaveis para nome da agenda
PASTA = 'lista_contatos/'
EXTENCAO = '.txt' #extençao para o arquivo a ser criado 
Lista = PASTA

class cl_contato:
    def __init__(self, nome, telefone, categoria):
        self.nome = nome
        self.telefone = telefone
        self.categoria = categoria

def app():
    criar_directorio()
    exibe_menu()

    #Pergunta ao usuario oque deseja fazer.
    pergunta = True
    while pergunta:
        opicao = input('Selecione uma opção do Menu:\r\n')
        opicao = int(opicao)
        #executa as opcoes do Menu
        if opicao == 1:
            print('Adicionar Novo Contato')
            novo_contato()
            pergunta = False
        elif opicao == 2:
            print('Editar Contato.')
            edita_contato()
            pergunta = False
        elif opicao == 3:
            print('Ver Contatos.')
            ler_contatos()
            pergunta = False
        elif opicao == 4:
            print('Buscar Contato.')
            buscar_contatos()
            pergunta = False
        elif opicao == 5:
            print('Apagar Contato.')
            apagar_contato()
            pergunta = False
        else:
            print('Esta opção não esta disponivel')

#FUNCOES DA  AGENDA
def novo_contato():
    print('Escreva os dados do novo contato.')
    nome_contato = input('Nome do Contato:\r\n')

    #valida a existencia de um contato
    contato_existe = contato_existente(nome_contato)
    if not contato_existe:

        with open(PASTA + nome_contato + EXTENCAO,'w') as arquivo:
            #carregar os outros campos da agenda
            telefone_contato = input('Telefone do contato: \r\n')
            categoria_contato = input('Categoria do contato: \r\n')
            #instanciar a classe de contatos 
            contato = cl_contato(nome_contato, telefone_contato, categoria_contato)
            #escreve no arquivo
            arquivo.write('Nome:' + contato.nome + '\r\n')
            arquivo.write('Telefone:' + contato.telefone + '\r\n')
            arquivo.write('Categoria:' + contato.categoria + '\r\n')

            print('Contato criado com sucesso!')
            #fecha arquivo
            arquivo.close

    else:
        #caso o contato ja exista

        print(f'{nome_contato} ja existe')
        app()
def edita_contato():
    print('Qual contato deseja editar')
    nome_anterior = input('esqueva o nome do contato que sera editado\r\n')

    contato_existe = contato_existente(nome_anterior)

    if contato_existe:
        print('Contato existe e pode ser editado')

        with open(PASTA + nome_anterior + EXTENCAO,'w') as arquivo:
            novo_nome_contato = input('Digite o novo Nome do Contato:\r\n')
            novo_telefone_contato = input('Digite o novo Telefone do contato: \r\n')
            novo_categoria_contato = input('Digite a nova Categoria do contato: \r\n')

            contato = cl_contato(novo_nome_contato, novo_telefone_contato, novo_categoria_contato)
            #escreve no arquivo
            arquivo.write('Nome:' + contato.nome + '\r\n')
            arquivo.write('Telefone:' + contato.telefone + '\r\n')
            arquivo.write('Categoria:' + contato.categoria + '\r\n')

            arquivo.close
            # renomear o arquivo
            os.rename(PASTA + nome_anterior + EXTENCAO, PASTA + novo_nome_contato + EXTENCAO)

            

            print(f'\r\nContrato {nome_contato} salvo com sucesso\r\n')
    else:
        print('Contato não pode ser editado porque não existe')
def ler_contatos():
    arquivo = os.listdir(PASTA)
    arquivo_txt = [i for i in arquivo if i.endswith(EXTENCAO)]
    for arquivo in arquivo_txt:
        with open(PASTA + arquivo) as contatos:
            for linha in contatos:
                #mosta os conteudos das linhas
                print(linha.rstrip())
            #separa os contatos
            print('--------------------')
            print('\r\n')
def buscar_contatos():
    contato_buscado = input('Qual contato deseja buscar:\r\n')
    try:
        with open(PASTA + contato_buscado + EXTENCAO) as contato:
            print('\r\nInformações do Contato\r\n')
            for linha in contato:
                print(linha.rstrip())
            print('\r\n')
    except IOError:
        print('O contato não existe')
        print(IOError)
def apagar_contato():
    nome_excluir = input('Qual contato deseja apagar?\r\n')
    try:
        os.remove(PASTA + nome_excluir + EXTENCAO)
        print('Contato apagado com sucesso')
    except:
        print('Não foi possivel excluir o Contato porque ele não existe')
        print('Selecione um Contato Valido')
        apagar_contato()
def contato_existente(contato_busca):
    return os.path.isfile(PASTA + contato_busca + EXTENCAO)
def exibe_menu():
    #menu da agenda de contatos
    print('Selecione do Menu oque deseja fazer:')
    print('1) Adicionar Novo Contato.')
    print('2) Editar Contato.')
    print('3) Ver Contatos.')
    print('4) Buscar Contato.')
    print('5) Apagar Contato.')
def criar_directorio():
    if not os.path.exists(PASTA): #verifica existencia da pasta de contatos
        os.makedirs(PASTA)# caso nao exista ela é criada com o nome na variavel PASTA
        print('Lista de Contatos foi criada com sucesso.')
    else:
        print(f'A {Lista} ja existe')

app()