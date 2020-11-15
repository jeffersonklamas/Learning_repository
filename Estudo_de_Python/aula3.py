# Operadores Lógicos

# Validando se o valor é igual ou menor que 10 para calcular a média, já validando item a item
a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Digitou número maior que 10. Digite novamente: Primeiro bimestre: '))
b = int(input('Segundo bimestre:  '))
if b > 10:
    b = int(input('Digitou número maior que 10. Digite novamente: Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Digitou número maior que 10. Digite novamente: Terceiro bimestre: '))
d = int(input('Quarto bimestre:   '))
if d > 10:
    d = int(input('Digitou número maior que 10. Digite novamente: Quarto bimestre: '))
media = (a+b+c+d)/4
print('media = {}'.format(media))


# Validando se o valor é igual ou menor que 10 para calcular a média
# a = int(input('Primeiro bimestre: '))
# b = int(input('Segundo bimestre:  '))
# c = int(input('Terceiro bimestre: '))
# d = int(input('Quarto bimestre:   '))
# media = (a + b + c + d) / 4
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('media: {}'.format(media))
# else:
#     print('Foi digitado alguma nota errada')

# A instrução abaixo usando o operador lõgico or not inverte a questão se apenas
# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segun do valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or not resto_b > 0:
#     print('foi digitado um número par')
# else:
#     print('nenhum número par foi digitado')


# Na instrução abaixo quero saber se há um número par entre os dois números informados
# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segun do valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or resto_b == 0: # nesta instrução se apenas um deles for verdadeira já valida a informação devido ao operador lógico or.
#     print('foi digitado um número par')
# else:
#     print('nenhum número par foi digitado')

# A instrução abaixo verifica se um número é par
# a = int(input('Entre com um valor '))
# resto = a % 2 # o sinal de igual simples é apenas para inofrmar que recebe
# if resto == 0: # lembrando o sinal de igual igual duplo é a divisão do resto
#     print('número é par')
# else:
#     print('número é impar')

# a = int(input('Primeiro valor: ')) # O int converte uma str para numero inteiro
# b = int(input('Segundo valor:  ')) # O int converte uma str para numero inteiro
# c = int(input('Terceiro valor: ')) # O int converte uma str para numero inteiro
#
# if a > b and a > c: # E se, o dois pontos informa ao python que é para identação.
#     print('o maior número é: {}' .format(a))
# elif b > a and b > c: # elife vai verificar a segunda variavel
#     print('O maio número é: {}' .format(b), '\n')
# else: #else vai verificar a última variavel
#     print('O maior número é: {}' .format(c),'\n')
# print('final do programa')
