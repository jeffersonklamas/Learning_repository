# Organizando conjuntos e subconjuntos
# Conjuntos aritméticos
# Métodos de União
# Método de intersecção
# Método de diferença
# Método de diferença simétrica
# Remoção de duplicidade de listas utilizando conjuntos

# uma Lista é representada pelo que está entre [] - Colchetes
# uma tupla é o que esta representada pelo que está dentro de () - Parenteses
# um conjunto é representado pelo que esta dentro de {} - Chaves
# conjunto não permite duplicidade, se possuir mais do mesmo na hora em que for imprimir irá aparecer somente um dos integrantes do conjuntos
# conjunto = {1, 2, 3, 4} # isto é um conjunto
# print(type(conjunto))   # retorna tipo set

# conjunto = {1, 2, 3, 4, 1, 2, 3, 4, 4, 4, 4} # isto é um conjunto
# print(type(conjunto))   # retorna tipo set
# print(conjunto)

# conjunto = {1, 2, 3, 4} # isto é um conjuntO
# conjunto.add(6) # inclui um elemento ao conjunto
# conjunto.discard(2) # Exclui o conjunto informado
# print(type(conjunto))   # retorna tipo set
# print(conjunto)

# União de conjuntos
conjunto = {1,3,6,7,5}
conjunto2 = {2,4,5,8}
conjunto_uniao = conjunto.union(conjunto2) # Esta instrução irá unir os conjuntos, já excluindo as duplicidades e colocando em ordem
print('Conjunto União: {}'.format(conjunto_uniao))

# Itersecção dos conjuntos
conjunto_interseccao = conjunto.intersection(conjunto2) # Esta instrução irá fazer a intersecção dos elementos dos conjuntos
print('Conjuntio Intersecção: {}'.format(conjunto_interseccao))
#  Diferença de conjuntos
conjunto_diferenca = conjunto.difference(conjunto2)
print('Conjunto Diferença entre 1 e 2: {}'.format(conjunto_diferenca))
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Conjunto Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))
# Diferença simétrica, é uma operação que se faz com conjuntos, e consiste em unir os dois conjuntos e remover a parte em comum entre eles.
conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)
print('Conjunto simetrica: {}'.format(conjunto_dif_simetrica))
# Pertinência, A  relação de pertinência mostra se um elemento está dentro ou não de um conjunto, ou seja, se ele pertence ou não pertence a um conjunto.

conjunto_a = {1,2,3,}
conjunto_b = {1,2,3,4,5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('Elementos do conjunto A pertencem ao conjuinto B?: {}'.format(conjunto_subset))
conjunto_subset = conjunto_b.issubset(conjunto_a)
print('Elementos do conjunto B pertencem ao conjuinto A?: {}'.format(conjunto_subset))

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A?: {}'.format(conjunto_superset))
conjunto_superset = conjunto_a.issuperset(conjunto_b)
print('A é um super conjunto de B?: {}'.format(conjunto_superset))

#Converter uma lista para conjunto e já eliminar duplicidades
lista = ['cachorro', 'cachorro', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista) # converte para conjunto e elimina as duplicidades
print(conjunto_animais)
# Convertendo conjunto para listas
lista_animais = list(conjunto_animais) # converte conjunto para lista já sem a duplicidade
print(lista_animais)

conjunto_a = {1,1,3,4,5}
conjunto_b = {1,3,6}
conjunto_a.add(6)
conjunto_a.remove(1)
zebra = list(conjunto_a.intersection((conjunto_b))
print(zebra)