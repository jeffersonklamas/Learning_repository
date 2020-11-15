# O while é útil para forçar ao usuário a inserir o dado corretamente
a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Digitou número maior que 10. Digite novamente: Primeiro bimestre: '))
b = int(input('Segundo bimestre:  '))
while b > 10:
    b = int(input('Digitou número maior que 10. Digite novamente: Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Digitou número maior que 10. Digite novamente: Terceiro bimestre: '))
d = int(input('Quarto bimestre:   '))
while d > 10:
    d = int(input('Digitou número maior que 10. Digite novamente: Quarto bimestre: '))
media = (a+b+c+d)/4
print('media = {}'.format(media))


# nota = int(input('Entre com a nota: ')) # Neste caso enquanto o usuário não informar uma nota menor ou igual a 10, ficara em um loop eterno
# while nota > 10:
#     nota = int(input('Nota inválida. Entyre com a nota correta: '))

# Dependendo do que necessitar o For é melhor que o while.
# a = 0          # Enquanto o a for menor ou igual a 10 o pŕocesso irá mostrar os números.
# while a <= 10: # While força uma repetição e pode ser melhor que o range
#     print(a)
#     a += 1




# a = int(input('Entre com um número: ')) # Verificando todos os números primos até o número indicado pelo usuário
# for num in range (a+1): # treinando for dentro de for
#     div = 0
#     for x in range(1, num+1): #Esta percorrendo toda a lista, até o número informado,  para verificar se é divisível por ele mesmo.
#         resto = num % x # Pegando o resto da divisão.
#         #print(x, resto) # Verificando os números que estão passando pelo laçõ
#         if resto == 0: # Se o resto da divisão for igual a zero, significa que o número é divisível pelo número que está passando pelo laço
#             #div = div + 1 # Em vez de escrever div = div +1
#             div += 1 # Este formato informa ao python para concatenar o resultado de div mais um, uma forma mais legal de escrever
#     if div ==2:
#         print(num)


# for num in range (101): # Verificando os números primos de 0 a 100
#     div = 0
#     for x in range(1, num+1): #Esta percorrendo toda a lista, até o número informado,  para verificar se é divisível por ele mesmo.
#         resto = num % x # Pegando o resto da divisão.
#         #print(x, resto) # Verificando os números que estão passando pelo laçõ
#         if resto == 0: # Se o resto da divisão for igual a zero, significa que o número é divisível pelo número que está passando pelo laço
#             #div = div + 1 # Em vez de escrever div = div +1
#             div += 1 # Este formato informa ao python para concatenar o resultado de div mais um, uma forma mais legal de escrever
#     if div ==2:
#         print(num)

# a = int(input('Entre com um número: ')) # Número a ser inserido para verificar se é um número primo.
# div = 0
# for x in range(1, a+1): #Esta percorrendo toda a lista, até o número informado,  para verificar se é divisível por ele mesmo.
#     resto = a % x # Pegando o resto da divisão.
#     print(x, resto) # Verificando os números que estão passando pelo laçõ
#     if resto == 0: # Se o resto da divisão for igual a zero, significa que o número é divisível pelo número que está passando pelo laço
#         #div = div + 1 # Em vez de escrever div = div +1
#         div += 1 # Este formato informa ao python para concatenar o resultado de div mais um, uma forma mais legal de escrever
# if div ==2:
#     print('Número {} é primo'.format(a))
# else:
#     print('Número {} não é primo'.format(a))

# for x in range(100): # o Range vai neste caso iniciar do zero até 99 e cada vez que o range passa omesmo carrega na variável x
#     print(x)

# for run in range(101): # O comando For serve para criar laço de repetição.
#     div = 0
#     for x in range(1,num):
#         resto = num % x
#         print(x, resto)
#         if resto == 0:
#             div == 1
#         if div == 2
#             print(num)

# for x in range(101): # O for irá monstar os número de zero a 100
#     print(x)