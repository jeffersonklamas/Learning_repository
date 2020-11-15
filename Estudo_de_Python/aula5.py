# Diferencça entre listas e tuplas:
# As listas são mutáveis e é possível alterar as mesmas: incluir, excluir, ordenar, Para criar uma lista basta deixar entre []
# As tuplas são imutáveis. Para criar uma tupla, basta incluir entre parenteses
# É possível transformar uma lista em tupla e vice versa.
# Criando tuplas

# a = (12, 35, 60, 90)
# print(len(a)) # a instrução ao lado conta a quantidade de itens dentro da tupla
# print(type(a)) #  a instrução type informa o tipo do conteúdo da lista

lista = [12, 10, 7, 5]
lista_animal = ['cervo', 'arara', 'elefante', 'gato', 'cachorro']
lista_animal[0] = 'macaco' # Com esta instrução foi substituído o cervo e no lugar entrou o  macaco
print(lista_animal)

# a = (1,10,12,14)
# print(a)
# print(type(a))
# print(len(a)) # conta a quantidade de itens dentro da tupla
# a_animal = tuple(lista_animal) # A instrução tuple converte uma tupla em uma lista
# print(type(a_animal))
# print(a_animal)

lista_numerica = tuple(lista)
print(type(lista_numerica))
print(lista_numerica)

#a[0] = 2 # A tupla é imutável, não se consegue mudar o item






# Criando lista o certo é criar listas de numeros e string em separado
# as listas estão entre colchetes

# lista = [101, 3, 12, 40, 10]
# lista_animal = ['vermes', 'girafa', 'macaco', 'tamandua', 'aranha']

# Instrução para ordenar listas, por ser uma função, só o nome da lista e na sequência imprimir a lista.
# lista.sort() # .sort ordena em ordem crescente
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse() # .reverse ordena em ordem decrescente
# print(lista_animal)


#print(lista_animal) # lista somente os animais
# /rint(lista_animal[1]) # O esta entre colchetes após o nome da lista irá printar a variável correspondente ao item da lista, no python se começa do zero em em diante

# a instrução abaixo irá verificar se há um tipo especifico na lista e se não conter o mesmo será incluido na mesma.
# if 'lobo' in lista_animal:
#     print('Existe na lista')
# else:
#     print('Não existe na lista')
#     lista_animal.append('lobo') # neste caso irá incluir o animal na lista
#     print(lista_animal)

# A instrução abaixo irá retirar um elemento da lista, por default se deixar embranco irá retirar o ultimo elemento, se informar a posição, irá retiar o elemento da posição informada
# lista_animal.pop(1)
# print(lista_animal)

# A instrução abaixo remove o item indicado pelo nome
# lista_animal.remove('macaco')
# print(lista_animal)


# if 'formiga' in lista_animal: # esta instrução verifica se há um animal  especifico na lista
#     print('Existe na lista')
# else:
#     print('Não existe na lista ')

#print(min(lista)) # esta instrução mostra o menor número
#print(max(lista)) # esta instrução mostra o maior número
#print(sum(lista)) # esta instrução somente soma a lista

# soma = 0 # Neste caso irá percorrer a lista de inteiros e realizar o somatório
# for x in lista:
#     print(x)
#     soma += x
# print(soma)

# for x in lista_animal: # neste exemplo o x irá receber todos os elemtos da lista indicada
#     print (x)


