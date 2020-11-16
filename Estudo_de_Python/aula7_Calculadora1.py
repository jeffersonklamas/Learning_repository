# Construindo métodos , funções e classes em Python
# Aprender a utilização de métodos e funções no Python
# Aprender a utilização de classes
# Entender os motivos para se usar métodos, funções e classes.
#
# O que são métodos e funções
# Como declarar métodos e funções
# Vantagens de se utilizar métodos e funções
# Como implementar classes
# Vantagens de se utilizar classes
#
# Por convenção:
# função é tudo que se retornar um valor, método não retorna
# no python não há essa diferenciação explicita, no Python os métodos se chama de definição.
# No Python para se declarar um método usa-se apenas a palavra def e em seguida dando um nome para o métodos sempre em minúsculo
# Os métodos auxiliam para não precisar ficar regerando código
# Todo código que for ser usado várias vezes, cria-se um método para facilitar o processo de criação
# método sempre solicita duas entradas, separadas por vírgula
# def soma(a,b):
#     return a + b
# def subtracao(a,b):
#     return a - b
# def multiplicacao(a,b):
#     return a * b
# def divisao(a,b):
#     return a / b
# print(soma(1, 2))
# print(subtracao(10,6))
# print(multiplicacao(3,3))
# print(divisao(10,5))

# Se viu que no método há de se declarar separadamente os argumentos
# A classe irá simplificar colocando todo método identada dentro da classe
# Abaixo usando a classe, a classe se inicia com letra maiúscula.
# Para startar uma class se inicia com um método init, seguida de self para referenciar um parametro
# Usando class em forma de calculadora.

class Calculadora: # A class se inicia com letra maiúscula
    def __init__(self, num1, num2): # Referenciando parametro
        self.valor_a = num1 # parametro
        self.valor_b = num2
    def soma(self): # para estanciar inclui no método a palavra self
        return self.valor_a + self.valor_b # irá retornar

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

calculadora = Calculadora(10, 2) # parametro a ser chamado
#print(calculadora.valor_a) # chamou o valor de a
print('O resultado da soma é: {}'.format(calculadora.soma())) # calculando o valor de 10 + 2
print('O resultado da subtração é: {}'.format(calculadora.subtracao())) # subtraindo o valor de 10 - 2
print('O resultado da multiplicação é: {}'.format(calculadora.multiplicacao())) # multiplicando o valor de 10 * 2
print('O resultado da divisão é: {}'.format(calculadora.divisao())) # dividindo o valor de 10 / 2



