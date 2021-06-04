# Printando padrões de impressão
#

def sequencia(numero):
    for i in range (0,numero):
        for j in range (1, i + 2):
            print(j, end = "")
        print()
    for i in range(numero, 0, -1):
        for j in range(i-1, 0, -1):
            print(j, end = "")
        print()
sequencia(10)
