# Objetivos desta aula:
# Aprender a utilizar e interagir com módulos
# Entender a importância de se utilizar módulos
# Aprender sobre funções anônimas
#
# Como realizar a importação de um módulo
# Entender a importância de se trabalhar com módulos
# Acessar classes e métodos de um módulo
# Entender e trabalhar com funções anônimas (lambda)
#
# módulo é todo arquivo com extensão .py , e estes módulos é possível interagir entre eles
# sem necessitar criar um novo arquivo.
# para se fazer testes nos arquivo py é improtante inserir um main para se evitar que quando ao chamar o arquivo
# via terminal através do comando import o mesmo já não seja rodado.
# há também a possibilidade de se usar o from via terminal, para executar somente aquilo que se necessita.
# é necessário conhecer o arquivo que se está trabalhando, para poder chamar as variáveis
#
# Também é possível acessar o módulo através de um outro arquivo através do comando abaixo

from aula7_televisao import Televisao
televisao = Televisao
print(televisao.ligada)
televisao.power()
print(televisao.ligada)

