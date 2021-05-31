# Realizando cálculos em python, com interação com o usuário e
# uma forma de concatenação.

print("Demonstrando cálculo em Python. \n")

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

# Desenvolvendo os cálculos:

soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2
divisao_inteira = numero_1 // numero_2
modulo = numero_1 % numero_2
exponenciacao = numero_1 ** numero_2

# Printando a saída:
print("O valor da soma é: {}" .format(soma))
print("O valor da subtração é: {}" .format(subtracao))
print("O valor da multiplicação é: {} " .format(multiplicacao))
print("O valor da divisão é: {}" .format(divisao))
print("O resultado entre operandos e a parte decimal do resultado (Operação inteira //) é: {}" .format(divisao_inteira))
print("O resultado do resto da divisão entre os operandos é: {}" .format(modulo))
print("O resultado da exponenciação é: {} \n" .format(exponenciacao))

print("Fim....")

