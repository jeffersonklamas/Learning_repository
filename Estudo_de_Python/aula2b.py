# o Básico para iniciar, interação só via terminal.
a = 63
b = 6
soma = a + b
subtrair = a - b
multiplica = a * b
divide = a / b
resto = a % b # retorna o resto da divisão
# o '\n' cria uma linha em branco entre as linhas
print(soma)# Só este comando printa somente o resultado
print(subtrair)# Só este comando printa somente o resultado
print(multiplica)# Só este comando printa somente o resultado
print(divide)# Só este comando printa somente o resultado
print(resto , '\n')# Só este comando printa somente o resultado
# A instrução abaixo concatena a str entre aspas simples com a variável int dos resultados solicitados
print('soma = ' + str(soma)) # a função ao lado concatenou uma str com uma int, ele irá apresentar o resultado soma: (resultado de a + b)
print('subtrair = ' + str(subtrair)) # a função ao lado concatenou uma str com uma int, ele irá apresentar o resultado soma: (resultado de a - b)
print('multiplica = ' + str(multiplica))# a função ao lado concatenou uma str com uma int, ele irá apresentar o resultado soma: (resultado de a * b)
print('divide = ' + str(divide))# a função ao lado concatenou uma str com uma int, ele irá apresentar o resultado soma: (resultado de a / b)
print('resto = ' + str(resto) , '\n')# a função ao lado concatenou uma str com uma int, ele irá apresentar o resultado soma: (resultado de a % b)
# Pode ser usado també o .format para concatenar
print('soma = {}' .format(soma))
print('subtrair = {}' .format(subtrair))
print('multiplica = {}' .format(multiplica))
print('divide = {}' .format(divide))
print('resto = {}' .format(resto) , '\n')
#Outra forma de printar os resultados em uma única linha de comando é
print('soma: {soma} \nsubtrair: {sub}'
      '\nmultiplica: {multi} \ndivide: {divide} '
      '\nresto: {resto}' .format(soma=soma, sub=subtrair,
                                               multi=multiplica, divide=divide,
                                               resto=resto) ,'\n')
# Criando uma interação com o usuário.
a = int(input('Digite o primeiro número: ')) #O int converte a string em números
b = int(input('Digite o segundo número: ')) #O int converte a string em númer15os
soma = a + b
subtrair = a - b
multiplica = a * b
divide = a / b
resto = a % b # retorna o resto da divisão

#Outra forma de printar os resultados em uma única linha de comando é
resultado = ('soma: {soma} \nsubtrair: {sub} '
      '\nmultiplica: {multi} \ndivide: {divide} '
      '\nresto: {resto}' .format(soma=soma, sub=subtrair,
                                               multi=multiplica, divide=divide,
                                               resto=resto))

print(resultado)
