import shutil # importando biblioteca, sempre é útli importar no inicio como é no R, assim todos os módulos podem usar.

def escrever_arquivo(texto):
    #diretorio = "Escreva o diretorio'
    arquivo = open('teste.txt','w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    arquivo.write()

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n') # Transformando o arquivo em uma lista, toda vez que o arquivo achar um comando enter no arquivo, vai entender que é para transformar em uma listao que estiver naquela linha
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota: # lendo o arquivo
        lista_notas = x.split(',') # criando novo split para separar por vírgula a=o que contem na lista
        #print(lista_notas)
        aluno = lista_notas[0] # separando o nome dos alunos
        lista_notas.pop(0) # retirando o nos alunos para posterior realziar o calculo da média0
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int (i) for i in notas]) / 4 # criando a fórmula para já calcular a média usando a lambda
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media

# def copia_arquivo(nome_arquivo):
#     shutil.copy(nome_arquivo, 'Endereço destino') # por padrao se não colocar o nome do arquivo vai copiar com o mesmo nome
#
# def move_arquivo(nome_arquivo):
#     shutil.move(nome_arquivo, 'Endereço destino')

if __name__ == '__main__':
    lista_media = media_notas('nota.txt')
    print(lista_media)
    #escrever_arquivo('Primeira linhas. \n')
    # aluno = '\nBarrabas, 9, 9, 6, 10' # informando aluno por aluno no arquivo
    # atualizar_arquivo('nota.txt', aluno) # Inserindo a nota dos alunos

