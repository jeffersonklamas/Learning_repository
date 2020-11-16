# caso não queira estanciar o valor no inicio da class, segue a instrução a seguir,
# mas terá que informar o valor de cada um quando chamar a calculadora.
class Calculadora: # A class se inicia com letra maiúscula
#    def __init__(self): # Não referenciando parametro
#       pass # no init o mesmo não pode ficar em branco, então se usa o pass, neste caso como não vai se iniciar nada é possível fazer o mesmo sem o init e o pass
    def soma(self, valor_a, valor_b): # para estanciar inclui no método a palavra self separado por virgula
        return valor_a + valor_b      # irá retornar

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora() # parametro a ser chamado em branco, mas, informado logo abaixo
print('O resultado da soma é: {}'.format(calculadora.soma(5, 6))) # Como não informei no inicio, tenho que informar agora os valores
print('O resultado da subtração é: {}'.format(calculadora.subtracao(6, 3)))
print('O resultado da multiplicação é: {}'.format(calculadora.multiplicacao(6, 200)))
print('O resultado da divisão é: {}'.format(calculadora.divisao(200, 10)))
