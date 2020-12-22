### Cálculo para saber se um determinado número é primo 

import math

def eh_primo(n):
    raiz = int(math.sqrt(n))
    for d in range(2, raiz +1):
        if n % d == 0:
            return False
    return True

numero = int(input("Digite um número: "))
if eh_primo(numero):
    print("O numero {} é primo".format(numero))
else:
    print("O número {} Não é primo".format (numero))

