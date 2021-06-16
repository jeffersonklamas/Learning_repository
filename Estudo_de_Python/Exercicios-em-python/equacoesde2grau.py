#--------------------------------------------
# Cálculo de equações de segundo grau ( Bhaskara)
#
#--------------------------------------------
import math

a = float(input("Digite um valor para A: "))
b = float(input("Digite um valor para B: "))
c = float(input("Digite um valor para C: "))

# Calculo(a, b, c)

delta = b ** 2 - 4 * a * c

if delta == 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    print("A única raiz é: {0}".format(x1))
else:
    if delta < 0:
        print("Esta equação não pertence aos números Reais!!!")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("\nO Valor de x1: {}, e x2: {}\n".format(x1,x2))
        
"""
if __name__ == "__main__":
    segue = input("\nPara finalizar, Digite q ou pressione enter para um novo cálculo: \n")
    if (segue == "q"):
        break
"""
# End 
