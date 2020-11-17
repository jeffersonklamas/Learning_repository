# Manipulação de arquivos via python
# Após usar a instrução open seguida de nome do arquivo pode usar a letra w (escrever) ou a letra a (atualizar) o arquuivo

# open ('teste.txt', 'w') # criando um arquivo através do python
# arquivo = open('teste.txt', 'w') # escrevendo uma linha no arquivo
# arquivo.write('\n Segunda linha')
# arquivo = open('teste.txt', 'a') # atualiza o arquivo informado
# arquivo.write('\n Terceira linha')
# arquivo.close()

# Criando um método para ecscrever e atualizar um arquivo
# pode ser criado o arquivo no diretório que quiser é só informar o endereço do mesmo

def escrever_arquivo(texto):
    #diretorio = 'escreva o endereço onde será criado o arquivo'
    arquivo = open('teste.txt', 'w') # Insira o nome diretorio na primeira '' antes da virgula
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

# criando método para  ler um arquivo

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r') # r de read
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    #escrever_arquivo('Primeira linha. \n') # chamando a instrução para escrever no arquivo
    #atualizar_arquivo('Terceira linha. \n') # atualizando o arquivo
    ler_arquivo('teste.txt')