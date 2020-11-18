# Objetivo trabalhar com exceções, tratar exceções
# Como lançar uma exceção genérica
# Utilizar exceções específicas
# Encadeamento e exceções
# Else e Finally
# Criação de exceções customizadas
# Verificar a biblioteca do Python sobre exceções.

# Forçar um edrro para verificar uma exceção


lista = [1, 10]

try:  # No Python o try e except realizam o tratamento de exceção
    arquivo = open('teste.txt', 'r')
    print('Abrindo arquivo {}'.format(arquivo))
    texto = arquivo.read()
    divisao = 10 / 0
    numero = lista[3]
    # x = a
except ZeroDivisionError: # Aqui no caso estou pegando o erro e definindo o que irá aparecer para o usuário
    print('Não é possível realizar uma divisão por zero')
except IndexError:
    print('Erro ao acessar um indíce inválido da lista')
except BaseException as ex: # A BaseException é uma árvore de erros
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção') # o else éimportante após o trtatamento da exceção para o caso de não ocorrer nenhum erro, o Else irá dar continuidade na execução do programa.
finally:   # Tudo o que está no finally ele irá executar, com erro ou não.
    print('Sempre executa')
    print('Fechando o arquivo')
    arquivo.close()



