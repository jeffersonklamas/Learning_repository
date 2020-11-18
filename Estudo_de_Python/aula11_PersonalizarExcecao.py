# Personalizando exceções

# PAra se criar uma classe de exceção, é obrigatório a instrução a seguir, uma herda de Exception
class Error(Exception): # Essa calss está herdando de exceção
    pass                # Só para não dar erro

class InputError(Error): #Por convenção toda classe de exceção rtem que terminar com erro, é bom já deixar em ingles
    def __init__(self, message):  # Criando um construtor
        self.message = message

while True: # O while True é infinito, coloque o break para sair do loop
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('Nota não pode ser menor que zero')
        break
    except ValueError:
        print('Valor Inválido. Favor digitar apenas números.')
    except InputError as ex:
        print(ex)
