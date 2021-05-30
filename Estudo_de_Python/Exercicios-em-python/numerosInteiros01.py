""" Exercícios propostos no site: https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html """
## Dado um sequencia de números inteiros não-nulos, seguida por 0, impirmir seus quadrados.

def main():
    print("Calculo dos quadrados de uma sequência de numeros!")
    print("Para finalizar digite 0 (zero).\n")
    
    num = int(input("Digite um número: "))
    while num != 0:
        quadrado = num * num
        print("O número ", num, "ao quadrado é", quadrado)
        num = int(input("Digite um numero: "))
main()